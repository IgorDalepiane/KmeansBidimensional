from files import *
from numpy import genfromtxt
import numpy as np
from matplotlib import pyplot as plt
from scipy import *
from math import sqrt
a = readtable('datagen/dataX.dat')

b = []
x1 =column(a,0)
x2 =column(a,1)
k=16
mu=[]
membros=[]
for i in range(0,k):
  mu.append([0.0,0.0])
  membros.append(0.0)


for i in range(0,len(a)):
  temp = [float(a[i][0]),float(a[i][1]),randint(0,k-1)]
  membros[temp[2]]=membros[temp[2]]+1.0
  b.append(temp)
# print(b)

def dist(i,j):
  d=sqrt((b[i][0]-mu[j][0])**2+(b[i][1]-mu[j][1])**2)
  return d

for step in range(0,1000):
  for i in range(0,len(a)):
    # print(b[i][2])
    mu[b[i][2]][0]=mu[b[i][2]][0]+b[i][0]
    mu[b[i][2]][1]=mu[b[i][2]][1]+b[i][1]

  for i in range(0,k):
    mu[i][0]=mu[i][0]/membros[i]
    mu[i][1]=mu[i][1]/membros[i]

  for i in range(0,len(a)):
    near=dist(i,b[i][2])
    for j in range(0,k):
      nnear=dist(i,j)
      if(nnear<near):
        near=nnear
        b[i][2]=j


for i in range(0,k):
  nome = "./cluster"+str(i)+".dat"
  f = open(nome, "w")

  for j in range(0,len(a)):
    if(b[j][2]==i):
      f.write(str(b[j][0])+" "+str(b[j][1])+"\n")
  f.close()

cx=[]
cy=[]
for i in range(0,k):
  cx.append(mu[i][0])
  cy.append(mu[i][1])

plt.plot(x1,x2,"b.")
plt.plot(cx,cy,"ro")
plt.show()
