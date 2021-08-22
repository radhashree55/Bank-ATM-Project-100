class Atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceEnquiry(self):
        print("Your Balance is ₹500")

    def cashWithdrawal(self, amount):
        newAmount = 500 - amount
        print("You have withdrawed  ₹" + str(amount))
        print("Your remaining balance is  ₹" + str(newAmount))


def main():
    name = input("Hello, what is your name? ")
    print("Hello, " + name)
    cardNumber = input("Enter your 6-Digit Card Number: ")
    pin = input("Enter your 4-Digit Pin: ")
    accountHolder = Atm(cardNumber, pin)

    print("Select an activity:")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter activity number (1/2): "))

    if activity == 1:
        accountHolder.balanceEnquiry()

    elif activity == 2:
        amount = int(input("Enter withdrawal amount: ₹"))
        accountHolder.cashWithdrawal(amount)

    else:
        print("Enter a Valid Number")


main()
