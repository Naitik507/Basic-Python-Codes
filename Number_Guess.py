import random as r

tries = 0

list1 = []
for i in range(1,11):
    list1.append(i)

num = r.choice(list1)

print("We are playing guess the number you have to find out computer's number!")

def game(tries:int,num:int):
    
    user_num = int(input("Enter a number between 1 to 10: "))
    
    if user_num == num:
        tries += 1
        print("You nailed it!")
        print(f"you did it in {tries} tries only")
    
    elif user_num > 10 or user_num < 1:
        print("Enter a valid number!")
        game(tries,num)
    
    elif user_num > num and user_num < 10:
        print("Try lowering the number!")
        tries+=1
        game(tries,num)

    elif user_num < num and user_num > 1:
        print("Try increasing the number!")
        tries+=1
        game(tries,num)

game(tries,num)