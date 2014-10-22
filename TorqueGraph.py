import matplotlib.pyplot as plt

#f = raw_input("Enter file name: ")
inputFile = open("torqueTrackLog1.txt")

header = inputFile.readline() #first line

print(header)
        
    
class LogEntry:

    def __init__(self, Time):
        self.time = Time
    time = ""    
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
    line = file.readline()

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

def stripTime(time):
	stripped = time[(time.find(':')-2):-4]
	
	stripped = stripped.replace(":","")
    
	return stripped

dataList = []

for entry in inputFile.readline():
    dataLine = getValues(inputFile, entry)
    dataList.append(dataLine)
    

print(stripTime(dataList[1].time))

x = []
y = []
for data in dataList:
	#plt.plot([stripTime(data.time)],[data.RPM])
        x.append(stripTime(data.time))
        y.append(data.RPM)

plt.plot(x,y)
plt.xlim(int(stripTime(dataList[0].time)),int(stripTime(dataList[(len(dataList)-1)].time)))
plt.ylabel("RPM")
plt.ylim(0,5500)

#plt.draw()
plt.show()
