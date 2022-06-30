from django.contrib import admin
from About_Me.models import User, CommentsOfOthersModel, Education, WorkSamples, \
    ContactModel, JobTitles, Skill, Experiences, Description, WorkSampleCategory, Certificate, Visit, \
    CertificateCategory, \
    WorkSampleGallery


# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'is_active']
    list_editable = ['is_active']


admin.site.register(User, AdminUser)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(CertificateCategory)
admin.site.register(CommentsOfOthersModel)
admin.site.register(Education)
admin.site.register(WorkSamples)
admin.site.register(WorkSampleGallery)
admin.site.register(WorkSampleCategory)
admin.site.register(ContactModel)
admin.site.register(JobTitles)
admin.site.register(Experiences)
admin.site.register(Description)
admin.site.register(Visit)
