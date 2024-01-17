from DOMAIN.entitate import Entitate
class Card_client(Entitate):
    '''
    descrie entitatea cardului unui client
    '''

    def __init__(self, id_card, nume, prenume, cnp, data_nasterii,data_inregistrarii):
        # campuri/fields
        super().__init__(id_card)
        self.__id_card = id_card
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__data_nasterii= data_nasterii
        self.__data_inregistrarii = data_inregistrarii

    def __str__(self):
        return f"id: {self.__id_card}, nume: {self.__nume}, prenume: {self.__prenume}, " \
                f"cnp: {self.__cnp}, data nasterii: {self.__data_nasterii},data inregistrarii:{self.__data_inregistrarii}"

    def __eq__(self, other):
        return type(self) == type(other) and self.__id_card == other.__id_card

    #proprietati
    @property
    def id_card(self):
        return self.__id_card

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, prenume_nou):
        self.__prenume = prenume_nou

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        self.__cnp = cnp_nou

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @data_nasterii.setter
    def data_nasterii(self, data_nasterii_noua):
        self.__data_nasterii = data_nasterii_noua

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, data_inregistrarii_noua):
        self.__data_inregistrarii = data_inregistrarii_noua
