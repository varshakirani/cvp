#!/usr/bin/python2
import tensorflow as tf
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.nets as nets
import os
import sys
#Data load

def generateLabels(directory):

    dirNames = os.listdir(directory)
    flowerNames = []
    for n in dirNames:
        if not n.startswith('.') and not n.endswith(".txt"): #ignore hidden files and other files
            flowerNames.append(n)

    flowerLabel = {}
    for i,name in enumerate(flowerNames):
        flowerLabel[name] = i

    pathAndLabel = []

    for flower in flowerNames:
        for img in os.listdir(os.path.join(directory,flower)):
            filepath = os.path.join(directory,flower,img)
            label = flower
            pathAndLabel.append((filepath,flowerLabel[label]))


    path,labels = zip(*pathAndLabel)

    return list(path),list(labels),list(flowerNames)


def main():
    path,labels,flowerNames=generateLabels("flower/flower_photos")
    #print labels
    #print path
    #print flowerNames

if __name__ == '__main__':
    sys.exit(main())
else:
    print("Loaded as a module!")