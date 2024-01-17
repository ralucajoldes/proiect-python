from REPOSITORY.file_repository import FileRepository
from SERVICE.medicament_service import MedicamentService
from TESTS.clear import clear_file
from DOMAIN.medicament_validator import MedicamentValidator
from SERVICE.undo_redo_service import UndoRedoService


def test_adauga_medicament():
    clear_file("service_test.txt")
    medicament_repository = FileRepository("service_test.txt")
    medicament_validator = MedicamentValidator()
    undo_redo_service=UndoRedoService()
    service = MedicamentService(medicament_repository,medicament_validator,undo_redo_service)
    service.adauga('1', 'paracetamol', 'zetiva', 30, 'da')
    assert len(service.get_all()) == 1
    added = medicament_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'paracetamol'
    assert added.producator == 'zetiva'
    assert added.pret == 30
    assert added.necesita_reteta ==True

    try:
        service.adauga('1', 'paracet', 'zetiva', 30, 'da')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_sterge_medicament():
    clear_file("service_test.txt")
    medicament_repository = FileRepository("service_test.txt")
    medicament_validator = MedicamentValidator()
    undo_redo_service = UndoRedoService()
    service = MedicamentService(medicament_repository,medicament_validator,undo_redo_service)
    service.adauga('1', 'paracetamol', 'zetiva', 30, 'da')
    service.adauga('2', 'parace', 'zetiva', 33, 'da')

    try:
        service.sterge('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.sterge('1')
    assert len(service.get_all()) == 1
    deleted = medicament_repository.find_by_id('1')
    assert deleted is None
    remaining = medicament_repository.find_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.nume =='parace'
    assert remaining.producator == 'zetiva'
    assert remaining.pret == 33
    assert remaining.necesita_reteta == True

def test_modifica_medicament():
    clear_file("service_test.txt")
    medicament_repository = FileRepository("service_test.txt")
    medicament_validator = MedicamentValidator()
    undo_redo_service = UndoRedoService()
    service = MedicamentService(medicament_repository,medicament_validator,undo_redo_service)
    service.adauga('1', 'paracetamol', 'zetiva', 30, 'da')
    service.adauga('2', 'parace', 'zetiva', 33, 'da')

    service.modifica('1', 'aspirina', 'catena', 0, '')
    updated = medicament_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume== 'aspirina'
    assert updated.producator == 'catena'
    assert updated.pret == 30
    assert updated.necesita_reteta == True

    unchanged = medicament_repository.find_by_id('2')
    assert unchanged is not None
    assert unchanged.id_entitate == '2'
    assert unchanged.nume == 'parace'
    assert unchanged.producator == 'zetiva'
    assert unchanged.pret == 33
    assert unchanged.necesita_reteta == True

    try:
        service.modifica('3', '', '', 32, 'nu')
        assert False
    except Exception:
        assert True

