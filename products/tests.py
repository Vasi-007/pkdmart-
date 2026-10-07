from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AdminSiteTests(TestCase):
	def test_superuser_can_open_admin_site(self):
		admin_user = User.objects.create_superuser(
			username='siteadmin',
			password='PKD-Mart-Admin-2026!',
		)
		self.client.force_login(admin_user)

		response = self.client.get(reverse('admin:index'))

		self.assertEqual(response.status_code, 200)
