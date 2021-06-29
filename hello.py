import random
from numbers_game import sontop

#pythonda kirish qismi 
hello = 'Salom men python dasturiman'
print(hello) #print bu Salom men dasturchiman so'zini chiqarib beradi

name = input('Ismingiz nima >>')
print('Assalomu alaykum ', name + ' python darsimizga xush kelibsiz')

name_game = input(f"{name} Men bilan o\'yin o\'ynaysizmi? xa\yo >>")


if name_game == 'xa':
    start = sontop()
elif name_game == 'yoq':
    print('....')