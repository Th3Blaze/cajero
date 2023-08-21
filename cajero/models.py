from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class UsuarioBanco(models.Model):
    id_usuario=models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)],
        unique=True
    )
    nombre=models.CharField(max_length=250)
    contrasenha=models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)]
    )
    def __str__(self):
        return self.nombre

class CuentaBancaria(models.Model):
    id_usuario=models.ForeignKey(UsuarioBanco,on_delete=models.CASCADE)
    id_nro_cta=models.DecimalField(max_digits=15,decimal_places=0)
    balance=models.DecimalField(max_digits=100, decimal_places=2)
    sesion=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_nro_cta)
    
class GiroCuenta(models.Model):
    monto_giro=models.DecimalField(max_digits=10,decimal_places=2)
    id_nro_cta=models.ForeignKey(CuentaBancaria,on_delete=models.CASCADE)
    id_transaccion=models.CharField(max_length=30,default='')

    def __str__(self):
        return str(self.monto_giro)

class DepositoCuenta(models.Model):
    monto_deposito=models.DecimalField(max_digits=10,decimal_places=2)
    id_nro_cta=models.ForeignKey(CuentaBancaria,on_delete=models.CASCADE)
    id_transaccion=models.CharField(max_length=30,default='')

    def __str__(self):
        return str(self.monto_deposito)