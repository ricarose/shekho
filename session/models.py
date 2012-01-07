from django.db import models
from django.contrib.auth.models import User

SESSION_STATUS = (('confirmed', 'Confirmed'),
                    ('unconfirmed', 'Unconfirmed'),
                    ('cancelled', 'Cancelled'))

# Need type ?
class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    facilitator = models.ForeignKey(User, related_name="facilitator")
    status = models.CharField(max_length=20, choices = SESSION_STATUS,\
        default='unconfirmed')
    #location = models.TextField(blank=True)
    #time = models.DateTimeField(blank=True)
    type = models.CharField(max_length=30)
    duration = models.CharField(max_length = 50)
    attendees = models.ManyToManyField(User, null=True, blank=True,\
        related_name="attendees")
        
    def __unicode__(self):
    	return self.title
