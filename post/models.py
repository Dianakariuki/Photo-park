from email.mime import image
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ["-pk"]

    def save_post(self):
        '''
        Method to save our images
        '''
        self.save()

    def delete_post(self):
        '''
        Method to delete our images
        '''
        self.delete()


    def __str__(self):
        return self.title
    
class Comment(models.Models):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments

    def __str__(self):
        return self.comment
    class Meta:
        ordering=["-pk"]


    
