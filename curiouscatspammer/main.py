from asyncio import gather, run, ensure_future, sleep, get_event_loop
from httpx import AsyncClient
from random import choice

class catsex:
    def __init__(self, user: str, content: str, proxies: str) -> None:
        self.user = user
        self.content = content
        self.proxies = open(proxies, "r").read().splitlines() if proxies else False
        self.client = AsyncClient(
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Origin": "https://curiouscat.live/",
                "Referer": f"https://curiouscat.live/{user}",
            },
            verify=False,
        )

    async def send_request(self):
        proxy = choice(self.proxies) if self.proxies else False
        task = await self.client.post(
            url="https://curiouscat.live/api/v2/post/create",
            data={
                "anon": "true",
                "question": self.content,
                "to": self.user,
                "in_response_to": "undefined",
                "_ob": "registerOrSignin2",
            },
            proxies = {
                "http://": f"http://{proxy}",
                "https://": f"https://{proxy}",
            } if proxy else {}
        )
        print(str(task), task.text)
        if "error" in task.json():
            if task.json()["error"] == "ratelimited":
                await sleep(1.0838018)
                await self.send_request()

    async def start_fuck_meow(self):
        await gather(*[ensure_future(self.send_request()) for _ in range(int(input("amount: "))])


if __name__ == "__main__":
    cat = catsex(input("username: ").replace("https://curiouscat.live/", "").replace("curiouscat.live/", "").replace("/", ""), input("content: "), input("proxy path (blank to not use proxys): "))
    x = get_event_loop()
    x.run_until_complete(cat.start_fuck_meow())
