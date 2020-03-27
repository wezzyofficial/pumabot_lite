def symbCheck(text):
	exclude = [chr(i) for i in range(0, 33)]
	exclude.remove(' ')
	exclude.remove('\n')
	for c in text:
		if c in exclude:
			return True
		else:
			return False