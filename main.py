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

def trijsturis():
  a = int(input('ievadi malas garumu'))
  h = int(input("ievadi trijstūra augstumu"))
  laukums1 = a*h 
  print(laukums1)
def trapece():
  pamats1 = int(input('ievadi pirmā pamata garumu'))
  pamats2 = int(input('ievadi otrā pamata garumu'))
  h = int(input("ievadi trapeces augstumu")) 
  laukums2 = ((pamats1 + pamats2)* h) / 2
  print(laukums2)
def paralelograms():
  malas_garums = int(input("ievadi paralelograma malas garumu"))
  augstums = int(input("ievadi augstumu kas novilkts perpendikulāri malas garumam"))
  laukums3 = malas_garums * augstums
  print(laukums3)

figura = int(input('ievadi izvēlēto figūras saīsinājumu, kurus vēlies aprēkināt'))


