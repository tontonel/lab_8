from matplotlib import pyplot as plt


class VectorRepository:
	def __init__(self, vector_list = None):
		"""
		making a constructor for my vector infrastructure
		:param vector_list:
		"""
		if vector_list is None:
			vector_list = []
		self.__vector_list = vector_list

	def add(self, vector):
		"""
		add a vector in a infrastructure
		:param vector:
		:return:
		"""
		for vct in self.__vector_list:
			if vector.get_name_id() == vct.get_name_id():
				raise ValueError("There exist another vector with same name_id")
		self.__vector_list.append(vector)

	def get_all_vectors(self):
		"""
		returns all the vectors
		:return:
		"""
		return VectorRepository(self.__vector_list.copy())

	def get_vector_index(self, index):
		"""
		get a vector at an index
		:param index:
		:return:
		"""
		if not 0 <= index <= len(self.__vector_list):
			raise IndexError("Your index is out of range")

		return self.__vector_list[index]

	def update_vector_index(self, index, vector):
		"""
		update a vector at a given index
		:param index:
		:param vector:
		:return:
		"""
		if not 0 <= index <= len(self.__vector_list):
			raise IndexError("Your index is out of range")
		for vct in self.__vector_list:
			if vct.get_name_id() == vector.get_name_id():
				raise ValueError("There exist an identical ID in repository")
		self.__vector_list[index] = vector

	def update_vector_name_id(self, name_id, vector):
		"""
		update the vector with name_id
		:param name_id:
		:param vector:
		:return:
		"""
		if name_id == "":
			raise ValueError("ID is mandatory")
		for vct in self.__vector_list:
			if vct.get_name_id() == vector.get_name_id():
				raise ValueError("There exist an identical ID in repository")
		name_index = -1
		for i in range(len(self.__vector_list)):
			if self.__vector_list[i].get_name_id() == name_id:
				name_index = i
		if name_index != -1:
			self.__vector_list[name_index] = vector
			return
		raise ValueError(f"There is no vector with f{name_id} name_id")

	def delete_vector_index(self, index):
		"""
		delete a vector at a given index
		:param index:
		:return:
		"""
		if not 0 <= index <= len(self.__vector_list):
			raise IndexError("Your index is out of range")
		self.__vector_list.pop(index)

	def delete_vector_name_id(self, name_id):
		"""
		delete a vector with a given name_id
		:param name_id:
		:return:
		"""
		name_index = -1
		if name_id == "":
			raise ValueError("ID is mandatory")
		for i in range(len(self.__vector_list)):
			if self.__vector_list[i].get_name_id() == name_id:
				name_index = i
		if name_index == -1:
			raise ValueError(f"There is no vector with {name_id} name_id")
		self.__vector_list.pop(name_index)

	def plot_all_vectors(self):
		"""
		plot all the vectors in a chart
		:return:
		"""
		def check_shape(ty):
			"""
			returns the shape for the the value in the chart
			:param ty:
			:return:
			"""
			if ty == 1:
				return 'o'
			if ty == 2:
				return 's'
			if ty == 3:
				return '^'
			return 'd'

		for vector in self.__vector_list:
			for index, value in enumerate(vector.get_list()):
				plt.scatter(index, value, color = vector.get_color(), marker = check_shape(vector.get_type()))
		plt.show()

	def get_vectors_with_sum(self, given_sum):
		"""
		get a list of vectors with a given sum
		:return:
		"""
		vectors_sum = []
		for vector in self.__vector_list:
			if vector.sum_of_elements() == given_sum:
				vectors_sum.append(vector)
		if len(vectors_sum) == 0:
			raise Exception("There are no vectors with given sum")
		return VectorRepository(vectors_sum)

	def delete_between_indexes(self, index_1, index_2):
		"""
		delete vectors between two indexes
		:param index_1:
		:param index_2:
		:return:
		"""
		new_list = []
		if index_1 >= len(self.__vector_list) or index_2 >= len(self.__vector_list):
			raise IndexError("Out of range")
		for index, vector in enumerate(self.__vector_list):
			if not index_1 <= index <= index_2:
				new_list.append(vector)
		self.__vector_list = new_list

	def add_vectors_scalar(self, scalar):
		"""
		multiply all the vectors with a given scalar
		:return:
		"""
		if len(self.__vector_list) == 0:
			raise Exception("There are no vectors in repository")
		for vector in self.__vector_list:
			vector.add_scalar(scalar)

	def __str__(self):
		if len(self.__vector_list) == 0:
			return "\nThere is no vector in repository\n"
		text = "\n"
		for vector in self.__vector_list:
			text += vector.__str__()
		return text

	def __eq__(self, other):
		if len(self.__vector_list) == len(other.__vector_list):
			for i in range(len(self.__vector_list)):
				if self.__vector_list[i] != other.__vector_list[i]:
					return False
			return True
		return False
