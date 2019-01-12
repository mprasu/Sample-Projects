import os
class key:
	cnt=0	
	def search(self,dirpath,extension,keyword):
		for file in os.listdir(dirpath):#it returns list of directories and files in the form of list
			if os.path.isdir(dirpath+"/"+file)==True:
				self.search(dirpath+"/"+file,".txt","hello")
			else:
				if file.endswith(extension):
					print("in",dirpath,"/",file)
					fo = open(dirpath+"/"+file,'r+')
					doc=fo.read()
					if keyword in doc:
						lines = doc.splitlines()
						no_of_lines = len(lines)
						count=0
						for i in range(no_of_lines):
							select_line = lines[i].split()
							enum = list(enumerate(select_line,1))
							word_list = []
							for j in range(len(enum)):
								if enum[j][1] == keyword:
									count+=1
									key.cnt+=1
									word_list.append(dict({"file name":file,"line":i+1,"hello is in word number":j+1,}))
									print(word_list)
						else:
								print(keyword," is repeated  " ,count,"times in ",dirpath,"/",file)         			
if __name__=='__main__':
	p=key()
	dir=input("enter dir path")
	p.search(dir,".txt","hello")
	print("hello is repeated totally",key.cnt,"times in all files in",dir) 