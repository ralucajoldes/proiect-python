from REPOSITORY.file_repository import FileRepository
from SERVICE.tranzactie_service import Tranzactie_Service
from SERVICE.undo_redo_service import UndoRedoService
from SERVICE.sortari_service import SortariService
from TESTS.clear import clear_file
from DOMAIN.medicament import Medicament


def test_adauga_tranzactie():
    clear_file("tranzactie_test.txt")
    tranzactie_repository = FileRepository("tranzactie_test.txt")
    clear_file("medicament_test.txt")
    medicament_repository = FileRepository("medicament_test.txt")
    clear_file("card_test.txt")
    card_client_repository = FileRepository("card_test.txt")
    undo_redo_service = UndoRedoService()
    sortari_service = SortariService()
    service = Tranzactie_Service(tranzactie_repository, medicament_repository,card_client_repository,sortari_service,undo_redo_service)
    medicament_repository.adauga(Medicament('1', 'paracetamol', 'zetiva', 30, 'da'))

    service.adauga('1','1','0',30,'12.12.2000 12:12')
    assert len(service.get_all()) == 1

def test_sterge_tranzactie():
    clear_file("tranzactie_test.txt")
    tranzactie_repository = FileRepository("tranzactie_test.txt")
    clear_file("medicament_test.txt")
    medicament_repository= FileRepository("medicament_test.txt")
    clear_file("card_test.txt")
    card_client_repository= FileRepository("card_test.txt")
    sortari_service = SortariService()
    undo_redo_service = UndoRedoService()
    service = Tranzactie_Service(tranzactie_repository, medicament_repository,card_client_repository,sortari_service,undo_redo_service)
    medicament_repository.adauga(Medicament('2', 'paracetamol', 'zetiva', 30, 'da'))
    service.adauga('1','2','0',30,'12.12.2000 12:23')
    try:
        service.sterge('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.sterge('1')
    deleted = tranzactie_repository.find_by_id('1')
    assert deleted is None


def test_modifica_tranzactie():
    clear_file("tranzactie_test.txt")
    tranzactie_repository = FileRepository("tranzactie_test.txt")
    clear_file("medicament_test.txt")
    medicament_repository = FileRepository("medicament_test.txt")
    clear_file("card_test.txt")
    card_client_repository = FileRepository("card_test.txt")
    sortari_service = SortariService()
    undo_redo_service = UndoRedoService()
    service = Tranzactie_Service(tranzactie_repository, medicament_repository,card_client_repository,sortari_service,undo_redo_service)
    medicament_repository.adauga(Medicament('1', 'paracetamol', 'zetiva', 30, 'da'))
    service.adauga('1', '1', '0', 30, '12.12.2000 12:23')
    service.modifica('1', '', '', 1235,'29.08.2019 12:13')
    updated = tranzactie_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.id_medicament== '1'
    assert updated.id_card == '0'
    assert updated.nr_bucati == 1235
    assert updated.data_ora == '29.08.2019 12:13'
    try:
        service.modifica('3', '', '', '', '')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
