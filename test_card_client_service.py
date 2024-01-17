from REPOSITORY.file_repository import FileRepository
from SERVICE.card_client_service import Card_client_Service
from SERVICE.undo_redo_service import UndoRedoService
from TESTS.clear import clear_file


def test_adauga_card_client():
    clear_file("service_test.txt")
    card_client_repository = FileRepository("service_test.txt")
    undo_redo_service = UndoRedoService()
    service = Card_client_Service(card_client_repository,undo_redo_service)

    service.adauga('1','Popescu','Vasile','1234','12.12.2000','30.08.2019')
    assert len(service.get_all()) == 1
    added = card_client_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'Popescu'
    assert added.prenume == 'Vasile'
    assert added.cnp == '1234'
    assert added.data_nasterii == '12.12.2000'
    assert added.data_inregistrarii == '30.08.2019'

    try:
        service.adauga('1','Popescu','Vasile','1234','12.12.2000','30.08.2019')
        assert False
    except Exception:
        assert True


def test_sterge_card_client():
    clear_file("service_test.txt")
    card_client_repository = FileRepository("service_test.txt")
    undo_redo_service = UndoRedoService()
    service = Card_client_Service(card_client_repository,undo_redo_service)
    service.adauga('1','Popescu','Vasile','1234','12.12.2000','30.08.2019')
    service.adauga('2','Popescu','Ion','1239','12.12.2000','30.08.2019')

    try:
        service.sterge('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.sterge('1')
    assert len(service.get_all()) == 1
    deleted = card_client_repository.find_by_id('1')
    assert deleted is None
    remaining = card_client_repository.find_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.nume =='Popescu'
    assert remaining.prenume == 'Ion'
    assert remaining.cnp == '1239'
    assert remaining.data_nasterii == '12.12.2000'
    assert remaining.data_inregistrarii == '30.08.2019'

def test_modifica_card_client():
    clear_file("service_test.txt")
    card_client_repository = FileRepository("service_test.txt")
    undo_redo_service = UndoRedoService()
    service = Card_client_Service(card_client_repository,undo_redo_service)
    service.adauga('1', 'Popescu', 'Vasile', '1234', '12.12.2000', '30.08.2019')
    service.adauga('2', 'Popescu', 'Ion', '1239', '12.12.2000', '30.08.2019')

    service.modifica('1', 'Ionescu', '', '1235', '', '29.08.2019')
    updated = card_client_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume== 'Ionescu'
    assert updated.prenume == 'Vasile'
    assert updated.cnp == '1235'
    assert updated.data_nasterii =='12.12.2000'
    assert updated.data_inregistrarii == '29.08.2019'

    unchanged = card_client_repository.find_by_id('2')
    assert unchanged is not None
    assert unchanged.id_entitate == '2'
    assert unchanged.nume == 'Popescu'
    assert unchanged.prenume == 'Ion'
    assert unchanged.cnp =='1239'
    assert unchanged.data_nasterii == '12.12.2000'
    assert unchanged.data_inregistrarii == '30.08.2019'

    try:
        service.modifica('3', '', '', '', '','')
        assert False
    except Exception:
        assert True

