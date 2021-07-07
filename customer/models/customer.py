from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    phone_number = models.CharField(max_length=30, default=None, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='customer_qr_code/', blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        data = [self.name, self.phone_number, self.email]
        user_qr_code = qrcode.make(data=data)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(user_qr_code)
        fname = f"{self.name}-{self.phone_number}" + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super(Customer, self).save(force_insert=False, force_update=False, using=None,
                                   update_fields=None)
