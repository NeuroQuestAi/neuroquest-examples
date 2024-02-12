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
                {"name": "Gabriela Ehlert", "essay": os.getenv("NQ_ESSAY")}
            ),
        ) as resp:
            if resp.status == 201:
                print("Analysis created successfully! Check:")
                print(json.dumps(await resp.json(), indent=2))
            else:
                print(f"Analysis failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")


async def create_audio():
    upload_audio = {}

    async with aiohttp.ClientSession() as session:
        audio_filename = os.getenv("NQ_AUDIO")
        loop = asyncio.get_event_loop()
        with open(audio_filename, "rb") as f:
            f_content = await loop.run_in_executor(None, f.read)

        data = aiohttp.FormData()
        data.add_field("file", f_content, filename=audio_filename)

        async with session.post(
            "https://api-power-skills.neuroquest.ai/api/v1/audio/upload",
            data=data,
            headers={"token": os.getenv("NQ_TOKEN")},
        ) as resp:
            if resp.status == 201:
                print("Audio created successfully! Check:")
                upload_audio = await resp.json()
                print(json.dumps(upload_audio, indent=2))
            else:
                print(f"Analysis failed! Status code: {resp.status}")
                print(f"API response: {await resp.text()}")

    if upload_audio.get("code", 0) == 201:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api-power-skills.neuroquest.ai/api/v1/predict/create",
                headers={
                    "Content-Type": "application/json",
                    "token": os.getenv("NQ_TOKEN"),
                },
                data=json.dumps(
                    {
                        "name": "Audio-Mono",
                        "audio": upload_audio["data"]["audio"],
                        "lang": os.getenv("NQ_AUDIO_LANG"),
                    }
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
    parser.add_argument("--create", action="store_true", help="Create an analysis")
    parser.add_argument(
        "--audio", action="store_true", help="Create an analysis based on audio"
    )

    args = parser.parse_args()

    if args.login:
        await login()
    elif args.logout:
        await logout()
    elif args.create:
        await create()
    elif args.audio:
        await create_audio()
    else:
        print("No options provided. Use --login, --logout or --create or --audio")


if __name__ == "__main__":
    if (
        not os.getenv("NQ_USER")
        or not os.getenv("NQ_PASSWORD")
        or not os.getenv("NQ_TOKEN")
        or not os.getenv("NQ_ESSAY")
        or not os.getenv("NQ_AUDIO")
        or not os.getenv("NQ_AUDIO_LANG")
    ):
        print(
            "Environment variables not defined! Check: NQ_USER | NQ_PASSWORD | NQ_TOKEN | NQ_ESSAY | NQ_AUDIO | NQ_AUDIO_LANG"
        )
    else:
        asyncio.run(main())
