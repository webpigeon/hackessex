import json
from django.conf import settings
from django.db import models
from channels import Group

class Room(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField(blank=True, null=True)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def websocket_group(self):
        return Group("room-%s" % self.pk)

    def send_notification(self, question):
        notification = {
            "pk": question.pk,
            "body": question.text,
            "votes": question.votes
        }
        self.websocket_group.send(
            {"text": json.dumps(notification)}
        )

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField() # Text of the question
    votes = models.SmallIntegerField(default=0) # Sum of up/downvotes on the question
    # Do submitter - is it account ID?
    # tags = model.ManyToManyField() For now just use category instead
    category = models.CharField(max_length=255) # Just one category for now
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL)
    room = models.ForeignKey(Room, null=True)
    hide_id = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('home', kwargs={"room": self.room.pk})
    
    def save(self, *args, **kwargs):
        result = super(Question, self).save(*args, **kwargs)
        self.room.send_notification(self)
        return result

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
        return reverse('home', kwargs={"room": self.question.room.pk})

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-votes"]

