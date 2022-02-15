import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,10) # Get evenly spaced values within the interval [0,10)
    
a=[] # u[n] Null List Declaration
for sample in range(len(n)):
    if n[sample]>=0:
        temp=1
    else:
        temp=0
    a.append(temp)
plt.subplot (5,1,1)
plt.xlabel('n')
plt.ylabel('u[n]')
plt.title('Unit Step Discrete-Time Function for u[n]')
plt.stem(n,a)

b=[] # u[n-3] Null List Declaration
for sample in range(len(n)):
    if n[sample]>=3:
        temp=1
    else:
        temp=0
    b.append(temp)
plt.subplot (5,1,3)
plt.xlabel('n')
plt.ylabel('u[n-3]')
plt.title('Unit Step Discrete-Time Function for u[n-3]')
plt.stem(n,b)

result=[] # u[n-3] - u[n] Null List Declaration
for sample in range(len(n)):
    result.append(b[sample]-a[sample])
plt.subplot (5,1,5)
plt.xlabel('n')
plt.ylabel('u[n-3] - u[n]')
plt.title('Unit Step Discrete-Time Function for u[n-3] - u[n]')
plt.stem(n,result)
plt.show()
    
temp=[] # (u[n-3] - u[n])*0.5^n Null List Declaration
for sample in range(len(n)):
    temp.append((b[sample]-a[sample])*0.5**sample)
plt.xlabel('n')
plt.ylabel('(u[n-3] - u[n])*0.5^n')
plt.title('Impulse Response h[n]')
plt.stem(n,temp)
plt.show()

# Compute Frequency Response
frequency_response=[]
def summation(f):
    sum=0
    for k in range(len(temp)):
        exponential = np.exp(-2j * np.pi * k * f)
        sum = sum + float(temp[k])*exponential
    return(sum)

for w in range(len(temp)):
    frequency_response.append(summation(w))    

# Sketch Frequency Response
plt.xlabel('ω')
plt.ylabel('h(ω)')
plt.title("Frequency Response")
plt.plot(np.arange(0,len(frequency_response)),np.real(frequency_response))
plt.show()
print("\nThe Frequency Response of h[n] is as follows: {}".format(frequency_response))

# Compute Magnitude and Phase Spectrum
magnitude_spectrum = []
phase_spectrum = []

for sample in range(len(frequency_response)):
    magnitude_spectrum.append((frequency_response[sample].real**2 + frequency_response[sample].imag**2)**0.5)
    phase = np.arctan(frequency_response[sample].imag/frequency_response[sample].real)
    phase_spectrum.append(phase)

# Sketch Magnitude Spectrum
plt.xlabel('ω')
plt.ylabel('|h(ω)|')
plt.title("Magnitude Spectrum: ...{}...".format(magnitude_spectrum))
plt.plot(np.arange(0,len(magnitude_spectrum)),magnitude_spectrum)
plt.show()
print("\nThe Magnitude Spectrum of h[n] is as follows: {}".format(magnitude_spectrum))

# Sketch Phase Spectrum
plt.xlabel('ω')
plt.ylabel('Angle (in radians)')
plt.title("Phase Spectrum Φ(ω)")
plt.plot(np.arange(0,len(phase_spectrum)),phase_spectrum)
plt.show()
print("\nThe Phase Spectrum of h[n] is as follows: {}".format(phase_spectrum))
