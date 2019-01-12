class rest:
	cost_of_idly=25
	cost_of_dosa=30
	cost_of_vada=20
	total=0
	def items(self):
		return ("available items are idly,dosa,vada")
	def price(self):
		print ("cost of idly is",self.cost_of_idly)
		print ("cost of dosa is",self.cost_of_dosa)
		print ("cost of vada is",self.cost_of_vada)
	def choice(self):
		print(" enter\n 1 for idly\n 2 for dosa\n 3 for vada")
		choice=input("enter ur choice")
		if choice=="1":
			y=input("enter ur item quantity")
			self.total=self.total+int(y)*self.cost_of_idly
		elif choice=="2":
			y=input("enter ur item quantity")
			self.total=self.total+int(y)*self.cost_of_dosa
		elif choice=="3":
			y=input("enter ur item quantity")
			self.total=self.total+int(y)*self.cost_of_vada
		else:
			print("enter a valid choice")
			return self.choice()
		self.repeat()
	def repeat(self):
		c=input("enter\n 1 to order more\n 0 to quit")
		if c=="1":
			self.choice()	
		elif c=="0":
			print("Dear customer your order amount is Rs.",self.total)
		else:
			print("enter valid choice")
			return self.repeat()
if __name__=='__main__':
	p=rest()
	print(p.items())
	p.price()
	p.choice()