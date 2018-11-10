from util import get_image, save_image, main


def download_many(page_number):
    for page in range(1, page_number + 1):
        image = get_image(page)
        save_image(image, '{page:03}.jpg'.format(page=page))
    return page_number


if __name__ == '__main__':
    main(download_many)
