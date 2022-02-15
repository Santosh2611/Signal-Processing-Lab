# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:56:03 2021

@author: DeLL
"""

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal_c(): # Sinusoidal Continuous-Time Signal
    t = np.linspace(-0.02, 0.05, 1000) # linspace() creates evenly spaced sequences
    plt.plot(t, 325 * np.sin(2 * np.pi * 50 * t))
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Plot of CT signal: x(t) = 325*sin(100*pi*t)')
    plt.xlim([-0.02, 0.05]) # Set the x-limits of the current axes
    plt.show() # To view your plot

def sinusoidal_d(): # Sinusoidal Discrete-Time Signal
    n = np.arange(50) # Get evenly spaced values within a given interval
    dt = 0.07/50 # Fixes Signal Space Resolution
    x = 325 * np.sin(2 * np.pi * 50 * n *dt)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title('Plot of DT signal: x[n] = 325*sin(100*pi*n)')
    plt.stem(n, x) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view your plot
    
def exponential_c(): # Exponential Continuous-Time Signal
    t = np.linspace(-0.02, 0.05, 1000) # linspace() creates evenly spaced sequences
    plt.subplot(3,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.plot(t, np.exp(2j * np.pi * 50 *t).real) # Return the real part of the complex argument
    plt.xlabel('t')
    plt.ylabel('Re x(t)')
    plt.title('Real part of x(t)=exp(j*100*pi*t)')
    plt.xlim([-0.02, 0.05]) # Set the x-limits of the current axes
    plt.subplot(3,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.plot(t, np.exp(2j * np.pi *50 *t).imag) # Return the imaginary part of the complex argument
    plt.xlabel('t')
    plt.ylabel('Im x(t)')
    plt.title('Imaginary part of x(t)=exp(j*100*pi*t)')
    plt.xlim([-0.02, 0.05]) # Set the x-limits of the current axes
    plt.show() # To view your plot

def exponential_d(): # Exponential Discrete-Time Signal
    n=np.arange(-2,5) # Get evenly spaced values within a given interval
    arr=[] # Null Array Declaration
    for sample in range(len(n)): # Returns the length of the array
        if n[sample]<0:
            temp=1/(2**-(n[sample])) # Conversion of negative power to fractions (2^-1 = 1/2)
        else:
            temp=(2**(n[sample]))
        arr.append(temp) # Adds a single item to the existing list
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title('Plot of DT signal: x[n]=2^n')
    plt.stem(n,arr) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view your plot

def step_c(): # Unit Step Continuous-Time Signal
    t=np.linspace(-2, 10, 1000) # linspace() creates evenly spaced sequences
    arr=[] # Null Array Declaration
    for sample in range(len(t)): # Returns the length of the array
        if t[sample]>=0:
            temp=1
        else:
            temp=0
        arr.append(temp) # Adds a single item to the existing list
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Unit Step Continuous-Time Function')
    plt.step(t,arr) # Line forming a series of steps between data points
    plt.show() # To view your plot
    
def step_d(): # Unit Step Discrete-Time Signal
    n=np.arange(-2, 10) # Get evenly spaced values within a given interval
    arr=[] # Null Array Declaration
    for sample in range(len(n)): # Returns the length of the array
        if n[sample]>=0:
            temp=1
        else:
            temp=0
        arr.append(temp) # Adds a single item to the existing list
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.title('Unit Step Discrete-Time Function for 0 ≤ n ≤ 9')
    plt.stem(n,arr) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view your plot
    
def impulse_c(): # Unit Impulse Continuous-Time Signal
    t=np.arange(-2, 10) # Get evenly spaced values within a given interval
    arr=[] # Null Array Declaration
    for sample in range(len(t)): # Returns the length of the array
        if t[sample]==0:
            temp=1
        else:
            temp=0
        arr.append(temp) # Adds a single item to the existing list
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Unit Impulse Continuous-Time Function')
    plt.plot(t,arr) # Line forming a series of steps between data points
    plt.show() # To view your plot
    
def impulse_d(): # Unit Impulse Discrete-Time Signal
    n=np.arange(-2, 10) # Get evenly spaced values within a given interval
    arr=[] # Null Array Declaration
    for sample in range(len(n)): # returns the length of the array
        if n[sample]==0:
            temp=1
        else:
            temp=0
        arr.append(temp) # Adds a single item to the existing list
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.title('Unit Impulse Discrete-Time Function for 0 ≤ n ≤ 9')
    plt.stem(n,arr) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view your plot
    
def ramp_c(): # Ramp Function Continuous-Time Signal
    t=np.linspace(0, 10, 1000) # linspace() creates evenly spaced sequences
    plt.plot(t,t)
    plt.xlabel('t')
    plt.ylabel('r(t)')
    plt.title('Ramp Continuous-Time Function')
    plt.xlim([0, 10]) # Set the x-limits of the current axes
    plt.show() # To view your plot
    
def ramp_d(): # Ramp Function Discrete-Time Signal
    n=np.arange(0, 10) # linspace() creates evenly spaced sequences
    plt.xlabel('n')
    plt.ylabel('n(t)')
    plt.title('Ramp Discrete-Time Function for 0 ≤ n ≤ 9')
    plt.stem(n,n) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view your plot

# Main
while True:  # This simulates a Do Loop
    choice = int(input(
        "MENU:\n   1. Sinusoidal Continuous-Time Signal.\n   2. Sinusoidal Discrete-Time Signal.\n   3. Exponential Continuous-Time Signal.\n   4. Exponential Discrete-Time Signal.\n   5. Unit Step Continuous-Time Signal.\n   6. Unit Step Discrete-Time Signal.\n   7. Unit Impulse Continuous-Time Signal.\n   8. Unit Impulse Discrete-Time Signal.\n   9. Ramp Function Continuous-Time Signal.\n   10. Ramp Function Discrete-Time Signal.\n   11. Exit\nEnter the number corresponding to the menu to implement the choice: ")) # Menu Based Implementation

    if choice == 1:
        sinusoidal_c() # Sinusoidal Continuous-Time Signal
    elif choice == 2:
        sinusoidal_d() # Sinusoidal Discrete-Time Signal
    elif choice == 3:
        exponential_c() # Exponential Continuous-Time Signal
    elif choice == 4:
        exponential_d() # Exponential Discrete-Time Signal
    elif choice == 5:
        step_c() # Unit Step Continuous-Time Signal
    elif choice == 6:
        step_d() # Unit Step Discrete-Time Signal
    elif choice == 7:
        impulse_c() # Unit Impulse Continuous-Time Signal
    elif choice == 8:
        impulse_d() # Unit Impulse Discrete-Time Signal
    elif choice == 9:
        ramp_c() # Ramp Function Continuous-Time Signal
    elif choice == 10:
        ramp_d() # Ramp Function Discrete-Time Signal
    elif choice == 11: 
        break  # Exit loop
    else:
        print("Error: Invalid Input! Please try again.")
