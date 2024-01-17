from TESTS.test_domain import test_medicament,test_card_client,test_tranzactie
from TESTS.test_file_repository import test_add_repository,test_delete_repository,test_update_repository
from TESTS.test_medicament_service import test_adauga_medicament,test_sterge_medicament,test_modifica_medicament
from TESTS.test_card_client_service import test_adauga_card_client,test_sterge_card_client,test_modifica_card_client
from TESTS.test_tranzactie_service import test_adauga_tranzactie,test_sterge_tranzactie,test_modifica_tranzactie

def run_all_tests():
    test_medicament()
    test_card_client()
    test_tranzactie()
    test_add_repository()
    test_delete_repository()
    test_update_repository()
    test_adauga_medicament()
    test_sterge_medicament()
    test_modifica_medicament()
    test_adauga_card_client()
    test_sterge_card_client()
    test_modifica_card_client()
    test_sterge_tranzactie()
    test_adauga_tranzactie()
    test_modifica_tranzactie()
