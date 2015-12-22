from __future__ import unicode_literals
from django.db import models

from django_otp.models import Device
from django_otp.plugins.otp_totp.models import TOTPDevice

from base64 import b32encode, b32decode
from urllib import quote_plus
from os import urandom

def base32_validator(key):
    if not len(key) % 16 == 0: return False
    return True

def get_default_key():
    return b32encode(urandom(10))

class GADevice(TOTPDevice):

    base32_key = models.CharField(max_length=16,
                           validators=[base32_validator],
                           default=get_default_key,
                           help_text=u'A base32 encoded string of up to 10 characters')

    @property
    def bin_key(self):
        return b32decode(self.base32_key)

    def qr_img(self):
        if not self.pk: # not saved to db
            return "First insert your key and save"
        return u'<img src="{}" />'.format(self.get_qr_url())
    qr_img.short_description = "QR Code"
    qr_img.allow_tags = True

    def get_qr_url(self):

        otpauth = "otpauth://totp/{}@{}?secret={}".format(self.user, "oipa", self.base32_key)
        get_args = "chs=200x200&chld=M%7C0&cht=qr&chl="
        qr_url = "https://chart.googleapis.com/chart?" + get_args + quote_plus(otpauth)

        return qr_url

    class Meta(TOTPDevice.Meta):
        verbose_name = "Google Authenticator Device"

