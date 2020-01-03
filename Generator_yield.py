import random

def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum, x, n)
        if x < n-1:
            #print(sum)
            yield
        else:
            yield sum



def a_lot_of_long_processes(q_ty_of_process):
    #Создается кол-во процессов long_process равное q_ty_of_process
    n = 0  
    R={}
    for _ in range(q_ty_of_process):
        full_process_name = "ID" +"_" + str(n)
        R[full_process_name] = long_process(full_process_name,random.randint(q_ty_of_process,q_ty_of_process+10))
        for key in R:
            print(R.keys())
            print(R[key])
        n += 1
    while True == True :
        flag = True
        for key in R:
            try :
                next(R[key])
                flag = False 
            except:
                pass
        if flag == True:
            break
    print(R.keys(), R.values())

a_lot_of_long_processes(7)


