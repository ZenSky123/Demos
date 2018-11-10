import os
import time

import requests

BASE_URL = "http://web.cartoonmad.com/e267dk57cd6/3583/001/{page:03}.jpg"

DEST_DIR = 'downloads/'
MAX_PAGE = 15


def save_image(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img*10)


def get_image(page):
    t0 = time.time()
    url = BASE_URL.format(page=page)
    resp = requests.get(url)
    elapsed = time.time() - t0
    print("Download Page{} with {:.2f}s".format(page, elapsed))
    return resp.content


def main(download_many):
    t0 = time.time()
    count = download_many(MAX_PAGE)
    elapsed = time.time() - t0
    print('\n{} images downloaded in {:.2f}s'.format(count, elapsed))
