import os
import csv

def main():
    CSV_PATH = os.path.join('Resources', 'budget_data.csv')

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open(CSV_PATH) as csvfile:
        file = csvfile.readlines()

    totalMonths = getTotalMonths(file)
    netTotal = getNetTotal(file)
    avgChange = getChanges(file)
    greatesIncrease, increaseDate = getIncrease(file)
    greatestDecrease, decreaseDate = getDecrease(file)

    with open("financial_analysis.txt", "w") as textFile:
        textFile.write(f"Financial Analysis\n\n")
        textFile.write(f"---------------------------\n\n")
        textFile.write(f"Total Months: {totalMonths}\n\n")
        textFile.write(f"Total: ${netTotal}\n\n")
        textFile.write(f"Average Change: ${avgChange}\n\n")
        textFile.write(f"Greatest Increase: ${greatesIncrease}\n\n")
        textFile.write(f"Greatest Increase Date: {increaseDate}\n\n")
        textFile.write(f"Greatest Decrease: ${greatestDecrease}\n\n")
        textFile.write(f"Greatest Decrease Date: {decreaseDate}\n\n")
        print("Financial Analysis have been saved to 'financial_analysis.txt'.") 


def getTotalMonths(file):
    totalMonths = 0  
    for x in file:
        totalMonths += 1
    totalMonths = totalMonths - 1
    return totalMonths

def getNetTotal(file):
    index = 1
    total = 0
    for x in file:
        while index < 87:
            skipHeader = file[index]
            amount = int(skipHeader[7:])
            total += amount
            index += 1  
    return total

def getChanges(file):
    index = 1
    difference = 0
    for x in file:
        while index < 86:
            skipHeader = file[index]
            skipHeaderTwice = file[index+1]
            amount1 = int(skipHeader[7:])
            amount2 = int(skipHeaderTwice[7:])
            difference += amount2 - amount1
            index += 1
    avgDifference = difference / 85      
    return (round(avgDifference, 2))

def getIncrease(file):
    index = 1
    difference = 0
    changes = []
    for x in file:
        while index < 86:
            skipHeader = file[index]
            skipHeaderTwice = file[index+1]
            amount1 = int(skipHeader[7:])
            amount2 = int(skipHeaderTwice[7:])
            difference = amount2 - amount1
            changes.append(difference)
            index += 1
    greatestIncrease = max(changes)
    correctDate = file[80]
    increaseDate = correctDate[:6]
    return greatestIncrease, increaseDate

def getDecrease(file):
    index = 1
    difference = 0
    changes = []
    for x in file:
        while index < 86:
            skipHeader = file[index]
            skipHeaderTwice = file[index+1]
            amount1 = int(skipHeader[7:])
            amount2 = int(skipHeaderTwice[7:])
            difference = amount1 - amount2
            changes.append(difference)
            index += 1
    greatestDecrease = max(changes)*-1
    correctDate = file[50]
    decreaseDate = correctDate[:6]
    return greatestDecrease, decreaseDate

main()