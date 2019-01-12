import MySQLdb
import csv
db=MySQLdb.connect("localhost","root","root","charan")
cursor=db.cursor()
fo=None
fo=open("trans.csv")
trans=csv.reader(fo)
data=list(trans)
sql="DROP TABLE IF EXISTS transactions"
cursor.execute(sql)
sql="create table transactions(id int,chain int,dept int,category int,company int,brand int,dt char(20),productsize float,productmeasure char(20),purchasequantity int,purchaseamount float)"
cursor.execute(sql)
for rec in data:
	sql="INSERT INTO transactions(id,chain,dept,category,company,brand,dt,productsize,productmeasure,purchasequantity,purchaseamount)VALUES('%d','%d','%d','%d','%d','%d','%s','%f','%s','%d','%f')"%(int(rec[0]),int(rec[1]),int(rec[2]),int(rec[3]),int(rec[4]),int(rec[5]),str(rec[6]),float(rec[7]),str(rec[8]),int(rec[9]),float(rec[10]))	
	cursor.execute(sql)
	db.commit()
def top_2_customers():
	sql="select id,sum(purchaseamount)as custspendings from transactions group by id order by custspendings desc limit 2"
	cursor.execute(sql)
	res=cursor.fetchall()
	print res
def top_2_brands():
	sql="select brand,sum(purchaseamount)as custspendings from transactions group by brand order by custspendings desc limit 2"
	cursor.execute(sql)
	res=cursor.fetchall()
	print res
def chain_wise_sales():
	sql="select chain,sum(purchaseamount),sum(purchasequantity) from transactions group by chain"
	cursor.execute(sql)
	res=cursor.fetchall()
	print res
print("enter \n 1 for top two customers\n 2 for top two brands\n 3 for chain wise sales")
s=raw_input("enter choice ")
if s=="1":
	top_2_customers()
elif s=="2":
	top_2_brands()
elif s=="3":
	chain_wise_sales()
else:
	print("enter a valid choice")
db.close()
