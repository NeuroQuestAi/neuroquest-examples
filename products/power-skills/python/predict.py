import argparse
import asyncio
import json
import os

import aiohttp


async def login():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-power-skills.neuroquest.ai/api/v1/auth/login",
            headers={"Content-Type": "application/json"},
            data=json.dumps(
                {"email": os.getenv("NQ_USER"), "password": os.getenv("NQ_PASSWORD")}
            ),
        ) as resp:
            if resp.status == 200:
                print("Login successful! User credential information:")
                print(json.dumps(await resp.json(), indent=2))
            else:
                print(f"Login failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def logout():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api-power-skills.neuroquest.ai/api/v1/auth/logout?email={os.getenv('NQ_USER')}",
            headers={
                "Content-Type": "application/json",
                "token": os.getenv("NQ_TOKEN"),
            },
        ) as resp:
            if resp.status == 200:
                print("Logout successful.")
            else:
                print(f"Logout failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def create():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-power-skills.neuroquest.ai/api/v1/predict/create",
            headers={
                "Content-Type": "application/json",
                "token": os.getenv("NQ_TOKEN"),
            },
            data=json.dumps(
                {"name": "John Green", "essay": os.getenv("NQ_ESSAY")}
            ),
        ) as resp:
            if resp.status == 201:
                print("Analysis created successfully! Check:")
                print(json.dumps(await resp.json(), indent=2))
            else:
                print(f"Analysis failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def main():
    parser = argparse.ArgumentParser(description="Example using the Person-Predict API")

    parser.add_argument("--login", action="store_true", help="Login to the API")
    parser.add_argument("--logout", action="store_true", help="Logout of the API")
    parser.add_argument("--create", action="store_true", help="Create an analysis")

    args = parser.parse_args()

    if args.login:
        await login()
    elif args.logout:
        await logout()
    elif args.create:
        await create()
    else:
        print("No options provided. Use --login, --logout or --create")


if __name__ == "__main__":
    if (
        not os.getenv("NQ_USER")
        or not os.getenv("NQ_PASSWORD")
        or not os.getenv("NQ_TOKEN")
        or not os.getenv("NQ_ESSAY")
    ):
        print("Environment variables not defined! Check: NQ_USER or NQ_PASSWORD or NQ_TOKEN or NQ_ESSAY.")
    else:
        asyncio.run(main())
