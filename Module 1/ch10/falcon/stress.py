# -*- coding: utf-8 -*-
import concurrent.futures
import urllib.request

URLS = ['http://127.0.0.1:8000/quote'] * 2000

def load_url(url, timeout):
    return urllib.request.urlopen(url, timeout=timeout).read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = dict((executor.submit(load_url, url, 60), url)
                         for url in URLS)

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        if future.exception() is not None:
            print('%r generated an exception: %s' % (url,
                                                     future.exception()))
        else:
            print('%r page is %d bytes' % (url, len(future.result())))
            # print(future.result())
