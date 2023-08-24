import asyncio,httpx,random

async def download_url(url,id):
    print("Downloading : %d : %s" % (id,url))
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    await asyncio.sleep(id)
    print("URL : %d downloaded" % id)

    return response.json()["alt"]

async def main():
    data = await asyncio.gather(
        download_url(f"https://idnes.cz/{random.randint(0, 600)}/info.0.json",0)
        # download_url(f"https://xkcd.com/{random.randint(0, 600)}/info.0.json",1),
        # download_url(f"https://xkcd.com/{random.randint(0, 600)}/info.0.json",0)
    )

    print(data)


asyncio.run(main())