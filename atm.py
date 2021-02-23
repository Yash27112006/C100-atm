class ATM(object):
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number


    def balanceEnquiry(self):
        print("Your balance is more than your income. It is INR 35,000.")

    def cashWithdrawl(self,money):
        balance = 35000 - money
        print("You have withdrawn amount " + str(money) + ". Your current balance is "+ str(balance))
        print("Withdrawl successfull. Have a good day :)")
    
    def cashDeposit(self,money):
        balance = 35000 + money
        print("You have deposited " + str(money) + ". You current balance is " + str(balance))
        print("Thank you for depositing money. Have a good day.")

def bankWork():
    name = input("Enter your name: ")
    print("Hello " + name + " ! Welcome to RBI (Rajgarhia Bank Of India).")
    print("")
    card_number = input("Please provide your card number: ")
    pin_number = input("Please provide your pin number: ")

    if (len(card_number) == 10 and len(pin_number) == 6):
        createUser = ATM(card_number,pin_number)
        print("")
        print("What are your wishing to do today ??")
        print("Choose 1 for balance enquiry.")
        print("Choose 2 for cash withdrawl.")
        print("Choose 3 for cash deposit.")
        print("")

        yourWish = int(input("Type your number: "))

        if (yourWish == 1):
            createUser.balanceEnquiry()
        elif (yourWish == 2):
            print("")
            money = int(input("Enter the amount to be withdrawn: "))
            createUser.cashWithdrawl(money)
        elif (yourWish == 3):
            print("")
            money = int(input("Enter the amount to be deposited: "))
            createUser.cashDeposit(money)
        else:
            print("Please enter 1, 2 or 3.")
    elif (len(pin_number) < 6):
        print("Enter a valid pin number.")
    elif (len(card_number) < 10):
        print("Enter a valid card number.")


bankWork()
