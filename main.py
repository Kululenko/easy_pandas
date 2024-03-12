import csv


#with open("weather_data.csv") as data:
#    for lines in data.readlines():
#        print(lines)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        temperatures.append(row[1])

    print(temperatures[1:])