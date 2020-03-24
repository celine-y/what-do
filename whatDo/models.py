from django.db import models
from django.conf import settings

# Create your views here.

class Activity(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    #activity name
    name = models.CharField(max_length=255, null=False)
    #description
    description = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

class Effort(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    activity = models.ForeignKey(Activity,
        on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)

    media = models.ImageField(
        upload_to='effort',
        blank=True
    )

    caption = models.CharField(max_length=255, blank=True, default='')
