dataPath = input("Path to voltage data: ")

from matplotlib import pyplot as plt

dataFiles = []
for i in ["/voltageData.txt", "/currentData.txt", "/powerData.txt",  "/velocityData.txt", "/positionData.txt"]:
    dataFiles.append(open(dataPath + i))

dataFileLines = [i.read().splitlines() for i in dataFiles]
dataNums = [[x.split(' ') for x in i] for i in dataFileLines]
dataByMotor = [[[int(x[k]) for x in j] for k in range(8)] for j in dataNums]
for i in range(4):
    dataFiles[i].close()
del dataFileLines, dataNums

fig, axes = plt.subplots(5, 1, True, figsize=(15, 9))
plt.subplots_adjust(bottom=0.05, top=0.95, left=0.1, right=0.925, hspace=0.30)

timeRange = list(range(0, len(dataByMotor[0][0])*20, 20))

axes[4].plot(timeRange, dataByMotor[4][0], label="Back Left")
axes[4].plot(timeRange, dataByMotor[4][1], label="Front Left")
axes[4].plot(timeRange, dataByMotor[4][2], label="Back Right")
axes[4].plot(timeRange, dataByMotor[4][3], label="Front Right")
axes[4].plot(timeRange, dataByMotor[4][4], label="Tray")
axes[4].plot(timeRange, dataByMotor[4][5], label="Lift")
axes[4].plot(timeRange, dataByMotor[4][6], label="Left Intake")
axes[4].plot(timeRange, dataByMotor[4][7], label="Right Intakes")

for i in [0, 1, 3]:
    for j in range(8):
        axes[i].plot(timeRange, dataByMotor[i][j])
for i in range(8):
    axes[2].plot(timeRange, [dataByMotor[0][i][j]*dataByMotor[1][i][j] for j in range(len(dataByMotor[0][0]))])

axes[0].set_title("Voltage (mV)")
axes[1].set_title("Current (mA)")
axes[2].set_title("Power (W)")
axes[3].set_title("Velocity (m/s)")
axes[4].set_title("Position (Ticks)")
axes[4].legend(loc="upper left", fontsize="xx-small")
axes[0].set_yticks(range(-12000, 12001, 4000))
axes[1].set_yticks(range(0, 3000, 300))

plt.show()