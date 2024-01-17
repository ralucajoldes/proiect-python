from REPOSITORY.file_repository import FileRepository
from SERVICE.card_client_service import Card_client_Service
from SERVICE.medicament_service import MedicamentService
from SERVICE.tranzactie_service import Tranzactie_Service
from SERVICE.sortari_service import SortariService
from TESTS.run_all import run_all_tests
from UI.console import Console
from DOMAIN.medicament_validator import MedicamentValidator
from SERVICE.undo_redo_service import UndoRedoService
def main():

    medicament_repository = FileRepository('medicament.txt') #MasinaRepository()
    card_client_repository = FileRepository('card_client.txt')
    tranzactie_repository = FileRepository('tranzactie.txt')
    medicament_validator=MedicamentValidator()
    sortari_service=SortariService()
    undo_redo_service=UndoRedoService()
    medicament_service = MedicamentService(medicament_repository,medicament_validator,undo_redo_service)
    card_client_service = Card_client_Service(card_client_repository,undo_redo_service)
    tranzactie_service = Tranzactie_Service(tranzactie_repository, medicament_repository, card_client_repository,sortari_service,undo_redo_service)


    user_interface = Console(medicament_service, card_client_service, tranzactie_service,sortari_service,undo_redo_service)
    user_interface.run_console()


run_all_tests()
main()
