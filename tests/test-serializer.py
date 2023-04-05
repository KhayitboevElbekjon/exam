from unittest import TestCase
from asosiy.serializer import *
from rest_framework.test import APIClient
class TestSuvSerializer(TestCase):
    def test_suv(self):
        suv={
            "brend":"alibaba",
            "narx":12000,
            "litr":1,
            "batafsil":"Quyidagi suv shifobaxsh hisoblanadi",
        }
        serializer=SuvSerializer(data=suv)
        assert serializer.is_valid()==True
    def SetUP(self)->None:
        self.client=APIClient()
    def test_suv(self):
        natija=self.client.get('/suv/3/')
        assert natija.status_code==200
        assert natija.data['id']==3
class TestMijozSerializer(TestCase):
    def test_mijoz(self):
        mijoz={
            "ism":"alibaba",
            "tel":"+998552124578",
            "manzil":"toshkent",
            "qarz":125000,
            "user_fk":1
        }
        serializer=MijozSerializer(data=mijoz)
        assert serializer.is_valid()==True