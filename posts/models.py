# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Posts(models.Model):
	title =models.CharField(max_length=200)
	body =models.TextField()
	updated_date=models.DateTimeField()
	image =models.ImageField(upload_to='images/')

