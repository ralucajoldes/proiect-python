from DOMAIN.delete_operation import DeleteOperation
from DOMAIN.tranzactie import Tranzactie
from DOMAIN.update_operation import UpdateOperation
from REPOSITORY.file_repository import FileRepository
from DOMAIN.add_operation import AddOperation
from SERVICE.undo_redo_service import UndoRedoService
from SERVICE.sortari_service import SortariService




class Tranzactie_Service:
    def __init__(self, tranzactie_repository: FileRepository,
                 medicament_repository: FileRepository,
                 card_client_repository: FileRepository,
                 sortari_service: SortariService,
                 undo_redo_service:UndoRedoService):
        self.__tranzactie_repository = tranzactie_repository
        self.__medicament_repository=medicament_repository
        self.__card_client_repository=card_client_repository
        self.__sortari_service=sortari_service
        self.__undo_redo_service = undo_redo_service


    def adauga(self,id_tranzactie,id_medicament, id_card, nr_bucati, data_ora):
        '''
        Adauga o tranzactie.

        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament: id-ul medicamentului
        :param id_card: id-ul cardului
        :param nr_bucati:numarul de bucati
        :param data_ora: data si ora tranzactiei
        :raises KeyError: daca id-ul exista deja
        :return: -
        '''
        tranzactie = Tranzactie(id_tranzactie,id_medicament, id_card, nr_bucati, data_ora)
        if self.__medicament_repository.find_by_id(id_medicament) is None:
            raise KeyError('Nu se poate crea tranzactia, pentru ca nu exista un medicament cu id-ul ', id_medicament)
        medicament=self.__medicament_repository.find_by_id(id_medicament)
        if id_card != '0':
            if medicament.necesita_reteta == False:
                reducere=0.1*(tranzactie.nr_bucati*medicament.pret)
                pret=(tranzactie.nr_bucati*medicament.pret)-reducere
                print(f'Pretul este {pret} care s-a redus cu {reducere}')
            else:
                reducere = 0.15 * (tranzactie.nr_bucati * medicament.pret)
                pret = (tranzactie.nr_bucati * medicament.pret) - reducere
                print(f'Pretul este {pret} care s-a redus cu {reducere}')

        self.__tranzactie_repository.adauga(tranzactie)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__tranzactie_repository, tranzactie))
        self.__undo_redo_service.add_to_redo(AddOperation(self.__tranzactie_repository, tranzactie))

    def sterge(self, id_tranzactie):
        tranzactie = self.__tranzactie_repository.find_by_id(id_tranzactie)
        self.__tranzactie_repository.sterge(id_tranzactie)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__tranzactie_repository, tranzactie))
        self.__undo_redo_service.add_to_redo(DeleteOperation(self.__tranzactie_repository, tranzactie))

    def modifica(self,id_tranzactie,id_medicament, id_card, nr_bucati, data_ora):
        '''
        Modifica o tranzactie.

        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament:noul id al medicamentului sau nimic
        :param id_card:noul id al cardului sau nimic
        :param nr_bucati:noul numar de bucati sau nimic
        :param data_ora: noua data si ora a tranzactiei
        :raises KeyError: daca id-ul nu exista
        :return: -
        '''
        tranzactie = self.__tranzactie_repository.find_by_id(id_tranzactie)
        tranzactie_initiala=self.__tranzactie_repository.find_by_id(id_tranzactie)
        if tranzactie is None:
            raise KeyError(f'Tranzactia cu id-ul {id_tranzactie} nu exista!')

        if id_medicament != '':
            tranzactie.id_medicament = id_medicament
        if id_card != '':
            tranzactie.id_card= id_card
        if nr_bucati!= '':
            tranzactie.nr_bucati= nr_bucati
        if data_ora != '':
            tranzactie.data_ora = data_ora
        self.__tranzactie_repository.modifica(tranzactie)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__tranzactie_repository,tranzactie,tranzactie_initiala))
        self.__undo_redo_service.add_to_redo(UpdateOperation(self.__tranzactie_repository, tranzactie,tranzactie_initiala))
        medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)
        if  tranzactie.id_card !='0':
            if medicament.necesita_reteta == False:
                reducere=0.1*(tranzactie.nr_bucati*medicament.pret)
                pret=(tranzactie.nr_bucati*medicament.pret)-reducere
                print(f'Pretul este {pret} care s-a redus cu {reducere}')
            else:
                reducere = 0.15 * (tranzactie.nr_bucati * medicament.pret)
                pret = (tranzactie.nr_bucati * medicament.pret) - reducere
                print(f'Pretul este {pret} care s-a redus cu {reducere}')

    def get_all(self):
        return self.__tranzactie_repository.get_all()

    def afisare_tranzactii_din_interval(self,ziuap,ziuau):
        '''
        Verifica toate tranzactiile care sunt in intervalul dat.
        :param ziuap: prima zi a intervalului
        :param ziuau: ultima zi a intervalului
        :return : o lista cu tranzactiile din interval
        '''
        tranzactii_din_interval=[]
        for tranzactie in self.__tranzactie_repository.get_all():
            data=tranzactie.data_ora.strftime('%d.%m.%Y')
            tranzactie_data=data.split('.')
            ziua=tranzactie_data[0]
            if int(ziua)>=int(ziuap) and int(ziua)<=int(ziuau):
                tranzactii_din_interval.append(tranzactie)
        return tranzactii_din_interval

    def sterge_tranzactii_din_interval(self,ziuap,ziuau):
        '''
        Sterge toate tranzactiile care sunt in intervalul dat.
        :param ziuap: prima zi a intervalului
        :param ziuau: ultima zi a intervalului
        :return : -
        '''
        for tranzactie in self.__tranzactie_repository.get_all():
            data=tranzactie.data_ora.strftime('%d.%m.%Y')
            tranzactie.data=data.split('.')
            ziua=tranzactie.data[0]
            if int(ziua)>=int(ziuap) and int(ziua)<=int(ziuau):
                deleted=self.__tranzactie_repository.find_by_id(tranzactie.id_tranzactie)
                self.__tranzactie_repository.sterge(tranzactie.id_tranzactie)
                self.__undo_redo_service.add_to_undo(DeleteOperation(self.__tranzactie_repository, deleted))
                self.__undo_redo_service.add_to_redo(DeleteOperation(self.__tranzactie_repository, deleted))

    def ordonare_medicamente_dupa_nr_vanzari(self):
        '''
        Ordoneaza medicamentele in ordine descrescatoare dupa numarul de vanzari
        :return:
        '''
        tranzactii=self.__tranzactie_repository.get_all()
        medicamente_vandute={}
        for tranzactie in tranzactii:
            if tranzactie.id_medicament in medicamente_vandute:
                medicamente_vandute[tranzactie.id_medicament]+=int(tranzactie.nr_bucati)
            else:
                medicamente_vandute[tranzactie.id_medicament]=int(tranzactie.nr_bucati)
        medicamente_vandute_ord=sorted(medicamente_vandute.items(),key=lambda mv: mv[1],reverse=True)
        return medicamente_vandute_ord

    def ordonare_carduri_dupa_reducerere(self):
        '''
        Afișarea cardurilor client ordonate descrescător după valoarea reducerilor obținute.
        :return:
        '''
        carduri=self.__card_client_repository.get_all()
        tranzactii=self.__tranzactie_repository.get_all()
        ordonare={}
        for card in carduri:
            valoare=0
            for tranzactie in tranzactii:
                if tranzactie.id_card == card.id_card:
                    medicament=self.__medicament_repository.find_by_id(tranzactie.id_medicament)
                    if medicament.necesita_reteta==False:
                        reducere = 0.1 * (tranzactie.nr_bucati * medicament.pret)
                        valoare+=reducere
                    elif medicament.necesita_reteta==True:
                        reducere = 0.15 * (tranzactie.nr_bucati * medicament.pret)
                        valoare += reducere
            ordonare[card.id_card]=valoare
        carduri_ord = sorted(ordonare.items(), key=lambda x: x[1], reverse=True)
        return carduri_ord

    def dictionar_medicamente(self):
        '''

        :return:
        '''
        tranzactii=self.__tranzactie_repository.get_all()
        medicamente_vandute={}
        for tranzactie in tranzactii:
            if tranzactie.id_medicament in medicamente_vandute:
                medicamente_vandute[tranzactie.id_medicament]+=int(tranzactie.nr_bucati)
            else:
                medicamente_vandute[tranzactie.id_medicament]=int(tranzactie.nr_bucati)
        return medicamente_vandute

    def afisare_tranzactii_din_interval_filtru(self,ziuap,ziuau):
        '''
        Verifica toate tranzactiile care sunt in intervalul dat.
        :param ziuap: prima zi a intervalului
        :param ziuau: ultima zi a intervalului
        :return : o lista cu tranzactiile din interval
        '''
        lista_tranzactii=[]
        for tranzactie in self.__tranzactie_repository.get_all():
            data=tranzactie.data_ora.strftime('%d.%m.%Y')
            tranzactie_data=data.split('.')
            ziua=tranzactie_data[0]
            lista_tranzactii.append(ziua)
        lista_filtrata=list(filter(lambda ziua:int(ziua)>=int(ziuap) and int(ziua)<=int(ziuau),lista_tranzactii))
        tranzactii_din_interval=[]
        for tranzactie in self.__tranzactie_repository.get_all():
            data=tranzactie.data_ora.strftime('%d.%m.%Y')
            tranzactie_data=data.split('.')
            ziua=tranzactie_data[0]
            if ziua in lista_filtrata:
                tranzactii_din_interval.append(tranzactie)
        return tranzactii_din_interval

    def ordonare_medicamente_quicksort(self):
        medicamente=self.__medicament_repository.get_all()
        tranzactii=self.__tranzactie_repository.get_all()
        lista_cantitati=[]
        for medicament in medicamente:
            cantitate=0
            for tranzactie in tranzactii:
                if tranzactie.id_medicament==medicament.id_medicament:
                    cantitate+=int(tranzactie.nr_bucati)
            lista_cantitati.append(cantitate)
        rezultat=list(zip(medicamente,lista_cantitati))
        return self.__sortari_service.quicksort(rezultat,reverse=True,key=lambda x:x[1])













