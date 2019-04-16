# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Register
from .models import Items
from .models import Order



# Register your models here.
admin.site.register(Register)
admin.site.register(Items)
admin.site.register(Order)

