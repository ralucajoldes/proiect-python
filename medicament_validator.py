from DOMAIN.medicament import Medicament


class MedicamentValidator:

    def valideaza(self, medicament: Medicament):

        errors = []
        if medicament.pret <0:
            errors.append('Pretul trebuie sa fie mai mare ca 0!')

        if errors != []:
            raise ValueError(errors)