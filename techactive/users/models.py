from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name + " " + self.l_name
