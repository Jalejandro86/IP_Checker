
def checker():
	
	usr_in = input('Enter Address:  ')
	
	x = usr_in.split('.')
	
	
	if len(x) != 4:
		print('Invalid IP')
		raise SystemExit
	
	for num in x:
		if not num.isdigit():
			print('Invalid IP')
			raise SystemExit
			
		if len(num) > 1:
			check_zro = int(num[0])
			#print(check_zro)
			
			if check_zro == 0:
				print('Invalid IP')
				raise SystemExit
			
		
	for num in x:
		if int(num) >= 0 and int(num)<= 255:
			continue
		
		else:
			print('Invalid IP')
			raise SystemExit
		

	if int(x[0]) <= 126:
		print(usr_in , 'is a Valid Class A IP Address')
	elif int(x[0]) >=128 and int(x[0]) <= 191:
		print(usr_in , 'is a Valid Class B IP Address')
	elif int(x[0]) >=192 and int(x[0]) <= 223:
		print(usr_in , 'is a Valid Class C IP Address')
	else:
		raise SystemExit
		
	
if __name__ == "__main__":	
	checker()