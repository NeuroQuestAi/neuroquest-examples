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
                print("Please reset the environment variable NQ_TOKEN with the new token.")
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


async def create_by_text():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-text",
            headers={
                "Content-Type": "application/json",
                "token": os.getenv("NQ_TOKEN"),
            },
            data=json.dumps(
                {"name": "Gabriela Ehlert", "essay": os.getenv("NQ_ESSAY")}
            ),
        ) as resp:
            if resp.status == 201:
                print("Analysis created successfully! Check:")
                print(json.dumps(await resp.json(), indent=2))
            else:
                print(f"Analysis failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def create_by_audio():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-audio",
            headers={
                "Content-Type": "application/json",
                "token": os.getenv("NQ_TOKEN"),
            },
            data=json.dumps(
                {"name": "Gabriela Ehlert", "document_id": os.getenv("NQ_AUDIO_DOC_ID")}
            ),
        ) as resp:
            if resp.status == 201:
                print("Analysis created successfully! Check:")
                print(json.dumps(await resp.json(), indent=2))
            else:
                print(f"Analysis failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def main():
    parser = argparse.ArgumentParser(description="Example using the Power-Skills API")

    parser.add_argument("--login", action="store_true", help="Login to the API")
    parser.add_argument("--logout", action="store_true", help="Logout of the API")
    parser.add_argument(
        "--create-by-text", action="store_true", help="Create an analysis by text"
    )
    parser.add_argument(
        "--create-by-audio", action="store_true", help="Create an analysis by audio"
    )

    args = parser.parse_args()

    if args.login:
        await login()
    elif args.logout:
        await logout()
    elif args.create_by_text:
        await create_by_text()
    elif args.create_by_audio:
        await create_by_audio()
    else:
        print(
            "No options provided. Use --login, --logout or --create-by-text or --create-by-audio"
        )


if __name__ == "__main__":
    if (
        not os.getenv("NQ_USER")
        or not os.getenv("NQ_PASSWORD")
        or not os.getenv("NQ_TOKEN")
        or not os.getenv("NQ_ESSAY")
        or not os.getenv("NQ_AUDIO_DOC_ID")
    ):
        print(
            "Environment variables not defined! Check: NQ_USER | NQ_PASSWORD | NQ_TOKEN | NQ_ESSAY | NQ_AUDIO_DOC_ID"
        )
    else:
        asyncio.run(main())
