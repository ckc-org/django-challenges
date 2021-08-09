import random
import string
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse
from tests.utils import CkcAPITestCase

from challenge.models import Company


User = get_user_model()


def generate_random_string(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


class ChallengeTests(CkcAPITestCase):
    def test_users_endpoint_has_reasonable_query_count(self):

        for quantity in [10, 100]:
            User.objects.all().delete()
            Company.objects.all().delete()
            for _ in range(quantity * 3):
                company = Company.objects.create(
                    name=generate_random_string(15),
                    assets_value=Decimal(round(random.random() * (10 ** 7), 2)),
                    liabilities_value=Decimal(round(random.random() * (10 ** 7) * 0.5, 2)),
                )

            for _ in range(quantity):
                user = User.objects.create_user(f'{generate_random_string(15)}@user.com', 'test')
                user.companies.set(random.sample(list(Company.objects.filter(owner__isnull=True)), 3))

            with self.assertNumQueries(1):
                resp = self.client.get(reverse('user-list'))
                data = resp.json()
                assert all([user['net_worth'] != 0 for user in data])
