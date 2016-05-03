# Kirsten Richmond

# Program 02

#2.3


#defining functions

def add(x, y):  #this function adds two numbers
    return x + y

def subtract(x, y): #defining the function of subtracting numbers
    return x - y

def multiply(x, y): #defining the function of multiplying two numbers
    return x * y

def divide(x, y): #defininf the function of dividing two numbers
    return x / y


#taking input from the user

  

print("Select which operation you would like to use")
print("1.Addition") #if the user wants to add
print("2.Subtraction") #selects 2 if they want to subtract
print("3.Multiplication") #selects 3 if they want to multiply
print("4.Division") #selects 4 if they want to divide

   

while (True):
        choice = input("Enter your choice(1/2/3/4):") #this will be the choice the user makes

        num1 = int(input("Enter the first number: ")) #after the user chose the function
#they choose what the first number will be

        num2 = int(input("Enter the second number: ")) #the user will enter the second
#number that they want to use in the equation


#if the user chooses number 1
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
    #this function will take the two numbers the user input and add them

#if the user chooses choice 2
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
    #this function will take the numbers the user chose and subtract them

#if the user chooses number 3    
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    #this function takes the two numbers the user chose and mutiplies them


#if the user chooses number 4
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        else:
            print("Invalid Input")

        input("Would you like to start again? Y/N")
        if 'Y':
            continue
        elif 'N':
            print ("goodbye")
            break
        
        







