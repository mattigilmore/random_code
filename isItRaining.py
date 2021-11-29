def outside():
    print("Go out side")
    
    
answer = input("is it raining?").lower()
if answer.startswith('y'):
    answer = input("Do you have an umbrelle").lower()
    if answer.startswith('n'):
        while True:
            answer = input(" wait till its not raining.\n Is it still raining?").lower()
            print(answer)
            if answer.startswith('n'):
                outside()
                break
else:
    outside()
#cedit for  cleaning up and telling me about the start .startswith() goes to Aporetic on python discode.
	
		


