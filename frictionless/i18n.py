# (canada fork only): add i18n support
import gettext
import os

i18n_dir = os.path.join(os.path.dirname(__file__), 'i18n')
try:
    real_gettext = gettext.translation('frictionless', i18n_dir).ugettext
except AttributeError:
    real_gettext = gettext.translation('frictionless', i18n_dir).gettext
except IOError:
    real_gettext = lambda x:x


def _(text):
    global real_gettext
    return real_gettext(text)


def set_language(lang):
    """Use a different language for errors than the default

    # Raises
        IOError: translation for lang is not found.
    """
    global real_gettext
    try:
        real_gettext = gettext.translation('frictionless', i18n_dir, [lang]).ugettext
    except AttributeError:
        real_gettext = gettext.translation('frictionless', i18n_dir, [lang]).gettext
    except IOError:
        real_gettext = lambda x:x
