from django.conf import settings
from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.TextField() # Text of the question
    votes = models.SmallIntegerField(default=0) # Sum of up/downvotes on the question
    # Do submitter - is it account ID?
    # tags = model.ManyToManyField() For now just use category instead
    category = models.CharField(max_length=255) # Just one category for now
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL)
    hide_id = models.BooleanField(default=True)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('home')


    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-votes"]

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    votes = models.SmallIntegerField(default=0)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('home')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-votes"]

