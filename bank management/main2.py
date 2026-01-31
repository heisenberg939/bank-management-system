import json
import random
import string
from pathlib import Path


class bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update():
        with open(bank.database, 'w') as fs:
            fs.write(json.dumps(bank.data, indent=4))

    @classmethod
    def __accontgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spcl = random.choices('!@#$%^&*', k=1)
        acc_id = alpha + num + spcl
        random.shuffle(acc_id)
        return "".join(acc_id)

    def createaccount(self):
        info = {
            "name": input("tell your name:- "),
            "age": int(input("tell your age:- ")),
            "email": input("tell your email:- "),
            "pin": int(input("tell your pin (4 digits):- ")),
            "accountno": bank.__accontgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("\naccount has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            bank.data.append(info)
            bank.update()

    def depositmoney(self):
        accnumber = input("tell your account number:- ")
        pin = int(input("tell your pin:- "))

        userdata = [i for i in bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to deposit:- "))
            if amount > 10000:
                print("you can deposit below 10000 only")
            else:
                userdata[0]['balance'] += amount
                bank.update()
                print("amount deposited successfully")

    def withdrawmoney(self):
        accnumber = input("tell your account number:- ")
        pin = int(input("tell your pin:- "))

        userdata = [i for i in bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to withdraw:- "))
            if amount > userdata[0]['balance']:
                print("insufficient balance")
            else:
                userdata[0]['balance'] -= amount
                bank.update()
                print("amount withdrawn successfully")

    def details(self):
        accnumber = input("tell your account number:- ")
        pin = int(input("tell your pin:- "))

        userdata = [i for i in bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            for key, value in userdata[0].items():
                print(f"{key} : {value}")

    def updatedetails(self):
        accnumber = input("tell your account number:- ")
        pin = int(input("tell your pin:- "))

        userdata = [i for i in bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            userdata[0]['name'] = input("enter new name:- ")
            userdata[0]['email'] = input("enter new email:- ")
            bank.update()
            print("details updated successfully")

    def deleteaccount(self):
        accnumber = input("tell your account number:- ")
        pin = int(input("tell your pin:- "))

        userdata = [i for i in bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            bank.data.remove(userdata[0])
            bank.update()
            print("account deleted successfully")


# ---------------- MAIN PROGRAM ---------------- #

user = bank()

print("\npress 1 for creating an account")
print("press 2 for depositing the money")
print("press 3 for withdrawing the money")
print("press 4 for account details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response:- "))

if check == 1:
    user.createaccount()
elif check == 2:
    user.depositmoney()
elif check == 3:
    user.withdrawmoney()
elif check == 4:
    user.details()
elif check == 5:
    user.updatedetails()
elif check == 6:
    user.deleteaccount()
else:
    print("invalid choice")
   