# Function to Calculate X(k) for Direct Method
def summation(k):
    sum = 0
    for n in range(size_x):
        exponential = np.exp(-2j * np.pi * k * n / size_x)
        sum = sum + float(x[n]) * exponential
    return(sum)

# import library source files
import numpy as np
import matplotlib.pyplot as plt

# Given Input Sequence x[n]
size_x = int(input("Enter the size of input x[n]: "))
x = [0] * (size_x)
print("Enter the elements of the input x[n] one-by-one as follows: -")
for sample in range(0, size_x, 1):
    x[sample] = input("Element " + str(sample + 1) + ": ")

# Sketch Input Sequence 
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title("Input Sequence x{}".format(x))
plt.stem(np.arange(0, size_x), x)
plt.grid(True) # Configure the grid lines
plt.show()
print("\nThe entered input x[n] is: -" + str(x) + "\n")

# Compute Discrete Fourier Transform Coefficients Using Direct Method
fourier_transform_direct = []
for k in range(size_x):
    fourier_transform_direct.append(summation(k))
print("\nThe Discrete Fourier Transform (DFT) coefficients of the sequence x[n] obtained using direct method are as follows: {}". format(fourier_transform_direct))

# Compute Magnitude and Phase Spectrum of DFT Coefficients
magnitude_spectrum_direct = []
phase_spectrum_direct = []
for sample in range(len(fourier_transform_direct)):
    magnitude_spectrum_direct.append((fourier_transform_direct[sample].real**2 + fourier_transform_direct[sample].imag**2)**0.5)
    phase_direct = np.arctan(fourier_transform_direct[sample].imag / fourier_transform_direct[sample].real)
    phase_spectrum_direct.append(phase_direct)
    
# Sketch Magnitude Spectrum Using Direct Method
plt.xlabel('k')
plt.ylabel('|x[k]|')
plt.title("Magnitude Spectrum Obtained Using Direct Method")
plt.stem(np.arange(0, len(magnitude_spectrum_direct)), magnitude_spectrum_direct)
plt.grid(True) # Configure the grid lines
plt.show()
print("\nThe magnitude spectrum of DFT coefficients obtained using direct method are as follows: {}". format(magnitude_spectrum_direct))

# Sketch Phase Spectrum Using Direct Method
plt.xlabel('k')
plt.ylabel('Angle (in radians)')
plt.title("Phase Spectrum Obtained Using Direct Method")
plt.stem(np.arange(0, len(phase_spectrum_direct)), phase_spectrum_direct)
plt.grid(True) # Configure the grid lines
plt.show()
print("\nThe phase spectrum of DFT coefficients obtained using direct method are as follows: {}". format(phase_spectrum_direct))

# Compute DFT Coefficients Using Linear Transformation Method

# Compute W(N) 1D Array
r1 = c1 = size_x
wn = []
for i in range(r1):
    for j in range(c1):
        wn.append(np.exp(-2j * np.pi * i * j / size_x))

# numpy.reshape() is used to give a new shape to an array without changing its data.

wn_multidim = np.reshape(wn, (r1, c1)) # An N*N W(N) matrix
print("\nThe matrix W(N) is as follows:\n{}".format(wn_multidim))
r2 = size_x; c2 = 1
x_multidim = np.reshape(x, (r2, c2)) # An N*1 x(N) matrix
print("\nThe matrix x(N) is as follows:\n{}".format(x_multidim))
  
# Compute X(N) = W(N) * x(N), an N*1 matrix
fourier_transform_multidim = [[0]*c2]*r1 # Null Multidimensional Array
fourier_transform_l_t = [] # Convert Multidimensional Array to 1D
for i in range(r1):
    for j in range(c2):
        fourier_transform_multidim[i][j] = 0
        for k in range(c1):
            fourier_transform_multidim[i][j] += wn_multidim[i][k] * float(x_multidim[k][j])
        temp = fourier_transform_multidim[i][j]
        fourier_transform_l_t.append(fourier_transform_multidim[i][j])
     
print("\nThe Discrete Fourier Transform (DFT) coefficients of the sequence x[n] obtained using linear transformation method are as follows: {}". format(fourier_transform_l_t))

# Compute Magnitude and Phase Spectrum of DFT Coefficients
magnitude_spectrum_l_t = []
phase_spectrum_l_t = []
for sample in range(len(fourier_transform_l_t)):
    magnitude_spectrum_l_t.append((fourier_transform_l_t[sample].real**2 + fourier_transform_l_t[sample].imag**2)**0.5)
    phase_l_t = np.arctan(fourier_transform_l_t[sample].imag / fourier_transform_l_t[sample].real)
    phase_spectrum_l_t.append(phase_l_t)
    
# Sketch Magnitude Spectrum Using Linear Transformation Method
plt.xlabel('k')
plt.ylabel('|x[k]|')
plt.title("Magnitude Spectrum Obtained Using Linear Transformation Method")
plt.stem(np.arange(0, len(magnitude_spectrum_l_t)), magnitude_spectrum_l_t)
plt.grid(True) # Configure the grid lines
plt.show()
print("\nThe magnitude spectrum of DFT coefficients obtained using linear trasnformation method are as follows: {}". format(magnitude_spectrum_l_t))

# Sketch Phase Spectrum Using Linear Transformation Method
plt.xlabel('k')
plt.ylabel('Angle (in radians)')
plt.title("Phase Spectrum Obtained Using Linear Transformation Method")
plt.stem(np.arange(0, len(phase_spectrum_l_t)), phase_spectrum_l_t)
plt.grid(True) # Configure the grid lines
plt.show()
print("\nThe phase spectrum of DFT coefficients obtained using linear trasnformation method are as follows: {}". format(phase_spectrum_l_t))
