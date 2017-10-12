from urllib.parse import urlencode
from .json_request import json_request

ACCESS_TOKEN = '%s|%s' % ('160427621214246', 'f6972339db4bc061e62699cc36987674')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.8'
LIMIT_REQUEST = 50


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_name_to_id(pagename):
    url = fb_gen_url(
        node=pagename,
        access_token = ACCESS_TOKEN
        )

    json_result = json_request(url=url)
    return json_result.get('id')


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node = fb_name_to_id(pagename) + '/posts',
        fields = 'id,message,link,name,type,shares,created_time,reactions.limit(0).summary(true),\
            comments.limit(0).summary(true)',
        since = since,
        until = until,
        limit = LIMIT_REQUEST,
        access_token = ACCESS_TOKEN
        )

    while True:
        json_result = json_request(url=url)
        posts = json_result.get('data')
        paging = json_result.get('paging')

        yield posts

        url = paging.get('next')
        if url is None:
            break