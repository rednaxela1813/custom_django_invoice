from django.db import models
from clients.models import ClientPrivatPerson, ClientLegalPerson
from products.models import Product
import uuid
from service.models import Service


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order_number = models.CharField(max_length=255)
    client_privat_person = models.ForeignKey(ClientPrivatPerson, on_delete=models.CASCADE, null=True, blank=True)
    client_legal_person = models.ForeignKey(ClientLegalPerson, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.uuid}"
