"""
Copyright (c) 2020
This is part of https://fmrchallenge.org

This is free software, released under the Apache License, Version 2.0.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0
"""
from django.test import Client, TestCase


class AnonymousReads(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
