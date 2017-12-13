# coding: utf-8
# AskJANcode.py allows you to get JANcode from Amazon via Product Advertising API.
import urllib
import urllib.request
import time
import hashlib, hmac
import base64
import os
import re

class Amazon:

    _AMAZON_URL = "http://ecs.amazonaws.jp/onca/xml"
    _ACCESS_KEY = os.environ['AMA_ACCESS_KEY']
    _SECRET_KEY = os.environ['AMA_SECRET_KEY']
    _ASSOCIATE_TAG = os.environ['AMA_ASSOCIATE_TAG']
    _VERSION = "2011-08-01"

    def _url(self, Asin):
        req_params = ({'Service': "AWSECommerceService"
                          , 'AWSAccessKeyId': self._ACCESS_KEY
                          , 'AssociateTag' : self._ASSOCIATE_TAG
                          , 'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
                          , 'Version':  self._VERSION
                          , 'Operation': "ItemLookup"
                          , 'ResponseGroup': "ItemAttributes"
                          , 'ItemId': Asin
        })
        upr = urllib.parse.urlparse(self._AMAZON_URL)
        req_param_str = '&'.join((k + "=" + urllib.parse.quote(
                        req_params[k].encode('utf-8'),safe='~'))
                        for k in sorted(req_params.keys()))
        signature = urllib.parse.quote(base64.b64encode(hmac.new(
                                  self._SECRET_KEY.encode('ascii')
                                  , ("GET\n" + upr.netloc + "\n" + upr.path + "\n"
                                     + req_param_str).encode('ascii')
                                  , hashlib.sha256).digest()))
        url = self._AMAZON_URL + "?" + req_param_str + "&Signature=" + signature
        return url

a = Amazon()
with urllib.request.urlopen(a._url("B071D1JPFM")) as res:
    texts = res.read().decode("utf-8")
for partial_html in re.findall(r'<EAN>.*?</EAN>', texts, re.DOTALL):
    print(partial_html.replace('<EAN>', '').replace('</EAN>', ''))