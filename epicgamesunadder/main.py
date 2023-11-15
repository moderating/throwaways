import asyncio
from aiohttp import ClientSession

URL = "https://launcher.store.epicgames.com/graphql"

async def run():
    async with ClientSession() as client:
        async with client.post(
            url=URL,
            headers=HEADERS,
            json={
                "operationName": "friends",
                "variables": {"displayNames": False},
                "query": "query friends($displayNames: Boolean) {\n  Friends {\n    summary(displayNames: $displayNames) {\n      friends {\n        account {\n          id\n          displayName\n          externalAuths {\n            type\n            externalAuthId\n            externalAuthIdType\n            externalDisplayName\n            authIds {\n              id\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      incoming {\n        account {\n          id\n          displayName\n          externalAuths {\n            type\n            externalAuthId\n            externalAuthIdType\n            externalDisplayName\n            authIds {\n              id\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      outgoing {\n        account {\n          id\n          displayName\n          externalAuths {\n            type\n            externalAuthId\n            externalAuthIdType\n            externalDisplayName\n            authIds {\n              id\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      blocklist {\n        account {\n          id\n          displayName\n          externalAuths {\n            type\n            externalAuthId\n            externalAuthIdType\n            externalDisplayName\n            authIds {\n              id\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        ) as bruh:
            print(bruh.status)
            friends_dict = (await bruh.json())["data"]["Friends"]["summary"]["friends"]
            for friend in friends_dict:
                async with client.post(
                    url=URL,
                    headers=HEADERS,
                    json={
                        "operationName": "deleteFriend",
                        "variables": {"friendId": friend["account"][0]["id"]},
                        "query": "mutation deleteFriend($friendId: String!) {\n  Friends {\n    deleteFriend(friendToDelete: $friendId) {\n      success\n      __typename\n    }\n    __typename\n  }\n}\n",
                    },
                ) as bruh2:
                    print(bruh2.status)

if __name__ == "__main__":
    TOKEN = input("Token: ")
    SID = input("Session id: ")
    HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Cookie": f"EPIC_BEARER_TOKEN={TOKEN}; EPIC_SSO=Marker; EPIC_LOCALE_COOKIE=en-US; _epicSID={SID}; cma={TOKEN}",
        "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/14.2.4-22208432+++Portal+Release-Live UnrealEngine/4.23.0-22208432+++Portal+Release-Live Chrome/90.0.4430.212 Safari/537.36",
        "X-EPIC-CORRELATION-ID": "77784667-c583-4ea3-8774-8c2b9f5b6b12",
        "X-Epic-Agent": "epic-social",
        "accept": "*/*",
        "apollographql-client-name": "overlay",
        "apollographql-client-version": "1.0",
        "content-type": "application/json",
        "sec-ch-ua": '"Chromium";v="90"',
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://launcher.store.epicgames.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://launcher.store.epicgames.com/en-US/",
    }
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run())
