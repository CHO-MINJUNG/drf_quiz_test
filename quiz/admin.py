from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz)
# 이것을 통해 관리자 페이지에서 퀴즈 목록 관리 가능