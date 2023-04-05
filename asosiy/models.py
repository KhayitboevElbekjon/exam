from django.contrib.auth.models import User
from django.db import models
class Suv(models.Model):
    brend=models.CharField(max_length=50)
    narx=models.IntegerField()
    litr=models.IntegerField()
    batafsil=models.CharField(max_length=500)

class Mijoz(models.Model):
    ism=models.CharField(max_length=25)
    tel=models.CharField(max_length=13)
    manzil=models.CharField(max_length=200)
    qarz=models.IntegerField()
    user_fk=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
class Admin(models.Model):
    ism=models.CharField(max_length=25)
    yosh=models.IntegerField()
    ish_vaqti=models.IntegerField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class Haydovchi(models.Model):
    ism=models.CharField(max_length=25)
    tel=models.CharField(max_length=13)
    kiritilgan_sana=models.DateField()
class Buyurtma(models.Model):
    suv_fk=models.ForeignKey(Suv,on_delete=models.CASCADE)
    buyurtma_vaqti=models.DateTimeField()
    mijoz_fk=models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    miqdor=models.CharField(max_length=25)
    umumiy_narx=models.IntegerField()
    admin_fk=models.ForeignKey(Admin,on_delete=models.CASCADE)
    haydovchi_fk=models.ForeignKey(Haydovchi,on_delete=models.CASCADE)