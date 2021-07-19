import random
import string

from django.contrib.auth import get_user_model
from django.urls import reverse
from tests.utils import CkcAPITestCase

from challenge.models import Company, Address


User = get_user_model()


def generate_random_string(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


class ChallengeTests(CkcAPITestCase):
    def test_users_endpoint_has_reasonable_query_count(self):

        for quantity in [100, 1000]:
            for _ in range(quantity):
                company = Company.objects.create(name=generate_random_string(15))
                company.addresses.set([Address.objects.create(street_addr=generate_random_string(15)) for __ in range(quantity)])

            for _ in range(quantity):
                user = User.objects.create_user(f'{generate_random_string(15)}@user.com', 'test')
                user.companies.set(random.sample(list(Company.objects.all()), quantity // 10))

            with self.assertNumQueries(3):
                resp = self.client.get(reverse('user-list'))
