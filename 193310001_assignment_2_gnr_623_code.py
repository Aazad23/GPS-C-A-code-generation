# -*- coding: utf-8 -*-
"""193310001_Assignment-2_GNR-623

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Plrswkfp8ba06z6ECp9_QiCt2m7LqoBY

# C/A code Generation for Satellite Vehicle no. 11
"""

Satellite_Vehicle_No = 11

# Indexes from which Output for each step is Taken  
G2_Taps = [3,4]
G1_Taps = [10]

"""### POLYNOMIAL G1 = 1+X****3** + X*****10***
### POLYNOMIAL G2 = 1+X****2** + X****3** + X****6** + X****8** + X****9** + X*****10***
"""

# THE FEEDBACK TO BE TAKEN FROM BIT 3 AND 10 FOR G1 and 2,3,6,8,9 and 10 for G2

feed_G1 = [3,10]
feed_G2 = [2,3,6,8,9,10]

"""#Shift Registers"""

def shift_reg(register, feedback, output):

    # calculate output
    out = [register[i-1] for i in output]
    if len(out) > 1:
        out = sum(out) % 2
    else:
        out = out[0]

    fb = sum([register[i-1] for i in feedback]) % 2   
   
    # shift to the right
    for i in reversed(range(len(register[1:]))):
        register[i+1] = register[i]
        
    # put feedback in position 1
    register[0] = fb
    
    return out

# Since Stellite generate 1023 bit long code in 1 ms

"""# PNR(C/A) code Calculation"""

def PRN(feed_G1,feed_G2,G1_Taps,G2_Taps):
  #  linear feedback shift register Initialization for gold code 1 and 2
  G1 = [ 1 for i in range(10)]
  G2 = [ 1 for i in range(10)]
  
  CA = [] 
 
  # create sequence
    
  for i in range(1023): 
    g1 = shift_reg(G1,feed_G1, G1_Taps)
    g2 = shift_reg(G2, feed_G2, G2_Taps)
    CA.append((g1 + g2) % 2)

# return C/A code!
  return CA

result = PRN(feed_G1,feed_G2,G1_Taps,G2_Taps)
print(result)

import pandas as pd
df= pd.DataFrame(result, columns=['Code'])

"""# Plotting Output"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(25,5))
plt.plot(np.arange(0,1,1/1023), result, 'black')
plt.xlabel('Time in ms')
plt.title('C/A code for Satellite 11')
plt.show()

