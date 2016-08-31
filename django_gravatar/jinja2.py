from django.utils.html import escape

from jinja2 import Markup
from jinja2.ext import Extension

from .helpers import GRAVATAR_DEFAULT_SIZE, get_gravatar_profile_url, get_gravatar_url


def gravatar_url(user_or_email, size=GRAVATAR_DEFAULT_SIZE):
    """ Builds a gravatar url from an user or email """
    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email

    try:
        return escape(get_gravatar_url(email=email, size=size))
    except:
        return ''


def gravatar(user_or_email, size=GRAVATAR_DEFAULT_SIZE, alt_text='', css_class='gravatar'):
    """ Builds an gravatar <img> tag from an user or email """
    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email

    try:
        url = escape(get_gravatar_url(email=email, size=size))
    except:
        return ''

    return Markup(
        '<img class="{css_class}" src="{src}" width="{width}"'
        ' height="{height}" alt="{alt}" />'.format(
            css_class=css_class, src=url, width=size, height=size, alt=alt_text
        )
    )


def gravatar_profile_url(user_or_email):
    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email

    try:
        return get_gravatar_profile_url(email)
    except:
        return ''


class GravatarExtension(Extension):
    def __init__(self, environment):
        super(GravatarExtension, self).__init__(environment)
        environment.globals['gravatar_profile_url'] = gravatar_profile_url
        environment.globals['gravatar_url'] = gravatar_url
        environment.globals['gravatar'] = gravatar
