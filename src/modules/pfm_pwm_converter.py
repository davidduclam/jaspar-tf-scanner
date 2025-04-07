import numpy as np

# ---- PFM TO PWM CONVERSION ----
def pfm_to_pwm(pfm_dict):
    """Convert a Position Frequency Matrix (PFM) to a PWM using Laplace smoothing"""
    pfm_array = np.array([pfm_dict[base] for base in "ACGT"], dtype=float)

    bg = np.array([0.25, 0.25, 0.25, 0.25])  # Background frequency for A, C, G, T
    total = np.sum(pfm_array, axis=0)  # Sum across all bases at each position

    # Adding pseudocount to avoid zero probabilities
    probabilities = (pfm_array + bg[:, None]) / (total + 1)

    pwm = np.log2(probabilities / bg[:, None])  # Log-odds conversion
    return pwm