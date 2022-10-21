from django.test import TestCase
from prometeo.models import BankAccount
from django.utils.crypto import get_random_string

class BankTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):      
        bank_name_test = get_random_string(length=128)
        country_test = get_random_string(length=128)

        # Creación de un BankAccount
        BankAccount.objects.create(bank_name = bank_name_test, country = country_test)
        

    def test_bank_max_length(self):
        # Test 1: Verifica si el max_lenght del bank coincide con el max_lenght del modelo
        bank_test = BankAccount.objects.get(id=1)
        max_length = bank_test._meta.get_field('bank_name').max_length
        self.assertEqual(max_length, 5000)

    def test_object_name_is_bank_name(self):
        # Test 2: Verifica si el def __str__(self) del modelo coincide con el bankname
        bank_test = BankAccount.objects.get(id=1)
        expected_object_name = f'{bank_test.bank_name}'
        self.assertEqual(str(bank_test), expected_object_name)

