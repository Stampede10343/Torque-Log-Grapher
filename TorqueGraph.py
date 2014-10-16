
#f = raw_input("Enter file name: ")
inputFile = open("torquetracklog1.txt")

header = inputFile.next() #first line

print(header)
        
    
class LogEntry:

    def __init__(self, Time):
        self.time = Time
        
    Gx = 0.0
    Gy = 0.0
    Gz = 0.0
    engineLoad = 0.0
    coolantTemp = 0
    intakePressure = 0
    RPM = 0
    timingAdv = 0
    intakeTemp = 0
    fuelTrim = 0.0


def getValues(file, logEntry):
    line = file.next()

    valueList = line.split(',')

    #print(valueList)
    entry = LogEntry(valueList[1])

    entry.Gx = valueList[8]
    entry.Gy = valueList[9]
    entry.Gz = valueList[10]
    entry.engineLoad = valueList[12]
    entry.coolantTemp = valueList[13]
    entry.intakePressure = valueList[14]
    entry.RPM = valueList[15]
    entry.timingAdv = valueList[17]
    entry.intakeTemp = valueList[18]
    entry.fuelTrim = valueList[19]

    return entry

dataList = []

for entry in inputFile.next():
    dataLine = getValues(inputFile, entry)
    dataList.append(dataLine)
    

