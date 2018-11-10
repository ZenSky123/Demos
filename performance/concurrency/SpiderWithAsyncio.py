import asyncio
import aiohttp

from util import save_image, main, BASE_URL
import time


async def get_image(page):
    t0 = time.time()
    url = BASE_URL.format(page=page)
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        image = await resp.read()
    elapsed = time.time() - t0
    print("Download Page{} with {:.2f}s".format(page, elapsed))
    return image


async def download_one(page):
    image = await get_image(page)
    save_image(image, "{page:03}.jpg".format(page=page))
    return page


def download_many(page_number):
    loop = asyncio.get_event_loop()
    to_do = [download_one(page) for page in range(1, page_number + 1)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)
