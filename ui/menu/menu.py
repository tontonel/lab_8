def menu():
	"""
	prints menu and read command
	:return:
	"""
	print("1.Add a vector to repository")
	print("2.Get all vectors")
	print("3.Get a vector at a given index")
	print("4.Update a vector at a given index")
	print("5.Update a vector identified by name_id")
	print("6.Delete a vector by index")
	print("7.Delete a vector by name_id")
	print("8.Plot vectors in a chart")
	print("9.Get the list of vectors having a given sum of elements")
	print("10.Delete all vectors that are between two given indexes")
	print("11.Update all vectors by adding a given scalar to each element")
	print("0.Exit")
	command = int(input("Enter a command: "))
	print("")
	if not 0 <= command <= 11:
		raise ValueError("Your command is invalid")
	return command
