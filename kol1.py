#Kol1.py ###Monika Juzek

#Banking simulator. Write a code in python that simulates the banking system.
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck


class Client:
    def __init__(self, name, surname, cash, id):
        self.name = name
        self.surname = surname
        self.cash = cash
        self.id_number = id


class Bank:
    def __init__(self, name):
        self.clients = []
        self.name = name

    def new_client(self, name, surname, cash):
        client = Client(name, surname, cash, len(self.clients)+1)
        self.clients.append(client)

    def client_list(self):
        for x in self.clients:
            print("ID number: ", x.id_number, '    ', x.name, " ", x.surname, "- cash: ", x.cash)

    def cash_input(self, c_number, money):
        self.clients[int(c_number)-1].cash += money

    def cash_withdrawal(self, c_number, money):
        self.clients[int(c_number)].cash -= money

    def money_transfer(self, c_number1, c_number2, money):
        self.clients[int(c_number1)].cash += money
        self.clients[int(c_number2)].cash -= money

    def write_client_data(self, file_name):
        f = open(file_name,'a')
        for c in (self.clients):
            f.write("{} {} : {}\n".format(c.name, c.surname,c.cash))
        f.close()

class Transfer:
    def money_transfer(self, bank_name_1, client_id_1,  bank_name_2, client_id_2, money):
       bank_name_1.clients[int(client_id_1)].cash -= money
       bank_name_2.clients[int(client_id_2)].cash += money

stop_commend = "no"
banks = []
bank_number = 0
while stop_commend == "no":
    print("\nEnter bank name.If you do not want to add another client type: break")
    print("")
    b_name = input()
    if (b_name == "break"):
        stop_commend = "yes"
        break
    banks.append(Bank(b_name))
    print("Created a bank: \n", b_name)

    c_name = "1"

    while c_name != "break":
        print("\nEnter client name.If you do not want to add another client type: break")
        c_name = input()
        if (c_name == "break"): break
        print("Enter client surname")
        c_surname = input()
        print("Enter client's amount of cash")
        c_cash = input()
        banks[bank_number].new_client(c_name, c_surname, int(c_cash))
        print("New client added: ", c_name, c_surname)
        print("ID number: ", len(banks[bank_number].clients))
        print("")

    print("List of clients of ", banks[bank_number].name, " bank:")
    banks[bank_number].client_list()
    bank_number += 1


print("\nWhat you want to do: cash input, cash withdrawal or money transfer")
answear = input()
if answear == "cash input":
    print("Enter bank name")
    b_name = input()
    print("Enter client ID number")
    c_id = input()
    print("Enter amount of cash to input")
    cash_input = input()
    for i in range (len(banks)):
        if banks[i].name == b_name:
            banks[i].cash_input(int(c_id), int(cash_input))
    print("Bank: ", banks[i].name, "- client: ", banks[i].clients[int(c_id)-1].name, " " , banks[i].clients[int(c_id)-1].surname, " - cash: ", banks[i].clients[int(c_id)-1].cash)


elif answear == "cash withdrawal":
    print("Enter bank name")
    b_name = input()
    print("Enter client ID number")
    c_id = input()
    print("Enter amount of cash to withdraw")
    cash_withdrawal = input()
    for i in range(len(banks)):
        if banks[i].name == b_name:
            banks[i].cash_withdrawal(int(c_id)-1, int(cash_withdrawal))
            print("Bank: ", banks[i].name, "- client: ", banks[i].clients[int(c_id)-1].name, " ",
                  banks[i].clients[int(c_id)-1].surname, " - cash: ", banks[i].clients[int(c_id)-1].cash)


else:
    print("Transfer form client#1 to client#2")
    print("Enter bank name of client#1")
    b_name_1 = input()
    print("Enter client ID of client#1")
    c_id_1 = input()
    print("Enter bank name of client#2")
    b_name_2 = input()
    print("Enter client ID of client#2")
    c_id_2 = input()
    print("Enter amount of cash to transfer")
    cash_transfer = input()
    if b_name_1 == b_name_2:
        for i in range(len(banks)):
            if banks[i].name == b_name_1:
                banks[i].money_transfer(int(c_id_1)-1,int(c_id_2)-1, int(cash_transfer))
    else:
        t= Transfer()
        for i in range(len(banks)):
            if banks[i].name == b_name_1: bank_number_1 = i
        for i in range(len(banks)):
            if banks[i].name == b_name_2: bank_number_2 = i
        t.money_transfer(banks[int(bank_number_1)],int(c_id_1)-1,banks[int(bank_number_2)],int(c_id_2)-1, int(cash_transfer))

print("\nEnter file name to save the list of clients from bank")
file_name = input()
for i in range(len(banks)):
    banks[i].write_client_data(file_name)
