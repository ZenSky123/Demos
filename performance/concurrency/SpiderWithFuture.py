from concurrent import futures

from util import get_image, save_image, main

MAX_WORKERS = 15


def download_one(page):
    image = get_image(page)
    save_image(image, '{page:03}.jpg'.format(page=page))
    return page


def download_many(page_number):
    workers = min(MAX_WORKERS, page_number)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, range(1, page_number + 1))
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
