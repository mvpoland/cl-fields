import datetime
from decimal import Decimal

from django.db import models
from django.test import TestCase

from .fields import JSONField


class TestModel(models.Model):
    json = JSONField()


class JSONFieldTest(TestCase):
    '''JSONField Wrapper Tests'''

    def test_json_field(self):
        '''Test saving a JSON object in our JSONField'''
        data = [
            u'this',
            u'is',
            u'an obj',
            1,
            Decimal('3.1415'),
            {'key1': 'value 1',
             'key 2': 2,
             'key 3': Decimal(5)}
        ]
        obj = TestModel.objects.create(json=data)
        new_data = TestModel.objects.get(id=obj.id).json
        self.assertTrue(len(new_data), len(data))
        self.assertTrue(new_data[:4], data[:4])
        # JSON can't represent decimals, so test that separately
        self.assertTrue(str(new_data[5]), str(data[5]))

    def test_modify(self):
        '''Test modifying a JSON object in our JSONField'''
        data_1 = {'a': 1, 'b': 2}
        data_2 = {'a': 3, 'b': 4}
        obj = TestModel.objects.create(json=data_1)
        self.failUnlessEqual(obj.json, data_1)
        obj.json = data_2
        self.failUnlessEqual(obj.json, data_2)
        obj.save()
        self.failUnlessEqual(obj.json, data_2)
