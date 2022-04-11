from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError
from tes2.models import Transaccion

class Command(BaseCommand):
    help = "Actualiza el estatus de las transacciones en base a la fecha"

    # def inicia_transacciones(self, *args, **kwargs):
    #     transaccciones = Transaccion.objects.filter(estatus = "4")
    #     for tr in transaccciones:
    #         self.stdout.write(self.style.SUCCESS(tr.id_transaccion))

    def handle(self, *args, **kwargs):
        try:
            transaccciones = Transaccion.objects.all()
            if transaccciones.count() == 0:
                self.stdout.write(self.style.ERROR("No HAY!"))
            for tr in transaccciones:
                self.stdout.write(self.style.SUCCESS(tr.id_transaccion))
        except tr.DoesNotExist:
            self.stdout.write(self.style.ERROR("No hay Transacciones"))
            return
        
        self.stdout.write(self.style.SUCCESS("Transacciones impresas"))
        return
        


