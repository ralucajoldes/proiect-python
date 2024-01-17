from DOMAIN.card_client import Card_client
from DOMAIN.delete_operation import DeleteOperation
from DOMAIN.update_operation import UpdateOperation
from REPOSITORY.file_repository import FileRepository
from DOMAIN.id_nu_exista import id_nu_exista
from DOMAIN.id_nu_este_unic import id_nu_este_unic
from DOMAIN.add_operation import AddOperation
from SERVICE.undo_redo_service import UndoRedoService


class Card_client_Service:
    def __init__(self, card_repository: FileRepository,undo_redo_service:UndoRedoService):
        self.__card_repository = card_repository
        self.__undo_redo_service = undo_redo_service

    def find_by_cnp(self, cnp):
        '''

        '''
        for card_client in self.__card_repository.get_all():
            if card_client.cnp == cnp:
                return cnp
        return None

    def get_by_id(self,id_card):
        return  self.__card_repository.find_by_id(id_card)


    def adauga(self, id_card, nume, prenume, cnp, data_nasterii,data_inregistrarii):
        '''
        Adauga un card.

        :param id_card: id-ul cardului
        :param nume:numele beneficiarului cardului
        :param prenume:prenumele beneficiarului cardului
        :param cnp:cnp-ul beneficiarului cardului
        :param data_nasterii: data nasterii beneficiarului cardului
        :param data_inregistrarii: data inregistrarii cardului
        :raises KeyError: daca id-ul exista deja
        :return: -
        '''
        card_client = Card_client(id_card, nume, prenume, cnp, data_nasterii,data_inregistrarii)
        if self.find_by_cnp(card_client.cnp) is not None:
            raise id_nu_este_unic(f'Cardul cu cnp-ul  {cnp} exista!')


        self.__card_repository.adauga(card_client)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__card_repository, card_client))
        self.__undo_redo_service.add_to_redo(AddOperation(self.__card_repository, card_client))


    def sterge(self, id_card):
        card_client = self.__card_repository.find_by_id(id_card)
        self.__card_repository.sterge(id_card)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__card_repository, card_client))
        self.__undo_redo_service.add_to_redo(DeleteOperation(self.__card_repository, card_client))

    def modifica(self, id_card, nume, prenume, cnp, data_nasterii,data_inregistrarii):
        '''
        Modifica un card.
        :param id_card: id - ul cardului
        :param nume: numele nou al beneficiarului cardului sau nimic
        :param prenume: prenumele nou al beneficiarului cardului sau nimic
        :param cnp: cnp - ul nou al beneficiarului cardului sau nimic
        :param data_nasterii: noua data de nastere a beneficiarului cardului sau nimic
        :param data_inregistrarii: noua data de inregistrare a cardului sau nimic
        :raises KeyError: daca id - ul nu exista
        :return: -
        '''
        card_client = self.__card_repository.find_by_id(id_card)
        card_initial=self.__card_repository.find_by_id(id_card)
        if card_client is None:
            raise id_nu_exista(f'Cardul cu id-ul {id_card} nu exista!')


        if nume != '':
            card_client.nume = nume
        if prenume != '':
            card_client.prenume= prenume
        if cnp!= '':
            if self.find_by_cnp(cnp) is not None:
                raise id_nu_este_unic(f'Cardul cu cnp-ul  {cnp} exista!')
            card_client.cnp = cnp
        if data_nasterii != '':
            card_client.data_nasterii = data_nasterii
        if data_inregistrarii != '':
            card_client.data_inregistrarii= data_inregistrarii
        self.__card_repository.modifica(card_client)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__card_repository, card_client,card_initial))
        self.__undo_redo_service.add_to_redo(UpdateOperation(self.__card_repository, card_client,card_client))

    def get_all(self):
        return self.__card_repository.get_all()

    def cautare(self,sir):
        carduri=self.__card_repository.get_all()
        lista=[]
        for card in carduri:
            if card.id_card == sir:
                lista.append(card)
            elif card.nume == sir:
                lista.append(card)
            elif card.prenume == sir:
                lista.append(card)
            elif card.cnp == sir:
                lista.append(card)
            elif str(card.data_nasterii) == sir:
                lista.append(card)
            elif str(card.data_inregistrarii) == sir:
                lista.append(card)
        return lista
