import numpy as np 
from signals import create_sine_wave 
sine = create_sine_wave(5,2)
print(r'the first 10 samples of my sine wave are',sine[:10])
