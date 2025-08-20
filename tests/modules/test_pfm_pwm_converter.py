import pytest
import numpy as np
from modules import pfm_pwm_converter

def test_pfm_to_pwm_basic():
    pfm = {
        "A": [2, 1, 0, 0],
        "C": [0, 1, 3, 0],
        "G": [1, 1, 0, 4],
        "T": [1, 1, 1, 0]
    }
    pwm = pfm_pwm_converter.pfm_to_pwm(pfm)
    assert pwm.shape == (4, 4)
    # Check a known value (e.g., first position for A)
    expected = np.log2((2 + 0.25) / (4 + 1) / 0.25)
    np.testing.assert_allclose(pwm[0, 0], expected, rtol=1e-5)
