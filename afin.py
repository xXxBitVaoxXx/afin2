from math import gcd


def cipher():
	alphabet = 'qwertyuiopasdfghjklzxcvbnmйцукёенгшщзхъфывапролджэячсмитьбю'
	alphabet = ''.join(sorted(set(alphabet)))
	length = len(alphabet)
	res = ''
	print(alphabet)
	print(len(alphabet))

	with open("otext.txt", 'r') as l:
		text = l.read()
		text = text.lower().rstrip()

	al = [alpha for alpha in range(1, length) if gcd(length, alpha) == 1]
	print(' '.join(map(str,al)))

	alpha = int(input("Выбирите альфа: "))
	while alpha not in al:
		alpha = int(input("Выберете альфа: "))

	betta = int(input("Выбирите бетта: "))
	
	for char in text:
		num = alphabet.find(char)
		y = (alpha * num + betta) % length
		res += alphabet[y]
	print(res)	


	with open('ctext.txt', 'w') as f:
		for char in range(len(text)):
			f.write(res[char])	



		

cipher()
