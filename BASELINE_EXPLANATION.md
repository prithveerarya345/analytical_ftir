# Baseline Calculation for Peak Filtering - Concise Explanation

## How Baseline is Handled in Peak Detection

The baseline is **not explicitly calculated** as a separate step. Instead, the `scipy.signal.find_peaks` algorithm uses the **prominence** parameter to automatically determine the baseline relative to each peak.

### Key Concept: Peak Prominence

**Prominence** measures how much a peak stands out above its surrounding baseline:

```
Prominence = Peak Height - Baseline Level
```

Where:
- **Peak Height**: The absorbance value at the peak maximum
- **Baseline Level**: The lowest point between the peak and the next higher peak on either side

### How It Works:

1. **For each potential peak**, the algorithm looks left and right
2. **Finds the lowest point** between the peak and the next higher peak on each side
3. **Takes the higher of these two points** as the baseline reference
4. **Calculates prominence** = peak height - baseline reference
5. **Only keeps peaks** where prominence ≥ 0.02 absorbance units

### Visual Example:

```
Absorbance
    |
0.3 |        ╱╲
    |       ╱  ╲
0.2 |      ╱    ╲     ╱╲
    |     ╱      ╲   ╱  ╲
0.1 |____╱________╲_╱____╲____ Baseline
    |            ╱
0.0 |___________╱
    |
    └─────────────────────────> Wavenumber
    
Peak 1: Height = 0.3, Baseline = 0.1, Prominence = 0.2 ✓ (kept)
Peak 2: Height = 0.15, Baseline = 0.1, Prominence = 0.05 ✓ (kept)
Peak 3: Height = 0.12, Baseline = 0.1, Prominence = 0.02 ✓ (kept)
Noise: Height = 0.11, Baseline = 0.1, Prominence = 0.01 ✗ (filtered out)
```

### Why This Works:

- **No manual baseline correction needed** - algorithm handles it automatically
- **Adaptive** - baseline is determined relative to each peak's local environment
- **Filters noise effectively** - small fluctuations on a noisy baseline are rejected
- **Standard practice** - this is how professional FTIR software handles baselines

### Parameters Used:

- **Prominence = 0.02**: Peak must be 0.02 absorbance units above its local baseline
- **Height = 0.05**: Additional check - peak must be at least 0.05 absorbance units tall
- **Distance = 20 points**: Peaks must be separated to avoid detecting noise as multiple peaks

### In Simple Terms:

The algorithm asks: *"Is this peak significantly higher than the surrounding area?"* 

If yes → Real absorption band (kept)
If no → Noise or artifact (filtered out)

The "surrounding area" (baseline) is automatically determined for each peak by finding the lowest points on either side before the next higher peak.

