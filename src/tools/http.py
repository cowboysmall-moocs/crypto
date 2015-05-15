import urllib2


def make_request(target, key, value):
    try:

        urllib2.urlopen(urllib2.Request('%s?%s=%s' % (target, key, urllib2.quote(value.encode('hex')))))

    except urllib2.HTTPError, e:          

        return e.code == 404

