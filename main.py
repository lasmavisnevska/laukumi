print("nebuus labi....")
print("porgramma pieprasa figūras elementus un aprēkina to laukumu")
print('nospiediet burtu:')
print("T - ja figura ir trijstūris")
print('tr - ja trapece')
print('p - ja figūra ir paralelograms')
print('ta - ja figura ir taisnstūris')
print('k - ja figura ir kvadrāts')
print('R -  ja figūra ir riņķis')
print('_________________________________________________________')

def taisnsturis():
  a = int(input("Ievadi ta garumu"))
  b = int(input("Ievadi ta platumu"))
  laukums4 = a*b
  print(laukums4)

def kvadrats():
  a = int(input("Ievadi kvadrāta malas garumu"))
  laukums5 = a*a
  print(laukums5)

def rinkis():
  a = 3.14
  b = int(input("Ievadi riņķa rādiusu"))
  laukums6 = a*(b*b)
  print(laukums6)