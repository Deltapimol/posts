from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=500)
    text = models.TextField()
    post_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    #commentator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    commentator = models.CharField(blank=False,null=False,max_length = 50)
    comment = models.CharField(blank=False,null=False,max_length=500)
    comment_datetime = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.comment

class Reply(models.Model):
    
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    reply = models.CharField(blank=False,null=False,max_length=500)
    reply_datetime = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.reply

class ReplyToReply(models.Model):
    
    reply = models.ForeignKey(Reply, on_delete = models.CASCADE)
    reply_respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    reply_reply = models.CharField(blank=False,null=False,max_length = 500)
    reply_datetime = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.reply_reply  

class Contact(models.Model):
    
    GeneralInformation = 'GI'
    I_am_a_liver_patient = 'IAALP'
    I_am_a_friend_family_of_a_liver_patient = 'IAAFFOALP'
    I_am_a_living_donor =  'IAALD'
    Information_regarding_organ_registration = 'IROR'
    Other = 'Other'
    
    reasons =  ((GeneralInformation, 'General Information'),
                (I_am_a_liver_patient, 'I am a liver patient'),
                (I_am_a_friend_family_of_a_liver_patient, 'I am a friend/family of a liver patient'),
                (I_am_a_living_donor, 'I am a living donor'),
                (Information_regarding_organ_registration, 'Information regarding organ registration'),
                (Other, 'Other'))
    
    first_name = models.CharField(blank=False, null=False,max_length=20, error_messages={'blank':'First name field cant be blank.'})
    last_name = models.CharField(blank=False,null=False,max_length=20)
    email = models.EmailField(blank=False,null=False)
    contact_no = models.IntegerField(blank=False,null=False)
    location = models.CharField(blank=False,null=False,max_length=50) 
    reason_for_contact = models.CharField(max_length=10, choices=reasons,default='GI')
    datetime = models.TimeField(null=True)
    
    def __str__(self):
        return self.first_name
       
     
    
    


    
    
