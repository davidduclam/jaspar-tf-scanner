from modules import pfm_pwm_converter

# Example PFM dictionary
pfm = {
    "A": [5, 0, 0, 0],
    "C": [0, 5, 0, 0],
    "G": [0, 0, 5, 0],
    "T": [0, 0, 0, 5]
}

# Convert PFM to PWM
pwm = pfm_pwm_converter.pfm_to_pwm(pfm)

# Print the resulting PWM
print("Position Weight Matrix (PWM):")
print(pwm)
