from django_hosts import patterns,host
from django.conf import settings
host_patterns = patterns('',
    host('api','markets.apiurls',name='api'),
    host('www',settings.ROOT_URLCONF,name='www'),
    # host('beta',settings.ROOT_URLCONF,name='www'),
    # host('help',settings.ROOT_URLCONF,name='www'),
)
