from flask import Flask, render_template, jsonify
import numpy as np
from scipy.signal import find_peaks

app = Flask(__name__)

# FTIR functional group assignments (wavenumber ranges in cm^-1)
# Based on authoritative sources:
# - NIST Chemistry WebBook (https://webbook.nist.gov/)
# - Bio-Rad KnowItAll IR Database
# - Standard FTIR reference texts (Silverstein, Bassler, Morrill)
# - Thermo Fisher Scientific FTIR Reference Chart
# - Chemistry LibreTexts IR Correlation Tables
# - Published bacterial FTIR studies (Naumann et al., 1991; Dziuba et al., 2014)
# Ordered by specificity (more specific ranges first)
FUNCTIONAL_GROUPS = [
    # O-H and N-H stretching region
    ('O-H Stretching (Water/Alcohols)', (3200, 3600)),
    ('N-H Stretching (Amines/Proteins)', (3300, 3500)),
    ('O-H Stretching (Carboxylic Acids)', (2500, 3300)),
    
    # C-H stretching region
    ('C-H Stretching (Aromatic)', (3000, 3100)),
    ('C-H Stretching (Alkenes)', (3010, 3100)),
    ('C-H Stretching (Lipids/Proteins)', (2800, 3000)),
    ('C-H Stretching (Alkanes)', (2850, 2960)),
    
    # Triple bond region
    ('C≡C Stretching (Alkynes)', (2100, 2260)),
    ('C≡N Stretching (Nitriles)', (2200, 2260)),
    
    # Carbonyl region
    ('C=O Stretching (Carboxylic Acids)', (1700, 1725)),
    ('C=O Stretching (Aldehydes)', (1720, 1740)),
    ('C=O Stretching (Ketones)', (1705, 1725)),
    ('C=O Stretching (Esters)', (1735, 1750)),
    ('Amide I (Proteins)', (1600, 1700)),
    ('C=O Stretching (Amides)', (1630, 1690)),
    
    # Double bond region
    ('C=C Stretching (Alkenes)', (1620, 1680)),
    ('C=C Stretching (Aromatic)', (1450, 1600)),
    
    # Amide and amine region
    ('Amide II (Proteins)', (1500, 1600)),
    ('N-H Bending (Amines)', (1500, 1650)),
    
    # Bending and deformation region
    ('C-H Bending (Methyl)', (1370, 1380)),
    ('C-H Bending (Methylene)', (1465, 1475)),
    ('C-H Bending (Lipids)', (1400, 1500)),
    ('C-H Bending / COO- Symmetric', (1350, 1450)),
    ('C-H Bending (Aromatic)', (900, 1100)),
    
    # Phosphate and nucleic acid region
    ('PO2- Asymmetric Stretching (Nucleic Acids)', (1220, 1260)),
    ('P=O Stretching (Phosphates)', (1200, 1300)),
    ('C-O Stretching (Esters)', (1000, 1300)),
    ('C-O Stretching (Ethers)', (1050, 1150)),
    ('PO2- Symmetric Stretching (Nucleic Acids)', (1050, 1100)),
    ('C-O Stretching (Carbohydrates)', (1000, 1150)),
    ('C-O-C Stretching (Carbohydrates)', (950, 1050)),
    
    # Fingerprint region
    ('C-C Stretching (Alkanes)', (800, 1200)),
    ('C-N Stretching (Amines)', (1000, 1350)),
    ('C-S Stretching (Thiols)', (600, 700)),
]

def load_ftir_data(filename):
    """Load FTIR data from text file"""
    wavenumbers = []
    transmittance = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('##'):
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        wavenumber = float(parts[0])
                        trans = float(parts[1])
                        wavenumbers.append(wavenumber)
                        transmittance.append(trans)
                    except ValueError:
                        continue
    
    return np.array(wavenumbers), np.array(transmittance)

def detect_peaks(wavenumbers, transmittance, prominence=0.02, distance=20, height=0.05):
    """
    Detect absorption peaks in FTIR spectrum using standard practice.
    
    Standard FTIR Practice:
    ---------------------
    According to FTIR spectroscopy best practices:
    1. Convert transmittance (%) to absorbance: A = -log10(T/100)
    2. Detect peaks in absorbance spectrum (not valleys in transmittance)
    3. This approach is standard because:
       - Absorbance is directly proportional to concentration (Beer's Law)
       - Peaks in absorbance are more intuitive and easier to interpret
       - Better signal-to-noise ratio for peak detection
       - Standard practice in FTIR analysis software
    
    Peak Filtering Parameters:
    -------------------------
    prominence (default=0.02): Minimum peak prominence in absorbance units.
        - A peak must be at least 0.02 absorbance units above its 
          surrounding baseline to be detected
        - Filters out noise and very small absorption bands
        - Typical range: 0.01-0.05 for biological samples
        - Lower values = more peaks (including noise)
        - Higher values = fewer peaks (only strong absorptions)
    
    distance (default=20): Minimum distance between peaks in data points.
        - Peaks must be at least 20 data points apart (~8-10 cm^-1)
        - Prevents detecting multiple peaks from the same broad band
        - Reduces false positives from spectral noise
        - Lower values = more peaks (may include duplicates)
        - Higher values = fewer peaks (may miss close but distinct bands)
    
    height (default=0.05): Minimum peak height in absorbance units.
        - Peaks must have at least 0.05 absorbance units
        - Additional filter to remove very weak absorption bands
        - Typical range: 0.03-0.10 for biological samples
    
    Wavenumber Range Filter:
    -----------------------
    Only peaks in 800-3600 cm^-1 are considered (typical FTIR range).
    This excludes the far-infrared region where data quality may be lower.
    
    Returns:
    --------
    peak_wavenumbers: Array of wavenumbers where peaks are detected
    peak_transmittance: Array of transmittance values at peak positions
    peak_indices: Array of indices in the original data arrays
    """
    # Convert transmittance (%) to absorbance using standard formula
    # A = -log10(T/100) where T is transmittance percentage
    # Handle edge cases where transmittance might be 0 or very small
    transmittance_clipped = np.clip(transmittance, 0.1, 100)  # Avoid log(0)
    absorbance = -np.log10(transmittance_clipped / 100.0)
    
    # Find peaks in absorbance spectrum (standard FTIR practice)
    # This detects actual absorption peaks, not valleys
    peaks, properties = find_peaks(
        absorbance, 
        prominence=prominence, 
        distance=distance,
        height=height
    )
    
    # Filter peaks to only include those in relevant wavenumber ranges
    # Focus on the fingerprint region and functional group regions
    relevant_peaks = []
    for peak_idx in peaks:
        wavenum = wavenumbers[peak_idx]
        # Only consider peaks in the range 800-3600 cm^-1 (typical FTIR range)
        if 800 <= wavenum <= 3600:
            relevant_peaks.append(peak_idx)
    
    peak_wavenumbers = wavenumbers[relevant_peaks]
    peak_transmittance = transmittance[relevant_peaks]
    
    return peak_wavenumbers, peak_transmittance, np.array(relevant_peaks)

def identify_functional_group(wavenumber):
    """Identify functional group based on wavenumber"""
    # Check each functional group range (in order of specificity)
    for group_name, (min_wavenum, max_wavenum) in FUNCTIONAL_GROUPS:
        if min_wavenum <= wavenumber <= max_wavenum:
            return group_name
    # If no match, return None (will be filtered out)
    return None

def analyze_spectrum(wavenumbers, transmittance):
    """Analyze spectrum and return peaks with functional groups"""
    peak_wavenumbers, peak_transmittance, peak_indices = detect_peaks(wavenumbers, transmittance)
    
    # Convert transmittance to absorbance for peak values
    transmittance_clipped = np.clip(peak_transmittance, 0.1, 100)
    peak_absorbance = -np.log10(transmittance_clipped / 100.0)
    
    peaks_data = []
    for wavenum, trans, abs_val in zip(peak_wavenumbers, peak_transmittance, peak_absorbance):
        functional_group = identify_functional_group(wavenum)
        # Only include peaks that match known functional groups
        if functional_group:
            peaks_data.append({
                'wavenumber': float(wavenum),
                'transmittance': float(trans),
                'absorbance': float(abs_val),
                'functional_group': functional_group
            })
    
    return peaks_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """Load and process all three FTIR data files"""
    files = {
        '1': '1_ab.txt',
        '2': '2_ec.txt',
        '3': '3_eb.txt'
    }
    
    all_data = {}
    all_peaks = {}
    
    for sample_id, filename in files.items():
        wavenumbers, transmittance = load_ftir_data(filename)
        peaks_data = analyze_spectrum(wavenumbers, transmittance)
        
        # Convert transmittance to absorbance for plotting
        # A = -log10(T/100) where T is transmittance percentage
        transmittance_clipped = np.clip(transmittance, 0.1, 100)  # Avoid log(0)
        absorbance = -np.log10(transmittance_clipped / 100.0)
        
        all_data[sample_id] = {
            'wavenumbers': wavenumbers.tolist(),
            'transmittance': transmittance.tolist(),
            'absorbance': absorbance.tolist()  # Add absorbance for plotting
        }
        all_peaks[sample_id] = peaks_data
    
    # Create comparison table
    # Get all unique functional groups from all samples
    all_groups = set()
    for sample_peaks in all_peaks.values():
        for peak in sample_peaks:
            all_groups.add(peak['functional_group'])
    
    # Create comparison table
    comparison_table = []
    for group in sorted(all_groups):
        row = {'functional_group': group}
        for sample_id in ['1', '2', '3']:
            # Check if this functional group appears in this sample
            has_group = any(peak['functional_group'] == group for peak in all_peaks[sample_id])
            row[sample_id] = 'Yes' if has_group else 'No'
        comparison_table.append(row)
    
    return jsonify({
        'spectra': all_data,
        'peaks': all_peaks,
        'comparison_table': comparison_table
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

