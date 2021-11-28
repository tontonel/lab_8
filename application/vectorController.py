from domain.vector import MyVector
from infrastructure.vectorRepository import VectorRepository


class VectorController:
	def __init__(self, repository: VectorRepository = VectorRepository()):
		"""
		initialize controller
		"""
		self.__repo = repository

	def add_vector(self, name_id, ty, color, value):
		"""
		add a vector in repository
		:return:
		"""
		new_vector = MyVector(name_id, ty, color, value)
		self.__repo.add(new_vector)
		print(self.__repo)

	def get_all_vectors(self):
		"""
		get all vectors from repository
		:return:
		"""
		print(self.__repo.get_all_vectors())

	def get_vector_index(self, index):
		"""
		get a vector with a given index
		:return:
		"""
		print("")
		print(self.__repo.get_vector_index(index))

	def update_at_index(self, index, name_id, ty, color, value):
		"""
		update at a given index
		:param index:
		:param name_id:
		:param ty:
		:param color:
		:param value:
		:return:
		"""
		new_vector = MyVector(name_id, ty, color, value)
		self.__repo.update_vector_index(index, new_vector)
		print(self.__repo)

	def update_at_name_id(self, name, name_id, ty, color, value):
		"""
		update at a given index
		:param name:
		:param name_id:
		:param ty:
		:param color:
		:param value:
		:return:
		"""
		new_vector = MyVector(name_id, ty, color, value)
		self.__repo.update_vector_name_id(name, new_vector)
		print(self.__repo)

	def delete_at_index(self, index):
		"""
		delete at a given index
		:return:
		"""
		self.__repo.delete_vector_index(index)
		print(self.__repo)

	def delete_at_name_id(self, name_id):
		"""
		delete at vector with given name_id
		:param name_id:
		:return:
		"""
		self.__repo.delete_vector_name_id(name_id)
		print(self.__repo)

	def plot_all_vectors(self):
		"""
		plot all vectors in a chart
		:return:
		"""
		self.__repo.plot_all_vectors()

	def get_vectors_sum(self, s):
		"""
		get all vectors with a given sum
		:param s:
		:return:
		"""
		print(self.__repo.get_vectors_with_sum(s))

	def delete_between_indexes(self, index_1, index_2):
		"""
		delete vectors between two indexes
		:param index_1:
		:param index_2:
		:return:
		"""
		self.__repo.delete_between_indexes(index_1, index_2)
		print(self.__repo)

	def update_with_scalar(self, scalar):
		"""
		update all vectors with a given scalar
		:param scalar:
		:return:
		"""
		self.__repo.add_vectors_scalar(scalar)
		print(self.__repo)
