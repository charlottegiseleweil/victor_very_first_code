import random

def un_sur_combien(nombre_max, challenge):
  ## Write down challenge:
  print("Challenge: "+challenge +'\n')

  ## Players choose numbers
  print('Victor dit:')
  nb_victor = random.randrange(0,nombre_max)
  print(nb_victor)
  print('Charlotte dit:')
  nb_cha = random.randrange(0,nombre_max)
  print(nb_cha)

  ## Check if numbers are the same
  if nb_cha == nb_victor:
    print('Tu dois faire le challenge!!')
    print(challenge)
  else:
    print('Ok next')





un_sur_combien(10, "Va dire à tes parents que tu kiffes coder")
