from django.db import models

# Create your models here.





from django.db import models

class TenantModel(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    # Your fields here

class Tenant1Model(TenantModel):
    class Meta:
        db_table = 'tenant1_model'

class Tenant2Model(TenantModel):
    class Meta:
        db_table = 'tenant2_model'



# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class MyUser(AbstractUser):
#     bio = models.TextField(blank=True,null=True)
#     profile_pic = models.ImageField(blank=True,null=True)

#     def __str__(self):
#         return self.username





