import datetime
from datetime import date
import MySQLdb
db = MySQLdb.connect("localhost","root","root","hoteldb" )
c=db.cursor()
class Ratna:
      def rooms(self): 
        print"Single Room             :",self.csgl,"  left:",self.room['sgl'],' book press: 1'
        print"Single+TV Room          :",self.csgl_tv,"  left:",self.room['sgl_tv'],' book press: 2'
        print"Single+TV+AC Room       :",self.csgl_tv_ac,"  left:",self.room['sgl_tv_ac'],' book press: 3'
        print"Double Room             :",self.cdub,"  left:",self.room['dub'],' book press: 4'
        print"Double+Tv Room          :",self.cdub_tv,"  left:",self.room['dub_tv'],' book press: 5'
        print"Double+TV+AC Room       :",self.cdub_tv_ac,"  left:",self.room['dub_tv_ac'],' book press: 6'
        return self
      def release_rooms(self):
          #if self.p_date!=str(date.today()):if we remove commmant it will check rooms once in a day
             sql="select no_of_rooms,type_of_room,left_date from ratna_rooms where status='no'";
             try:
                c.execute(sql)
                db.commit()
                print "sql execute release_rooms"
             except:
                db.rollback()
                print(" error ----------122-------")
             tuple_t=c.fetchall()
             self.p_date=str(date.today()) 
             for no,type_room,d1 in tuple_t:
                 dy1=date(int(d1[0:4]),int(d1[5:7]),int(d1[8:]))
                 try:
                    days=int(str(date.today()-dy1)[0:2])
                 except ValueError:
                    print "no of rooms:",no 
                    self.room[type_room]=self.room[type_room]+no
                    sql="update ratna_rooms set status='yes' where left_date='%s'"%d1;  
                    try:
                      c.execute(sql)
                      db.commit()
                      #print "sql execute Yes 00000"
                      days=0
                    except:
                      db.rollback()
                      print(" error ---------")
                 #print days,d1
                 if days>0:
                    #print "no of rooms:",no   
                    self.room[type_room]=self.room[type_room]+no
                    sql="update ratna_rooms set status='yes' where left_date='%s'"%d1;  
                    try:
                      c.execute(sql)
                      db.commit()
                    except:
                      db.rollback()
                      print(" error -akkkkkkkkk--------")
             return self
      def update_rooms(self):
           print self.csgl
      def bookrooms(self,username,book,n,d):
            #print"booked"
            if book==1:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','sgl','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi" 
                 self.room['sgl']=self.room['sgl']-n
                 print self.room['sgl']
                 print"Number of single bed rooms booked ",n," Amount ",self.csgl*n*d
                 return self
               except:
                 db.rollback()
                 print(" error -----111111----")
            elif book==2:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','sgl_tv','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi" 
                 self.room['sgl_tv']=self.room['sgl_tv']-n
                 print"Number of single+tv bed rooms booked ",n," Amount ",self.csgl_tv*n*d
                 return self
               except:
                 db.rollback()
                 print(" error ----2222222222222-----")
            elif book==3:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','sgl_tv_ac','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi" 
                 self.room['sgl_tv_ac']=self.room['sgl_tv_ac']-n
                 print"Number of single+TV+AC bed rooms booked ",n," Amount ",self.csgl_tv_ac*n*d
                 return self
               except:
                 db.rollback()
                 print(" error -----33333333333----")
            elif book==4:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','dub','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi" 
                 self.room['dub']=self.room['dub']-n
                 print"Number of duble bed rooms booked ",n," Amount ",self.cdub*n*d
                 return self 
               except:
                 db.rollback()
                 print(" error ------4444444444444---")
            elif book==5:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','dub_tv','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi"
                 self.room['dub_tv']=self.room['dub_tv']-n 
                 print"Number of double+TV bed rooms booked ",n," Amount ",self.cdub_tv*n*d
                 return self 
               except:
                 db.rollback()
                 print(" error -------55555555--")
            elif book==6:
               left_date=str(date.today()+datetime.timedelta(d))
               sql="insert into ratna_rooms values('%s','%d','%d','dub_tv_ac','%s','%s','no')"%(username,n,d,self.p_date,left_date)
               try:
                 c.execute(sql)
                 db.commit()
                 #print "hi"
                 self.room['dub_tv_ac']=self.room['dub_tv_ac']-n 
                 print"Number of double+TV+AC bed rooms booked ",n," Amount ",self.cdub_tv_ac*n*d
                 return self
               except:
                 db.rollback()
                 print(" error ---66666666666666--")
            else:print"plese enter valid no:"  
                

        
