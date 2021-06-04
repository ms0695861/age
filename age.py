#age judement

driving = input('Have you ever driven a car? (Y/N): ')
if driving != 'Y' and driving != 'N':
	print('Please enter Y or N! Thanks!')
	raise SystemExit
age = input('How old are you?: ')
age = int(age)

if driving == 'Y':
	if age >= 18:
		print('PASS!!')
	else:
		print('It is illegal')
elif driving == 'N':
	if age >= 18:
		license = input('Did you have driver license? (Y/N): ')
		if license != 'Y' and license != 'N':
				print('Please enter Y or N! Thanks!')
				raise SystemExit
		elif license == 'Y':
			print('Why not drive?')
		elif license == 'N':
			print('Why not get driver license?')
	else:
		print('You can drive few year later.')
