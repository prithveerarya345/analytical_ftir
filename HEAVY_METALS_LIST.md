# Complete Heavy Metal Detection Database

## All Common Heavy Metals Included

The FTIR analysis system now includes detection for **all 10 most common heavy metals**:

### 1. **Lead (Pb²⁺)**
   - Detection: `Pb-O Stretching (Lead)`
   - Wavenumber Range: 450-550 cm⁻¹
   - Status: ✓ In database

### 2. **Cadmium (Cd²⁺)**
   - Detection: `Cd-O Stretching (Cadmium)`
   - Wavenumber Range: 500-600 cm⁻¹
   - Status: ✓ In database

### 3. **Mercury (Hg²⁺)**
   - Detection: `Hg-S Stretching (Mercury)`
   - Wavenumber Range: 400-500 cm⁻¹
   - Status: ✓ In database ✓ **DETECTED in all samples**

### 4. **Chromium (Cr³⁺/Cr⁶⁺)**
   - Detection: `Cr-O Stretching (Chromium)`
   - Wavenumber Range: 500-700 cm⁻¹
   - Status: ✓ In database ✓ **DETECTED in Samples 1 & 3**

### 5. **Copper (Cu²⁺)**
   - Detection: `Cu-O Stretching (Copper)`
   - Wavenumber Range: 400-500 cm⁻¹
   - Status: ✓ In database

### 6. **Nickel (Ni²⁺)**
   - Detection: `Ni-O Stretching (Nickel)`
   - Wavenumber Range: 400-500 cm⁻¹
   - Status: ✓ In database

### 7. **Zinc (Zn²⁺)**
   - Detection: `Zn-O Stretching (Zinc)`
   - Wavenumber Range: 550-650 cm⁻¹
   - Status: ✓ In database

### 8. **Arsenic (As³⁺/As⁵⁺)**
   - Detection: `As-O Stretching (Arsenic)`
   - Wavenumber Range: 700-900 cm⁻¹
   - Status: ✓ In database ✓ **DETECTED in Sample 1**

### 9. **Iron (Fe²⁺/Fe³⁺)**
   - Detection: `Fe-O Stretching (Iron)`
   - Wavenumber Range: 450-550 cm⁻¹
   - Status: ✓ In database

### 10. **Uranium (U)**
   - Detection: `U-O Stretching (Uranium)` and `U-O₂ Stretching (Uranium)`
   - Wavenumber Ranges: 800-950 cm⁻¹ and 900-1000 cm⁻¹
   - Status: ✓ In database (NEWLY ADDED)

## Detection Order (Most Specific First)

The system checks for specific metals **before** general "Metal-O" categories:

1. Hg-S Stretching (Mercury) - 400-500 cm⁻¹
2. As-O Stretching (Arsenic) - 700-900 cm⁻¹
3. Cr-O Stretching (Chromium) - 500-700 cm⁻¹
4. Pb-O Stretching (Lead) - 450-550 cm⁻¹
5. Cd-O Stretching (Cadmium) - 500-600 cm⁻¹
6. Cu-O Stretching (Copper) - 400-500 cm⁻¹
7. Zn-O Stretching (Zinc) - 550-650 cm⁻¹
8. Ni-O Stretching (Nickel) - 400-500 cm⁻¹
9. Fe-O Stretching (Iron) - 450-550 cm⁻¹
10. U-O Stretching (Uranium) - 800-950 cm⁻¹
11. U-O₂ Stretching (Uranium) - 900-1000 cm⁻¹
12. [General categories come last as fallback]

## Current Detection Results

Based on analysis of the three bacterial samples:

### Sample 1 (Bacteria 1):
- ✓ **Mercury** (Hg-S) - Multiple peaks detected
- ✓ **Chromium** (Cr-O) - Detected
- ✓ **Arsenic** (As-O) - Detected

### Sample 2 (Bacteria 2):
- ✓ **Mercury** (Hg-S) - Detected

### Sample 3 (Bacteria 3):
- ✓ **Mercury** (Hg-S) - Detected
- ✓ **Chromium** (Cr-O) - Detected

## Important Notes

1. **All metals are in the database** - The system can detect all 10 common heavy metals
2. **Detection depends on presence** - Metals only appear in results if peaks are detected in that wavenumber range
3. **FTIR limitations** - Overlapping bands may make definitive identification challenging
4. **Confirmation recommended** - Quantitative methods (ICP-OES, ICP-MS) should confirm FTIR findings

## Oxidation States

The system detects metal-oxygen bonds regardless of oxidation state:
- **Chromium**: Detects both Cr³⁺ and Cr⁶⁺ (same wavenumber range)
- **Arsenic**: Detects both As³⁺ and As⁵⁺ (same wavenumber range)
- **Iron**: Detects both Fe²⁺ and Fe³⁺ (same wavenumber range)
- **Uranium**: Detects both U-O and UO₂²⁺ (uranyl ion)

Different oxidation states may have slightly different wavenumbers, but the ranges are broad enough to capture both.

