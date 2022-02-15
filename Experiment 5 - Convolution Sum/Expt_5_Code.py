# import library source files
import numpy as np
import matplotlib.pyplot as plt

size_x = int(input("Enter the size of input x[n]: "))
x = [0] * (size_x) # Declare an array with the number of elements equal to value of size.
print("Enter the elements of the input x[n] one-by-one as follows: -")
for i in range(0, size_x, 1):
    x[i] = input("Element " + str(i+1) + ": ")
print("The entered input x[n] is: - " + str(x) + "\n")

plt.subplot(3,1,1)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Input x{}'.format(x)) # Formats the specified value(s) and insert them inside the string's placeholder.
plt.stem(np.arange(0,size_x),x)

size_h = int(input("Enter the size of impulse response h[n]: "))
h = [0] * (size_h) # Declare an array with the number of elements equal to value of size.
print("Enter the elements of the impulse response h[n] one-by-one as follows: -")
for i in range(0, size_h, 1):
    h[i] = input("Element " + str(i+1) + ": ")
print("The entered impulse response h[n] is: - " + str(h) + "\n")

plt.subplot(3,1,3)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response h{}'.format(h)) # Formats the specified value(s) and insert them inside the string's placeholder.
plt.stem(np.arange(0,size_h),h)

plt.show()

temp = [] # Duplicate for impulse response
for i in range(size_x):
    temp=h.copy() # Creates a copy of an existing list
    for j in range(len(temp)):
        temp[j]=int(temp[j]) * int(x[i]) 
    for k in range(i):
        temp.append(0) # Adds required zeros at the end of list
        for l in range(len(temp)-1,0,-1):
            temp[l] = temp[l-1] # Shifts the zeros to the beginning of the list
        temp[k] = 0 # Prepares for next iteration
    plt.title('Intermediate plot x[{}] * h[n-{}] = {}'.format(i,i,temp)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.xlabel('n')
    plt.ylabel('x[{}] * h[n-{}]'.format(i,i)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.stem(np.arange(0,len(temp)),temp)
    plt.show()

# String padding refers to adding, usually, non-informative characters to a string to one or both ends of it. This is most often done for output formatting and alignment purposes, but it can have useful practical applications. numpy.pad() function is used to pad the numpy arrays.

size = (size_x + size_h) - 1 # Compute the size of system response
x = np.pad(x,(0,size - size_x),'constant')
h = np.pad(h,(0,size - size_h),'constant')
y = np.zeros(size, dtype = int) # Returns a new array of given shape and type, with zeros.
iteration = 1 # Variable used for displaying the iteration sequence
    
for i in range (size):
    for j in range (size):
        if i >= j:
            y[i] = int(y[i] + (int(x[i-j])*int(h[j]))) 
            print("Iteration " + str(iteration) + ": " + str(y))  # Display result of each iteration
            iteration += 1
print("\nThe system response is: - " + str(y) + "\n")

plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('System Response y{}'.format(y)) # Formats the specified value(s) and insert them inside the string's placeholder.
plt.stem(np.arange(0,size),y)
plt.show()
