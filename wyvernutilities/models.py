from django.db import models
from enum import Enum

# Create your models here.


class Status(Enum):

    inactive = 0
    active = 1
