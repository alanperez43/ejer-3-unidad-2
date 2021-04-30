class menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3test
        }
    def opcion(self,op,lista,bi):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(lista,bi)
    def op1(self,lista,bi):
        #tener encuenta lo que esta en el archivo ,de ahi se a cargado la listabi
        ide=int(input("Ingresar identificador de camion a buscar: "))
        total=bi.buscar(ide)
        if(total != -1):
            print("Total de quilos para el camion {} es de {}".format(ide,total))
        else:
            print("ERROR")
    def op2(self,lista,bi):
        d=int(input("Ingresar dia para mostra: "))
        print("{}      {}        {}".format("PATENTE","CONDUCTOR","CANT.KG"))
        for i in lista:
            id=i.getid()
            kg=bi.m(d,id)
            print("{}      {}        {}".format(str(i.getpatente()),str(i.getnom()),kg))
        
    def op3test(self,lista,bi):
        self.registrar(1,90,3000.4)
        self.registrar(5,45,23)
        self.registrar(5,45,900.5)
        self.registrar(1,45,800.0)
        self.registrar(10,45,1000.1)
        print("test id 1 kg:",self.op1(1,lista,arre))
        print("test dia 45:")
        self.op2(45,lista,arre)   
