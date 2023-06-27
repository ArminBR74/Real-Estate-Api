from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseUserManager(models.Manager):
    @classmethod
    def normalize_username(cls, username):
        username = username or ''
        if len(username)< 4 :
            raise ValueError(_('username must have at least 4 char'))
        return username.lower()
    
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError('you must choosen a username')
        
        user = self.model(
            username = self.normalize_username(username)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        
        user = self.create_user(
            username=username,
            password=password
            )
        user.is_admin = True
        user.save(using=self._db)
        return user