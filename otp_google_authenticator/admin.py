from django.contrib import admin
from otp_google_authenticator.models import GADevice

class GADeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~django_otp.plugins.otp_totp.models.TOTPDevice`.
    """
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['base32_key', 'qr_img', 'step', 't0', 'tolerance'],
        }),
        ('State', {
            'fields': ['drift'],
        }),
    ]
    readonly_fields = ('qr_img',)
    raw_id_fields = ['user']

admin.site.register(GADevice, GADeviceAdmin)
