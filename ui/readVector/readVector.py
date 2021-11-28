
def read_vector():
	name_id = input("Enter the name_id: ")
	ty = int(input("Enter the type of the vector: "))
	color = input("Enter color: ")
	value = []
	elem = input("Enter value: ")
	while elem != "":
		value.append(int(elem))
		elem = input("Enter value: ")
	return [name_id, ty, color, value]