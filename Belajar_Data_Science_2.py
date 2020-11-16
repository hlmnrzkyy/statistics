import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.io.parsers.read_csv("Effects-of-COVID-19-on-trade-1-February-28-October-2020-provisional.csv")
dataArray = np.asarray(data)

x = [2015, 2016, 2017, 2018, 2019, 2020]

# Year - Value (Dollars)

dataE2015 = []
dataE2016 = []
dataE2017 = []
dataE2018 = []
dataE2019 = []
dataE2020 = []

dataI2015 = []
dataI2016 = []
dataI2017 = []
dataI2018 = []
dataI2019 = []
dataI2020 = []

dataR2015 = []
dataR2016 = []
dataR2017 = []
dataR2018 = []
dataR2019 = []
dataR2020 = []


for i in range(1, len(dataArray[:, 0])):

    if dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataE2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataE2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataE2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataE2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataE2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataE2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataI2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataI2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataI2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataI2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataI2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataI2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataR2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataR2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataR2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataR2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataR2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataR2020.append(dataArray[i, 10])

    else:
        print("Data Error")

y1 = [sum(dataE2015),
     sum(dataE2016),
     sum(dataE2017),
     sum(dataE2018),
     sum(dataE2019),
     sum(dataE2020)]

y2 = [sum(dataI2015),
     sum(dataI2016),
     sum(dataI2017),
     sum(dataI2018),
     sum(dataI2019),
     sum(dataI2020)]

y3 = [sum(dataR2015),
     sum(dataR2016),
     sum(dataR2017),
     sum(dataR2018),
     sum(dataR2019),
     sum(dataR2020)]

plt.figure(1)
plt.plot(x, y1, ".r")
plt.plot(x, y2, ".g")
# plt.plot(x, y3, ".b")

plt.legend(["Exports", "Imports"]) # , "Reimports"])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.grid
plt.ylabel('Value (Dollar)')
plt.title('Effects of Covid-19 on Trade \n 1 Februari to 28 Oktober \n')

# Year - Value (Tonnes)

dataE2015 = []
dataE2016 = []
dataE2017 = []
dataE2018 = []
dataE2019 = []
dataE2020 = []

dataI2015 = []
dataI2016 = []
dataI2017 = []
dataI2018 = []
dataI2019 = []
dataI2020 = []

dataR2015 = []
dataR2016 = []
dataR2017 = []
dataR2018 = []
dataR2019 = []
dataR2020 = []


for i in range(1, len(dataArray[:, 0])):

    if dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2015 and dataArray[i, 8] == "Tonnes":
        dataE2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2016 and dataArray[i, 8] == "Tonnes":
        dataE2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2017 and dataArray[i, 8] == "Tonnes":
        dataE2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2018 and dataArray[i, 8] == "Tonnes":
        dataE2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2019 and dataArray[i, 8] == "Tonnes":
        dataE2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2020 and dataArray[i, 8] == "Tonnes":
        dataE2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2015 and dataArray[i, 8] == "Tonnes":
        dataI2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2016 and dataArray[i, 8] == "Tonnes":
        dataI2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2017 and dataArray[i, 8] == "Tonnes":
        dataI2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2018 and dataArray[i, 8] == "Tonnes":
        dataI2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2019 and dataArray[i, 8] == "Tonnes":
        dataI2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2020 and dataArray[i, 8] == "Tonnes":
        dataI2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2015 and dataArray[i, 8] == "Tonnes":
        dataR2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2016 and dataArray[i, 8] == "Tonnes":
        dataR2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2017 and dataArray[i, 8] == "Tonnes":
        dataR2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2018 and dataArray[i, 8] == "Tonnes":
        dataR2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2019 and dataArray[i, 8] == "Tonnes":
        dataR2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2020 and dataArray[i, 8] == "Tonnes":
        dataR2020.append(dataArray[i, 10])

    else:
        print("Data Error")

y1 = [sum(dataE2015),
     sum(dataE2016),
     sum(dataE2017),
     sum(dataE2018),
     sum(dataE2019),
     sum(dataE2020)]

y2 = [sum(dataI2015),
     sum(dataI2016),
     sum(dataI2017),
     sum(dataI2018),
     sum(dataI2019),
     sum(dataI2020)]

y3 = [sum(dataR2015),
     sum(dataR2016),
     sum(dataR2017),
     sum(dataR2018),
     sum(dataR2019),
     sum(dataR2020)]

plt.figure(2)
plt.plot(x, y1, ".r")
# plt.plot(x, y2, ".g")
# plt.plot(x, y3, ".b")

plt.legend(["Exports"]) # , "Imports"]) # , "Reimports"])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.grid
plt.ylabel('Value (Tonnes)')
plt.title('Effects of Covid-19 on Trade \n 1 Februari to 28 Oktober \n')

# Reimports

dataE2015 = []
dataE2016 = []
dataE2017 = []
dataE2018 = []
dataE2019 = []
dataE2020 = []

dataI2015 = []
dataI2016 = []
dataI2017 = []
dataI2018 = []
dataI2019 = []
dataI2020 = []

dataR2015 = []
dataR2016 = []
dataR2017 = []
dataR2018 = []
dataR2019 = []
dataR2020 = []


for i in range(1, len(dataArray[:, 0])):

    if dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataE2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataE2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataE2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataE2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataE2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Exports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataE2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataI2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataI2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataI2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataI2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataI2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Imports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataI2020.append(dataArray[i, 10])

    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2015 and dataArray[i, 8] != "Tonnes":
        dataR2015.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2016 and dataArray[i, 8] != "Tonnes":
        dataR2016.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2017 and dataArray[i, 8] != "Tonnes":
        dataR2017.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2018 and dataArray[i, 8] != "Tonnes":
        dataR2018.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2019 and dataArray[i, 8] != "Tonnes":
        dataR2019.append(dataArray[i, 10])
    elif dataArray[i, 0] == "Reimports" and dataArray[i, 1] == 2020 and dataArray[i, 8] != "Tonnes":
        dataR2020.append(dataArray[i, 10])

    else:
        print("Data Error")

y1 = [sum(dataE2015),
     sum(dataE2016),
     sum(dataE2017),
     sum(dataE2018),
     sum(dataE2019),
     sum(dataE2020)]

y2 = [sum(dataI2015),
     sum(dataI2016),
     sum(dataI2017),
     sum(dataI2018),
     sum(dataI2019),
     sum(dataI2020)]

y3 = [sum(dataR2015),
     sum(dataR2016),
     sum(dataR2017),
     sum(dataR2018),
     sum(dataR2019),
     sum(dataR2020)]

plt.figure(3)
# plt.plot(x, y1, ".r")
# plt.plot(x, y2, ".g")
plt.plot(x, y3, ".b")

plt.legend(["Reimports"])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.grid
plt.ylabel('Value (Dollar)')
plt.title('Effects of Covid-19 on Trade \n 1 Februari to 28 Oktober \n')

plt.show()