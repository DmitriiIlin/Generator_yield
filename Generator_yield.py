import random

def long_process(id, n):
    #Ф-ция суммирования n чисел. Возвращает сумму, промежуточный результат суммы равен None-то что вернет данная функция
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum, x, n)
        if x < n-1:
            #print(sum)
            yield None
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
    while True == True :
        if len(input_generators) == 0:
            print(sum)
            break
        for generator in input_generators:
            value=next(input_generators[generator]) 
            if value == None:
                print(value)
                pass
            else: 
                print(value)
                sum += value
                del input_generators[generator]
                break
    return sum

working_generators(create_generators(create_input_data(10)))

