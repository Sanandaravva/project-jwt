from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
import uuid
import jwt
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from datetime import datetime, timedelta

from ..mixins import TimeAuditModel

# Create your models here.
# class UserModel(User):
    # token = models.CharField(max_length=64, blank=True)
    # def save(self, *args, **kwargs):
    #     self.token = uuid.uuid4().hex + uuid.uuid4().hex
    #     super(User, self).save(*args, **kwargs)
    # @property
    # def token(self):
    #     token=jwt.encode(
    #         {'id': self.id, 'username': self.username, 'email': self.email, 
    #          'exp': datetime.utcnow() + timedelta(hours=24)},
    #           settings.SECRET_KEY, algorithm='HS256')
    #     return token
