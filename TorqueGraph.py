import matplotlib.pyplot as plt

f = input("Enter file name: ")
if f.endswith(".txt"):
	inputFile = open(f)
else:
	inputFile = open(f + ".txt")

header = inputFile.readline()  # first line

print(header)


class LogEntry:

	def __init__(self, time):
		self.time = time
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


def getValues(file):
	vLine = file.readline()

	valueList = vLine.split(',')

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

for line in inputFile:
	dataLine = getValues(inputFile)
	dataList.append(dataLine)


print(stripTime(dataList[1].time))

timeList = []
rpmList = []
timing = []
engLoad = []
for data in dataList:
	timeList.append(stripTime(data.time))
	rpmList.append(data.RPM)
	t = float(data.timingAdv)
	timing.append(t)
	e = float(data.engineLoad)
	engLoad.append(e)

plt.figure(1)
#fig.add_subplot(211)

rpmPlot = plt.subplot(212)
rpmPlot.plot(timeList,rpmList)

loadPlot = plt.subplot(211)
loadPlot.plot(timeList,timing)

loadPlot.plot(timeList, engLoad)
loadPlot.set_ylim(5,50)

rpmPlot.set_xlim(int(stripTime(dataList[0].time)),int(stripTime(dataList[(len(dataList)-1)].time)))
rpmPlot.set_ylabel("RPM")
rpmPlot.set_ylim(0,6000)

plt.title("RPM and Timing Advance")

plt.show()