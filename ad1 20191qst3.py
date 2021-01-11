class Resolucao:
  def __init__(self,matriz):
    self.matriz = matriz
 
  def calculaMatriz(self):
    min = int(self.matriz[0][0])
    max = int(self.matriz[0][0])
    pos1 = ""
    pos2 = ""
    for l in range(len(self.matriz)):
      for c in range(len(self.matriz[l])):
        if(int(self.matriz[l][c]) > max):
          max = int(self.matriz[l][c])
          pos2 = f"({l}, {c})"
        if(int(self.matriz[l][c]) < min):
          min = int(self.matriz[l][c])
          pos1 = f"({l}, {c})"
    return min,max,pos1,pos2       

  def printaMatriz(self,me,ma,p1,p2):
    print("----- Matriz Lida ------")
    for l in range(len(self.matriz)):
      for c in range(len(self.matriz[l])):
        print(self.matriz[l][c], end=" ")
      print()  
    print("------------------------")  
    print(f"Menor valor: {me} na posicção {p1}")
    print(f"Maior valor: {ma} na posicção {p2}")



matriz = []
entrada = input()

while entrada != "":
   matriz.append(entrada.split(" "))
   entrada = input()

res = Resolucao(matriz)
valores = res.calculaMatriz()
res.printaMatriz(valores[0],valores[1],valores[2],valores[3])