import re
from models.song import SongSpecification

class SongQualityValidator:

    MIN_LYRICS_LENGTH = 200
    MAX_STYLE_PROMPT_LENGTH = 1000

    @classmethod
    def validate(cls, song: SongSpecification) -> list[str]:

        errors = []

        cls._validate_lyrics(song, errors)
        cls._validate_style_prompt(song, errors)
        cls._validate_vocal_consistency(song, errors)
        cls._validate_bpm(song, errors)

        return errors
    @classmethod
    def _validate_lyrics(
        cls,
        song: SongSpecification,
        errors: list[str]
    ):

        lyrics = song.lyrics.strip()

        if song.vocal_gender == "instrumental":

            if lyrics:
                errors.append(
                    "Instrumental song must have empty lyrics."
                )

            return

        if len(lyrics) < cls.MIN_LYRICS_LENGTH:

            errors.append(
                f"Lyrics are too short. "
                f"Minimum length is {cls.MIN_LYRICS_LENGTH} characters."
            )

        # Una canción vocal debe tener varias secciones.
        required_sections = [
            "[Verse 1]",
            "[Chorus]",
            "[Verse 2]"
        ]

        missing_sections = [
            section
            for section in required_sections
            if section.lower() not in lyrics.lower()
        ]

        if missing_sections:

            errors.append(
                "Lyrics are missing required song sections: "
                + ", ".join(missing_sections)
            )

        forbidden_patterns = [
            r"style prompt",
            r"production quality",
            r"bpm:",
            r"bass:",
            r"synths:",
            r"percussion:",
            r"drums:",
            r"distorted synths",
            r"industrial percussion",
        ]

        for pattern in forbidden_patterns:

            if re.search(pattern, lyrics, re.IGNORECASE):

                errors.append(
                    f"Lyrics contain production instructions: '{pattern}'"
                )
  
    @classmethod
    def _validate_style_prompt(
        cls,
        song: SongSpecification,
        errors: list[str]
    ):

        style = song.style_prompt.strip()

        if not style:

            errors.append(
                "Style prompt cannot be empty."
            )

        if len(style) > cls.MAX_STYLE_PROMPT_LENGTH:

            errors.append(
                "Style prompt exceeds 1000 characters."
            )

        if "style prompt" in style.lower():

            errors.append(
                "Style prompt contains the phrase 'Style Prompt'."
            )

    @classmethod
    def _validate_vocal_consistency(
        cls,
        song: SongSpecification,
        errors: list[str]
    ):

        if song.vocal_gender == "instrumental":

            if song.lyrics.strip():

                errors.append(
                    "Instrumental song must have empty lyrics."
                )

        else:

            if not song.lyrics.strip():

                errors.append(
                    "Vocal song must contain lyrics."
                )

    @classmethod
    def _validate_bpm(
        cls,
        song: SongSpecification,
        errors: list[str]
    ):

        if song.bpm < 60 or song.bpm > 220:

            errors.append(
                f"BPM {song.bpm} is outside the allowed range."
            )