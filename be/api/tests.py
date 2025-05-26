from django.test import TestCase
from api.models import User, Order
from django.urls import reverse

# Create your tests here.
class UserOrderTestCase(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="test1")
        self.user2 = User.objects.create_user(username="user2", password="test2")

        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user2)
        Order.objects.create(user=self.user2)

    def test_authenticated_user(self):
        def subtest_user1():
            self.client.force_login(self.user1)
            response1 = self.client.get(reverse("user-orders", kwargs={"user_pk": self.user1.pk}))
            response2 = self.client.get(reverse("user-orders", kwargs={"user_pk": self.user2.pk}))

            user1_orders = response1.json()
            user2_orders = response2.json()

            self.assertEqual(response1.status_code, 200)    
            self.assertEqual(response2.status_code, 200)

            self.assertTrue(all([ order['user']['id'] == self.user1.id for order in user1_orders ]))
            self.assertTrue(all([ order['user']['id'] == self.user2.id for order in user2_orders ]))

            print("test user 1 successfully")

        def subtest_user2():
            self.client.force_login(self.user2)
            response1 = self.client.get(reverse("user-orders", kwargs={"user_pk": self.user1.pk}))
            response2 = self.client.get(reverse("user-orders", kwargs={"user_pk": self.user2.pk}))

            user1_orders = response1.json()
            user2_orders = response2.json()

            self.assertEqual(response1.status_code, 200)    
            self.assertEqual(response2.status_code, 200)

            self.assertTrue(all([ order['user']['id'] == self.user1.id for order in user1_orders ]))
            self.assertTrue(all([ order['user']['id'] == self.user2.id for order in user2_orders ]))

            print("test user 2 successfully")

        subtest_user1()
        subtest_user2()

    def test_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse("user-orders", kwargs={"user_pk": self.user1.pk}))

        self.assertTrue(response.status_code != 200)
        self.assertEqual(response.status_code, 403)

        print("Test unauthenticated user successfully✅")