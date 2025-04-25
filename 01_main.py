import random 
number = random.randint(0,100)

while True:
    try: 
        user_input = int(input("\nEnter a number b/w 0-100: "))
        if 0 <= user_input <= 100:
                if number < user_input:
                        print("-Too High!!")
                elif number > user_input:
                    print("-Too Low!!")
                else:
                    print("=> Congrats!! You Guessed the Number 🎉")
                    break
        else:
            print("❗Please enter a valid number (0-100) 🙏")
    except ValueError:
        print("❗Invalid Number!! Try again") 