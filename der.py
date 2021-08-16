class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedlimit={}
    
    def start(self,add,noe):
        self.speedlimit[add]=noe
        print(self.speedlimit)
    
    def stop(self):
        print("stop")

    def accelerate(self):
        print("accelerating")
        "accelerator functionality here"
    
    def changegear(self,geartype):
        print("gearchanged")
        "gear related functionality here"

audi=Car("a6","red","audi",{"ab":100})
print(audi.start(1,99))
