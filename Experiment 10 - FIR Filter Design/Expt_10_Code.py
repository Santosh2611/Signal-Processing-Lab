import matplotlib.pyplot as plt # Provides an implicit way of plotting
import numpy as np # Support for large, multi-dimensional arrays and matrices
from scipy import integrate # Compute a definite integral

N = int(input("\nEnter the number of coefficients for FIR Filter: "))
hd_w = int(input("Enter the frequency response value: "))

# Inverse discrete-time Fourier transform:
hd_n = []
for n in range(N//2 + 1):
    expression = lambda w: hd_w * np.exp(-1j * w * n) # Expression within the integral
    temp = integrate.quad(expression, (-2*np.pi)/5, (2*np.pi)/5)
    integral = temp[0] / (2*np.pi) # quad() gives a tuple, integral_value[0] + constant[1]
    hd_n.append(integral)

# Compute desired filter coefficients:
for n in reversed(range(N//2)): # Backward iteration will start occurring from the rear
    symmetric = hd_n[n]
    hd_n.append(symmetric)

print("\nThe desired filter coefficients h_d[n] is as follows:\n {}". format(hd_n))

# Design FIR filter using rectangular window technique (Impulse Response):

# Rectangular window function:    
wn_rectangular = []
for n in range(N):
    if n<N:
        temp=1
    else:
        temp=0
    wn_rectangular.append(temp)

# Expected filter coefficients obtained using rectangular window technique:
hn_rectangular = []
for n in range(N):
    hn_rectangular.append(hd_n[n] * wn_rectangular[n])

# Sketch expected filter coefficients obtained using rectangular window technique:
plt.xlabel('n')
plt.ylabel('Magnitude of h[n]')
plt.title("Impulse Response Using Rectangular Window Technique")
plt.stem(np.arange(0, len(hn_rectangular)), hn_rectangular)
plt.grid(True)
plt.show()
print("\nThe expected filter coefficients h[n] obtained using rectangular window technique is as follows:\n {}". format(hn_rectangular))

# Design FIR filter using rectangular window technique (Frequency Response):

hr_w_rectangular = [] # Real function of ω
h_w_rectangular = [] # Frequency response (magnitude)
h_w_rectangular_decibels = [] # Frequency response (decibels)
index_rectangular = 0 # Index variable to iterate through "hr_w_rectangular" list
x_axis_rectangular = [] # Define the angle axis

for degrees in range(0, 190, 10):
    
    w_rectangular = degrees * (np.pi/180)
    sum_rectangular = 0
    
    if (N % 2 == 1):
        
        for n in range(((N-3)//2) + 1):
            summation = hn_rectangular[n] * np.cos(w_rectangular) * (((N-1)//2) - n)
            sum_rectangular = sum_rectangular + summation
        hr_w_rectangular.append(hn_rectangular[(N-1)//2] + (2 * sum_rectangular))
            
    else:
        
        for n in range((N//2)-1):
            summation = hn_rectangular[n] * np.cos(w_rectangular) * (((N-1)//2) - n)
            sum_rectangular = sum_rectangular + summation
        hr_w_rectangular.append(2 * sum_rectangular)
            
    h_w_rectangular.append(hr_w_rectangular[index_rectangular] * np.exp(-1j * w_rectangular * ((N-1)//2)))
    
    h_w_rectangular_decibels.append(20 * np.log10(abs(h_w_rectangular[index_rectangular])))
                                    
    index_rectangular = index_rectangular + 1
    
    x_axis_rectangular.append(degrees) 
    
# Sketch frequency response obtained using rectangular window technique:
plt.xlabel('ω in Degrees')
plt.ylabel('H[ω] in Decibels')
plt.title("Frequency Response Using Rectangular Window Technique")
plt.plot(x_axis_rectangular, h_w_rectangular_decibels)
plt.grid(True)
plt.show()
print("\nThe frequency response H[ω] in decibels obtained using rectangular window technique is as follows:\n {}". format(h_w_rectangular_decibels))
    
# Design FIR filter using Hanning window technique (Impulse Response):

# Hanning window function:
wn_hanning = []
for n in range(N):
    wn_hanning.append(0.5 * (1 - np.cos((2 * np.pi * n) / (N - 1)))) 

# Expected filter coefficients obtained using Hanning window technique:
hn_hanning = []
for n in range(N):
    hn_hanning.append(hd_n[n] * wn_hanning[n])

# Sketch expected filter coefficients obtained using Hanning window technique:
plt.xlabel('n')
plt.ylabel('Magnitude of h[n]')
plt.title("Impulse Response Using Hanning Window Technique")
plt.stem(np.arange(0, len(hn_hanning)), hn_hanning)
plt.grid(True)
plt.show()
print("\nThe expected filter coefficients h[n] obtained using Hanning window technique is as follows:\n {}". format(hn_hanning))  
 
# Design FIR filter using Hanning window technique (Frequency Response):

hr_w_hanning = [] # Real function of ω
h_w_hanning = [] # Frequency response in magnitude
h_w_hanning_decibels = [] # Frequency response (decibels)
index_hanning = 0 # Index variable to iterate through "hr_w_hanning" list
x_axis_hanning = [] # Define the angle axis

for degrees in range(0, 190, 10):
    
    w_hanning = degrees * (np.pi/180)
    sum_hanning = 0 
    
    if (N % 2 == 1):
        
        for n in range(((N-3)//2) + 1):
            summation = hn_hanning[n] * np.cos(w_hanning) * (((N-1)//2) - n)
            sum_hanning = sum_hanning + summation
        hr_w_hanning.append(hn_hanning[(N-1)//2] + (2 * sum_hanning))
            
    else:
        
        for n in range((N//2)-1):
            summation = hn_hanning[n] * np.cos(w_hanning) * (((N-1)//2) - n)
            sum_hanning = sum_hanning + summation
        hr_w_hanning.append(2 * sum_hanning)
            
    h_w_hanning.append(hr_w_hanning[index_hanning] * np.exp(-1j * w_hanning * ((N-1)//2)))
    
    h_w_hanning_decibels.append(20 * np.log10(abs(h_w_hanning[index_hanning])))
    
    index_hanning = index_hanning + 1
    
    x_axis_hanning.append(degrees) 
    
# Sketch frequency response obtained using Hanning window technique:
plt.xlabel('ω in Degrees')
plt.ylabel('H[ω] in Decibels')
plt.title("Frequency Response Using Rectangular Window Technique")
plt.plot(x_axis_hanning, h_w_hanning_decibels)
plt.grid(True)
plt.show()
print("\nThe frequency response H[ω] in decibels obtained using Hanning window technique is as follows:\n {}". format(h_w_hanning_decibels))
