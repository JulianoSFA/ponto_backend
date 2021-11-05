from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager
    """

    def create_user(self, username, email, first_name, last_name, password):
        """
        Create a new user object
        :param username: the username
        :param email: the email
        :param first_name: the user first name
        :param last_name: the user last name
        :param password: the user raw password
        :return: user object
        """
        if not username:
            raise ValueError('User must have an username')
        if not password:
            raise ValueError('User must have an password')
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)

        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        """
        Create a new super user
        :param username: the username
        :param email: the email
        :param first_name: the user first name
        :param last_name: the user last name
        :param password: the user raw password
        :return: user object
        """

        user = self.create_user(username, email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
