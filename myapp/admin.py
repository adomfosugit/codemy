from django.contrib import admin

# Register your models here.
from .models import Bakery
from .models import Bridal_Fan
from .models import Dowry_Wrapping
from .models import Boquet
from .models import Souvenirs
admin.site.register(Bakery)
admin.site.register(Bridal_Fan)
admin.site.register(Dowry_Wrapping)
admin.site.register(Boquet)
admin.site.register(Souvenirs)