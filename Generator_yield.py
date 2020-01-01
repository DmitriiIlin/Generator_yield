import random

def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum, x)
        if x < n-1:
            print(sum)
            yield
        else:
            yield sum



def a_lot_of_long_processes(q_ty_of_process):
    #Создается кол-во процессов long_process равное q_ty_of_process
    n = 0
    q_ty = 0
    input_parametr=[]
    massive_for_processes={}
    R={}
    while q_ty <= q_ty_of_process :
        input_parametr.append(random.randint(q_ty_of_process,q_ty_of_process+10))
        full_process_name = "ID" +"_" + str(n)
        massive_for_processes[full_process_name] = None
        R[full_process_name] = long_process(full_process_name,input_parametr[n])
        for key in R:
            print(R.keys())
            print(R[key])
            if massive_for_processes[key] is None: massive_for_processes[key] = next(R[key])
            else: print("this is Done")
        n += 1
        q_ty += 1
    if q_ty == q_ty_of_process+1:
        max_input = max(input_parametr)
        for i in range(max_input - q_ty_of_process):
            for key in R:
                if massive_for_processes[key] is None: massive_for_processes[key] = next(R[key])
                else: print("this is Done" + " " + str(key))
    print(massive_for_processes)


a_lot_of_long_processes(7)


