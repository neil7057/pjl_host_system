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
            name="Clearance",
            friendly_name="clearance",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="white hoodie",
            description="Oreo themed white hoodie",
            price=13.99,
            has_sizes=True,
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="coca cola x 3",
            description="oreo floured cola drink - 3 cans",
            has_sizes=False,
            price=10,
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
        self.assertEqual(self.categoryTest.name, 'Clearance')

    def test_category_friendly_name(self):
        """ Test the category name """
        self.assertEqual(self.categoryTest.friendly_name, 'clearance')

    def test_product_name(self):
        """ Test the product name """
        self.assertEqual(self.productTest.name, 'white hoodie')

    def test_product_description(self):
        """ Test the product description """
        self.assertEqual(
            self.productTest.description,
            'Oreo themed white hoodie')

    def test_product_price(self):
        """ Test the product price """
        self.assertEqual(self.productTest.price, 13.99)

    def test_product_size(self):
        """ Test if product has sizes """
        self.assertEqual(self.productTest.has_sizes, True)

    def test_product_name2(self):
        """ Test the product name """
        self.assertEqual(self.productTest2.name, 'coca cola x 3')

    def test_product_description2(self):
        """ Test the product description """
        self.assertEqual(
            self.productTest2.description,
            'oreo floured cola drink - 3 cans')

    def test_product_size2(self):
        """ Test if product has sizes """
        self.assertEqual(self.productTest2.has_sizes, False)

    def test_product_price2(self):
        """ Test product price """
        self.assertEqual(self.productTest2.price, 10)
