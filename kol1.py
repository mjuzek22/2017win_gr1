
class Client():
	def __init__(self,name, surname, cash):
		self.name = name
		self.surname = surname
		self.cash = cash

class Bank():
	def __init__(self):
		self.clients = [1]

	def new_client(self,name, surname, cash):
		client = Client(name, surname, cash)
		self.clients.append(client)

	def cash_input(self,c_number, money):
		self.clients[int(c_number)].cash += money

	def cash_withdrawal(self, c_number,money):
		self.clients[int(c_number)].cash +-= money
	
	def money_transfer(self, client_1, client_2, money):
		self.clients[int(client_2)].cash += money
		self.clients[int(client_1)].cash -= money
