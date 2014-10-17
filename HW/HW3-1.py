print ("Welcome to May's Dungeon!")
command = "c"
currentroom = "kitchen"
insidelibrary = "c"

while (command != "q"):
	if currentroom == "kitchen":
		command = input ("You are in the kitchen. There are doors to the west(w),south(s) and east(e)")
		if command == "s":
			currentroom = "furnace"
		elif command == "w":
		    currentroom = "hallway"
		elif command == "e":
			currentroom = "livingroom"
	elif currentroom == "livingroom":
		command = input ("You are in the living room. There is door to the west(w)")
		if command == "w":
			currentroom = "kitchen"
	elif currentroom == "hallway":
		command = input ("You are in the hallway. There are doors to the south(s) and east(e)")
		if command == "s":
			currentroom = "library"
		elif command == "e":
			currentroom = "kitchen"
	elif currentroom == "library":
		command = input ("You are in the library. You sense the princess is here, but where? Look around (l)")
		if command == "l":
			insidelibrary = "lookaround"
			while (command != "q" and command != "n"):
				if insidelibrary == "lookaround":
					command = input ("You look, and see a picture (p), bookcase (b) closet(c)")
					if command == "b":
						insidelibnrary = "bookcase"
					elif command == "c":
						insidelibrary = "closet"
					elif command == "p":
						insidelibrary = "picture"
				elif insidelibrary == "bookcase":
					command = input("You look through the bookcase,and see your Python texebool.")
					if command == "b":
						insidelibrary = "bookcase"
					elif command == "c":
						insidelibrary = "closet"
					elif command == "p":
						insidelibrary = "picture"
				elif insidelibrary == "closet":
					command = input("You rummage through the closet,and you find SKELETONS!")
					if command == "b":
						insidelibrary = "bookcase"
					elif command == "c":
						insidelibrary = "closet"
					elif command == "p":
						insidelibrary = "picture"
				elif insidelibrary == "picture":
					print ("You look at the picture,and see the princess hiding in it! You are a hero!")
					command = "q"	
			if command == "n":
				currentroom = "hallway"
	elif currentroom == "furnace":
		print ("You enter the furnace and fry yourself to death!")
		command = "q"
		
print ("Goodbye!")


