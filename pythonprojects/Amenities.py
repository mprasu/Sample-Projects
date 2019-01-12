

class Bill_Amenities:

    pr=[1000,400,600,1200]
    ch=["AC","Television","Internet","Refrigirator"]
    bk=[]
    cost=0

    def choosing_amenities(self,t):
        for a in range(0, t):
            print(f"----{self.ch[a]}--->Rs.{self.pr[a]}")
            try:
                n = int(input(f'Press 1 to choose the Aminity {self.ch[a]} Else Press 0  '))
            except Exception:
                print("Invalid Choice...Skipping this Aminities")
                continue
            if n == 1:
                self.bk.append(self.ch[a])
                self.cost += self.pr[a]
            else:
                continue

    def book_amenities(self,t,x):
        a = 0
        print("Choose the amenities you want:")
        if t == 1:
            self.choosing_amenities(x)
            return self.bk,self.cost
        elif t == 2:
            self.choosing_amenities(x)
            return self.bk, self.cost
        elif t == 3:
            self.choosing_amenities(x)
            return self.bk, self.cost


    def amenities(self,t):
        a=0
        print("Available amenities are:")
        if t==1:
           x=4
           for a in range(0,x):
               print(f"----{self.ch[a]}---")
           return(self.book_amenities(t,x))
        elif t==2:
            x=3
            for a in range(0,x):
                print(f"----{self.ch[a]}---")
            return(self.book_amenities(t,x))
        elif t==3:
            x=2
            for a in range(0,2):
                print(f"----{self.ch[a]}---")
            return(self.book_amenities(t,x))


#b=Bill_Amenities()

#print(type(b.amenities(2)))