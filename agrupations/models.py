from django.db import models

class Client(models.Model):
    ci = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} {self.las|t_name}'
    
class Proyect(models.Model):
    name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=2)
    proyect = models.ForeignKey('Proyect', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class House(models.Model):
    nomenclature = models.CharField(max_length=4)
    proyect = models.ForeignKey('Proyect', on_delete=models.CASCADE)
    block = models.ForeignKey('Block', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Agrupation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    balance_types = models.ManyToManyField(BalanceType, through='AgrupationBalanceType')
    d_id = models.CharField(max_length=6, editable=False, unique=True)
    sale_value = models.PositiveIntegerField()

    def progress(self):
        total_states = ProcessState.objects.count()
        completed_states = self.statestatus_set.filter(Q(status="COMPLETADO") | Q(status = "NO APLICA")).count()
        return (completed_states / total_states) * 100

    def __str__(self):
        return f"{self.client.name} - {self.house}"
    
class BalanceType(models.Model):
    name = models.CharField(max_length=20)
    amount = models.PositiveIntegerField(max_digits=10)

    def __str__(self):
        return self.name
    
class AgrupationBalanceType(models.Model):
    agrupation = models.ForeignKey(Agrupation, on_delete=models.CASCADE)
    balance_type = models.ForeignKey(BalanceType, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(max_digits=10)

    def __str__(self):
        return f"{self.agrupation} - {self.balance_type.name}"
    
class ProcessState(models.Model):
    STATE_CHOICES = [
        ("VENDIDA", "Vendida"),
        ("FINANCIAMIENTO", "Financiamiento"),
        ("CUOTA INICIAL", "Cuota Inicial"),
        ("FIDUCIA", "Fiducia"),
        ("AVALUO", "Avaluo"),
        ("POSTULACION SUBSIDIO", "Postulacion Subsidio"),
        ("ASIGNACION SUBSIDIO", "Asignacion Subsidio"),
        ("RATIFICACION FINANCIAMIENTO", "Ratificacion Financiamiento"),
        ("REVISION FIDUCIA", "Revision Fiducia"),
        ("PAGO DERECHOS NOTARIALES", "Pago Derechos Notariales"),
        ("ESCRITURACION", "Escriturada"),
        ("CASA TERMINADA", "Casa Terminada"),
        ("HIPOTECA DESEMBOLSADA", "Hipoteca Desembolsada"),
        ("CASA ENTREGADA", "Casa Entregada"),
        ("SUBSIDIO DESEMBOLSADO", "Subsidio Desembolsado")
    ]
    name = models.CharField(max_length=50, choices=STATE_CHOICES)

    def __str__(self):
        return self.name
        
class StateStatus(models.Model):
    STATUS_CHOICES = [
        ("PENDIENTE", "Pendiente"),
        ("EN PROCESO", "En Proceso"),
        ("COMPLETADO", "Completado"),
        ("NO APLICA", "No Aplica"),
    ]
    agrupation = models.ForeignKey(Agrupation, on_delete=models.CASCADE)
    process_state = models.ForeignKey(ProcessState, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.agrupation} - {self.process_state} - {self.status}"