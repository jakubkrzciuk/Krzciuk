while True:
	try:
		z=("+","-","*","/")
		y=("Result: ")
		x=int(input("Enter a number (or a letter to exit): "))
		d=str(input("Enter an operation: "))
		while d not in z:
			print("Wrong char")
			d=str(input("Enter an operation: "))
		z=int(input("Enter second number: "))
		
		if d=="+":
			print((y),(x+z))
		elif d=="-":
			print((y),(x-z))
		elif d=="*":
			print((y),(x*z))
		elif d=="/":
			print((y),(x/z))

		print("\n")
		break
	except:
		print("Invalid Sign")
		break	