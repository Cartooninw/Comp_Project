import ATM 
import random
import User_system
import openpyxl
import os 
import pandas

#Variable Declaration
member = ["yes","no"]
yes_options = "yes"
items = {"shirt":5,"shoes":30,"foods":2,"monkey paw":100,"crucifix":20,"curse items":340,"Music Box":10,"Another monkey paw":100,"And monkey paw":100,"water":1,"fruits":1}
items_list = list(items.keys())
items_price = list(items.values())
shipping_charge = 0 
basket = {}
items_amount = []

def register_membership(User,ATM,Answer):
    print("Hello word")



#Check membershihp
def membership_checker():
    multi_yes = ["yes","i have","i do","of course","!","why not","yeah"]
    memberchecker = input("Do u have membership?:").lower
    for i in multi_yes:
        if i == memberchecker:
            return member[0]
            break
        else:
            break
#distance calculator
def distance_calculator_system(distance):
    global shipping_charge
    if distance <= 20.00:
        if 0.01 <=distance<=5.00 :
            shipping_charge += 20
        elif 5.01 <=distance<=10.00 :
            shipping_charge += 40
        elif 10.01 <=distance<=15.00 :
            shipping_charge += 70
        elif 15.01 <=distance<=20.00 :
            shipping_charge += 100
    else:
        return "cancel"

#add to basket
def shopping_system(select,count):
    global basket,items_amount
    if select in items_list:
        basket[select] = count



#put all items in basket compare with prices in item_price and add on item_amount prepare for price all together
def shopping_calculator(amount,price):
    global items_list
    for lists_sequence in range(len(items_list)):
        itemvalue = items_list[lists_sequence]
        if itemvalue in basket:
            items_amount.append(items_price[lists_sequence] * basket[itemvalue])



#main        
def main():
    while True:
        #random distance because it's tester
        distance = random.uniform(0.00 , 25.00)

        #main input
        select_recive = input("pick your items:")
        item_count = int(input("How many you want?:"))

        #add on basket system
        shopping_system(select_recive,item_count)

        #ask if want to stop
        stop_shopping = input("Need More? y/n:").lower()

        #early analyse 
        shopping_calculator(items_amount,items_price)

        #declare shipfee for check if can delevery
        shipfee = distance_calculator_system(distance)


        if stop_shopping not in yes_options :
            if shipfee != "cancel":


                #summary and calculate all price 
                while True:
                    cash = ATM.Cash 
                    Total = sum(items_amount)
                    print(f"Your items price is {Total}\ndistance is {distance:.2f}\nYour shipping rate is {shipping_charge}\nTotal is:{Total + shipping_charge}")
                    if cash >= (Total+shipping_charge):
                        print(f"ordered successful")
                        ATM.Cash -= Total
                        items_amount.clear()
                        break
                    else:
                        print(f"Your cash isn't enough.\nYou have {cash} available \nPlease add your cash.")
                        #Active ATM increase crash
                        ATM.main()
                    print(cash)
            else:
                print("Distance is so far, ordered cancelled")



                
if __name__ == "__main__":
    main()