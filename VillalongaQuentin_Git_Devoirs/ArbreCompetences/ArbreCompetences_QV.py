

class Arbre():

    nodeCounter = 0
    treeCounter = 0

    def __init__(self, skillName, skillPoint, leftChild = None, rightChild = None):
        self.__skillName = skillName
        self.__skillPoint = skillPoint
        self.__leftChild = leftChild
        self.__rightChild = rightChild
        Arbre.treeCounter += 1
        if (leftChild != None or rightChild != None):
            Arbre.nodeCounter += 1
        
    
    def setName(self, skillName):
        self.__skillName = skillName
    
    def getName(self):
        return self.__skillName
    
    def setSkillPoint(self, skillPoint):
        self.__skillPoint = skillPoint
    
    def getSkillPoint(self):
        return self.__skillPoint
    
    def setRightChild(self, rightChild):
        if (self.getRightChild() == None and self.getLeftChild() == None):
            Arbre.nodeCounter += 1
        self.__rightChild = rightChild
    
    def getRightChild(self):
        return self.__rightChild
    
    def setLeftChild(self, leftChild):
        if (self.getRightChild() == None and self.getLeftChild() == None):
            Arbre.nodeCounter += 1
        self.__leftChild = leftChild
    
    def getLeftChild(self):
        return self.__leftChild
    
    def levelUpSkill(self):
        self.__skillPoint += 1
    
    def reset(self):
        self.__skillPoint = 0
        if (self.getLeftChild() != None or self.getRightChild() != None):
            Arbre.nodeCounter -= 1
            if (self.getLeftChild() != None):
                self.getLeftChild().reset()
            if (self.getRightChild() != None):
                self.getRightChild().reset()

    def getDepth(self):
        if (self.getLeftChild() == None and self.getRightChild() == None):
            return 0
        elif (self.getLeftChild() == None):
            return 1 + self.getRightChild().getDepth()
        elif (self.getRightChild() == None):
            return 1 + self.getLeftChild().getDepth()
        else:
            return 1 + max(self.getLeftChild().getDepth(), self.getRightChild().getDepth())

    def display(self, command = 1):
        if (command == 1):
            print(self.getName(), self.getSkillPoint(), "p ")
        if (self.getLeftChild() == None and self.getRightChild() == None):
            pass
        elif (self.getRightChild() == None):
            self.getLeftChild().display()
        elif (self.getLeftChild() == None):
            self.getRightChild().display()
        else:
            print(self.getLeftChild().getName(), self.getLeftChild().getSkillPoint(), "p", self.getRightChild().getName(), self.getRightChild().getSkillPoint(), "p")
            self.getLeftChild().display(0)
            self.getRightChild().display(0)



arbre1 = Arbre("Test", 5, Arbre("TestChildGauche", 3, Arbre("TestChildGauche2", 6)), Arbre("TestChildDroite", 4))
print(arbre1.getDepth())
arbre1.display()
