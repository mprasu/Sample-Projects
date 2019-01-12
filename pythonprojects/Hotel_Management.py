
from demo.Amenities import Bill_Amenities
import shelve

class Hotel:
    'Welcome to eswar resorts'
    rooms = 20
    singlebedrooms = 5
    doublebedrooms = 10
    triplebedrooms = 5
    bookedrooms = 0
    sbrprice = 4000
    dbrprice = 3000
    tbrprice = 2000
    choice = 0
    token = True
    usr = 'admin'
    pwd = 'test'
    flag = False
    i = 0
    ctc=()


    def totalrooms(self):

        print('Total Available Rooms--->', self.rooms)
        print('\t Available SingleBed Rooms--->', self.singlebedrooms)
        print('\t Available DoubleBed Rooms--->', self.doublebedrooms)
        print('\t Available TripleBed Rooms--->', self.triplebedrooms)

    def prices(self):

        print('Monthly Room Rent prices are given below:')
        print(f'\t SingleBed Room rent--->Rs.{self.sbrprice}')
        print(f'\t DoubleBed Room rent--->Rs.{self.dbrprice}')
        print(f'\t TripleBed Room rent--->Rs.{self.tbrprice}')

    def booking(self,t,rm,pr):
        try:
            self.choice = int(input('Enter number of Rooms you want '))
        except Exception:
            print(f"Enter a valid choice {self.usr}")
            self.booking(t,rm,pr)
        if self.choice > rm:
            print(f'Sorry Available Rooms of your choice are {rm}')
            return 0
        else:
            b=Bill_Amenities()
            self.ctc=b.amenities(t)
            print(f"Dear,{self.usr} You have choosen {self.choice} rooms and {self.ctc[0]} amenities.......")
            print(f"Your total Bill Amount is {self.choice*pr + self.ctc[1]}")
            try:
                chk= int(input(f"Press 1 to Confirm your Booking or 0 to Cancel your Booking...."))
            except Exception:
                print(f" You have entered an Invalid choice...So Cancelling your booking...")
                chk=0
            if chk==1:
                self.rooms -= self.choice
                print(f'Congrats your rooms are booked with Amenities {self.ctc[0]}... Have a great day')
                return self.choice
            else:
                print(f"Your Booking is Canceled....")
                return 0

    def chck(self,t):

            if t == 1:
                self.singlebedrooms -= self.booking(t, self.singlebedrooms, self.sbrprice)
            elif t == 2:
                self.doublebedrooms -= self.booking(t, self.doublebedrooms, self.dbrprice)
            elif t == 3:
                self.triplebedrooms -= self.booking(t, self.triplebedrooms, self.tbrprice)
            else:
                print('Enter a valid choice........')

    def login(self):

        u=input('Enter UserName ')
        pw=input('Enter Password ')
        if u==None or pw==None or u!=self.usr or pw!=self.pwd:
            return False
        else:
            return True

    def register(self):

        u = input('Enter UserName ')
        pw1 = input('Enter Password ')
        pw2 = input('ReEnter Password ')
        if pw1==pw2:
            self.usr=u
            self.pwd=pw1
            print("Registered Successfully......Login to Book rooms!")
            return True
        else:
            print('Entered Passwords should be same.....Try Again')
            self.register()

    def authenticate(self):

        while self.token:
            if self.flag==False:
                try:
                    self.i=int(input('Enter 1 to login \n'
                  'Enter 2 to register '))
                except Exception:
                    print(f"Enter a valid choice....")
                    continue
            else:
                self.i==1
            if self.i==1:
                if self.flag==False:
                    auth=self.login()
                if auth:
                    print('Welcome.....', self.usr)
                    self.flag=True
                    self.totalrooms()
                    self.prices()
                    try:
                        type = int(input('Enter 1 for SingleBed Rooms\n'
                                     'Enter 2 for DoubleBed Rooms\n'
                                     'Enter 3 for TripleBed Rooms\n'))
                    except Exception:
                        print("Invalid Choice......")
                    else:
                        self.chck(type)
                        self.totalrooms()
                    try:
                        ex=int(input('Enter 0 to LOGOUT and 1 to Book more rooms '))
                    except Exception:
                        print("Invalid Choice...Logging Out for Security Reasons")
                        ex=0
                    if ex==0:
                        print('Bye...',self.usr)
                        self.token=False
                        break
                    elif ex==1:
                        continue
                    else:
                        print(f'Enter a valid choice....{self.usr}!')
                        self.token=False
                        break
                else:
                    print('Enter Valid UserName and Password to Login to the System')
                    break
            elif self.i==2:
                self.register()
                self.authenticate()
            else:
                print(f'Enter a valid choice....!')

    def __repr__(self):
        try:
            print(self.ctc[0])
        except Exception:
            return (f"{self.choice} rooms booked by {self.usr} with Zero Amenities ")
        else:
            return(f"{self.choice} rooms booked by {self.usr} with Amenities {self.ctc[0]} ")

if __name__ == '__main__':
    print(Hotel.__doc__)
    p=Hotel()
    print()
    p.authenticate()
    print()
    p.totalrooms()
    bookedrooms = p.choice
    db = shelve.open('Nile_Hotel_users')
    db[p.usr]=p
    print(db[p.usr])
    db.close()