import numpy as np 
import matplotlib.pyplot as plt
from signals import create_sine_wave 
sine = create_sine_wave(5,2)
print(r'the first 10 samples of my sine wave are',sine[:10])

plt.plot(sine[:10]) 
plt.ylabel('amplitude')
plt.xlabel('time')
plt.show
plt.savefig('sineplot.png')