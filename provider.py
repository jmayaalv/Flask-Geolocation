# coding=utf-8
import json
import urllib

KEYS = dict(
        region_name='region',
        zipcode = 'zip_code',
        country_name = 'country',
        city_name = 'city',
        cityName = 'city',
        countryName = 'country',
        countryCode = 'country_code',
        zipCode = 'zip_code',
        timeZone = 'time_zone',
        statusCode = 'status_code',
        ipAddress = 'ip',
        statusMessage = 'status_message',
        regionName = 'region',
    )

def remove_accents(str):
    if str is None:
        return None
    return str.lower().replace(u'á',u'a').replace(u'é',u'e').replace(u'í',u'i').replace(u'ó',u'o').replace(u'ú',u'u').replace(u'ü',u'u')
    
def get_geolocation_data(url, ip, key=None):
    if key:
        return dict(map(lambda (key, value): (KEYS.get(key, key), remove_accents(value)), json.load(urllib.urlopen(url % (key, ip))).items()))
    else:
        return dict(map(lambda (key, value): (KEYS.get(key, key), remove_accents(value)), json.load(urllib.urlopen(url % (ip,))).items()))
        
    
class FreeGeoIP(object):
    """
    Geolocates IP using the JSON API from http://freegeoip.net
    """
    
    
    BASE_URL = 'http://freegeoip.net/json/%s'
    
    def __call__(self, ip, *args, **kwargs):
        return  get_geolocation_data(self.BASE_URL, ip)
        
class IPInfoDB(object):
    """
    Geolocates IP using the JSON API from http://www.ipinfodb.com/
    """
    

    BASE_URL = 'http://api.ipinfodb.com/v3/ip-city?format=json&key=%s&ip=%s'

    def __call__(self, ip, *args, **kwargs):
        return  get_geolocation_data(self.BASE_URL, ip, kwargs['key'])

class HostIP(object):
    """
    Geolocates IP using the JSON API from http://www.hostip.info/
    """


    BASE_URL = 'http://api.hostip.info/get_json.php?format=json&ip=%s'

    def __call__(self, ip, *args, **kwargs):
        return  get_geolocation_data(self.BASE_URL, ip)
        
def test():
    geolocation_providers = ('HostIP','IPInfoDB','FreeGeoIP')
    result = None
    for gl in geolocation_providers:
        result = getattr(__import__('provider'), gl)()('91.192.165.119', key='fea993b0e07e57724e68f5f3ef7a661367f8608e7f012e7d4b1a7b0029bf13e5')
        if result is not None and result['city'] is not None:
            break
    return result