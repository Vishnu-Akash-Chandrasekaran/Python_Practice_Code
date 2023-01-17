#functional concept
def TV_fun(model,operation):
    print("Model is: ",model)
    print("Operation is: ", operation)
def Fridge_fun(model,operation):
    print("Model is: ",model)
    print("Operation is: ", operation)

TV_fun("Samsung","Video")
Fridge_fun("LG","Cooling")

TV_fun("Videocon","Make Ice")
Fridge_fun("BPL","audio song")

#oops concept
#while creating object it automatically will creare an constructor
#self is the address of the current file

class TVFun:
    def TV_fun(self,model,operation):
        print("Model is: ",model)
        print("Operation is: ", operation)

class FridgeFun:
    def Fridge_fun(self,model,operation):
        print("Model is: ",model)
        print("Operation is: ", operation)

t1=TVFun()
t1.TV_fun("Samsung","Video")
f1=FridgeFun()
f1.Fridge_fun("LG","Cooling")

#t1.Fridge_fun("TV","cooling")
