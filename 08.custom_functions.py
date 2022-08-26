# Define the function to convert temperature between different units
# The first function argument (inputValue) is the value of the temperature
# The second function argument (inputUnit) is the unit of the input temperature
# The third function argument (outputUnit) is the desired unit system
# Possible units are K, C, F, and R
def tempCon(inputValue, inputUnit, outputUnit):

    # Start an if statement to convert the input temperature to K
    # If the input units are K
    if inputUnit=="K":

        # Convert input value from K to K
        t=inputValue

    # If the input units are C
    elif inputUnit=="C":

        # Convert input value from C to K
        t=inputValue+273.15

    # If the input units are F
    elif inputUnit=="F":

        # Convert input value from F to K
        t=(inputValue-32)*(5/9)+273.15

    # If the input units are R
    elif inputUnit=="R":

        # Convert input value from R to K
        t=(inputValue-459.67-32)*(5/9)+273.15

    # If the input units are ones that aren't supported
    else:

        # Output an error that incorrect input units were used
        print("Your input unit isn't correct.")

        # End the function so that it doesn't proceed, will return none
        return

    # Start an if statement to convert K to the desired output units
    # If the output units are K
    if outputUnit=="K":

        # Convert K to K
        temp=t

    # If the output units are C
    elif outputUnit=="C":

        # Convert K to C
        temp=t-273.15

    # If the output units are F
    elif outputUnit=="F":

        # Convert K to F
        temp=(t-273.15)*(9/5)+32

    # If the output units are R
    elif outputUnit=="R":

        # Convert K to R
        temp=(t-273.15)*(9/5)+32+459.67

    # If the output units are ones that aren't supported
    else:

        # Output an error that incorrect output units were used
        print("Your output unit isn't correct.")

        # End the function so that it doesn't proceed, will return none
        return

    # return the converted temperature value
    return temp