from unittest import TestCase, main
from infrastructure.vectorRepository import VectorRepository
from domain.vector import MyVector


class VectorRepositoryTest(TestCase):

	def setUp(self):
		self.repo = VectorRepository([MyVector("123", 3, "b", [2, 3, 4]),
									  MyVector("543", 2, "r", [4, 7, 5, 4]),
									  MyVector("435", 4, "g", [7, 4, 6, 3, 5, 7])])

	def test_add(self):
		with self.assertRaises(ValueError):
			self.repo.add(MyVector("123", 2, "r", [1, 3, 4]))
			self.repo.add(MyVector("543", 1, "r", [1, 10, 4]))
			self.repo.add(MyVector("435", 70, "r", [1, 7, 4]))
		self.repo.add(MyVector("415", 3, "m", [2, 5, 2]))
		self.repo.add(MyVector("532", 6, "r", [3, 5, 3]))

	def test_get_all_vectors(self):
		self.repo.get_all_vectors()
		self.repo.add(MyVector("415", 3, "m", [2, 5, 2]))
		self.repo.get_all_vectors()
		self.repo.add(MyVector("532", 6, "r", [3, 5, 3]))
		self.repo.get_all_vectors()
		self.repo.add(MyVector("128", 2, "r", [1, 3, 4]))
		self.repo.get_all_vectors()

	def test_get_vector_index(self):
		with self.assertRaises(IndexError):
			self.repo.get_vector_index(-1)
			self.repo.get_vector_index(8)
			self.repo.get_vector_index(7)
		self.assertEqual(self.repo.get_vector_index(1), MyVector("543", 2, "r", [4, 7, 5, 4]))
		self.assertEqual(self.repo.get_vector_index(2), MyVector("435", 4, "g", [7, 4, 6, 3, 5, 7]))

	def test_update_vector_index(self):
		with self.assertRaises(IndexError):
			self.repo.update_vector_index(-1, MyVector("54100", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_index(7, MyVector("54100", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_index(5, MyVector("54100", 2, "r", [4, 7, 5, 4]))
		with self.assertRaises(ValueError):
			self.repo.update_vector_index(1, MyVector("123", 3, "b", [2, 3, 4]))
			self.repo.update_vector_index(2, MyVector("543", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_index(0, MyVector("435", 4, "g", [7, 4, 6, 3, 5, 7]))
		self.repo.update_vector_index(0, MyVector("465", 4, "g", [7, 4, 6, 3, 5, 7]))
		self.assertEqual(self.repo, VectorRepository([MyVector("465", 4, "g", [7, 4, 6, 3, 5, 7]),
									  MyVector("543", 2, "r", [4, 7, 5, 4]),
									  MyVector("435", 4, "g", [7, 4, 6, 3, 5, 7])]))

	def test_update_vector_name_id(self):
		with self.assertRaises(ValueError):
			self.repo.update_vector_name_id("412", MyVector("543", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_name_id("5467", MyVector("543", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_name_id("", MyVector("543", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_name_id("435", MyVector("543", 2, "r", [4, 7, 5, 4]))
			self.repo.update_vector_name_id("123", MyVector("543", 2, "r", [4, 7, 5, 4]))
		self.repo.update_vector_name_id("123", MyVector("700", 2, "r", [4, 7, 5, 4]))
		self.repo.update_vector_name_id("700", MyVector("54100", 2, "r", [4, 7, 5, 4]))

	def test_delete_vector_index(self):
		with self.assertRaises(IndexError):
			self.repo.delete_vector_index(-1)
			self.repo.delete_vector_index(10)
			self.repo.delete_vector_index(7)
		self.repo.delete_vector_index(0)
		self.repo.delete_vector_index(0)
		self.repo.delete_vector_index(0)

	def test_delete_vector_name_id(self):
		with self.assertRaises(ValueError):
			self.repo.delete_vector_name_id("7356")
			self.repo.delete_vector_name_id("343")
			self.repo.delete_vector_name_id("15")
			self.repo.delete_vector_name_id("123")
			self.repo.delete_vector_name_id("123")
		self.repo.delete_vector_name_id("543")
		self.repo.delete_vector_name_id("435")

	def test_get_vectors_with_sum(self):
		with self.assertRaises(Exception):
			self.repo.get_vectors_with_sum(700)
			self.repo.get_vectors_with_sum(-100)
			self.repo.get_vectors_with_sum(1)
		self.assertTrue(self.repo.get_vectors_with_sum(9) == VectorRepository([MyVector("123", 3, "b", [2, 3, 4])]))
		self.assertTrue(self.repo.get_vectors_with_sum(20) == VectorRepository([MyVector("543", 2, "r", [4, 7, 5, 4])]))

	def test_delete_between_indexes(self):
		with self.assertRaises(IndexError):
			self.repo.delete_between_indexes(1, 7)
			self.repo.delete_between_indexes(6, 7)
			self.repo.delete_between_indexes(7, 2)
			self.repo.delete_between_indexes(-1, 10)
			self.repo.delete_between_indexes(-10, 1)
		self.repo.delete_between_indexes(0, 1)
		self.repo.delete_between_indexes(0, 0)

	def test_add_vectors_scalar(self):
		self.repo = VectorRepository([])
		with self.assertRaises(Exception):
			self.repo.add_vectors_scalar(10)
			self.repo.add_vectors_scalar(-10)
		self.repo = VectorRepository([MyVector("123", 3, "b", [2, 3, 4]),
									  MyVector("543", 2, "r", [4, 7, 5, 4]),
									  MyVector("435", 4, "g", [7, 4, 6, 3, 5, 7])])
		self.repo.add_vectors_scalar(100)
		self.repo.add_vectors_scalar(-100)
