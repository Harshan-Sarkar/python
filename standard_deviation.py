import csv
import math
path = "E:\Python\WHJR_PYTHON\cl105\standard_deviation_test_file.csv"
with open(path, newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = []
for item in file_data:
    for number in item:
        data.append(int(number))
print(data)
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total / n
    return mean
squaredlist = []
for num in data:
    a = int(num) - mean(data)
    a = a ** 2
    squaredlist.append(a)
sumsd = 0
for i in squaredlist:
    sumsd = sumsd + i
print(len(data))
result = float(sumsd) / (len(data) - 1)
std_deviation = math.sqrt(result)
print(std_deviation)