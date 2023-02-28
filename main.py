import function as fun
import time
import matplotlib.pyplot as plt

dimension = int(input("Masukkan dimensi : "))
numOfPoint = int(input("Masukkan banyak titik : "))
maxCoordinate = int(input("Masukkan limit koordinat (Contoh : jika memasukkan 10, maka titik akan berada\npada rentang -10 sampai 10 di setiap sumbu, dengan 2 digit desimal.)  : "))

start_time_DNC = time.time()

listOfPoint = fun.createListOfPoint(dimension, numOfPoint, maxCoordinate)
smallestDistanceDivideAndConquer, closestPoint = fun.divideAndConquer(listOfPoint)

end_time_DNC = time.time()
total_time_DNC = (end_time_DNC - start_time_DNC) * 1000

start_time_BF = time.time()

smallestDistanceBruteForce = fun.bruteForce(listOfPoint)

end_time_BF = time.time()
total_time_BF = (end_time_BF - start_time_BF) * 1000

print(f"\nsmallest distance with divide and conquer : {smallestDistanceDivideAndConquer:.2f}. Number of calculation = {fun.divideAndConquerCalculationCount}.")
print(f"Total runtime for Divide and Conquer : {total_time_DNC} ms.\n")
print(f"smallest distance with brute force : {smallestDistanceBruteForce:.2f}. Number of calculation = {fun.burteForceCalculationCount}.")
print(f"Total runtime for Brute Force : {total_time_BF} ms.")
if dimension==3:
    fig = plt.figure(figsize=(maxCoordinate, maxCoordinate))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xbound(lower=-maxCoordinate, upper=maxCoordinate)
    ax.set_ybound(lower=-maxCoordinate, upper=maxCoordinate)
    ax.set_zbound(lower=-maxCoordinate, upper=maxCoordinate)
    for point in listOfPoint:
        if point in closestPoint:
            ax.scatter(*point, c="red")
        else:
            ax.scatter(*point, c="blue")

    plt.show()
