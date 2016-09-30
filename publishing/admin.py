from django.contrib import admin

from publishing.models import PublishingProfile, PublishingRegion, PublishingLanguage


class PublishingProfileAdmin(admin.ModelAdmin):
    pass


class PublishingRegionAdmin(admin.ModelAdmin):
    pass


class PublishingLanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublishingProfile, PublishingProfileAdmin)
admin.site.register(PublishingRegion, PublishingRegionAdmin)
admin.site.register(PublishingLanguage, PublishingLanguageAdmin)