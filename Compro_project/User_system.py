import os 
import pandas as pd
import openpyxl
import random as rd
import string
import time
cur_path = os.getcwd()


def delay(second):
   time.sleep(second)
#main function of UserSystem. Create for all of user system.

class Fund_User:
  
  def __init__(self,Data):
    self.Data = Data

  def load_file(self):
    try:
      data =  pd.read_excel(self.Data, engine="openpyxl")
      return data
    except FileNotFoundError:
      print("File Not Found. Please Create/Check your file.")





class shop_User_system:
  def __init__(self,data):
    self.data = data
    self.load = Fund_User(self.data).load_file()
    
    
  def register(self,username,password):
      if username in self.load["username"]:
        print("Username has been used. Please Enter again!")
      else:
        load["username"].append(username)
        load["password"].append(password)
        self.save


        
  def login(self,username,password):
    if username not in load["username"]:
      print("This username doesn't exsit. Please register.")
    else:
      usernameCheck = load[load["username"] == username]
      if password  in usernameCheck:
        print("Connecting")
        return True
      else:
        if password == " ":
          pwc = input("Enter your password separated by \(oldpass/\\newpass):")
          pwin = pwc.split("/")
          if pwin[0] == (password == usernameCheck):
            load.loc[(load["username"] == username), "password"] = pwin[1]
            self.save
        else:
          return False

        
class ATM_User_system:

  
  def __init__(self,data):
    self.data = data
    self.User = Fund_User(self.data)
    self.load = self.User.load_file()
    self.balance = None
    self.using = None
  def register(self,realname,id,password,pin):
    Data = self.load
    if ((realname[0].lower() + realname[1].lower()) not in (Data["FirstName"] + Data["LastName"]).tolist() )and (id not in Data["ID"].tolist()):
      try:
        int(pin)
        while True:
          if len(str(pin)) == 4:
            new_user ={"FirstName":realname[0].lower(),"LastName":realname[1].lower(),"ID":id,"Password":password,"Pin":pin,"Balance":0}
            Data = pd.concat([Data,pd.DataFrame([new_user])],ignore_index=False)
            Data.to_excel(self.data,index=False,engine="openpyxl")
            break
          else:
              print("Please enter pin 4 numbers.")
              pin = int(input("Please Enter your pin(4 numbers):"))
      except ValueError:
        print("Pin Is allow only number. Please set number as pin.")
    else:
      print("This Name/Id have been used. Please change your Name/Id.")
  def login(self,id,password):
    Data = self.load
    if (id in Data["ID"].tolist()):
      if ((password == Data.loc[Data["ID"] == id,"Password"].item()) or (password == Data.loc[Data["ID"] == id,"Pin"].item())) :
        print("Logging")
        time.sleep(3)
        self.using = id
        print("Pass!")
        return ("Pass")
      else:
        print("Name or password was wrong. please check carefully before enter.")
        return ("Fail")
    else:
       print("ID not found. Please register.")
       return ("Fail")
  def logout(self):
    self.using = None
  def CheckBalance(self): 
    try:
      self.balance = self.load.loc[self.load["ID"] == self.using,"Balance"].item()
      print(f"You have {self.balance } Dollar in the bank.")
    except ValueError:
      print("Please Login before checking balance.")
Test = ATM_User_system(cur_path + "/atmdata.xlsx")
Test.login("d","pass")
Test.CheckBalance()
Test.logout()
Test.CheckBalance()
