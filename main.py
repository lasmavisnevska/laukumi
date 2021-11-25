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

