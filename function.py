import random
import sys

DEFINE_MAX_DISTANCE = float('inf')
burteForceCalculationCount = 0
divideAndConquerCalculationCount = 0


def createListOfPoint(dimension, numOfPoint, maxCoordinate):
    listOfPoint = []
    for i in range(numOfPoint):
        point = []
        for j in range(dimension):
            point.append(round(random.uniform(-maxCoordinate, maxCoordinate), 2))
        listOfPoint.append(point)
    listOfPoint.sort(key = lambda x:x[0])
    return listOfPoint

def calculateDistance(firstPoint, secondPoint):
    euclideanSquare = 0
    for i in range(len(firstPoint)):
        euclideanSquare += (firstPoint[i]-secondPoint[i])**2
    return euclideanSquare**0.5

def inMiddleArea(point, midOfAxis, maxDist):
    inMiddle = (abs(point[0]-midOfAxis)<=maxDist)
    return inMiddle

def divideAndConquer(listOfPoint):
    global divideAndConquerCalculationCount
    closestPoint = []
    if len(listOfPoint)==1:
        return DEFINE_MAX_DISTANCE, closestPoint
    if len(listOfPoint)==2:
        divideAndConquerCalculationCount += 1
        closestPoint += listOfPoint
        return calculateDistance(listOfPoint[0], listOfPoint[1]), closestPoint
    else:
        firstSection = listOfPoint[:len(listOfPoint)//2]
        secondSection = listOfPoint[len(listOfPoint)//2:]
        midOfAxis = ((listOfPoint[(len(listOfPoint)//2)-1][0] - listOfPoint[(len(listOfPoint)//2)][0]) / 2) + listOfPoint[(len(listOfPoint)//2)-1][0]
        smallestDistanceFirstSection, closestPointFirstSection = divideAndConquer(firstSection)
        smallestDistanceSecondSection, closestPointSecondSection = divideAndConquer(secondSection)
        smallestDistance = min(smallestDistanceFirstSection, smallestDistanceSecondSection)
        closestPoint = closestPointFirstSection if (smallestDistance == smallestDistanceFirstSection) else closestPointSecondSection
        for firstPoint in firstSection :
            if inMiddleArea(firstPoint, midOfAxis, smallestDistance):
                for secondPoint in secondSection :
                    if inMiddleArea(secondPoint, midOfAxis, smallestDistance):
                        distance = calculateDistance(firstPoint, secondPoint)
                        divideAndConquerCalculationCount += 1
                        smallestDistance = min(distance, smallestDistance)
                        closestPoint = closestPoint if (smallestDistance!=distance) else [firstPoint, secondPoint]
        return smallestDistance, closestPoint
        
def bruteForce(listOfPoint):
    global burteForceCalculationCount, firstPoint, secondPoint
    smallestDistance = DEFINE_MAX_DISTANCE
    for firstPoint in listOfPoint:
        for secondPoint in listOfPoint:
            if firstPoint != secondPoint :
                smallestDistance = min(smallestDistance, calculateDistance(firstPoint, secondPoint))
                burteForceCalculationCount += 1
    return smallestDistance