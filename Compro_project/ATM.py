import random
import openpyxl
import os 
import pandas


account_balance = 150000.02
option_note = [1000, 500,100 ,20]
bank_note = [50,0,36,21]
unlockpin = False
Cash = 0

#Pin check with only 5 attemps
def Pin_system():
    global unlockpin
    Pin_correct = "1234"
    Max_pin_attemp = 5
    Pin_attemp = 0
    while Pin_attemp != Max_pin_attemp:
        user_pin = input("Please Enter your pin:")
        if user_pin == Pin_correct:
            print("Logging in , Please wait a minute")
            unlockpin = True
            break
        else:
            if Pin_attemp != 4:
                print(f"Invlid Pin, You have {Max_pin_attemp - Pin_attemp - 1} remaining. Please Enter again.")
                Pin_attemp += 1
                print(Pin_attemp)
            else:
                print("Your accout have been locked. Please contract to our Call center")
                break



#Ready to print
def Bank_List():
    for A,B in zip(bank_note,option_note):
        print(f"{A}    {B}")




 #withdraw       
def Withdraw_system(amount):
    global account_balance,bank_note,Cash
    amount_keeper = 0
#
    for i in range(len(option_note)):
        if amount <= account_balance :
            if amount >= option_note[i]:
                Cash += amount
                for i in range(len(bank_note)):
                    while amount >= option_note[i] and bank_note[i] > 0 :  
                        amount -= option_note[i]  
                        bank_note[i] -= 1
                        amount_keeper += option_note[i]
                account_balance -= amount_keeper
                Cash -= amount
                return(f"Successful Withdraw !. Your account balance is:{account_balance}\n")
            else:
                return("The amount is not relevant with banknotes. \n Please Enter again")
        else:
            return("You Enter Over price your account balance. Please Enter again!")
  
        
def main():
    global Cash
    Pin_system()
    if unlockpin == True:
        while True:
            amountEnter = int(input("Please Enter your amount to withdraw:"))
            withdraw = Withdraw_system(amountEnter)
            if withdraw != "The amount is not relevant with banknotes. \n Please Enter again":
                print(withdraw)
                print(f"Your cash is {Cash}")
                Bank_List()
                again = input("Do you want to withdraw again? y/n:").lower()
                if again == "y":
                    pass   
                else:
                    break
            else:
                print(withdraw)
                pass


    
            
if __name__ == "__main__":
    main()

