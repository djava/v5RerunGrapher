dataPath = input("Path to voltage data: ")

from matplotlib import pyplot as plt

dataFiles = []
for i in ["/voltageData.txt", "/currentData.txt", "/powerData.txt",  "/velocityData.txt", "/positionData.txt"]:
    dataFiles.append(open(dataPath + i))

print("0 - Back Left\n1 - Front Left\n2 - Back Right\n3 - Front Right\n4 - Tray\n5 - Lift\n6 - Left Intake\n7 - Right Intake")
mtr = int(input('Which motor? '))

mtrDict = {0: "Back Left", 1: "Front Left", 2: "Back Right", 3: "Front Right", 4: "Tray", 5: "Lift", 6: "Left Intake", 7: "Right Intake"}

dataFileLines = [i.read().splitlines() for i in dataFiles]
dataNums = [[x.split(' ') for x in i] for i in dataFileLines]
dataByMotor = [[[int(x[k]) for x in j] for k in range(8)] for j in dataNums]
for i in range(4):
    dataFiles[i].close()
del dataFileLines, dataNums

fig, axes = plt.subplots(5, 1, True, figsize=(15, 9))
plt.subplots_adjust(bottom=0.05, top=0.95, left=0.1, right=0.925, hspace=0.30)

timeRange = list(range(0, len(dataByMotor[0][0])*20, 20))


for i in [0, 1, 3, 4]:
    axes[i].plot(timeRange, dataByMotor[i][mtr], label=mtrDict[mtr])

axes[2].plot(timeRange, [dataByMotor[0][mtr][j]*dataByMotor[1][mtr][j] for j in range(len(dataByMotor[0][0]))])

axes[0].set_title("Voltage (mV)")
axes[1].set_title("Current (mA)")
axes[2].set_title("Power (W)")
axes[3].set_title("Velocity (m/s)")
axes[4].set_title("Position (Ticks)")
axes[0].set_yticks(range(-12000, 12001, 4000))
axes[1].set_yticks(range(0, 3000, 300))
axes[4].legend(loc="upper left")

plt.show()