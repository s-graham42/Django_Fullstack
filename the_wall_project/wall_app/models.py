from django.db import models
from login.models import User

# Create Validators here.
class MsgManager(models.Manager):
    def msg_validator(self, postData):
        errors = {}
        if len(postData['new_message']) < 5:
            errors['msg_short'] = "Message too short.  Please enter at least 5 characters."
        if len(postData['new_message']) > 1000:
            errors['msg_long'] = "Message too long.  Please keep it to less than 1000 characters."
        return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['new_comment']) < 5:
            errors['comment_short'] = "Message too short.  Please enter at least 5 characters."
        if len(postData['new_comment']) > 1000:
            errors['comment_long'] = "Message too long.  Please keep it to less than 1000 characters."
        return errors


# Create your models here.
class Msg(models.Model):
    msg = models.TextField()
    user = models.ForeignKey(User, related_name="owned_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MsgManager()
    # msg_comments = list of comments associated with this message.

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="owned_comments", on_delete=models.CASCADE)
    msg = models.ForeignKey(Msg, related_name="msg_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()