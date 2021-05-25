from django.db import models
import uuid
# Create your models here.
class Uuuid(models.Model):
    pub_date = models.DateTimeField('date published')
    uuid_char = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)