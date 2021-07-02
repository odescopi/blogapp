from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator,XtdCommentModerator
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from django_comments_xtd.models import ContentType,XtdComment
from django.utils import timezone
from blog.utils import unique_slug_generator

# from entries.models import Entry



class PublicManager(models.Manager):
    def published(self):
        return super(PublicManager, self).get_queryset().filter(publish__lte=timezone.now())


# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField()
#
#     def __str__(self):
#         return self.user.username



# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    body = models.TextField('write here')
    publish = models.DateTimeField('publish',auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    objects = PublicManager()
    status = models.CharField(blank=False, max_length=20, choices=STATUS_CHOICES, default='draft')
    approved_comments = models.BooleanField(default=True)
    slug = models.SlugField('slug', unique_for_date='publish',max_length=250,null=True)

    # class Meta:
    #     verbose_name_plural = "posts"

    class Meta:
        # db_table = 'entries_post'
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('Article:post-detail', kwargs={'slug': self.slug})


class PostCommentModerator(XtdCommentModerator):
    email_notification = True
    auto_moderate_field = 'publish'
    moderate_after = 365
    removal_suggestion_notification = True


moderator.register(Post, PostCommentModerator)


@receiver(post_delete, sender=Post)
def delete_comments(sender, instance, **kwargs):
    ct = ContentType.objects.get(app_label="article", model="post")
    XtdComment.objects.filter(content_type=ct, object_pk=instance.id).delete()


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Post)

