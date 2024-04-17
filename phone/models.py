from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Phone(models.Model):
    CHOICE_PHONE_TYPE = (
        ("mobile", "Mobile"),
        ("home", "Home"),
        ("work", "Work"),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = PhoneNumberField(unique=True)
    type = models.CharField(max_length=10, choices=CHOICE_PHONE_TYPE, blank=True, null=True)
    owner_privat = models.ForeignKey("clients.ClientPrivatPerson", on_delete=models.CASCADE, blank=True, null=True)
    owner_legal = models.ForeignKey("clients.ClientLegalPerson", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    old_number = models.BooleanField(default=False)


    def __str__(self):
        return str(self.phone)
