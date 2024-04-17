import uuid
from django.db import models
from phone.models import Phone


class ClientPrivatPerson(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    ICO = models.CharField(max_length=10, blank=True, null=True)
    DIC = models.CharField(max_length=10, blank=True, null=True)

    email = models.EmailField()
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class ClientLegalPerson(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    ICO = models.CharField(max_length=10, blank=True, null=True)
    DIC = models.CharField(max_length=10, blank=True, null=True)
    VAT_payer = models.BooleanField(default=False)
    email = models.EmailField()
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
