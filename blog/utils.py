import string
from django.utils.text import slugify
import random

from django_comments_xtd.utils import get_user_avatar
# from avatar.templatetags.avatar_tags import avatar_url



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


# def get_avatar_url(comment):
#     ret = None
#     if comment.user is not None:
#         try:
#             return avatar_url(comment.user)
#         except Exception as exc:
#             pass
#     return get_user_avatar(comment)

