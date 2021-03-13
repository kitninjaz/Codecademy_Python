import csv

DictReadInsuranceData = {}
insuranceData = []
with open('insurance.csv') as insurancefile:
    DictReadInsuranceData = csv.DictReader(insurancefile, delimiter=",")

    for row in DictReadInsuranceData:
        insuranceData.append(row)
   
print(insuranceData[0])

#Find out the average age of the patients in the dataset.
def averageAge(peepData):
    peepCount = 0
    ageSum = 0
    for peep in peepData:
        ageSum += float(peep["age"])
        peepCount += 1
    print("The average age of the {totalCount} patients is {averageAge}".format(averageAge=ageSum/peepCount, totalCount=peepCount))

def averageAgeBySex(peepData):
    females = {"count": 0, "ageSum": 0}
    males = {"count": 0, "ageSum": 0}

averageAge(insuranceData)



#Analyze where a majority of the individuals are from.

#Look at the different costs between smokers vs. non-smokers.

#Figure out what the average age is for someone who has at least one child in this dataset.