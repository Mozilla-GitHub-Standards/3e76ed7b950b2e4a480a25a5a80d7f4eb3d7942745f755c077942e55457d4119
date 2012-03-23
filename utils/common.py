import ConfigParser
import urllib2, httplib
import os

HTTP_EXCEPTIONS = (urllib2.HTTPError, urllib2.URLError, httplib.BadStatusLine)

def get_configuration(conf_file):
    # load configuration
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    cfg = {}
    for section in config.sections():
        for item in config.items(section):
            if section != 'defaults':
                key = '%s_%s' % (section, item[0])
            else:
                key = item[0]
            cfg[key] = item[1]
    return cfg

def get_base_dir(path):
    return os.path.abspath(os.path.dirname(os.path.realpath(path)))

def in_ldap_group(email, group):
    """
    Checks ldap if either email or the bz_email are a member of the group.
    """
    bz_email = ldap.get_bz_email(email)
    return ldap.is_member_of_group(email, group) \
            or (bz_email and ldap.is_member_of_group(bz_email, group))

