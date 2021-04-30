class camiones():
    __idcamion=None
    __nomcond=None
    __patente=None
    __marca=None
    __pesovacio=None
    def __init__(self,idcamion,nomcond,pat,marca,pesovacio):
        self.__idcamion=idcamion
        self.__nomcond=nomcond
        self.__patente=pat
        self.__marca=marca
        self.__pesovacio=pesovacio
    def getid(self):
        return self.__idcamion
    def getnom(self):
        return self.__nomcond
    def getpatente(self):
        return self.__patente
    def getmarca(self):
        return self.__marca
    def getpesovacio(self):
        return float(self.__pesovacio)