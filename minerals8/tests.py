from django.test import TestCase

from django.urls import reverse

from .models import Mineral
from .views import mineral_list, mineral_detail
# Create your tests here.

class MineralTest(TestCase):
""" test mineral app"""
    def setUp(self):
        self.test_min = Mineral.objects.create(
            name="thisisfake",
            category="not real"
        )

    def test_view_detail(self):
        resp = self.client.get(reverse('detail', args=[self.test_min.pk]))
        self.assertTemplateUsed('minerals/detail.html')

    def create_mineral(self, name="fake"):
        return Mineral.objects.create(name=name)

    def test_mineral_creation(self):
        min = self.create_mineral()
        self.assertTrue(isinstance(min, Mineral))
        self.assertEqual(min.pk, 876)

    def test_view_list(self):
        min = self.create_mineral()
        resp = self.client.get(reverse('list'))
        self.assertTemplateUsed('minerals/list.html')

    def test_database(self):
        min = self.create_mineral()
        data = Mineral.objects.count()
        self.assertEqual(data, 876 )
