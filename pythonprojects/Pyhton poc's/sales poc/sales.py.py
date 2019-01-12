import csv
fo=None
fo=open("sales.csv")
sales=csv.reader(fo)
data=list(sales)
print("enter \n 1 for yearly report\n 2 for monthly report\n 3 for quarterly report")
s=raw_input("enter choice ")
def monthly():
	z=raw_input('enter year ')
	l=raw_input('enter month ')
	sum=0.0
	for rec in data:	
		x=rec[0].split('-')
		if x[2]==z:
			if x[1]==l:
				sum=float(rec[1])+sum
	print sum
def yearly():
	z=raw_input('enter year ')
	sum=0.0
	for rec in data:	
		x=rec[0].split('-')
		if x[2]==z:
			sum=float(rec[1])+sum
	print sum
def quarterly():
	z=raw_input('enter year')
	first=0.0
	second=0.0
	third=0.0
	fourth=0.0
	for rec in data:
		x=rec[0].split('-')
		if x[2]==z:
			m=int(x[1])
			if m<=3:
				first=float(rec[1])+first	
			if m<=6 and m>3:
				second=float(rec[1])+second
			if m<=9 and m>6:
				third=float(rec[1])+third
			if m<=12 and m>9:
				fourth=float(rec[1])+fourth
	print ("first quarter sales sum is",first)
	print ("second quarter sales sum is",second)
	print ("third quarter sales sum is",third)
	print ("fourth quarter sales sum is",fourth)
if s=="1":
	yearly()
elif s=="2":
	monthly()
elif s=="3":
	quarterly()
if fo:
	fo.close()
	print "file is closed"
