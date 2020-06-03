from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class user_profile_manager(BaseUserManager):
    """Manager for user profiles"""

    def creat_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def creat_super_user(self, email, name, password):
        """Create a new super user"""
        super_user = self.creat_user(email, name, password)
        super_user.is_superuser = True
        super_user.is_stuff = True
        super_user.save(using=self._db)

        return super_user


class user_profile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = user_profile_manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        return self.email
    