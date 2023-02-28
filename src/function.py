import random
import sys

DEFINE_MAX_DISTANCE = float('inf')      # Digunakan jika pada satu bagian hanya terdapat 1 titik
divideAndConquerCalculationCount = 0    # Menghitung banyak kalkulasi divide and conquer
burteForceCalculationCount = 0          # Menghitung banyak kalkulasi brute force


def createListOfPoint(dimension, numOfPoint, maxCoordinate):
    # Membuat list of titik dengan dimensi, banyak titik, dan rentang posisi yang sudah ditentukan. menghasilkan nested list
    listOfPoint = []
    for i in range(numOfPoint):
        point = []
        for j in range(dimension):
            point.append(round(random.uniform(-maxCoordinate, maxCoordinate), 2))
        listOfPoint.append(point)
    listOfPoint.sort(key = lambda x:x[0])
    return listOfPoint

def calculateDistance(firstPoint, secondPoint):
    # Menghitung jarak 2 buah titik
    euclideanSquare = 0
    for i in range(len(firstPoint)):
        euclideanSquare += (firstPoint[i]-secondPoint[i])**2
    return euclideanSquare**0.5

def inMiddleArea(point, midOfAxis, maxDist):
    # Memeriksa apakah point ada di area tengah atau tidak. menghasilkan nilai boolean
    inMiddle = (abs(point[0]-midOfAxis)<=maxDist)
    return inMiddle

def divideAndConquer(listOfPoint):
    # Algoritma divide and conquer
    global divideAndConquerCalculationCount
    closestPoint = []
    if len(listOfPoint)==1:                                                         # Jika dalam list hanya ada 1 titik, jaraknya di set
        return DEFINE_MAX_DISTANCE, closestPoint                                    # dengan nilai infinity
    if len(listOfPoint)==2:
        divideAndConquerCalculationCount += 1                                       # Jika ada 2 titik, dihitung dan
        closestPoint += listOfPoint                                                 # dikembalikan jaraknya. titik yang dihitung selalu
        return calculateDistance(listOfPoint[0], listOfPoint[1]), closestPoint      # dicatat untuk pengerjaan bonus visualisasi
    else:
        # Jika lebih dari 2, maka akan dibagi menjadi bagian pertama dan kedua
        firstSection = listOfPoint[:len(listOfPoint)//2]
        secondSection = listOfPoint[len(listOfPoint)//2:]

        # Catat posisi tengah 
        midOfAxis = ((listOfPoint[(len(listOfPoint)//2)-1][0] - listOfPoint[(len(listOfPoint)//2)][0]) / 2) + listOfPoint[(len(listOfPoint)//2)-1][0]

        # Hitung jarak terdekat di bagian pertama dan kedua dengan algoritma divide and conquer
        smallestDistanceFirstSection, closestPointFirstSection = divideAndConquer(firstSection)
        smallestDistanceSecondSection, closestPointSecondSection = divideAndConquer(secondSection)
        
        # Ambil jarak terkecil antara titik di bagian pertama dan kedua sebagai smallest distance, catat titiknya
        smallestDistance = min(smallestDistanceFirstSection, smallestDistanceSecondSection)
        closestPoint = closestPointFirstSection if (smallestDistance == smallestDistanceFirstSection) else closestPointSecondSection
        
        # Untuk titik yang terletak di bagian berbeda akan dicek apakah ada di area tengah atau tidak
        for firstPoint in firstSection :
            if inMiddleArea(firstPoint, midOfAxis, smallestDistance):
                # Jika titik pertama ada di area tengah, akan lanjut memeriksa titik kedua. jika tidak akan lanjut ke
                # titik berikutnya
                for secondPoint in secondSection :
                    if inMiddleArea(secondPoint, midOfAxis, smallestDistance):
                        # Jika titik kedua ada di area tengah juga, maka akan dihitung jarak titik pertama dan kedua
                        # dan dipilih jarak yang lebih dekat. catat titik terdekat jika ada perubahan
                        distance = calculateDistance(firstPoint, secondPoint)
                        divideAndConquerCalculationCount += 1
                        smallestDistance = min(distance, smallestDistance)
                        closestPoint = closestPoint if (smallestDistance!=distance) else [firstPoint, secondPoint]
                    else:
                        # Titik sudah terurut, jika titik kedua urutan i sudah tidak masuk area tengah, titik selanjutnya
                        # sudah pasti tidak masuk area tengah. di lakukan perintah break untuk optimasi
                        break
        return smallestDistance, closestPoint
        
def bruteForce(listOfPoint):
    # Algoritma brute force untuk perbandingan. hanya dicari jaraknya saja
    global burteForceCalculationCount
    smallestDistance = DEFINE_MAX_DISTANCE

    # Pasangkan semua titik ke titik lainnya
    for firstPoint in listOfPoint:
        for secondPoint in listOfPoint:
            # Titik tidak boleh dipasangkan dengan dirinya sendiri.
            if firstPoint != secondPoint : 
                # Hitung jarak, cari yang terkecil
                smallestDistance = min(smallestDistance, calculateDistance(firstPoint, secondPoint))
                burteForceCalculationCount += 1
    return smallestDistance