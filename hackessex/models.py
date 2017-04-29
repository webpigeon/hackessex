from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField() # Text of the question
    votes = models.SmallIntegerField() # Sum of up/downvotes on the question
    # Do submitter - is it account ID?
    tags = model.ManyToManyField()
    
