from json import dumps

results = [{}, {}]

with open('test_7.txt') as file_obj:
    lines = file_obj.readlines()

    for line in lines:
        name, stat, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

    results[1]['average_profit'] = round(sum(profit for stat, profit in results[0].items() if profit > 0) / len(results[0]))

with open('test_7.json', 'w') as file_obj_2:
    file_obj_2.write(dumps(results))
