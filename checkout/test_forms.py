from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Order Form Tests
    """

    def test_not_required_fields(self):
        """ Test form is valid with empty non-required fields """
        form = OrderForm(
            {
                'full_name': 'OreoTest',
                'email': 'testoreo@test.com',
                'phone_number': '12345678',
                'street_address1': 'sesame street',
                'street_address2': '',
                'town_or_city': 'Toytown',
                'county': 'sussex',
                'postcode': 'Yah',
                'country': 'GB',
            }
            )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only the fields
        'full_name', 'email', 'phone_number',
        'street_address1', 'street_address2',
        'town_or_city', 'postcode', 'country',
        'county'
        are displayed on form
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county')
        )
