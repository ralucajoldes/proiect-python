from DOMAIN.medicament import Medicament
from DOMAIN.tranzactie import Tranzactie
from DOMAIN.card_client import Card_client
from REPOSITORY.file_repository import FileRepository
from TESTS.clear import clear_file

def test_add_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")

    medicament1 = Medicament('1', 'paracetamol', 'zetiva', 30, 'da')

    entitati_repository.adauga(medicament1)
    assert len(entitati_repository.get_all()) == 1
    try:
        medicament2 = Medicament('1', 'paraceamol', 'zetiva', 30, 'da')
        entitati_repository.adauga(medicament2)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_delete_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")
    medicament1 = Medicament('1', 'paracetamol', 'zetiva', 30, 'da')
    medicament2 = Medicament('2', 'paraceamol', 'zetiva', 30, 'da')
    entitati_repository.adauga(medicament1)
    entitati_repository.adauga(medicament2)
    try:
        entitati_repository.sterge('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    entitati_repository.sterge('1')
    assert len(entitati_repository.get_all()) == 1

def test_update_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")
    medicament1 = Medicament('1', 'paracetamol', 'zetiva', 30, 'da')
    medicament2 = Medicament('2','tramadol', 'zetiva', 30, 'nu')
    entitati_repository.adauga(medicament1)
    entitati_repository.adauga(medicament2)

    medicament3 = Medicament('1','acc', 'zetiva', 30, 'nu')
    entitati_repository.modifica(medicament3)
    updated = entitati_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume == 'acc'
    assert updated.producator == 'zetiva'
    assert updated.pret == 30
    assert updated.necesita_reteta == 'nu'