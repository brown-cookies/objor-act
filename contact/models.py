from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} from {self.full_name} - {self.email}"
