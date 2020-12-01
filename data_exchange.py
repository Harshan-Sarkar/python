x = input("Enter your first file name : ")
y = input("Enter your second file name : ")

def Data_exchange(file_name_1, file_name_2):
    one = open(file_name_1, 'r')
    two = open(file_name_2, 'r')
    data1 = one.read()
    data2 = two.read()
    one.close()
    two.close()
    a = open(file_name_1, 'w')
    b = open(file_name_2, 'w')
    a.write(data2)
    b.write(data1)
    a.close()
    b.close()
Data_exchange(x, y)
# 1.txt
# 2.txt