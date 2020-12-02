"""
Copyright (c) 2020
This is part of https://fmrchallenge.org

This is free software, released under the Apache License, Version 2.0.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0
"""
from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
