from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    # post text
    post_text = models.TextField(
        verbose_name="Post Text", blank=False, null=False)

    # post author
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='author')

    # post created at
    created_date = models.DateTimeField(auto_now_add=True)

    # Updated at
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post_text} bt {self.post_author}"

    class Meta:
        ordering = ['-created_date']
        db_table = "Post"

    # implement get_absolute_url
    # TODO


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comments")

    comment = models.TextField(verbose_name="Comment", blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        ordering = ['-created_at', ]
        db_table = "Post Comment"


class LikeModel(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes")

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes")

    liked_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked {self.post}"

    class Meta:
        # Unique Constraints Between Post ----> User
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'], name="one like for one user in each post"
            )
        ]

        # table name
        db_table = "Post Like"
