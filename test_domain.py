from DOMAIN.medicament import Medicament
from DOMAIN.card_client import Card_client
from DOMAIN.tranzactie import Tranzactie

def test_medicament():
    medicament = Medicament(1, 'paracetamol', 'zetiva', 30, 'da')
    assert medicament.id_entitate == 1
    assert medicament.nume == 'paracetamol'
    assert medicament.producator == 'zetiva'
    assert medicament.pret == 30
    assert medicament.necesita_reteta =='da'

def test_card_client():
    card_client=Card_client(1,'Popescu','Vasile','1234','12.12.2000','30.08.2019')
    assert card_client.id_entitate == 1
    assert card_client.nume == 'Popescu'
    assert card_client.prenume == 'Vasile'
    assert card_client.cnp == '1234'
    assert card_client.data_nasterii == '12.12.2000'
    assert card_client.data_inregistrarii == '30.08.2019'

def test_tranzactie():
    tranzactie=Tranzactie(1,1,1,50,'17.09.2019 12:30')
    assert tranzactie.id_entitate == 1
    assert tranzactie.id_medicament == 1
    assert tranzactie.id_card == 1
    assert tranzactie.nr_bucati == 50
    assert tranzactie.data_ora == '17.09.2019 12:30'

