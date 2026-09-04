from typing import Literal

from pydantic import BaseModel, Field, model_validator


class SongSpecification(BaseModel):

    title: str = Field(
        description="Título original de la canción"
    )

    genre: str = Field(
        description="Género musical principal"
    )

    mood: str = Field(
        description="Estado emocional de la canción"
    )

    bpm: int = Field(
        description="BPM aproximado de la canción"
    )

    language: str = Field(
        description="Idioma de la letra"
    )

    theme: str = Field(
        description="Tema principal de la canción"
    )

    lyrics: str = Field(
        description="Letra completa y original de la canción"
    )

    style_prompt: str = Field(
        description="Descripción detallada del estilo musical para Suno"
    )

    vocal_gender: Literal[
        "male",
        "female",
        "duet",
        "instrumental"
    ] = Field(
        description="Tipo de voz"
    )

    energy: Literal[
        "low",
        "medium",
        "high",
        "progressive"
    ] = Field(
        description="Nivel de energía"
    )

    @model_validator(mode="after")
    def validate_song(self):

        if self.vocal_gender == "instrumental" and self.lyrics.strip():
            raise ValueError(
                "Una canción instrumental no puede contener letras."
            )

        if (
            self.vocal_gender != "instrumental"
            and not self.lyrics.strip()
        ):
            raise ValueError(
                "Una canción con voz debe contener letras."
            )

        return self