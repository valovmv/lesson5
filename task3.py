with open('test_3.txt', 'r') as file_obj:
    employees = file_obj.readlines()

    summ_salary = 0

    for employee in employees:
        name, salary = employee.split()

        summ_salary += int(salary)

        if int(salary) < 20000:
            print(name)

print('Средняя зарплата: ', round(summ_salary / len(employees), 2))
