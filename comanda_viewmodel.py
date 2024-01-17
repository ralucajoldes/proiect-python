class TranzactieViewModel:

    def __init__(self, id_tranzactie, medicament, card, nr_bucati,data_ora):
        self.id_tranzactie = id_tranzactie
        self.medicament = medicament
        self.card = card
        self.nr_bucati = nr_bucati
        self.data_ora = data_ora

    def __str__(self):
        return f'Tranzactia cu id-ul {self.id_tranzactie}, medicamentul: {self.medicament}, ' \
               f'cardul: {self.card}, numarul de bucati : {self.nr_bucati}, data si ora: {self.data_ora}'