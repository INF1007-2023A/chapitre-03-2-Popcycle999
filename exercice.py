#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	test_orthogonal = v1[0] * v2[0] + v1[1] * v2[1] 
	if test_orthogonal == 0:
		return True
	pass

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	x= 0
	y= 0
	for v in values:
		if v >= 0:
			x += v
			y += 1
		pass # La variable v contient une valeur de la liste.
	return x/y

def bills(value):
	twenties = value//20
	reste1 = (value/20 - value//20)*20

	tens = reste1//10
	reste2 = (reste1/10 - reste1//10)*10

	fives = reste2//5
	reste3 = (reste2/5 - reste2//5)*5

	twos = reste3//2
	ones = round((reste3/2 - reste3//2)*2)

	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.

	return (twenties, tens, fives, twos, ones)

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    
	result = ""
	abs_value = abs(value)
	while abs_value >= 1:
		nombre = abs_value % base
		result = digit_letters[nombre] + result
		abs_value = abs_value - base**nombre
	if value < 0:
		result = "-" + result
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
