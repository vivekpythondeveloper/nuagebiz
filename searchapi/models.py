from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

# Create your models here.
class SearchApi(models.Model):
    product_id                  = models.IntegerField(null=False,blank=False, default=None)
    product_name                = models.CharField(max_length=255, null=False, blank=False)
    product_search_name         = models.CharField(max_length=255, null=False, blank=False,default='')
    image_file                  = models.ImageField(upload_to='images/')
    image_url                   = models.URLField(null=False, blank=False)
    price                       = models.DecimalField(max_digits=20, decimal_places=2, default=0)


    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}", File(img_temp))
        super(SearchApi, self).save(*args, **kwargs)