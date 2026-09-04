from ollama import ResponseError
from pydantic import ValidationError

from models.song import SongSpecification
from validators.song_validator import SongQualityValidator
from llm.base import LLMProvider

from prompts.music_system_prompt import SYSTEM_PROMPT
from prompts.music_correction_prompt import build_correction_prompt


class MusicAgent:

    def __init__(self, llm: LLMProvider):
        self.llm = llm

    def create_song_specification(
        self,
        idea: str,
        max_retries: int = 2
    ) -> SongSpecification:

        last_error = None

        for attempt in range(1, max_retries + 1):

            try:

                user_prompt = idea

                if last_error:
                    user_prompt = f"""
                ORIGINAL USER IDEA:
                {idea}

                PREVIOUS VALIDATION ERROR:
                {last_error}

                {build_correction_prompt(last_error)}
                """

                print(
                    f"\nGenerating song specification "
                    f"(attempt {attempt}/{max_retries})..."
                )

                content = self.llm.generate(
                    system_prompt=SYSTEM_PROMPT,
                    user_prompt=user_prompt,
                    response_schema=SongSpecification.model_json_schema()
                )

                song = SongSpecification.model_validate_json(content)

                quality_errors = SongQualityValidator.validate(song)

                if quality_errors:
                    raise ValueError(
                        "Song quality validation failed:\n"
                        + "\n".join(
                            f"- {error}"
                            for error in quality_errors
                        )
                    )

                print(
                    f"Song specification validated successfully "
                    f"on attempt {attempt}."
                )

                return song

            except ValidationError as error:

                last_error = str(error)

                print(
                    f"Validation failed on attempt "
                    f"{attempt}/{max_retries}:"
                )

                print(last_error)

            except ValueError as error:

                last_error = str(error)

                print(
                    f"Quality validation failed on attempt "
                    f"{attempt}/{max_retries}:"
                )

                print(last_error)

            except ResponseError as error:

                last_error = f"Ollama error: {error}"

                print(
                    f"Ollama error on attempt "
                    f"{attempt}/{max_retries}:"
                )

                print(last_error)

        raise RuntimeError(
            "SOLARA could not generate a valid song specification "
            f"after {max_retries} attempts."
        )