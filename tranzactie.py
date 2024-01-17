from DOMAIN.entitate import Entitate
class Tranzactie(Entitate):
    '''
    descrie entitatea tranzactie
    '''

    def __init__(self,id_tranzactie,id_medicament, id_card, nr_bucati, data_ora):
        # campuri/fields
        super().__init__(id_tranzactie)
        self.__id_tranzactie=id_tranzactie
        self.__id_medicament=id_medicament
        self.__id_card = id_card
        self.__nr_bucati = nr_bucati
        self.__data_ora= data_ora

    def __str__(self):
        return f"id: {self.__id_tranzactie}, id_medicament: {self.__id_medicament}, id_card: {self.__id_card}, " \
                f"nr_bucati: {self.__nr_bucati}, data si ora: {self.__data_ora}"

    def __eq__(self, other):
        return type(self) == type(other) and self.__id_tranzactie == other.__id_tranzactie

    #proprietati
    @property
    def id_tranzactie(self):
        return self.__id_tranzactie

    @property
    def id_medicament(self):
        return self.__id_medicament

    @id_medicament.setter
    def id_medicament(self, id_medicament_nou):
        self.__id_medicament = id_medicament_nou

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, id_card_nou):
        self.__id_card = id_card_nou

    @property
    def nr_bucati(self):
        return self.__nr_bucati

    @nr_bucati.setter
    def nr_bucati(self, nr_bucati_nou):
        self.__nr_bucati = nr_bucati_nou

    @property
    def data_ora(self):
        return self.__data_ora

    @data_ora.setter
    def data_ora(self, data_ora_noua):
        self.__data_ora = data_ora_noua
