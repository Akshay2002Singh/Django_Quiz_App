from django.contrib import admin
from home.models import contact,quiz_question,quiz_submissions,admin_access

# Register your models here.
admin.site.register(contact)
admin.site.register(quiz_question)
admin.site.register(quiz_submissions)
admin.site.register(admin_access)