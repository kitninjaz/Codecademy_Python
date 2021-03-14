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
    return {'count': peepCount, 'ageSum': ageSum}
    

def averageAgeBySex(peepData):
    female = {'count': 0, 'ageSum': 0}
    male = {'count': 0, 'ageSum': 0}
    unknown = {'count': 0, 'ageSum': 0}
    for peep in peepData:
        if peep['sex'] == 'female':
            female['count'] += 1
            female['ageSum'] += float(peep['age'])
        elif peep['sex'] == 'male':
            male['count'] += 1
            male['ageSum'] += float(peep['age'])
        else:
            unknown['count'] += 1
            unknown['ageSum'] += float(peep['age'])
    print("The dataset contains {count} females, with an average age of {averageAge}".format(count = female['count'], averageAge = female['ageSum']/female['count']))
    print("The dataset contains {count} males, with an average age of {averageAge}".format(count = male['count'], averageAge = male['ageSum']/male['count']))
    if unknown['count'] == 0:
        print("Luckily the data is complete and each patient in the dataset has been assigned a sex!")
    elif unknown['count'] == 1:
        print("There is 1 patient with an unknown sex or a non female/male sex, their age is {ageSum}".format(ageSum = unknown['ageSum']))
    else:
        print("There are {count} patients with an unknown sex or a non female/male sex, with an average age of {averageAge}".format(count = unknown['count'], averageAge = unknown['ageSum']/unknown['count']))

averageAgeData = averageAge(insuranceData)
print("The average age of the {totalCount} patients is {averageAge}".format(averageAge=averageAgeData['ageSum']/averageAgeData['count'], totalCount=averageAgeData['count']))

averageAgeBySex(insuranceData)
print("")



#Analyze where a majority of the individuals are from.
def regionAnalysis(peepData):
    regions = {}
    for peep in peepData:
        region = peep['region']
        if regions.get(region,'nope') == 'nope':
            regions[region] = 0
        else:
            regions[region] += 1
    print("Breakdown by region - ")
    for region, count in regions.items():
        print("***{region}: {regionCount} """.format(regionCount = count, region = region))

regionAnalysis(insuranceData)
print("")

#Look at the different costs between smokers vs. non-smokers.
def smokerStatus(peepData,smokingStatus):
    peepSubset = []
    for peep in peepData:
        if peep['smoker'] == smokingStatus:
            peepSubset.append(peep)
    return peepSubset

def costAnalysis(peepData):
    initial = peepData[0]
    costRange = {'min': float(initial['charges']), 'max': float(initial['charges']), 'sum': 0, 'count': 0}
    for peep in peepData:
        insCost = float(peep['charges'])
        if insCost < costRange['min']:
            costRange['min'] = insCost
        if insCost > costRange['max']:
            costRange['max'] = insCost
        costRange['sum'] += insCost
        costRange['count'] += 1
    return costRange

smokerCosts = costAnalysis(smokerStatus(insuranceData,'yes'))
nonsmokerCosts = costAnalysis(smokerStatus(insuranceData,'no'))


print("""Insurance Cost breakdown for smokers - 
***Min: {min}
***Max: {max}
***Average: {average}
""".format(min = smokerCosts['min'], max = smokerCosts['max'], average = smokerCosts['sum']/smokerCosts['count']))

print("""Insurance Cost breakdown for nonsmokers - 
***Min: {min}
***Max: {max}
***Average: {average}
""".format(min = nonsmokerCosts['min'], max = nonsmokerCosts['max'], average = nonsmokerCosts['sum']/nonsmokerCosts['count']))

averageDifference =  (smokerCosts['sum']/smokerCosts['count']) - (nonsmokerCosts['sum']/nonsmokerCosts['count'])
print("On average the insurance cost for a smoker is {difference} more than for a nonsmoker".format(difference = averageDifference))
print("")

#Figure out what the average age is for someone who has at least one child in this dataset.
def numOfChildren(peepData,children):
    peepSubset = []
    for peep in peepData:
        if int(peep['children']) >= children:
            peepSubset.append(peep)
    return peepSubset

oneChildAverageAgeData = averageAge(numOfChildren(insuranceData,1))
oneChildAverageAge = oneChildAverageAgeData['ageSum']/oneChildAverageAgeData['count']
print("The average age for someone who has at least one child in this dataset is {averageage}".format(averageage = oneChildAverageAge))