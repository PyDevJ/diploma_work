from django.contrib.auth.models import (
    BaseUserManager
)
# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту


class UserManager(BaseUserManager):
    """
    Функция создания пользователя — в нее мы передаем обязательные поля
    """
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Функция создания суперпользователя — с ее помощью создается админинстратор
        это можно сделать с помощью команды createsuperuser
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role="admin"
        )
        user.save(using=self._db)

        return user
