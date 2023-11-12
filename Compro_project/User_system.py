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
    self.load_file(self.Data)


  def load_file(self,File):
    try:
      data = pd.read.excel(File)
    except FileNotFoundError:
      print("File Not Found. Please Create/Check your file.")


  def save_file(self):
    writer = pd.ExcelWriter(self.Data, engine='openpyxl') 
    df.to_excel(writer, index=False) 
    writer.save()




class shop_User_system:
  def __init__(self,data):
    self.data = data
    self.load = Fund_User(data)
    self.save = Fund_User.save_file(data)
    
    
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
    self.load = Fund_User(data)
    self.save = Fund_User.save_file(data)
    
 
  def register(self,realname,id,password,pin):
    Data = self.load
    if ((realname[0] + realname[1]) not in  (Data["FirstName"] + Data["LastName"]) )and (id not in Data["Id"]):
      Data["FirstName"].append(realname[0].lower())
      Data["LastName"].append(realname[1].lower())
      Data["ID"].append(id)
      Data["Password"].append(password)
      try:
        int(pin)
        while len(str(pin)) != 4:
          if len(str(pin)) == 4:
            Data["pin"].append(pin)
          else:
            print("Please enter pin 4 numbers.")
            pin = int(input("Please Enter your pin(4 numbers):"))
      except ValueError:
        "Pin Is allow only number. Please set number as pin."
  def login(self,id,password):
    Data = self.load
    if (id in Data["Id"]) and ((password == Data.loc[Data["Id" == id],"Password"]) or (password == Data.loc[Data["Id" == id],"Id"])) :
      print("Logging")
      return ("Pass")
    else:
      print("Name or password was wrong. please check carefully before enter.")
      return ("Fail")

  


    