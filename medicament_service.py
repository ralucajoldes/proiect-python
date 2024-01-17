from DOMAIN.add_operation import AddOperation
from DOMAIN.delete_operation import DeleteOperation
from DOMAIN.medicament import Medicament
from DOMAIN.update_operation import UpdateOperation
from REPOSITORY.file_repository import FileRepository
from DOMAIN.medicament_validator import MedicamentValidator
from DOMAIN.id_nu_exista import id_nu_exista
from xlsxwriter import Workbook
from SERVICE.undo_redo_service import UndoRedoService

import random


class MedicamentService:
    def __init__(self, medicament_repository: FileRepository,medicament_validator:MedicamentValidator,undo_redo_service:UndoRedoService):
        self.__medicament_repository = medicament_repository
        self.__medicament_validator=medicament_validator
        self.__undo_redo_service=undo_redo_service

    def get_by_id(self,id_medicament):
        return  self.__medicament_repository.find_by_id(id_medicament)

    def adauga(self, id_medicament, nume, producator, pret, necesita_reteta):
        '''
        Adauga o medicament.

        :param id_medicament: id-ul medicamentului
        :param nume:numele medicamentului
        :param producator:producatorul medicamentului
        :param pret:pretul medicamentului
        :param necesita_reteta: da daca necesita reteta medicamentul,nu in caz contrar
        :raises KeyError: daca id-ul exista deja
        :return: -
        '''
        medicament = Medicament(id_medicament, nume, producator, pret, necesita_reteta)
        self.__medicament_validator.valideaza(medicament)
        if necesita_reteta =='da':
            medicament.necesita_reteta = True
        else:
            medicament.necesita_reteta = False

        self.__medicament_repository.adauga(medicament)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__medicament_repository,medicament))
        self.__undo_redo_service.add_to_redo(AddOperation(self.__medicament_repository,medicament))

    def sterge(self, id_medicament):
        medicament = self.__medicament_repository.find_by_id(id_medicament)
        self.__medicament_repository.sterge(id_medicament)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__medicament_repository, medicament))
        self.__undo_redo_service.add_to_redo(DeleteOperation(self.__medicament_repository, medicament))

    def modifica(self, id_medicament, nume, producator, pret, necesita_reteta):
        '''
        Modifica un medicament.
        :param id_medicament:id-ul medicamentului
        :param nume: noul nume al medicamentului sau nimic
        :param producator:noul producator al medicamentului sau nimic
        :param pret: noul pret al medicamentului sau 0
        :param necesita_reteta: da / nu sau nimic
        :raises KeyError: daca id - ul nu exista
        :return: -
        '''
        medicament = self.__medicament_repository.find_by_id(id_medicament)
        medicament_initial= self.__medicament_repository.find_by_id(id_medicament)
        if medicament is None:
            raise id_nu_exista(f'Medicamentul cu id-ul {id_medicament} nu exista!')

        if nume != '':
            medicament.nume = nume
        if producator != '':
            medicament.producator= producator
        if pret!= 0:
            medicament.pret = pret
        if necesita_reteta != '':
            medicament.necesita_reteta = necesita_reteta

        if necesita_reteta == 'da' or necesita_reteta == '':
            medicament.necesita_reteta= True
        else:
            medicament.necesita_reteta = False

        self.__medicament_repository.modifica(medicament)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__medicament_repository, medicament,medicament_initial))
        self.__undo_redo_service.add_to_redo(UpdateOperation(self.__medicament_repository, medicament,medicament_initial))

    def get_all(self):
        return self.__medicament_repository.get_all()

    def afisare_rec(self,lista):
        if len(lista)==0:
            return []
        else:
            return[lista.pop()]+self.afisare_rec(lista)

    def scumpire(self,procent,val_data):
        '''
        Scumpirea cu un procentaj dat al unui medicament cu pretul mai mic decat o valoare data.
        :param procent: procentul cu care se scumpeste
        :param val_data:valoarea data
        :return: -
        '''
        medicamente =self.__medicament_repository.get_all()
        for medicament in medicamente:
            medicament_initial=self.__medicament_repository.find_by_id(medicament.id_medicament)
            if medicament.pret<val_data:
                adaos=procent/100 *medicament.pret
                medicament.pret=medicament.pret+adaos
                self.__medicament_repository.modifica(medicament)
                self.__undo_redo_service.add_to_undo(UpdateOperation(self.__medicament_repository, medicament,medicament_initial))
                self.__undo_redo_service.add_to_redo(UpdateOperation(self.__medicament_repository, medicament,medicament_initial))


    def populate_entities(self,n):
        '''
        Creeaza n entitati random.
        :param n: numarul de entitati de creat
        :return :
        '''
        for i in range(n):
            id_medicament=str(round(random.random()*10000))
            while self.__medicament_repository.find_by_id(id_medicament)!= None:
                id_medicament=str(round(random.random()*10000))
            nume=random.choice(['íi','sjh','gffh','h','fgf'])
            producator=random.choice(['í','sh','gff','hi','f'])
            pret=random.randint(1,1000)
            necesita_reteta=random.choice([True,False])
            self.adauga(id_medicament,nume,producator,pret,necesita_reteta)


    def cautare(self,sir):
        medicamente=self.__medicament_repository.get_all()
        lista=[]
        for medicament in medicamente:
            if medicament.id_medicament == sir:
                lista.append(medicament)
            elif medicament.nume == sir:
                lista.append(medicament)
            elif medicament.producator == sir:
                lista.append(medicament)
            elif str(medicament.pret) == sir:
                lista.append(medicament)
            elif str(medicament.necesita_reteta) == sir:
                lista.append(medicament)
        return lista

    def export(self):
        new_workbook=Workbook('medicamente.xlsx')
        new_worksheet=new_workbook.add_worksheet()
        new_worksheet.write(0,0,'id_medicament')
        new_worksheet.write(0, 1, 'nume')
        new_worksheet.write(0, 2, 'producator')
        new_worksheet.write(0, 3, 'pret')
        new_worksheet.write(0, 4, 'necesita reteta')
        medicamente=self.__medicament_repository.get_all()
        row=1
        for medicament in medicamente:
            new_worksheet.write(row, 0,medicament.id_medicament)
            new_worksheet.write(row, 1, medicament.nume)
            new_worksheet.write(row, 2, medicament.producator)
            new_worksheet.write(row, 3, medicament.pret)
            new_worksheet.write(row, 4, medicament.necesita_reteta)
            row+=1
        new_workbook.close()







