import random
## Program sprawdza najpierw wszystkie wektory, a następnie porównuje
## Następnie pobiera kolejną paczkę która zaiwera kolejne rekordy razem z poprzednimi
## Program dzieli się na 3 pod_programy
## 1 - Paczka od 1 do 1/3 rekordów
## 2 - Paczka od 1/3 do 2/3 rekordów
## 3 - Paczka od 2/3 do 3/3 rekordów
## 4 - Paczka całości
## Należy na początku wybrać, z której paczki chcemy korzystać , a następnie podać wektor, który zostanie sprawdzony a następnie dopisany do pliku

## Metody
def checkA(vector):
  howmanyA = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() is "A"):
      howmanyA += 1
  
  return howmanyA

def checkB(vector):
  howmanyB = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() == "B"):
      howmanyB += 1
  return howmanyB

def checkC(vector):
  howmanyC = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() == "C"):
      howmanyC += 1
  return howmanyC


def validiator(vector):
  if(checkA(vector) > checkB(vector) > checkC(vector)):
    print("A")
  elif(checkA(vector) < checkB(vector) > checkC(vector)):
    print("B")
  elif(checkA(vector) < checkB(vector) < checkC(vector)):
    print("C")
  elif(checkA(vector) == checkB(vector) and checkA(vector) > checkC(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("A")
    else:
      print("B")
  elif(checkA(vector) == checkC(vector) and checkA(vector) > checkB(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("A")
    else:
      print("C")
  elif(checkB(vector) == checkC(vector) and checkB(vector) > checkA(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("B")
    else:
      print("C")
  elif(checkA(vector) == checkC(vector) == checkB(vector)):
    rand = random.randint(0,2)
    if( rand == 0):
      print("A")
    elif(rand == 1):
      print("B")
    else:
      print("C")

## Wybranie z której paczki chcemy korzystac
print("Paczka od 0 do 1/3 całości - Podaj 1 ")
print("Paczka od 1/3 do 2/3 całości - Podaj 2 ")
print("Paczka od 2/3 do 1 całości - Podaj 3 ")
print("Sprawdź w całości - Podaj 4 ")
package = int(input("Podaj z którego przedziału program ma sprawdzić wektor : "))

if package==1:
  print("Sprawdzamy od 0 do 1/3")
  print("Podaj wektor : ")
  file = open("learning0.txt","r")
  wektory = []
  for line in file: 
    wektory.append(line.split("|"))
  file.close()
  vector = input()
  print(checkA(vector))
  print(checkB(vector))
  print(checkC(vector))
  validiator(vector)
  if checkA(vector) != 0 :  
    vector_zapis = "{}  |A".format(vector)
  elif checkB(vector) != 0 : 
    vector_zapis = "{}  |B".format(vector)
  elif checkC(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)
  elif checkA(vector) != 0 and checkB != 0 :
    vector_zapis = "{}  |B".format(vector)
  elif checkA(vector) != 0 and checkC(vector) != 0 :
    vector_zapis = "{}  |A".format(vector)
  elif checkC(vector) != 0 and checkB(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)

  elif checkC(vector) != 0 and checkB(vector) != 0 and checkA(vector) != 0 :
    vector_zapis = "{} |B".format(vector)
  
  vote = int(input("Czy chcesz dopisać wprowadzone dane do pliku ? ( Tak - 1 | Nie - 2 ) : "))
  if vote == 1 :
    file = open("learning0.txt","a")
    file.write('\n')
    file.write(vector_zapis)
  else:
    pass
elif package==2:
  print("Sprawdzamy od 1/3 do 2/3")
  print("Podaj wektor : ")
  file = open("learning1.txt","r")
  wektory = []
  for line in file: 
    wektory.append(line.split("|"))
  file.close()
  vector = input()
  print(checkA(vector))
  print(checkB(vector))
  print(checkC(vector))
  validiator(vector)
  if checkA(vector) != 0 :  
    vector_zapis = "{}  |A".format(vector)
  elif checkB(vector) != 0 : 
    vector_zapis = "{}  |B".format(vector)
  elif checkC(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)
  elif checkA(vector) != 0 and checkB != 0 :
    vector_zapis = "{}  |B".format(vector)
  elif checkA(vector) != 0 and checkC(vector) != 0 :
    vector_zapis = "{}  |A".format(vector)
  elif checkC(vector) != 0 and checkB(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)

  elif checkC(vector) != 0 and checkB(vector) != 0 and checkA(vector) != 0 :
    vector_zapis = "{} |B".format(vector)
  
  vote = int(input("Czy chcesz dopisać wprowadzone dane do pliku ? ( Tak - 1 | Nie - 2 ) : "))
  if vote == 1 :
    file = open("learning1.txt","a")
    file.write('\n')
    file.write(vector_zapis)
  else:
    pass
elif package==3:
  print("Sprawdzamy od 2/3 do 1")
  print("Podaj wektor : ")
  file = open("learning2.txt","r")
  wektory = []
  for line in file: 
    wektory.append(line.split("|"))
  file.close()
  vector = input()
  print(checkA(vector))
  print(checkB(vector))
  print(checkC(vector))
  validiator(vector)
  if checkA(vector) != 0 :  
    vector_zapis = "{}  |A".format(vector)
  elif checkB(vector) != 0 : 
    vector_zapis = "{}  |B".format(vector)
  elif checkC(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)
  elif checkA(vector) != 0 and checkB != 0 :
    vector_zapis = "{}  |B".format(vector)
  elif checkA(vector) != 0 and checkC(vector) != 0 :
    vector_zapis = "{}  |A".format(vector)
  elif checkC(vector) != 0 and checkB(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)
  elif checkC(vector) != 0 and checkB(vector) != 0 and checkA(vector) != 0 :
    vector_zapis = "{} |B".format(vector)
  else : 
    pass  
  
  vote = int(input("Czy chcesz dopisać wprowadzone dane do pliku ? ( Tak - 1 | Nie - 2 ) : "))
  if vote == 1 :
    file = open("learning2.txt","a")
    file.write('\n')
    file.write(vector_zapis)
  else:
    pass
elif package==4:
  print("Sprawdzamy w całości")
  print("Podaj wektor : ")
  file = open("learning3.txt","r")
  wektory = []
  for line in file: 
    wektory.append(line.split("|"))
  file.close()
  vector = input()
  print(checkA(vector))
  print(checkB(vector))
  print(checkC(vector))
  validiator(vector) 
  if checkA(vector) != 0 :  
    vector_zapis = "{}  |A".format(vector)
  elif checkB(vector) != 0 : 
    vector_zapis = "{}  |B".format(vector)
  elif checkC(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)
  elif checkA(vector) != 0 and checkB != 0 :
    vector_zapis = "{}  |B".format(vector)
  elif checkA(vector) != 0 and checkC(vector) != 0 :
    vector_zapis = "{}  |A".format(vector)
  elif checkC(vector) != 0 and checkB(vector) != 0 :
    vector_zapis = "{}  |C".format(vector)

  elif checkC(vector) != 0 and checkB(vector) != 0 and checkA(vector) != 0 :
    vector_zapis = "{} |B".format(vector)
  else:
    pass
  
  vote = int(input("Czy chcesz dopisać wprowadzone dane do pliku ? ( Tak - 1 | Nie - 2 ) : "))
  if vote == 1 :
    file = open("learning3.txt","a")
    file.write('\n')
    file.write(vector_zapis)
  else:
    pass