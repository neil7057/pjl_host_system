from django.test import TestCase

from products.models import Product, Category


class TestBagViews(TestCase):
    """
    Bag Views Tests
    """

    def setUp(self):

        self.categoryTest = Category.objects.create(
            name="Clearance",
            friendly_name="clearance",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Oreo Cola",
            description="4 pack",
            has_sizes=False,
            price=8.99
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="Old Cap",
            description="old stock baseball cap",
            price=4,
            has_sizes=False
        )

    def test_bag_page(self):
        """ Test bag view """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        """ Test can add a product to the bag """

        response = self.client.post(
            f'/bag/add/{str(self.productTest.id)}/',
            {'quantity': 3, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.productTest.id)], 3)
        self.assertRedirects(response, '/bag/')

    def test_update_bag(self):
        """ Test can update a product in bag """

        response = self.client.post(
            f'/bag/add/{str(self.productTest.id)}/',
            {'quantity': 2, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.productTest.id)], 2)
        self.assertIn('bag', self.client.session)
        self.assertRedirects(response, '/bag/')

        response = self.client.post(
            f'/bag/adjust/{str(self.productTest.id)}/',
            {'quantity': 3, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.productTest.id)], 3)
        self.assertIn('bag', self.client.session)

    def test_remove_product_from_bag(self):

        self.client.post(
            f'/bag/add/{str(self.productTest.id)}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
        )
        bag_before = self.client.session['bag']
        self.assertIn(f'{self.productTest.id}', bag_before)

        self.client.post(f'/bag/remove/{str(self.productTest.id)}/')
        bag_after = self.client.session['bag']
        self.assertNotIn(f'{self.productTest.id}', bag_after)
        