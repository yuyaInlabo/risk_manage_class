# author yuya
import numpy as np
PB1 = 0.0009
PB2 = 1 - PB1
PAB1 = 0.95
PAB2 = 1 - 0.8


bunshi  = PB1 * PAB1
bunbo = (PB1 * PAB1) + (PB2 * PAB2)

PB1A = bunshi / bunbo
print(PB1A)