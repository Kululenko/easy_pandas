import csv
import pandas




with open("100days\\25days\\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        temperatures.append(row[1])
    temperatures_int = [] 
    for number in temperatures[1:]:
        temperatures_int.append(int(number))

    print(temperatures_int)



