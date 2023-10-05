from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class RawMaterials(models.Model):
    name = models.CharField(verbose_name='Тип сырья')


class QualityIndicators(models.Model):
    raw_materials = models.ForeignKey(RawMaterials, on_delete=models.CASCADE)
    iron_content = models.FloatField(verbose_name='Содержание железа')
    silicon_content = models.FloatField(verbose_name='Содержание кремния')
    aluminum_content = models.FloatField(verbose_name='Содержание алюминия')
    calcium_content = models.FloatField(verbose_name='Содержание кальция')
    sulfur_content = models.FloatField(verbose_name='Содержание серы')
    upload_date = models.DateField(verbose_name='Дата загрузки данных')
