def personCount():
    file = open('Wodociagi.txt','r')
    line = file.readlines()
    suma = 0
    name = input('Enter district code: ')
    for linia in line:
            district = linia.split(";")[0][7:]
            if (name == district):
                suma = suma + int(linia.split(";")[0][5:7])
    return suma

def monthlyWaterConsumption():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    suma = 0
    name = input('Enter month: ')
    for linia in line[1:]:
        month = linia.split(";")[int(name)]
        if month is not None:
            suma = suma + int(month)
    return suma

def averageAnnual():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    people = 0
    consumption = 0
    name = input('Enter district code: ')
    for linia in line:
        district = linia.split(";")[0][7:]
        if (name == district):
            people = people + int(linia.split(";")[0][5:7])
            for index in range(1,13):
                consumption = consumption + int(linia.split(";")[index])
    return consumption / people

def maxResidents():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    max = 0
    name = input('Enter district code: ')
    for linia in line:
        district = linia.split(";")[0][7:]
        if (name == district):
            number = int(linia.split(";")[0][5:7])
            if (max < number):
                max = number
    return max

def waterConsumptionPerPerson():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    people = 0
    consumption = 0
    for linia in line[1:]:
        people = people + int(linia.split(";")[0][5:7])
        for index in range(1, 13):
            consumption = consumption + int(linia.split(";")[index])
    return consumption / people

def maxWaterConsumption():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for linia in line[1:]:
        month = linia.split(";")
        for index in range(1,13):
            items[index - 1] = items[index - 1] + int(month[index].strip())
    return max(items)

def minWaterConsumption():
    file = open('Wodociagi.txt', 'r')
    line = file.readlines()
    items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for linia in line[1:]:
        month = linia.split(";")
        for index in range(1,13):
            items[index - 1] = items[index - 1] + int(month[index].strip())
    return min(items)
