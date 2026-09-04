from agents.music_agent import SongSpecification
from validators.song_validator import SongQualityValidator


song = SongSpecification(
    title="Test Song",
    genre="Drum and Bass",
    mood="Dark",
    bpm=175,
    language="English",
    theme="Futuristic City",
    lyrics="""
    [Intro]
    Running through the neon streets tonight.
    """,
    style_prompt="Create a dark Drum and Bass track.",
    vocal_gender="male",
    energy="high"
)


errors = SongQualityValidator.validate(song)


if errors:

    print("QUALITY VALIDATION FAILED")

    for error in errors:
        print(f"- {error}")

else:

    print("QUALITY VALIDATION PASSED")