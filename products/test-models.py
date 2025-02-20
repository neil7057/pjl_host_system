from django.test import TestCase
from products.models import Product, Category


class TestProductsModels(TestCase):
    """
    Products Models Tests
    """

    def setUp(self):
        """
        Creates test objects for Products app
        """

        self.categoryTest = Category.objects.create(
            name="biscuits",
            friendly_name="Biscuits",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Oreo twin pack",
            description="Twin pack of oreo cookies",
            price=3.99,
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="starwars multipack",
            description="star wars 49 pack",
            price=22.99,
        )

    def test_category_string_method(self):
        """ Tests the string method on the category model """
        category = Category(name='Category Name')
        self.assertEqual(str(category), category.name)

    def test_category_string_method_friendly_name(self):
        """ Tests the string method on the category model's friendly name """
        category = Category(friendly_name='Category Friendly Name')
        self.assertEqual(str(category.friendly_name), category.friendly_name)

    def test_product_string_method(self):
        """ Tests the string method on the product model """
        product = Product(name='Product Name')
        self.assertEqual(str(product), product.name)

    def test_category_name(self):
        """ Test the category name """
        self.assertEqual(self.categoryTest.name, 'Biscuits')

    def test_category_friendly_name(self):
        """ Test the category name """
        self.assertEqual(self.categoryTest.friendly_name, 'biscuits')

    def test_product_name(self):
        """ Test the product name """
        self.assertEqual(self.productTest.name, 'Oreo twin pack')

    def test_product_description(self):
        """ Test the product description """
        self.assertEqual(
            self.productTest.description,
            'Twin pack of oreo cookies'
        )

    def test_product_price(self):
        """ Test the product price """
        self.assertEqual(self.productTest.price, 3.99)
