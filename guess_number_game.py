import random

class InvalidRange(Exception):
    pass

class InvalidDecision(Exception):
    pass

def number_generator(mini, maxi):
    return random.randint(mini, maxi)

if __name__=='__main__':
    trails = 0
    start = False
    secret_saved = False
    while True:
        if start==False:
            try:
                lowest=int(input("Enter the lowest of range: "))
                highest=int(input("Enter the highest of range: "))
                if lowest >= highest:
                    raise InvalidRange("Lowest must be less than highest")
                start = True
            except ValueError:
                print("Low and high must be integers!")
                continue
            except InvalidRange as e:
                print(e)
                continue

        if secret_saved==False:
            secret_num = number_generator(lowest, highest)
            secret_saved=True

        try:
            trails += 1
            print(f"Trial No: {trails}")
            user_input = int(input(f"Enter a number between {lowest} and {highest}: "))
        except ValueError:
            print("User input must be an integer!!")
            start = False
            continue
        else:
            if user_input == secret_num:
                print("Correct Guess!")
                game_end = False

                while True:
                    try:
                        decision = input("Play again? (y/n): ").lower()
                        if decision not in ('y', 'n'):
                            raise InvalidDecision("Decision must be 'y' or 'n'!")
                    except InvalidDecision as e:
                        print(e)
                        continue
                    else:
                        break

                if decision == "y":
                    start = False
                    secret_saved = False
                    trails = 0
                    print("Game Restarting")
                    continue
                else:
                    print("Game Ending")
                    break
               
            else:
                if user_input > secret_num:
                    print("High")
                else:
                    print("Low")

    print("Thanks for playing the game")
