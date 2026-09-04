from agents.music_agent import MusicAgent
from app.services.suno_client import SunoClient


def main():

    agent = MusicAgent()
    suno = SunoClient()

    song = agent.create_song_specification(
        "Quiero una canción Afro House "
        "sobre dos personas que se encuentran durante una noche "
        "de verano frente al mar. La canción debe sentirse "
        "emocionante, elegante, profunda y bailable."
    )

    payload = suno.build_song_payload(song)

    print("\nSONG SPECIFICATION:\n")
    print(song.model_dump_json(indent=2))

    print("\nSUNO PAYLOAD:\n")
    print(payload)


if __name__ == "__main__":
    main()