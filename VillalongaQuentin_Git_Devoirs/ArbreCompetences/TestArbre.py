import ArbreCompetences_QV as acqv

arbre1 = acqv.Arbre("Test", 5, acqv.Arbre("TestChildGauche", 3, acqv.Arbre("TestChildGauche2", 6)), acqv.Arbre("TestChildDroite", 4))
arbre1.display()
print(acqv.Arbre.treeCounter)
