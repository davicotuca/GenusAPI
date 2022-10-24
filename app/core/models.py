"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Parametros(models.Model):
    """Parametros in the system."""
    pop_size = models.IntegerField(null=True)
    generations = models.IntegerField()
    pop_bottleneck = models.IntegerField(null=True)
    generation_bottleneck = models.IntegerField(null=True)
    p_inicial = models.DecimalField(max_digits=11, decimal_places=10)
    WAA = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    WAa = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Waa = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    s = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    h = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    u = models.DecimalField(max_digits=3, decimal_places=2, null=True)


class Grupo(models.Model):
    """Grupo object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Resultados(models.Model):
    """Resultado object."""
    resultado = JSONField()


class Simulacao(models.Model):
    """Grupo object."""
    resultado = models.ForeignKey(
        Resultados,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    parametros = models.ForeignKey(
        Parametros,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class GrupoSimulacao(models.Model):
    """Grupo object."""
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE,
    )
    simulacao = models.ForeignKey(
        Simulacao,
        on_delete=models.CASCADE,
    )
