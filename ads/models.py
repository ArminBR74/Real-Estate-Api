from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
# Create your models here.
class Ads(models.Model):
    title = models.CharField(_('title'),max_length=150)
    caption = models.TextField(_('caption')) 
    image = models.ImageField(_('image'), upload_to='images/ads')
    created_at = models.DateTimeField(default=now,verbose_name= _('date created'))
    is_public = models.BooleanField(default=True,
                                    help_text=_('public ads will be displayed'),
                                    verbose_name=_('is piblic'))
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,
                                  related_name='%(class)s', on_delete=models.CASCADE,
                                  verbose_name=_('publisher'))
    
    class Meta:
        ordering = ('-created_at',)
        get_latest_by = 'created_at'
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')

        def __str__(self) -> str:
            return self.title
