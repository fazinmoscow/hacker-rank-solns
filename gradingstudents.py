def gradeconv(a):
	if int(a)>=38:
		b=a[::1]
    
		if int(b[-1:])<=5 and 5-int(b[1])<3:
			w=b[1]
			w=w.replace(w,'5')	
			return(b[0]+w)
      
		elif 10-int(b[1])<3:
			s=str(int(b[0])+1)
			w=b[1]
			w=w.replace(w,'0')
			return(s+w)
      
		else:
			return(a)
      
	else:
		return(a)
    
n=int(input())

for i in range(n):
	print(gradeconv(input()))
	

