from django.db import models 
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an email address')
        
        if not password:
            raise ValueError('User must have a password')
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='Eメールアドレス',
        max_length=255,
        unique=True,
        primary_key=False,
    )
    username = models.CharField(
        verbose_name='ユーザーネーム',
        null=True,
        blank=True,
        unique=True,
        max_length=16,
    )
    # 一意のID。UUID4使用、後からINDEXの方に移動させる サーバー生成時にエラー確認。場所が悪いか？ コメントアウトすると動かせそう。
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.admin
    
    def has_module_perms(self,app_label):
        return self.admin
    
    # @property
    # def is_active(self):
    #     return self.is_active
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff