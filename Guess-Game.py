import random

# Global variables
y = random.randint(0, 9)
# y = 3 #testing variable
x = 0


def game(name, acc):
    """Game fn : Guessing game.
        arguments: 'name'- of the user and 'acc' of the user.
        fn purporse: Guessing game and prize money calucation
        return value: 'acc' after prize money calculation """
    acc = acc - 500  # deducting 500 as entry fee for playing the game
    c = 0  # count variable
    for c in range(1, 4):  # giving the guest 3 attempts to guess the no.
        x = input("Guess the number: ")
        if int(x) < y:
            print("Sorry,", name, "your guess is Too Low!!\n Attempts left: ", 3 - c)
            win = False
        if int(x) > y:
            print("Sorry,", name, "your guess is Too high!!\n Attempts left: ", 3 - c)
            win = False
        elif int(x) == y:
            print('*' * 6, "You are correct.", '*' * 6)
            win = True  # flag to check if he wins in the 3rd attempt.
            break
    # Prize money calculation
    if c == 1:
        acc += 5500  # prize is 5.5k, bcoz whenever we start the game we r deducting 500
        print(name, "!!, you have won Rs.5000/- ")
        print("Total account balance: Rs. ", acc, "/- ")
    elif c == 2:
        acc += 1500
        print(name, "!!, you have won Rs.1000/- ")
        print("Total account balance: Rs. ", acc, "/- ")
    elif c == 3 and win != True:
        print(name, "!!, you just lost Rs.500/- ")
        print("Total account balance: Rs. ", acc, "/- ")
        print("The actual no. was! ", y)
    elif c == 3 and win == True:
        acc += 500  # if he wins in third attempt, no money is withdrawn from hiis acc.
        print("Total account balance: Rs. ", acc, "/- ")
    return acc


def amount_transfer(acc, wallet):
    """ammount transfer : for transfering amunt from user's wallet to game account
        arguments: acc-game account , wallet- userr's wallet or credit card
        returns: acc - after the transcation is completed."""

    w = ''  # dummy string to get the i/p user
    w_a = 0  # Gameclub wallet/acc of the user; like (amzn_paybalance)
    print("Sorry!, you dont have sufficient balance to play the game.")
    w = input("Do you wish to add money from your wallet:\n* Type(yes/no): ")
    if w.lower() == 'yes':
        w_a = int(input("How much amount do you like to transfer: "))  # w_a is user acc in club
        wallet -= w_a  # subtracting money from user's original wallet
        acc += w_a  # adding it to user's gameclub acc
        print("Now your account balance is:", acc)
    elif w.lower() == 'no':
        print("Transcation Cancelled!")
        print("Thanks for playing buddy.\n Have a wonderful day!!")

    return acc


def main():
    # main program
    acc = 1000  # welcome bonus
    wallet = 5000  # user's wallet or credit card
    print("Welcome to Gotham Club!!")
    name = input("Enter your name: ")
    print("Hi, ", name, "as a welcome bonus we have given you Rs.1000/-.")
    # displaying the rules
    print("Here are the rules for playing this gambling game.\n*You have to guess a no. between 0 and 9.\n1)If you can successfuly guess it in the first chance\n*******You can Win Rs.5000/-**********")
    print("2)If you can successfuly guess it in second chance.\n***You can Win Rs.1000/-***")
    print("3)If you fail to find the no. in three chances-\n.You Lose Rs.500/- only!")
    while 1:
        if acc < 500:
            acc = amount_transfer(acc, wallet)  # since acc< 500, calling this fn to add funds
            if acc < 500:  # if the user again adds low funds in the above transcation, repeating the process
                print("Insufficient fund!!! Minimum balance required is Rs.500/-")
                y_n = input("Type \n* 'add' - to add more fund. or \n* 'exit' - to exit the game.")
                if y_n.lower() == 'exit':
                    break
                elif y_n.lower() == 'add':
                    continue
        acc = game(name, acc)
        print("Hi !!", name)
        y_n = input("Type \n* 'yes' -if you wish to play again or \n* 'no' - to quit.")
        if y_n.lower() == 'no':
            print(name, "Thanks for playing buddy.\n Have a wonderful day!!")
            break


main()