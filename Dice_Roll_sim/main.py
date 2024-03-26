import random 
#testssfsfsf
#fsf
def roll_dice(amount = 2) -> list[int]:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    
    #rolls: list[int] = []
    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)
        
    return rolls

def main():
    while True:
        try:
            #user_input: str = input("How many dice would you like to roll?")
            user_input = input("How many dice would you like to roll? ")

            if user_input.lower() == 'exit':
                print("Thanks for playing! ")
                break
            
            #* Convert input to integer and roll dice
            dice_rolls = roll_dice(int(user_input))
            #* Calculate the sum of the rolled dice
            total = sum(dice_rolls)
            #* Print the individual rolls and the total sum
            print(f"Rolls: {', '.join(map(str, dice_rolls))}. Total sum: {total}")
            
            # print(*roll_dice(int(user_input)), sep=', ')
            
            # total = roll_dice(int(user_input))
            # print(sum(total))
            
            print("When done type exit")
            
        except ValueError:
            print("Enter a Valid number")
            
if __name__ == "__main__":
    main()
