import pytest
import numpy as np
from modules import binding_site_finder

def test_scan_sequence_basic():
    dna_sequence = "ACGTACGT"

    pwm = np.array([
        [1, 0, 0, 0],  
        [0, 1, 0, 0], 
        [0, 0, 1, 0], 
        [0, 0, 0, 1], 
    ])
    # Motif length is 4, so we expect 5 windows
    expected_scores = [
        (0, 4),  # "ACGT" matches perfectly
        (1, 0),  # "CGTA" no match
        (2, 0),  # "GTAC" no match
        (3, 0),  # "TACG" no match
        (4, 4),  # "ACGT" matches perfectly
    ]
    scores = binding_site_finder.scan_sequence(dna_sequence, pwm)
    assert scores == expected_scores