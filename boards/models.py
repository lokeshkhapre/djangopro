# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
	name = models.CharField(max_length=30,unique=True)
	description = models.CharField(max_length=100)

class Topic(models.Model):
	subject = models.CharField(max_length=200)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='Topics')
	starter = models.ForeignKey(User ,related_name='Topics')

class Post(models.Model):
	message = models.TextField(max_length=1000)
	topic = models.ForeignKey(Topic, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts')
	updated_by = models.ForeignKey(User, null=True, related_name='+')




# Create your models here.
