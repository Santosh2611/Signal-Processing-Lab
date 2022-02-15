# import library source files
import numpy as np
import matplotlib.pyplot as plt

# Given Periodic Sequence
size_input = int(input("Enter the size of input x[n]: "))
user_defined_input = [0] * (size_input)
print("Enter the elements of the input x[n] one-by-one as follows: -")
for sample in range(0, size_input, 1):
    user_defined_input[sample] = input("Element " + str(sample+1) + ": ")
print("\nThe entered input x[n] is: - " + str(user_defined_input) + "\n")

# Null Array Declaration
x = []
fourier_series = []

# Compute Fundamental Time Period
for sample in range(1, size_input-1):
    x.append(user_defined_input[sample-1])
    if user_defined_input[0] == user_defined_input[sample]:
        breakpoint = sample - 2 # How many times does the sequence repeat?
        break
    
# Obtain Frequency Domain Representation
boldface = int(input("Enter the element position that indicates n = 0 index: "))
index = int((boldface - 1)/len(x))

# Sketch Input Sequence
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title("Input Sequence: ...{}...".format(x))
plt.stem(np.arange(-(index * len(x)), len(x) * (breakpoint - index)), x * breakpoint)
plt.show()

# Compute Fourier Series
def summation(k):
    sum = 0
    for n in range(len(x)):
        exponential = np.exp(-2j * np.pi * k * n / len(x))
        sum = sum + float(x[n])*exponential
    return (sum)

# Compute Fourier Series Coefficients
for k in range(len(x)):
    fourier_series.append(summation(k)/len(x))
print("\nThe Fourier Series Coefficients are as follows: {}".format(fourier_series))

# Compute Magnitude and Phase Spectrum
magnitude_spectrum = []
phase_spectrum = []
for sample in range(len(fourier_series)):
    magnitude_spectrum.append((fourier_series[sample].real**2 + fourier_series[sample].imag**2)**0.5)
    phase = np.arctan(fourier_series[sample].imag/fourier_series[sample].real)
    phase_spectrum.append(phase)
    
# Sketch Magnitude Spectrum
plt.xlabel('k')
plt.ylabel('|x[k]|')
plt.title("Magnitude Spectrum: ...{}...".format(magnitude_spectrum))
plt.stem(np.arange(0, len(magnitude_spectrum)), magnitude_spectrum)
plt.show()
print("\nThe Magnitude Spectrum is as follows: {}".format(magnitude_spectrum))

# Sketch Phase Spectrum
plt.xlabel('k')
plt.ylabel('Angle (in radians)')
plt.title('Phase Spectrum: ...{}...'.format(phase_spectrum))
plt.stem(np.arange(0, len(phase_spectrum)), phase_spectrum)
plt.show()
print("\nThe Phase Spectrum is as follows: {}". format(phase_spectrum))
