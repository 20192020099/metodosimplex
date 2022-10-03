#AUTOMATIZANDO
''' algoritmo simplex -------------------------------------------------'''
from scipy import linalg 
from numpy import *
import numpy as np

A = [[2,-1,3,1],
     [1,2,4,0]]

b = [[30],
     [40]]

c = [[-4],
     [-2],
     [-8],
     [0]]

XBasicas = [3,4]
XNo_basicas = [1,2]

'''construyendo B'''
B = []
for i in range(0, len(A)):
    for j in [elemento - 1 for elemento in XBasicas]:
        B.append(A[i][j])
#de lista a matriz
fila = len(A)
col = len(XBasicas)
B = [B[col*i : col*(i+1)] for i in range(fila)]
B = np.asmatrix(B)
B

Xb = (linalg.inv(B))*b
Xb = Xb.tolist()
Xb
#BUSCANDO SOLUCION BASICA
posiciones = [elemento - 1 for elemento in XBasicas]
D={}
for i in range(len(Xb)):
    D[posiciones[i]]=Xb[i]

X = [[0]]*len(A[0])
for i in posiciones:
    X[i]=D[i]
#construyendo la matriz columna
XB = np.asmatrix(X)
XB

matriz_ceros = []
posiciones = [r-1 for r in XBasicas]
for i in posiciones:
    matriz_ceros.append(c[i][0])

CtB = matriz_ceros

matriz_ceros = [] 
posiciones = [r-1 for r in XNo_basicas]
for i in posiciones:
    matriz_ceros.append(c[i][0])

CtN = matriz_ceros

N = []
for i in range(0, len(A)):
    for j in [elemento - 1 for elemento in XNo_basicas]:
        N.append(A[i][j])
#de lista a matriz
fila = len(A)
col = len(XNo_basicas)
N = [N[col*i : col*(i+1)] for i in range(fila)]
N = np.asmatrix(N)
N

CtB = np.asmatrix(CtB)
Yt = CtB*linalg.inv(B)
Yt

CtN = np.asmatrix(CtN)
CN_sombrero = CtN - Yt*N
CN_sombrero #si todos positivos, hemos terminado
lista_CN_sombrero = CN_sombrero.tolist()
print('CN_sombrero: \n',lista_CN_sombrero)
def interruptor(lista_CN_sombrero):
  for i in lista_CN_sombrero[0]:
    if i < 0 :
      return 'negativo encontrado'
      break
  contador = 0
  for i in lista_CN_sombrero[0]:
    if i >= 0 :
      contador += 1
      if contador == len(lista_CN_sombrero[0]):
        return 'todos positivos o cero'
print(interruptor(lista_CN_sombrero))  
print('')

#entrada o no al bucle
while interruptor(lista_CN_sombrero) == 'negativo encontrado' :
  ''' ubicando al menor'''
  CN_sombrero = CN_sombrero.tolist()
  min(CN_sombrero[0])
  indice = CN_sombrero[0].index(  min(CN_sombrero[0])  )

  '''variable entrante '''
  n = XNo_basicas[indice]
 
  n #señala la fila a trabajar
  print('n entrante: \n',n)
  print('')
  An = []
  for i in range(0, len(A)):
      for j in [elemento - 1 for elemento in [n]]:
          An.append(A[i][j])
  #de lista a matriz
  fila = len(A)
  col = 1
  An = [An[col*i : col*(i+1)] for i in range(fila)]
  An = np.asmatrix(An)
  An

  An_sombrero = linalg.inv(B)*An
  b_sombrero = linalg.inv(B)*np.asmatrix(b)
  An_sombrero = An_sombrero.tolist()
  b_sombrero  = b_sombrero.tolist()
  An_sombrero
  print('An_sombrero : \n',An_sombrero)
  print('')
  listar = []
  for i in range(len(A)):
      if An_sombrero[i][0] <= 0:
          listar.append(1000000)  #para evitar negativos              
      elif An_sombrero[i][0] > 0:
          ratio = b_sombrero[i][0]/An_sombrero[i][0]
          listar.append(ratio)
      
  ''' ubicando al menor en ratio test'''   
  min(listar)
  indice = listar.index( min(listar) )
  '''variable saliente'''  
  s = XBasicas[indice]
  s
  print('s saliente: \n',s)
  print('')

  indice_sale = XBasicas.index(s)
  XBasicas[indice_sale] = n
  indice_entra = XNo_basicas.index(n)
  XNo_basicas[indice_entra] = s

  XBasicas
 
  XNo_basicas
 

  B = []
  for i in range(0, len(A)):
      for j in [elemento - 1 for elemento in XBasicas]:
          B.append(A[i][j])
  #B de lista a matriz
  fila = len(A)
  col = len(XBasicas)
  B = [B[col*i : col*(i+1)] for i in range(fila)]
  B = np.asmatrix(B)
  B
 
  Xb = (linalg.inv(B))*b
  Xb = Xb.tolist()
  Xb

  #construyendo solucion basica
  posiciones = [elemento - 1 for elemento in XBasicas]
  D={}
  for i in range(len(Xb)):
      D[posiciones[i]]=Xb[i]

  X = [[0]]*len(A[0])
  for i in posiciones:
      X[i]=D[i]
  X
  #construyendo la matriz columna
  XB = np.asmatrix(X)
  XB

  matriz_ceros = []
  posiciones = [r-1 for r in XBasicas]
  for i in posiciones:
      matriz_ceros.append(c[i][0])

  CtB = matriz_ceros
  CtB
 
  matriz_ceros = []
  posiciones = [r-1 for r in XNo_basicas]
  for i in posiciones:
      matriz_ceros.append(c[i][0])

  CtN = matriz_ceros
  CtN
  
  N = []
  for i in range(0, len(A)):
      for j in [elemento - 1 for elemento in XNo_basicas]:
          N.append(A[i][j])
  #de lista a matriz
  fila = len(A)
  col = len(XNo_basicas)
  N = [N[col*i : col*(i+1)] for i in range(fila)]
  N = np.asmatrix(N)
  N

  QCtB = np.asmatrix(CtB)
  Yt = CtB*linalg.inv(B)
  Yt
 
  CtN = np.asmatrix(CtN)
  CN_sombrero = CtN - Yt*N
  CN_sombrero #si todos positivos, hemos terminado
  lista_CN_sombrero = CN_sombrero.tolist()
  print('CN_sombrero : \n',lista_CN_sombrero)  
  interruptor(lista_CN_sombrero)
  print(interruptor(lista_CN_sombrero))
  print('')  
'''hallando Z funcion objetivo'''
Z = CtB*linalg.inv(B)*b
Z_lista = Z.tolist()
Z_lista
print('RPTA')
print('Z= ', Z_lista[0][0])
