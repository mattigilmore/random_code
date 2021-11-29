#yesno() is to make sure they only put in y or n
yn=str(input("is it raining?"))
yn=yn.lower()
def outside():
	print("Go out side")


if yn== "yes" or "y":
		yn=str(input("Do you have an umbrelle"))
		yn=yn.lower()
		if yn == "n" or "no":
				endloop=True
				while endloop==True:
						yn=str(input(" wait till its not raining.\n Is it still raining?"))
						print(yn)
						yn=yn.lower()
						print(yn)
						if yn=="no" or "n":
								outside()
								endloop=False
						else:
								None
								
						

else:
	outside()

	
		


