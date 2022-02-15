# import library source files
import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,4) # Get evenly spaced values within the interval [0,4)

# Given Input Sequences:
x1 = [2,4,7,3]
x2 = [1,2,5,3]

def scaling (scale, choice): # Check Homogeneity Condition
    before_scaling=[]; after_scaling=[] 
    
    if choice == str(1): # Calculate for x1 = [2,4,7,3]
        
        for sample in range(len(n)):
            temp = sample * x1[sample]
            before_scaling.append(int(scale)*temp) # Scaling the output
    
        for sample in range(len(n)):
            temp = int(scale) * x1[sample]
            after_scaling.append(sample*temp) # Sending output into system
    
    else: # Calculate for x2 = [1,2,5,3]
        
        for sample in range(len(n)):
            temp = sample * x2[sample]
            before_scaling.append(int(scale)*temp) # Scaling the output
    
        for sample in range(len(n)):
            temp = int(scale) * x2[sample]
            after_scaling.append(sample*temp) # Sending output into system
    
    plt.subplot(3,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('y' + str(choice) + ' [n]')
    plt.title('Before Scaling x' + str(choice) + '{}'.format(before_scaling)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.stem(n,before_scaling) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    
    plt.subplot(3,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('y' + str(choice) + ' [n]')
    plt.title('After Scaling x' + str(choice) + '{}'.format(after_scaling)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.stem(n,after_scaling) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    
    plt.show() # To view both the sub-plots
    
    if (before_scaling == after_scaling): # Condition to check if both the systems are equal or not after scaling
        print("    The given system satisfies Homogeneity Condition.")
        return(1)
    else:
        print("    The given system does not satisfy Homogeneity Condition.")
        return(0)
    
def superposition(): # Check Additivity Condition
    before_adding=[]; after_adding=[]; y1=[]; y2=[]; x=[]
    
    for sample in range(len(n)):
        y1.append(sample*x1[sample])
        y2.append(sample*x2[sample])
        before_adding.append(y1[sample]+y2[sample]) # Processing System Individually
        
    plt.subplot(3,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.title('H (x1 (t) + x2 (t))')
    plt.stem(n,before_adding) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
        
    for sample in range(len(n)):
        x.append(x1[sample]+x2[sample])
        after_adding.append(sample*x[sample]) # Processing System Together
        
    plt.subplot(3,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.title('H (x1 (t)) + H (x2 (t))')
    plt.stem(n,after_adding) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    
    plt.show() # To view both the sub-plots
    
    print('\n   2. Superposition Condition: -')
    if (before_adding == after_adding): # Condition to check if both the systems are equal or not after adding
        print("    The given system satisfies Superposition Condition.")
        return(1)
    else:
        print("    The given system does not satisfy Superposition Condition.")
        return(0)

def time(shift, choice): # Check Time Variance
    input_delay=[]; output_delay=[]
    
    if choice == str(1): # Calculate for x1 = [2,4,7,3]
        
        # Output Delay
        for sample in range(len(x1)):
            output_delay.append(sample*x1[sample]) # Sending output into system
        
        for sample in range(int(shift)):
            output_delay.append(0) # Adds extra sample at the end for shifting
        
        for sample in range(int(shift)):
            for sample in range(len(output_delay)-1,0,-1):
                output_delay[sample]=output_delay[sample-1] # Shift the sample
        
        for sample in range(int(shift)):
            output_delay[sample]=0 # Assign zero to the empty elements for the shifted bit
                
        # Input Delay
        for sample in range(int(shift)):
            x1.append(0) # Adds extra sample at the end for shifting
        
        for sample in range(int(shift)):
            for sample in range(len(x1)-1,0,-1):
                x1[sample]=x1[sample-1] # Shift the sample
        
        for sample in range(int(shift)):
            x1[sample]=0 # Assign zero to the empty elements for the shifted bit
        
        for sample in range(len(x1)):
            input_delay.append(sample*x1[sample]) # Sending input into system
            
    else: # Calculate for x2 = [1,2,5,3]
        
        # Output Delay
        for sample in range(len(x2)):
            output_delay.append(sample*x2[sample]) # Sending output into system
        
        for sample in range(int(shift)):
            output_delay.append(0) # Adds extra sample at the end for shifting
        
        for sample in range(int(shift)):
                for sample in range(len(output_delay)-1,0,-1):
                    output_delay[sample]=output_delay[sample-1] # Shift the sample
        
        for sample in range(int(shift)):
            output_delay[sample]=0 # Assign zero to the empty elements for the shifted bit
                
        # Input Delay
        for sample in range(int(shift)):
            x2.append(0) # Adds extra sample at the end for shifting
        
        for sample in range(int(shift)):
            for sample in range(len(x2)-1,0,-1):
                x2[sample]=x2[sample-1] # Shift the sample
        
        for sample in range(int(shift)):
            x2[sample]=0 # Assign zero to the empty elements for the shifted bit
        
        for sample in range(len(x2)):
            input_delay.append(sample*x2[sample]) # Sending input into system
            
    plt.subplot(3,1,1) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('t')
    plt.ylabel('y (t)')
    plt.title('Shifting input by ' + str(shift) + ' for x' + str(choice) + '{}'.format(input_delay)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.stem(np.arange(len(input_delay)),input_delay) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    
    plt.subplot(3,1,3) # subplot(rows, columns, index) describes the figure layout
    plt.xlabel('t')
    plt.ylabel('y (t)')
    plt.title('Shifting output by ' + str(shift) + ' for x' + str(choice) + '{}'.format(output_delay)) # Formats the specified value(s) and insert them inside the string's placeholder.
    plt.stem(np.arange(len(output_delay)),output_delay) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
    
    plt.show() # To view both the sub-plots
    
    if (input_delay == output_delay): # Condition to check if both the systems are equal or not after shifting.
        print("  Since both the outputs are same, the given system is time invariant.")
        second_condition = 1 
    else:
        print("  Since both the outputs are not same, the given system is time variant.")
        second_condition = 0 
        
    return(second_condition)

# Main
while True:  # This simulates a Do Loop
    choice = input(
        "MENU: Determine whether the system y[n] = nx[n] is linear and time invariant.\n   1. x1 = [2, 4, 7, 3]\n   2. x2 = [1, 2, 5, 3]\n   3. Exit\nEnter the number corresponding to the menu to implement the input sequence: ") # Menu Driven Implementation
    
    if choice == str(1) or choice == str(2):
        
        scale = input ("A linear system is any system that obeys the properties of scaling (homogeneity) and superposition (additivity).\n   \n   1. Homogeneity Condition: -\n    Enter the value for scaling factor: ")
        
        if (scaling(scale, choice) == superposition()): # Condition to check if both the systems are linear or not
            print("\nSince both the properties are satisfied; the given system is linear.")
            first_condition = 1 
        else:
            print("\nSince both the properties are not satisfied; the given system is not linear.")
            first_condition = 0 
        
        shift = input("A system is time-invariant if a time shift (i.e., advance or delay) in the input always results only in an identical time shift in the output.\n  Enter the value for shifting factor: ")
        
        if (first_condition + time(shift, choice) == 2): # Condition to check for LTI system or not
            print("\nThe given system is a Linear Time Invariant (LTI) system.")
        else:
            print("\nThe given system is not a Linear Time Invariant (LTI) system.")
        
        break
    
    elif choice == str(3):
        break  # Exit loop
    
    else:
        print("Error: Invalid Input! Please try again.\n")
