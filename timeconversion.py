def timeconv(s):
	time=s.split(':')
  
	if time[2][-2:]=="PM" and time[0] != "12":
		time[0]=str(int(time[0])+12)
    
	elif time[0]=="12" and time[2][-2:]=="AM":
			time[0]=time[0].replace("12", "00")
      
	f=':'.join(time)
	print(f[:-2])

a=input()
timeconv(a)

