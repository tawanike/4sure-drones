from django.forms import ValidationError
from django.test import TestCase, Client
from medication.models import Medicine
# Create your tests here.


class MedicineModelTestCase(TestCase):

    def setUp(self):
        self.medication = {
            "name": "Telfast",
            "weight": 150,
            "code": "CRA03186",
            "image": "static/medication/download.jpeg"
        }

        Medicine.objects.create(**self.medication)

    def test_medicine_can_be_created(self):
        medication = Medicine.objects.all()
        self.assertEqual(medication.count(), 1)

    def test_create_medicine_failed(self):
        self.medication = {
            "name": "Telfast Suspension",
            "weight": 150,
            "code": "CRA03186",
            "image": "static/medication/download.jpeg"
        }
        with self.assertRaises(ValidationError):
            Medicine.objects.create(**self.medication)
