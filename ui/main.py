from ui.menu.menu import menu
from application.vectorController import VectorController
from ui.readVector.readVector import read_vector
from data_example import data_example
from infrastructure.vectorRepository import VectorRepository


def run():
	"""
	run the program
	:return:
	"""
	command = -1
	controller = VectorController(VectorRepository(data_example()))
	while command != 0:
		try:
			command = menu()
			if command == 1:
				[name_id, ty, color, value] = read_vector()
				controller.add_vector(name_id, ty, color, value)
			if command == 2:
				controller.get_all_vectors()
			if command == 3:
				index = int(input("Enter index: "))
				controller.get_vector_index(index)
			if command == 4:
				index = int(input("Enter index: "))
				[name_id, ty, color, value] = read_vector()
				controller.update_at_index(index, name_id, ty, color, value)
			if command == 5:
				name = input("Enter the name_id for given vector: ")
				[name_id, ty, color, value] = read_vector()
				controller.update_at_name_id(name, name_id, ty, color, value)
			if command == 6:
				index = int(input("Enter index: "))
				controller.delete_at_index(index)
			if command == 7:
				name_id = input("Enter name_id: ")
				controller.delete_at_name_id(name_id)
			if command == 8:
				controller.plot_all_vectors()
			if command == 9:
				s = int(input("Enter the sum: "))
				controller.get_vectors_sum(s)
			if command == 10:
				index_1 = int(input("Enter first index: "))
				index_2 = int(input("Enter second index: "))
				controller.delete_between_indexes(index_1, index_2)
			if command == 11:
				scalar = int(input("Enter the scalar: "))
				controller.update_with_scalar(scalar)
		except ValueError as Vr:
			print(f"\n{Vr}\n")
		except IndexError as Ir:
			print(f"\n{Ir}\n")
		except Exception as Ex:
			print(f"\n{Ex}\n")


