VERSION = (0, 0, 16)


def get_version():
    """Returns the version as a human-format string."""
    return '.'.join([str(i) for i in VERSION])

__author__ = 'dlancer'
__docformat__ = 'restructuredtext en'
__copyright__ = 'Copyright 2014, dlancer'
__license__ = 'BSD'
__version__ = get_version()
__maintainer__ = 'dlancer'
__email__ = 'dmdpost@gmail.com'
__status__ = 'Development'

# default the contact_form app config (only for Django v1.7+)
default_app_config = 'contact_form.apps.AppConfig'
