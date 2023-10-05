def bottle_song():
	for i in range(99, 0, -1):
		if i > 2:
			print(f'''{i} bottles of beer on the wall, {i} bottles of beer.
Take one down and pass it around, {i-1} bottles of beer on the wall.''')
		else:
			if i == 2:
				print(f'''{i} bottles of beer on the wall, {i} bottles of beer.
Take one down and pass it around, {i-1} bottle of beer on the wall.''')
				pass
			elif i == 1:
				print(f'''{i} bottle of beer on the wall, {i} bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.''')
			else:	
				print('''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.''')
	return "\nProgram finished.\n"

print(bottle_song())