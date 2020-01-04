import random

def long_process(id, n):
    #Ф-ция суммирования n чисел. Возвращает сумму, промежуточный результат суммы равен None-то что вернет данная функция
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum, x, n)
        if x < n-1:
            #print(sum)
            yield
        else:
            yield sum


def create_input_data(n):
    #Ф-ция создает массив с n случайных чисел
    output=[]
    for _ in range(n):
        output.append(random.randint(2,10))
    return output

def create_generators(input_data):
    #Функция получает на вход массив состоящий из данных типа int, запускает N процессов long_process, где N кол-во данных в input_data
    R={}
    for i in range(len(input_data)):
        full_process_name = "ID" +"_" + str(i)
        R[full_process_name] = long_process(full_process_name, input_data[i])
    return R

def working_generators(input_generators):
    #Ф-ция запускает генераторы и возвращает сумму всех отработавших генераторов.
    sum = 0
    names={}
    for key in input_generators:
        names[key] = None
    while True == True :
        if len(input_generators) == 0:
            print(sum)
            break
        for key in input_generators:
            if names[key] is None : 
                names[key] = next(input_generators[key]) 
            else:
                print(names[key]) 
                sum += names[key]
                del names[key]
                del input_generators[key]
                break
    return sum

working_generators(create_generators(create_input_data(7)))

