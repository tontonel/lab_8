from unittest import TestCase, main
from domain.vector import MyVector


class TestMyVector(TestCase):

	def setUp(self):
		self.vector = MyVector("123", 4, "r", [4, 7, 5])

	def test_add_scalar(self):
		self.vector.add_scalar(10)
		self.assertEqual(self.vector, MyVector("123", 4, "r", [14, 17, 15]))
		self.vector.add_scalar(-3)
		self.assertEqual(self.vector, MyVector("123", 4, "r", [11, 14, 12]))
		self.vector.add_scalar(5)
		self.assertEqual(self.vector, MyVector("123", 4, "r", [16, 19, 17]))
		self.vector.add_scalar(0)
		self.assertEqual(self.vector, MyVector("123", 4, "r", [16, 19, 17]))

	def test_add(self):
		with self.assertRaises(Exception):
			self.vector.__add__(MyVector("123", 4, "r", [4, 7, 5, 10]))
			self.vector.__add__(MyVector("123", 4, "r", [10, 4, 7, 5, 10]))
			self.vector.__add__(MyVector("123", 4, "r", [-1, 4, 7, 5, 10]))
		self.vector.__add__(MyVector("123", 4, "r", [10, 4, 7]))
		self.assertTrue(self.vector == MyVector("123", 4, "r", [14, 11, 12]))

	def test_sub(self):
		with self.assertRaises(Exception):
			self.vector.__sub__(MyVector("123", 4, "r", [4, 7, 5, 10]))
			self.vector.__sub__(MyVector("123", 4, "r", [10, 4, 7, 5, 10]))
			self.vector.__sub__(MyVector("123", 4, "r", [-1, 4, 7, 5, 10]))
		self.vector.__sub__(MyVector("123", 4, "r", [10, 4, 7]))
		self.assertTrue(self.vector == MyVector("123", 4, "r", [-6, 3, -2]))

	def test_mul(self):
		with self.assertRaises(Exception):
			self.vector.__mul__(MyVector("123", 4, "r", [4, 7, 5, 10]))
			self.vector.__mul__(MyVector("123", 4, "r", [10, 4, 7, 5, 10]))
			self.vector.__mul__(MyVector("123", 4, "r", [-1, 4, 7, 5, 10]))
		self.assertEqual(self.vector.__mul__(MyVector("123", 4, "r", [1, 2, 3])), 33)

	def test_sum_of_elements(self):
		self.assertEqual(self.vector.sum_of_elements(), 16)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 5, 10])
		self.assertEqual(self.vector.sum_of_elements(), 25)
		self.vector = MyVector("123", 4, "r", [1, 2, 3])
		self.assertEqual(self.vector.sum_of_elements(), 6)
		self.vector = MyVector("123", 4, "r", [4, 7, 5, 10])
		self.assertEqual(self.vector.sum_of_elements(), 26)

	def test_product_of_elements(self):
		self.assertEqual(self.vector.product_of_elements(), 140)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 0])
		self.assertEqual(self.vector.product_of_elements(), 0)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 5])
		self.assertEqual(self.vector.product_of_elements(), -140)
		self.vector = MyVector("123", 4, "r", [1, 2, 3])
		self.assertEqual(self.vector.product_of_elements(), 6)

	def test_average_of_elements(self):
		self.assertEqual(self.vector.average_of_elements(), 16 / 3)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 0])
		self.assertEqual(self.vector.average_of_elements(), 10 / 4)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 5])
		self.assertEqual(self.vector.average_of_elements(), 15 / 4)
		self.vector = MyVector("123", 4, "r", [1, 2, 3])
		self.assertEqual(self.vector.average_of_elements(), 2)

	def test_minimum_of_vector(self):
		self.assertEqual(self.vector.minimum_of_vector(), 4)
		self.vector = MyVector("123", 4, "r", [-1, 4, 7, 0])
		self.assertEqual(self.vector.minimum_of_vector(), -1)
		self.vector = MyVector("123", 4, "r", [-3, 4, 7, 5])
		self.assertEqual(self.vector.minimum_of_vector(), -3)
		self.vector = MyVector("123", 4, "r", [1, 2, 3])
		self.assertEqual(self.vector.minimum_of_vector(), 1)

	def test_maximum_of_vector(self):
		self.assertEqual(self.vector.maximum_of_vector(), 7)
		self.vector = MyVector("123", 4, "r", [-1, 4, 10, 0])
		self.assertEqual(self.vector.maximum_of_vector(), 10)
		self.vector = MyVector("123", 4, "r", [-3, 4, 5, 5])
		self.assertEqual(self.vector.maximum_of_vector(), 5)
		self.vector = MyVector("123", 4, "r", [1, 2, 3])
		self.assertEqual(self.vector.maximum_of_vector(), 3)


if __name__ == "__main__":
	main()