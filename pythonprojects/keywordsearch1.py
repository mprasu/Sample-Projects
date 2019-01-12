import os
class key:
	cnt=0	
	def search(self,dirpath,extension,keyword):
		for file in os.listdir(dirpath):#it returns list of directories and files in the form of list
			if os.path.isdir(dirpath+"/"+file)==True:
				self.search(dirpath+"/"+file,extension,keyword)
			else:
				if file.endswith(extension):
					print("in",dirpath,"/",file)
					fo = open(dirpath+"/"+file,'r+')
					doc=fo.read()
					if keyword in doc:
						lines = doc.splitlines()
						count2=0
						
						for i in range(len(lines)):
							if keyword in lines[i]:
								count1=0
								for word in lines[i].split():
									if word==keyword:
										count1+=1
										count2+=1
										key.cnt+=1
								
								print(keyword,"is repeated ",count1," times ","in line ",(i+1))			
						
						else:
								print(keyword," is repeated  " ,count2,"times in ",dirpath,"/",file)         			
if __name__=='__main__':
	p=key()
	dir=input("enter dir path")
	p.search(dir,".txt","Python")
	print("Python is repeated totally",key.cnt,"times in all files in",dir) 