from DOMAIN.entitate import Entitate
class Medicament(Entitate):
    '''
    descrie entitatea medicament
    '''

    def __init__(self, id_medicament, nume, producator, pret, necesita_reteta):
        # campuri/fields
        super().__init__(id_medicament)
        self.__id_medicament = id_medicament
        self.__nume = nume
        self.__producator = producator
        self.__pret = pret
        self.__necesita_reteta= necesita_reteta

    def __str__(self):
        return f"id: {self.__id_medicament}, nume: {self.__nume}, producator: {self.__producator}, " \
                f"pret: {self.__pret}, necesita_reteta: {self.__necesita_reteta}"

    def __eq__(self, other):
        return type(self) == type(other) and self.__id_medicament == other.__id_medicament

    #proprietati
    @property
    def id_medicament(self):
        return self.__id_medicament

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def producator(self):
        return self.__producator

    @producator.setter
    def producator(self, producator_nou):
        self.__producator = producator_nou

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, pret_nou):
        self.__pret = pret_nou

    @property
    def necesita_reteta(self):
        return self.__necesita_reteta

    @necesita_reteta.setter
    def necesita_reteta(self, necesita_reteta_noua):
        self.__necesita_reteta = necesita_reteta_noua
