from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.Textfield()

    def __str__(self):
        return f"This is an Author named {self.name} with the following details on bio {self.bio}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"This a post with title {self.title} by {self.author}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"This comment was for the post {self.post} at {self.created_at}"
