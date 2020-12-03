subjects = {}

try:
    with open('test_6.txt', 'r') as file_obj:
        for line in file_obj.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
except IOError as e:
    print(e)
except ValueError:
    print("Неверные данные")

print(subjects)
