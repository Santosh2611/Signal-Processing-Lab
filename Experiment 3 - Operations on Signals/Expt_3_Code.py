# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:56:58 2021

@author: Santosh (dell)
"""

import numpy as np
import matplotlib.pyplot as plt

def step_sub(): # Step Signal Subtraction
    n = np.arange(0,10) # Get evenly spaced values within the interval [0,10)
    
    a=[] # u[n] Null List Declaration
    for sample in range(len(n)):
        if n[sample]>=0:
            temp=1
        else:
            temp=0
        a.append(temp) # Adds a single item to the existing list
    plt.subplot (5,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('u [n]')
    plt.title('Unit Step Discrete-Time Function for u[n]')
    plt.stem(n,a) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.

    b=[] # u[n-2] Null List Declaration
    for sample in range(len(n)):
        if n[sample]>=2:
            temp=1
        else:
            temp=0
        b.append(temp) # Adds a single item to the existing list
    plt.subplot (5,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('u [n-2]')
    plt.title('Unit Step Discrete-Time Function for u[n-2]')
    plt.stem(n,b) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.

    result=[] # u[n] - u[n-2] Null List Declaration
    for sample in range(len(n)):
        result.append(a[sample]-b[sample]) # Adds a single item to the existing list by subtracting u[n-2] from u[n] list.
    plt.subplot (5,1,5) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('u [n] - u [n-2]')
    plt.title('Unit Step Discrete-Time Function for u[n] - u[n-2]')
    plt.stem(n,result) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view all the three sub-plots.
    
def impulse_plot(): # Plot Impulse Signal
    n=np.arange(0, 5) # Get evenly spaced values within the interval [0,5)
    arr=[2,3,4,5,0] # Intialize array with values as given in question.
    plt.xlabel('n')
    plt.ylabel('x [n]')
    plt.title('Unit Impulse Discrete-Time Function for x[n] = [2 3 4 5 0]')
    plt.stem(n,arr) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view the plot.
    
def x_of_n(n): # Generate x[n] as given in the question
    list=[] # Null List Declaration
    for sample in n:
        if sample<=3:
            if sample>=-3:
                list.append(abs(sample)) # abs() returns the absolute value of a number
            else:
                list.append(0) # Adds a single item to the existing list.
        else:
            list.append(0) # Adds a single item to the existing list.
    return (list) # Send the value of list back and exits the function.

def y_of_n(n): # Generate y[n] as given in the question
    list=[] # Null List Declaration
    for sample in n:
        if sample==0:
            list.append(0) # Adds a single item to the existing list.
        elif sample<=4:
            if sample>=-4:
                list.append(sample/abs(sample)) # abs() returns the absolute value of a number.
            else:
                list.append(0) # Adds a single item to the existing list.
        else:
            list.append(0) # Adds a single item to the existing list.
    return(list) # Send the value of list back and exits the function.

def sketch_1(): # Sketch x[3n - 1]
    n = np.arange(-6,7) # Get evenly spaced values within the interval [-6,7)
    plt.subplot(3,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('x [n]')
    plt.title('Function for x[n]')
    plt.stem(n, x_of_n(n)) # Calls the function x_of_n(n) and displays x[n] plot.
    
    list=[] # Null List Declaration
    for sample in n:
        list.append(3*sample -1)  # Adds a single item to the existing list, x[3n-1] 

    plt.subplot(3,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('x [3n-1]')
    plt.title('Function for x[3n-1]')
    plt.stem(n, x_of_n(list)) # Calls the function x_of_n(list) and displays x[3n-1] plot.
    plt.show() # To view both the sub-plots.
    
def sketch_2(): # Sketch x[n – 2] + y[n + 2]
    n = np.arange(-6,7) # Get evenly spaced values within the interval [-6,7)
    
    list_x=[] # Null List Declaration
    for sample in n:
        list_x.append(sample - 2)  # Adds a single item to the existing list, x[n-2] 
        
    plt.subplot(5,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('x [n-2]')
    plt.title('Function for x[n-2]')
    plt.stem(n, x_of_n(list_x)) # Calls the function x_of_n(list_x) and displays x[n-2] plot.
   
    list_y=[] # Null List Declaration
    for sample in n:
        list_y.append(sample + 2) # Adds a single item to the existing list, y[n+2]
    
    plt.subplot(5,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('y [n+2]')
    plt.title('Function for y[n+2]')
    plt.stem(n, y_of_n(list_y)) # Calls the function y_of_n(list_y) and displays y[n+2] plot.
    
    result = np.add(x_of_n(list_x),y_of_n(list_y)) # Display the resultant graph, x[n – 2] + y[n + 2]
    plt.subplot(5,1,5) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('x[n-2]+y[n+3]')
    plt.title('Function for x[n-2] + y[n+3]')
    plt.stem(n, result) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    plt.show() # To view all the three sub-plots.

# Main
while True:  # This simulates a Do Loop
    choice = input(
        "MENU:\n   1. Step Signal Subtraction.\n   2. Plot Impulse Signal.\n   3. Sketch x[3n - 1].\n   4. Sketch x[n – 2] + y[n + 2].\n   5. Exit\nEnter the number corresponding to the menu to implement the choice: ") # Menu Driven Implementation

    if choice == str(1): # str() returns the string version of the variable "choice"
        step_sub() # Step Signal Subtraction
    elif choice == str(2):
        impulse_plot() # Plot Impulse Signal
    elif choice == str(3):
        sketch_1() # Sketch x[3n - 1]
    elif choice == str(4):
        sketch_2() # Sketch x[n – 2] + y[n + 2]
    elif choice == str(5): 
        break  # Exit loop
    else:
        print("Error: Invalid Input! Please try again.")
