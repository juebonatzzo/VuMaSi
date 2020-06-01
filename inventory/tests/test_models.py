from django.test import TestCase
from inventory.models import Asset


class AssetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        Asset.objects.create(part='a',
                             vendor='microsoft',
                             product='internetexplorer',
                             version='8',
                             update='any_update',
                             edition='std',
                             language='English',
                             sw_edition='any_swe',
                             target_sw='any_tsw',
                             target_hw='any_thw',
                             other='other')

    def setUp(self):
        """Set up non-modified objects run before each test"""
        pass

    def test_asset_as_cpe23(self):
        """Asset cpe23 is correctly generated"""
        cpe23 = 'cpe:2.3:a:microsoft:internetexplorer:8:any_update:std:English:any_swe:any_tsw:any_thw:other'

        # lion = Animal.objects.get(name="lion")
        # cat = Animal.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
