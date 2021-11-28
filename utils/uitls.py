def check_color(color):
	"""
	check the valid color
	:param color:
	:return:
	"""
	valid_colors = ['r', 'g', 'b', 'y', 'm']
	for col in valid_colors:
		if color == col:
			return True
	return False
