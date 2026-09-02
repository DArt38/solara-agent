import asyncio

from services.suno import SunoClient


async def main():
    suno = SunoClient()

    credits = await suno.get_credits()
    print("Credits:", credits)

    payload = {
        "prompt": "A beautiful emotional Afro House song about a sunset in Ibiza",
        "customMode": False,
        "instrumental": False,
        "model": "V5"
    }

    # Cuando tengamos créditos:
    # result = await suno.generate_song(payload)
    # print(result)


if __name__ == "__main__":
    asyncio.run(main())