import time 
start_time = time.time()

for i in range(2):
    #ineer loop 
    for j in range(200):
        print(0, end=" ")
    print()

print(round((time.time() - start_time), 2))