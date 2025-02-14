import math
import statistics
import numpy as np
from sympy import Matrix, symbols
from statistics import mode

def standard_mode():
    # Basic arithmetic operations
    while True:
        print("Select operation:")
        print("1. addition")
        print("2. Subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. floor division")
        print("6. Exponentiation")
        print("7. Square Root")
        print("8. Percent")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice in ('1', '2', '3', '4', '5', '6'):
            a= int(input("enter first number: "))
            b= int(input("enter second number: "))
            if choice == '1':
                print(a+b)
            elif choice == '2':
                print(a-b)
            elif choice == '3':
                print(a*b)
            elif choice == '4':
                print(a/b)
            elif choice == '5':
                print(a//b)
            elif choice == '6':
                print(a**b)
            else:
                print("Invalid value. Please try again.")
        elif choice == '7':
            a = int(input("enter number to find square root: "))
            print(math.sqrt(a))
        elif choice == '8':
            a = int(input("enter number to find percentage: "))
            b = int(input("enter total number"))
            print(a/b*100)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
    pass

def scientific_mode():
    # Trigonometric, logarithmic, and exponential functions
    # Trigonometric function
    while True:
        print("Select function type: ")
        print("1. Trigonometric function")
        print("2. Logarithmic function")
        print("3. Exponential function")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice =='1':
            print("Select Trigonometric function: ")
            print("1. sin")
            print("2. cos")
            print("3. tan")
            print("4. cosec")
            print("5. sec")
            print("6. cot")
            print("7, Exit")
            choice = input("Enter choice: ")
            angle_degrees = float(input("enter value of angle in degrees: "))
            angle = angle_degrees*(math.pi/180)
            if choice == '1':
                sin_value = math.sin(angle)
                print("Sine of ",angle_degrees," degrees is :", sin_value)
            elif choice == '2':
                cos_value = math.cos(angle)
                print("Cosine of ",angle_degrees," degrees is :", cos_value)
            elif choice == '3':
                tan_value = math.tan(angle)
                print("Tangent of ",angle_degrees," degrees is :", tan_value)
            elif choice == '4':
                sin_value = math.sin(angle)
                if sin_value !=0 :
                    cosec_value = 1/sin_value
                    print("cosec of",angle_degrees," degrees is :", cosec_value)
                else:
                    print("cosec of",angle_degrees,"degrees is not defined")
            elif choice == '5':
                cos_value = math.cos(angle)
                if cos_value != 0:
                    sec_value = 1 / cos_value
                    print("sec of", angle_degrees, " degrees is :", sec_value)
                else:
                    print("sec of", angle_degrees, "degrees is not defined")
            elif choice == '6':
                tan_value = math.tan(angle)
                if tan_value != 0:
                    cot_value = 1 / tan_value
                    print("cot of", angle_degrees, " degrees is :", cot_value)
                else:
                    print("cot of", angle_degrees, "degrees is not defined")
            elif choice == '7':
                break
            else:
                print("Invalid value. Please try again.")

    #Logarithmic function
        elif choice == '2':
            print("select base option: ")
            print("1. e")
            print("2. 2")
            print("3. 10")
            print("4. Exit")
            choice = input("enter choice: ")
            x = float(input("enter any number to find log: "))
            if choice == '1':
                log_value = math.log(x)
                print("Natural logarithm of ", x ,"is :", log_value)
            elif choice == '2':
                log10_value = math.log2(x)
                print("Logarithm base 2 of ", x ,"is :", log10_value)
            elif choice == '3':
                log10_value = math.log10(x)
                print("Logarithm base 10 of ", x ,"is :", log10_value)
            elif choice == '4':
                break
            else:
                print("Invalid value. Please try again.")
    #Exponential functions
        elif choice == '3':
            value = float(input("enter value to find exponential function: "))
            exp_value = math.exp(value)
            print("Exponential of ", value ,"is :", exp_value)
        elif choice == '4':
            break
        else:
            print("Invalid value. Please try again.")
    pass
def engineering_mode():
    # Additional engineering calculations
    pass

def programming_mode():
    # Binary, octal, decimal, and hexadecimal calculations
    while True:
        print("Select operation:")
        print("1. conversion")
        print("2. boolean algebra/logic gate")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            print("Select conversion:")
            print("1. binary_to_decimal")
            print("2. decimal_to_binary")
            print("3. octal_to_decimal")
            print("4. decimal_to_octal")
            print("5. hexadecimal_to_decimal")
            print("6. decimal_to_hexadecimal")
            print("7. Exit")
            choice1 = input("Enter choice: ")
            if choice1 == '1':
                a = input("enter binary number to convert into decimal: ")
                print("decimal number for entered binary number",a,"is",int(a,2))
            elif choice1 == '2':
                a = int(input("Enter decimal number to convert into binary: "))
                print("Binary number for entered decimal number", a, "is", bin(a)[2:])
            elif choice1 == '3':
                a = input("Enter octal number to convert into decimal: ")
                print("Decimal number for entered octal number", a, "is", int(a, 8))
            elif choice1 == '4':
                a = int(input("Enter decimal number to convert into octal: "))
                print("Octal number for entered decimal number", a, "is", oct(a)[2:])
            elif choice1 == '5':
                a = input("Enter hexadecimal number to convert into decimal: ")
                print("decimal number for entered hexadecimal number", a, "is", int(a,16))
            elif choice1 == '6':
                a = int(input("Enter decimal number to convert into hexadecimal: "))
                print("hexadecimal number for entered decimal number", a, "is", hex(a)[2:])
            elif choice == '7':
                break
            else:
                print("Invalid value. Please try again.")
        elif choice == '2':
            a = int(input("enter value of first input"))
            b = int(input("enter value of second input"))
            print("Select operation/logic gate:")
            print("1. AND")
            print("2. OR")
            print("3. NAND")
            print("4. NOR")
            print("5. XOR")
            print("6. XNOR")
            print("7. Exit")
            choice1 = input("Enter choice: ")
            if choice1 == '1':
                print("output of AND gate: ",a and b)
            elif choice1 == '2':
                print("output of OR gate: ",a or b)
            elif choice1 == '3':
                print("output of NAND gate: ",not(a and b))
            elif choice1 == '4':
                print("output of NOR gate: ",not (a or b))
            elif choice1 == '5':
                print("output of XOR gate: ",a ^ b)
            elif choice1 == '6':
                print("output of NXOR gate: ",not (a ^ b))
            elif choice1 == '7':
                break
            else:
                print("Invalid value. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    pass

def statistical_mode():
    # Statistical calculations
    data_input = input("Enter a list of numbers separated by spaces: ")
    data = [float(num) for num in data_input.split()]
    while True:
        print("Select operation:")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Variance")
        print("5. Standard Deviation")
        print("6. Exit")
        choice1 = input("Enter choice: ")
        if choice1 == '1':
            mean  = sum(data)/len(data)
            print("mean of given data", data ," is: ",mean)
        elif choice1 == '2':
            data.sort()
            n = len(data)
            median = (data[n // 2] + data[-(n + 1) // 2]) / 2
            print("median of given data", data , " is: ", median)
        elif choice1 == '3':
            mode_v = mode(data)
            print("mode of given data", data ,"is: ", mode_v)
        elif choice1 == '4':
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            print("variance of given data", data, "is: ",variance )
        elif choice1 == '5':
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            standard_deviation = math.sqrt(variance)
            print("Standard Deviation of given data", data ,"is: ", standard_deviation)
        elif choice1 == '6':
            break
        else:
            print("Invalid value. Please try again.")
    pass

def fraction_mode():
    # Handling fractions
    pass

def complex_mode():
    # Complex number calculations
    pass

def matrix_mode():
    # Matrix operations
    pass

def calculator_menu():
    while True:
        print("Select Mode:")
        print("1. Standard")
        print("2. Scientific")
        print("3. Engineering")
        print("4. Programming")
        print("5. Statistical")
        print("6. Fraction")
        print("7. Complex Number")
        print("8. Matrix")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            standard_mode()
        elif choice == '2':
            scientific_mode()
        elif choice == '3':
            engineering_mode()
        elif choice == '4':
            programming_mode()
        elif choice == '5':
            statistical_mode()
        elif choice == '6':
            fraction_mode()
        elif choice == '7':
            complex_mode()
        elif choice == '8':
            matrix_mode()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator_menu()
