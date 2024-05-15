from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
# Create your models here.

class CustomerManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided')
        if not password:
            raise ValueError('Password is not provided')
        
        customer = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )

        customer.set_password(password)
        customer.save(using=self.db)
        return customer
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    

class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=200)
    date_registered = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'