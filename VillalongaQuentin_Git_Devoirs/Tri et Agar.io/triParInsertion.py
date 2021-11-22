
def triParInsertion(L):
        Ltriee = [L.pop(0)]
        while(len(L) > 0):
            index = -1
            for i in range(len(Ltriee)):
                if (L[0] > Ltriee[i]):
                    index = i 
            Ltriee.insert(index + 1, L.pop(0))
        return(Ltriee)


print(triParInsertion([0, 4, 3, 1, 6, 8, 3, 2, -4]))

