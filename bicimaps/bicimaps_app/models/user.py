from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

# Clase que permite redefinir la manera como se crea un usuario en Django
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Se debe proveer un email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password( password )
        user.save( using = self._db )
        print("Creando usuario")
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    has_bike = models.BooleanField(default=True)
    birth_date = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # def get_short_name(self):
    #     return self.email

    # def get_full_name(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True
    