
def triParInsertion(L):
        # On initialise Ltriee
        Ltriee = [L.pop(0)]
        while(len(L) > 0):
            index = -1
            # On cherche index, la position du dernier élément de Ltriee plus petit que L[0]
            for i in range(len(Ltriee)):
                if (L[0] > Ltriee[i]):
                    index = i
            # On insère l'élément L[0] dans Ltriee à la position suivant index. Si l'élément est plus petit que tous les éléments de la liste, on l'ajoute à la position 0
            Ltriee.insert(index + 1, L.pop(0))
        return(Ltriee)


print(triParInsertion([0, 4, 3, 1, 6, 8, 3, 2, -4]))

