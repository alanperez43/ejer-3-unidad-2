class bi():
    __lis=[]
    def __init__(self):
        for i in range(45):
            self.__lis.append([])
            for j in range(20):
                self.__lis[i].append(0)
    def mostrar(self):
        print(range(len(self.__lis)))
    def registrar(self,peso,id,dia):
        if(self.__lis[dia-1][id-1] is not None):
            self.__lis[dia-1][id-1]+=peso

        else:
            self.__lis[dia-1][id-1]=peso
        
    def buscar(self,id):
        if(id<0 and id>21):
            return -1
        else:
            acum=0
            for i in self.__lis:
                if i[id-1] is not None:
                    acum+=i[id-1]
            return acum
    def m(self,d,id):
       return self.__lis[d-1][id-1]