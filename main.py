import numpy as np
import time

while True:
    print('Input number or press enter.')
    count = ''
    count = input()
    if count == '':
        count = 5
    for i in range(int(count)):
        a = np.array([1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,20,
             21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39,40,
             41,42,43])
        num_list = np.random.choice(a, 6, replace=False)
        print(sorted(num_list))

    #time.sleep(3600)
