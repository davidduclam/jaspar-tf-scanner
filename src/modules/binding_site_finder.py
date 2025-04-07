# ---- SCAN DNA SEQUENCE FOR BINDING SITES ----
def scan_sequence(dna_sequence, pwm):
   """Scans DNA sequence for potential binding sites using PWM scoring."""
   seq_length = len(dna_sequence)
   motif_length = pwm.shape[1]
   scores = []

   for i in range(seq_length - motif_length + 1):
       subseq = dna_sequence[i : i + motif_length]
       score = sum(pwm["ACGT".index(base), j] for j, base in enumerate(subseq))
       scores.append((i, score))

   return scores