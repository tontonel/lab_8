from utils.uitls import check_color


class MyVector:

	def __init__(self, name_id, ty, color, values):
		"""
		construct the vector
		:param name_id: the name of the vector
		:param color: the color of the vector
		:param ty: the type of the vector
		:param values: the values given
		"""
		if len(values) == 0:
			raise ValueError("There are no values in the vector")
		if not check_color(color):
			raise ValueError("The only possible colors are: r, g, b, y, m")
		if ty <= 0:
			raise ValueError("The type of the vector should be greater or equal to 1")
		if len(name_id) == 0:
			raise ValueError("ID is mandatory")
		self.__name_id = name_id
		self.__type = ty
		self.__color = color
		self.__values = values.copy()

	def get_list(self):
		"""
		get the list of coordinates
		:return:
		"""
		return self.__values.copy()

	def get_name_id(self):
		"""
		get the name id
		:return:
		"""
		return self.__name_id

	def get_color(self):
		"""
		get the color
		:return:
		"""
		return self.__color

	def get_type(self):
		"""
		get the type of a vector
		:return:
		"""
		return self.__type

	def add_scalar(self, scalar):
		"""
		add a vector with a scalar
		:return:
		"""
		for i in range(len(self.__values)):
			self.__values[i] += scalar

	def __add__(self, other):
		"""
		add two vectors
		:param other:
		:return:
		"""
		if len(self.__values) != len(other.__values):
			raise Exception("The length of the values must be the same")
		for i in range(len(self.__values)):
			self.__values[i] += other.__values[i]

	def __sub__(self, other):
		"""
		subtract two vectors
		:param other:
		:return:
		"""
		if len(self.__values) != len(other.__values):
			raise Exception("The length of the values must be the same")
		for i in range(len(self.__values)):
			self.__values[i] -= other.__values[i]

	def __mul__(self, other):
		"""
		multiply two vectors
		:param other:
		:return:
		"""
		if len(self.__values) != len(other.__values):
			raise Exception("The length of the values must be the same")
		product = 0
		for i in range(len(self.__values)):
			product += self.__values[i] * other.__values[i]
		return product

	def sum_of_elements(self):
		"""
		calculate the sum of the elements in a vector
		:return:
		"""
		s = sum(self.__values)
		return s

	def product_of_elements(self):
		"""
		calculate the product of values in a vector
		:return:
		"""
		product = 1
		for elem in self.__values:
			product *= elem
		return product

	def average_of_elements(self):
		"""
		calculate the average of elements
		:return:
		"""
		s = 0
		for elem in self.__values:
			s += elem
		return s / len(self.__values)

	def minimum_of_vector(self):
		"""
		get the minimum of values in a vector
		:return:
		"""
		return min(self.__values)

	def maximum_of_vector(self):
		"""
		get the maximum value from values
		:return:
		"""
		return max(self.__values)

	def __str__(self):
		return f"vector: id {self.__name_id}, values ({self.__values}), color {self.__color}, type {self.__type}\n"

	def __eq__(self, other):
		if (self.__name_id == other.__name_id
			and self.__type == other.__type
			and self.__color == other.__color
			and other.__values == self.__values):
			return True
		return False

