import numpy as np
import matplotlib.pyplot as plt
import math

def file_read_1(filename, T, D):
    f = open(filename)
    line_count = 0
    for line in f:
        comma_count = 0
        i = 0
        j = 0
        if(line_count != 0):  
            print("b")
            while(i < len(line)):
                print("c")
                if (line[i] == ","):
                    comma_count += 1
                    val = line[j:i]
                    if(comma_count == 1):
                        time = float(val)
                    elif(val != ""):
                        T[comma_count-2].append(time)
                        D[comma_count-2].append(int(val))
                    j = i+1
                i+=1
            val = line[j:i]
            if((val != "\n") and (val != "")):
                T[comma_count-1].append(time)
                D[comma_count-1].append(int(val))
        else:
            print("a")
            while(i < len(line)):
                if (line[i] == ","):
                    T.append([])
                    D.append([])
                i += 1
        line_count+=1

if __name__ == "__main__":
    T = []
    D = []
    file_read_1("help2.csv", T, D)
    for i in range(len(T)):
        aT = np.array(T[i])
        aD = np.array(D[i])
        plt.plot(aT, aD)
        plt.show()
        print(T[i])
        print(D[i])