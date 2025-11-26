# FTIR Data Analysis Web App

A simple web application for analyzing and comparing FTIR (Fourier Transform Infrared) spectra from three bacterial samples.

## Features

1. **Interactive Spectra Visualization**: View all three FTIR spectra on separate plots and a comparison plot using Plotly
2. **Peak Detection**: Automatically identifies absorption peaks in each spectrum using absorbance conversion
3. **Functional Group Identification**: Maps detected peaks to their corresponding functional groups/chemical bonds
4. **Heavy Metal Detection**: Includes fingerprint region (400-1500 cm⁻¹) analysis for heavy metal detection via metal-ligand vibrations
5. **Comparison Table**: Shows a side-by-side comparison of which functional groups are present in each bacterial sample

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Data Files

The app expects three FTIR data files:
- `1_ab.txt` - Bacteria 1
- `2_ec.txt` - Bacteria 2  
- `3_eb.txt` - Bacteria 3

Each file should contain FTIR data in the format:
```
##TITLE=No Description
##DATA TYPE=INFRARED SPECTRUM
##XUNITS=1/CM
##YUNITS=%T
wavenumber    transmittance
...
```

## Functional Groups Detected

The app identifies over 30 functional groups based on wavenumber ranges. Key groups include:

**O-H and N-H Stretching:**
- O-H Stretching (Water/Alcohols): 3200-3600 cm⁻¹
- N-H Stretching (Amines/Proteins): 3300-3500 cm⁻¹
- O-H Stretching (Carboxylic Acids): 2500-3300 cm⁻¹

**C-H Stretching:**
- C-H Stretching (Aromatic): 3000-3100 cm⁻¹
- C-H Stretching (Lipids/Proteins): 2800-3000 cm⁻¹
- C-H Stretching (Alkanes): 2850-2960 cm⁻¹

**Carbonyl Region:**
- C=O Stretching (Carboxylic Acids): 1700-1725 cm⁻¹
- C=O Stretching (Esters): 1735-1750 cm⁻¹
- Amide I (Proteins): 1600-1700 cm⁻¹
- C=O Stretching (Amides): 1630-1690 cm⁻¹

**Amide and Protein Regions:**
- Amide II (Proteins): 1500-1600 cm⁻¹
- N-H Bending (Amines): 1500-1650 cm⁻¹

**Bending and Deformation:**
- C-H Bending (Lipids): 1400-1500 cm⁻¹
- C-H Bending (Methyl): 1370-1380 cm⁻¹
- C-H Bending (Methylene): 1465-1475 cm⁻¹

**Nucleic Acids and Phosphates:**
- PO2- Asymmetric Stretching (Nucleic Acids): 1220-1260 cm⁻¹
- PO2- Symmetric Stretching (Nucleic Acids): 1050-1100 cm⁻¹
- P=O Stretching (Phosphates): 1200-1300 cm⁻¹

**Carbohydrates and Ethers:**
- C-O Stretching (Carbohydrates): 1000-1150 cm⁻¹
- C-O-C Stretching (Carbohydrates): 950-1050 cm⁻¹
- C-O Stretching (Ethers): 1050-1150 cm⁻¹

**Heavy Metal Detection (Fingerprint Region):**
- Metal-O Stretching (Heavy Metals): 400-800 cm⁻¹
- Metal-OH Bending (Heavy Metals): 500-800 cm⁻¹
- Metal-S Stretching (Heavy Metals): 400-600 cm⁻¹
- Metal-N Stretching (Heavy Metals): 400-600 cm⁻¹
- Metal-Carbonate (Heavy Metals): 1400-1500 cm⁻¹
- Metal-Phosphate (Heavy Metals): 900-1100 cm⁻¹
- Metal-Sulfate (Heavy Metals): 1100-1200 cm⁻¹
- Metal-Nitrate (Heavy Metals): 1300-1400 cm⁻¹
- Specific metal bands: Pb-O, Cd-O, Hg-S, As-O, Cr-O, Cu-O, Zn-O, Ni-O, Fe-O

**References:**
- NIST Chemistry WebBook (https://webbook.nist.gov/)
- Thermo Fisher Scientific FTIR Reference Chart
- Chemistry LibreTexts IR Correlation Tables
- Standard FTIR reference texts (Silverstein, Bassler, Morrill)
- Published bacterial FTIR studies
- Heavy metal detection in fingerprint region (Food Safety and Risk, 2025)

## Technologies Used

- Flask (Python web framework)
- NumPy (Numerical computing)
- SciPy (Signal processing for peak detection)
- Plotly (Interactive data visualization)

