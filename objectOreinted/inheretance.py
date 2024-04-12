class parentBird:
    def __ini__(self):
        print("Bird has other children")
    def parentDisplay(): 
        print("bird can display her fly")

class childBird(parentBird):
    def __init__(self):
        super().__init__()
        print("i am the child of bird class")
    def childDisplay(self):
        print("child bird can display her fly")
            
child=childBird()    
child.childDisplay()           
child.parentDisplay()