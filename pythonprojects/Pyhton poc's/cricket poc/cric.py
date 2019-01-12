import MySQLdb
import csv
db=MySQLdb.connect("localhost","root","root","charan")
cursor=db.cursor()
fo=None
fo=open("Batting.csv")
bat=csv.reader(fo)
data=list(bat)
sql="DROP TABLE IF EXISTS batting"
cursor.execute(sql)
sql="create table batting(id int,name varchar(20),team varchar(20),runs int,hs int,avg float,sr float,sixes int)"
cursor.execute(sql)
for rec in data:
	sql="INSERT INTO batting(id,name,team,runs,hs,avg,sr,sixes)VALUES('%d','%s','%s','%d','%d','%f','%f','%d')"%(int(rec[0]),str(rec[1]),str(rec[2]),int(rec[3]),int(rec[4]),float(rec[5]),float(rec[6]),int(rec[7]))	
	cursor.execute(sql)
	db.commit()
fo.close()
fo=open("Bowling.csv")
bowl=csv.reader(fo)
data=list(bowl)
sql="DROP TABLE IF EXISTS bowling"
cursor.execute(sql)
sql="create table bowling(id int,name varchar(20),team varchar(20),overs float,runs int,wkts int,avg float,eco float,sr float)"
cursor.execute(sql)
for rec in data:
	sql="INSERT INTO bowling(id,name,team,overs,runs,wkts,avg,eco,sr)VALUES('%d','%s','%s','%f','%d','%d','%f','%f','%f')"%(int(rec[0]),str(rec[1]),str(rec[2]),float(rec[3]),int(rec[4]),int(rec[5]),float(rec[6]),float(rec[7]),float(rec[8]))	
	cursor.execute(sql)
	db.commit()
fo.close()
fo=open("player_cost.csv")
cost=csv.reader(fo)
data=list(cost)
sql="DROP TABLE IF EXISTS cost"
cursor.execute(sql)
sql="create table cost(id int,value float)"
cursor.execute(sql)
for rec in data:
	sql="INSERT INTO cost(id,value)VALUES('%d','%f')"%(int(rec[0]),float(rec[1]))	
	cursor.execute(sql)
	db.commit()
fo.close()
sql="DROP TABLE IF EXISTS id"
cursor.execute(sql)
sql="create table id(id int, name varchar(20))"
cursor.execute(sql)
sql="insert ignore into id select * from(select bt.id,bt.name from batting bt union all select bl.id,bl.name from bowling bl)UnionResult"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS final_id"
cursor.execute(sql)
sql="create table final_id(id int, name varchar(20))"
cursor.execute(sql)
sql="insert into final_id select distinct i.id, i.name from id i"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS bat_score"
cursor.execute(sql)
sql="create table bat_score(id int, score float)"
cursor.execute(sql)
sql="insert into bat_score select bt.id,((bt.runs)+2*bt.sixes+(bt.runs-bt.runs*100/bt.sr)) from batting bt order by bt.id"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS bowl_score"
cursor.execute(sql)
sql="create table bowl_score(id int, score float)"
cursor.execute(sql)
sql="insert into bowl_score select bl.id,(20*bl.wkts+1.5*6*bl.overs-bl.runs) from bowling bl order by bl.id"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS tot_score"
cursor.execute(sql)
sql="create table tot_score (id int, score float)"
cursor.execute(sql)
sql="insert into tot_score select * from (select bt.id, bt.score from bat_score bt union all select bl.id, bl.score from bowl_score bl) UnionResult"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS total_score"
cursor.execute(sql)
sql="create table total_score (id int, score float)"
cursor.execute(sql)
sql="insert into total_score select ts.id,sum(ts.score) from tot_score ts group by ts.id"
cursor.execute(sql)
db.commit()
sql="DROP view IF EXISTS first_join"
cursor.execute(sql)
sql="create view first_join as select a.id,a.name,b.score from id a join total_score b on (a.id = b.id)"
cursor.execute(sql)
sql="DROP TABLE IF EXISTS fin"
cursor.execute(sql)
sql="create table fin(id int,name char(20),score float,cost int,cost_per_score float)"
cursor.execute(sql)
sql="insert into fin select a.id,a.name,a.score,b.value,b.value/a.score from first_join a join cost b on (a.id = b.id)"
cursor.execute(sql)
db.commit()
sql="DROP TABLE IF EXISTS final"
cursor.execute(sql)
sql="create table final(id int,name char(20),score float,cost int,cost_per_score float)"
cursor.execute(sql)
sql="insert into final select distinct f.id,f.name,f.score,f.cost,f.cost_per_score from fin f order by f.cost_per_score"
cursor.execute(sql)
db.commit()
sql="select * from final"
cursor.execute(sql)
for res in cursor.fetchall():
	print res[0],"	",res[1],"	",res[2],"	",res[3],"	",res[4]
db.close()
