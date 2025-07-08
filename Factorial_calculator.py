def Process():

    def factorial(n):
        
        fact = 1
        
        for i in range(1,n+1):
            fact*=i
            
        print(f"The factorial of {n} is {fact}")

    def Loop():
        
        reply = input("Do you want to get the factorial for another number(Yes or No): ")

        if "yes" in reply.lower():
            calc()
        else:
            print(f"Thank you so much {name} for using khat's incredible factorial calculator!")

    def calc():
        
        num = int(input("Enter the number whose factorial you want: "))
        
        if num == 0:
            print(f"The factorial of 0 is 1")
            Loop()
        elif num == 1:
            print(f"The factorial of 1 is 1")
            Loop()
        elif num < 0:
            print("You are entering an invalid number!")
            Loop()
        elif num > 1:
            factorial(num)
            Loop()
            
    print(f"This is a factorial calculator!")
    print(f"I can give you the factorial of any number if it is valid")
    print(f"Let us collect some minor details about you!")
        
    name = input("Enter your name: ")

    print(f"Hey there {name}! let us go to the calculator part")
        

    calc()
        

if __name__ == "__main__":

    try:

        Process()

    except ValueError:

        print("This type of value you entered is invalid")
    
    except Exception as E:

        print(E)