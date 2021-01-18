import csv
path = "E:\Python\WHJR_PYTHON\cl104\HeightWeight.csv"
with open(path, newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
# Calculating the mean
n = len(new_data)
total = 0
for item in new_data:
    total += item
mean = total / n
print(str(mean))