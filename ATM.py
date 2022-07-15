import time
AMOUNT = 500000000


def greeting():
    print('\t\t\t========================================================================================')
    print("\t\t\t==============================  Welcome to Bank of Spain  ==============================")


def checkBalance():
    print("\t\t\t\t\t\t\t[INFO] Getting Information from your account")
    print(f"\t\t\t\t\t\t\t[INFO] Your Account Balace {AMOUNT}$")


def WithDraw(drawAmount):
    if drawAmount > AMOUNT:
        print("\t\t\t\t\t\t\t[INFO] Insufficient Account Balance.")

    else:
        print("\t\t\t\t\t\t\t[INFO] Processing")
        time.sleep(10)
        print("\t\t\t\t\t\t\t[INFO] Please Collect your Cash")
        print('\t\t\t========================================================================================')


def atm():

    password = 123

    if password == int(input('\t\t\t\t\t\t\tEnter pin \t')):
        options = {"1": 'Check Account Balance',
                   "2": "Withdraw Cash", "3": 'Bank Statement'}
        print('\n\n\t\t\t\t\t\t\tPlease Select Option')
        print('\t\t\t========================================================================================')
        for key, values in options.items():
            print(f'\t\t\t\t\t\t\t{key} {values}')
        opt = int(input('\t\t\t\t\t\t\t'))

        if opt == 1:
            print('\t\t\t========================================================================================')
            checkBalance()
            print('\t\t\t========================================================================================')

        elif opt == 2:
            print('\t\t\t========================================================================================')
            amount_ = int(input('\t\t\t\t\t\t\tEnter Amount for Withdraw  '))
            WithDraw(amount_)

        else:
            pass
    else:
        print('\t\t\t\t\t\t\tInvalid Pin')


if __name__ == '__main__':
    greeting()
    atm()
    print("\t\t\t\t\t\t\t do you want to use again yes/no")
    if input('\t\t\t\t\t\t\t-> ').lower() == "yes":
        print('\t\t\t========================================================================================')
        atm()
        print('\t\t\t========================================================================================')
    else:
        print('\t\t\t========================================================================================')
        print("\t\t\t\t\t\t\t Thank you......")
        print('\t\t\t========================================================================================')
