# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Jobs(models.Model):
	image = models.ImageFiled(upload_to='images/')
	summery =models.CharFiled(max_length=200)
	