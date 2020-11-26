from files import *
from numpy import genfromtxt
import numpy as np
from matplotlib import pyplot as plt
from scipy import *
from math import sqrt

####################################################
# Code performed during the machine learning class,#
# at Unipampa University Alegrete campus,          #
# together with professor Marcelo Resende Thielo.  #
####################################################

tableData = readtable('datagen/dataX.dat')

# Values with their respective clusters
newTable = []

x1 =column(tableData,0)
x2 =column(tableData,1)

# Number of clusters
c=6

# Provisional center of each cluster
cCenters=[]

# Count of members in each cluster
cMembers=[]

# Initializing variables
for i in range(0,c):
  cCenters.append([0.0,0.0])
  cMembers.append(0.0)

# Assigning random cluster to each data
for i in range(0,len(tableData)):
  xTemp = [float(tableData[i][0]),float(tableData[i][1]),randint(0,c-1)]
  cMembers[xTemp[2]]=cMembers[xTemp[2]]+1.0
  newTable.append(xTemp)

# Dunction to calculate the distance of a point with the center of your current cluster
def dist(i,j):
  d=sqrt((newTable[i][0]-cCenters[j][0])**2+(newTable[i][1]-cCenters[j][1])**2)
  return d

# Iteration to readjust cluster members
for step in range(0,1000):
  # Sum of the x and y coordinates of each point in the cluster
  for i in range(0,len(tableData)):
    cCenters[newTable[i][2]][0]=cCenters[newTable[i][2]][0]+newTable[i][0]
    cCenters[newTable[i][2]][1]=cCenters[newTable[i][2]][1]+newTable[i][1]

  # Average of the previous sum by the number of members in the cluster, to get the cluster center
  for i in range(0,c):
    cCenters[i][0]=cCenters[i][0]/cMembers[i]
    cCenters[i][1]=cCenters[i][1]/cMembers[i]

  # Checks if the distance from the point to the center of your current cluster 
  # is less than some other cluster,
  # if it moves to this nearest cluster
  for i in range(0,len(tableData)):
    near=dist(i,newTable[i][2])

    for j in range(0,c):
      newNear=dist(i,j)

      if(newNear<near):
        near=newNear
        newTable[i][2]=j

# Generate cluster files
for i in range(0,c):
  fileName = "./clusters/"+str(i)+".dat"
  f = open(fileName, "w")

  for j in range(0,len(tableData)):
    if(newTable[j][2]==i):
      f.write(str(newTable[j][0])+" "+str(newTable[j][1])+"\n")
  f.close()

# Groups cluster centers for plotting
f = open("./clusters/centroids.dat", "w")
cX=[]
cY=[]
for i in range(0,c):
  f.write(str(cCenters[i][0])+" "+str(cCenters[i][1])+"\n")
  cX.append(cCenters[i][0])
  cY.append(cCenters[i][1])
f.close()
# Plot the result
plt.plot(x1,x2,"b.")
plt.plot(cX,cY,"ro")
plt.show()
