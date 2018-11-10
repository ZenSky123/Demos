from concurrent import futures

from util import get_image, save_image, main

MAX_WORKERS = 5


def download_one(page):
    image = get_image(page)
    save_image(image, '{page:03}.jpg'.format(page=page))
    return page


def download_many(page_number):
    workers = min(MAX_WORKERS, page_number)
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        for page in range(1, page_number + 1):
            future = executor.submit(download_one, page)
            to_do.append(future)
            print("scheduled for {}: {}".format(page, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print("{} result: {!r}".format(future, res))
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)
