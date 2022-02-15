# import library source files
import numpy as np
import matplotlib.pyplot as plt

# Given Input Sequence x[n]
size_input = int(input("Enter the size of input x[n]: "))
user_defined_input = [0] * (size_input)
print("Enter the elements of the input x[n] one-by-one as follows: -")
for sample in range(0, size_input, 1):
    user_defined_input[sample] = input("Element " + str(sample+1) + ": ")
print("\nThe entered input x[n] is: - " + str(user_defined_input) + "\n")

# Null Array Declaration for Input Sequence x[n]
x = []
fourier_series_x = []
magnitude_spectrum_x = []
phase_spectrum_x = []

# Null Array Declaration for Resulting Sequence y[n]
y = []
fourier_series_y = []
magnitude_spectrum_y = []
phase_spectrum_y = []

# Compute Fundamental Time Period for x[n]
for sample in range(1, size_input-1):
    x.append(user_defined_input[sample-1])
    if user_defined_input[0] == user_defined_input[sample]:
        breakpoint = sample - 2 # How many time does the sequence repeat?
        break
    
# Obtain Frequency Domain Representation
boldface = int(input("Enter the element position that indicates n = 0 index: "))
index = int((boldface-1)/len(x))

# Sketch Input Sequence x[n]
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title("Input Sequence: ...{}...".format(x))
plt.stem(np.arange(-(index*len(x)), len(x)*(breakpoint-index)), x*breakpoint)
plt.show()

# Compute Fourier Series for x[n]
def summation(k):
    sum = 0
    for n in range(len(x)):
        exponential = np.exp(-2j * np.pi * k * n / len(x))
        sum = sum + float(x[n]) * exponential
    return (sum)

# Compute Fourier Coefficients for x[n]
for k in range(len(x)):
    fourier_series_x.append(summation(k)/len(x))
print("\nThe Fourier Coefficients for x[n] are as follows: {}".format(fourier_series_x))

# Sketch Fourier Coefficients of x[n]
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title("Fourier Coefficients of x[n]")
plt.stem(np.arange(0, len(fourier_series_x)), np.real(fourier_series_x))
plt.show()

# Compute Magnitude and Phase Spectrum for x[n]
for sample in range(len(fourier_series_x)):
    magnitude_spectrum_x.append((fourier_series_x[sample].real**2 + fourier_series_x[sample].imag**2)**0.5)
    phase = np.arctan(fourier_series_x[sample].imag/fourier_series_x[sample].real)
    phase_spectrum_x.append(phase)
    
# Sketch Magnitude Spectrum of x[n]
plt.xlabel('k')
plt.ylabel('|x[k]|')
plt.title("Magnitude Spectrum of x[n]: ...{}...".format(magnitude_spectrum_x))
plt.stem(np.arange(0, len(magnitude_spectrum_x)), magnitude_spectrum_x)
plt.show()
print("\nThe Magnitude Spectrum of x[n] is as follows: {}".format(magnitude_spectrum_x))

# Sketch Phase Spectrum of x[n]
plt.xlabel('k')
plt.ylabel('Angle (in radians)')
plt.title("Phase Spectrum of x[n]: ...{}...".format(phase_spectrum_x))
plt.stem(np.arange(0, len(phase_spectrum_x)), phase_spectrum_x)
plt.show()
print("\nThe Phase Spectrum of x[n] is as follows: {}".format(phase_spectrum_x))

intermediate = []

# Copy Input Sequence to Temporary Sequence intermediate[n]
for sample in range(size_input):
    intermediate.append(user_defined_input[sample])
    
# Input Shifting Factor
shifting_factor = int(input("\nEnter the shifting factor: "))

# Shift Temporary Sequence by "shifting_factor" of units
for i in range(shifting_factor):
    intermediate.append(0) # Adds required zeros at the end of list
    for j in range(len(intermediate)-1, 0, -1):
        intermediate[j] = intermediate[j-1] # Shifts the zeros at the beginning of list
    intermediate[i] = 0 # Prepare for next iteration
    
# Place rest of elements in relevant position
temp = size_input - shifting_factor
for k in range(shifting_factor):
    intermediate[k] = user_defined_input[temp]
    temp = temp + 1
    
# Compute Fundamental Time Period for y[n]
for sample in range(1, size_input-1):
    y.append(intermediate[sample-1])
    if user_defined_input[0] == user_defined_input[sample]:
        break

print("\nThe resulting sequence y[n] is: - " + str(y) + "\n")

# Sketch Resulting Sequence y[n]
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title("Resulting Sequence: ...{}... ". format(y))
plt.stem(np.arange(-(index*len(y)),len(y)*(breakpoint-index)),y*breakpoint)
plt.show()

# Compute Fourier Coefficients for y[n]
for k in range(len(x)):
    fourier_series_y.append(np.exp(-2j * np.pi * k * shifting_factor / len(x)) * fourier_series_x[k])
print("\nThe Fourier Coefficients for y[n] are as follows: {}".format(fourier_series_y))

# Sketch Fourier Coefficients of y[n]
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title("Fourier Coefficients of y[n]")
plt.stem(np.arange(0, len(fourier_series_y)), np.real(fourier_series_y))
plt.show()

# Compute Magnitude and Phase Spectrum for y[n]
for sample in range(len(fourier_series_y)):
    magnitude_spectrum_y.append((fourier_series_y[sample].real**2 + fourier_series_y[sample].imag**2)**0.5)
    phase = np.arctan(fourier_series_y[sample].imag/fourier_series_y[sample].real)
    phase_spectrum_y.append(phase)
    
# Sketch Magnitude Spectrum of y[n]
plt.xlabel('k')
plt.ylabel('|y[k]|')
plt.title("Magnitude Spectrum of y[n]: ...{}...".format(magnitude_spectrum_y))
plt.stem(np.arange(0, len(magnitude_spectrum_y)), magnitude_spectrum_y)
plt.show()
print("\nThe Magnitude Spectrum of y[n] is as follows: {}".format(magnitude_spectrum_y))

# Sketch Phase Spectrum of y[n]
plt.xlabel('k')
plt.ylabel('Angle (in radians)')
plt.title("Phase Spectrum of y[n]: ...{}...".format(phase_spectrum_y))
plt.stem(np.arange(0, len(phase_spectrum_y)), phase_spectrum_y)
plt.show()
print("\nThe Phase Spectrum of y[n] is as follows: {}".format(phase_spectrum_y))
