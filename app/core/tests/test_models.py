"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model # pega o model que esta difinido para a aplicação, assim se mudarmos, ja testa o atualizado


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password)) #confere a senha dessa forma pois ele é armazenada no formato hash