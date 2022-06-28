from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """Test for Puppy Model"""

    def setUp(self):
        Puppy.objects.create(name='Ellie', age=1, breed='SRD', color='Gray')
        Puppy.objects.create(name='Bolinha', age=2, breed='Golden', color='Golden')

    
    def test_puppy_breed(self):
        puppy_ellie = Puppy.objects.get(name='Ellie')
        puppy_bolinha = Puppy.objects.get(name='Bolinha')

        self.assertEqual(
            puppy_ellie.get_breed(), 'Ellie belongs to SRD breed'
        )

        self.assertEqual(
            puppy_bolinha.get_breed(), 'Bolinha belongs to Golden breed'
        )
            