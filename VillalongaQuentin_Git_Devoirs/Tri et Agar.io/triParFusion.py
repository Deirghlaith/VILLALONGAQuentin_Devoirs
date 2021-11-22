import time

def triParFusion(L):
    if(len(L) == 0 or len(L) == 1):
        return(L)
    else:
        L0 = triParFusion(L[:len(L)//2])
        L1 = triParFusion(L[len(L)//2:])
        Lfinal = []
        while(len(L0) > 0 or len(L1) > 0):
            if(len(L0) == 0):
                Lfinal.append(L1.pop(0))
            elif(len(L1) == 0):
                Lfinal.append(L0.pop(0))
            
            elif(L0[0] > L1[0]):
                Lfinal.append(L1.pop(0))
            else:
                Lfinal.append(L0.pop(0))
        return(Lfinal)


print(triParFusion([0, 4, 3, 1, 6, 8, 3, 2, -4]))