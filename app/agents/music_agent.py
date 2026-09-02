from ollama import chat
from pydantic import BaseModel, Field


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
        description="Tema principal de la canción, escrito en el mismo idioma de la canción"
    )

    lyrics: str = Field(
        description="Letra completa y original de la canción"
    )

    style_prompt: str = Field(
        description="Descripción detallada del estilo musical para Suno"
    )
    vocal_gender: str = Field(
        description="Tipo de voz: male, female, duet or instrumental"
    )
    energy: str = Field(
        description="Nivel de energía: low, medium, high or progressive"
    )


class MusicAgent:

    def __init__(self):
        self.model = "llama3:latest"

    def create_song_specification(
        self,
        idea: str
    ) -> SongSpecification:

        system_prompt = """
You are SOLARA, an expert AI music producer, songwriter and creative director.

Your task is to transform the user's musical idea into a professional song specification for Suno.

The user's concept is the primary creative direction.

Do not introduce unrelated themes, symbolism,
locations or concepts unless they naturally support
the user's idea.

Preserve the emotional intent of the user's request.

IMPORTANT RULES:

1. LANGUAGE
- Detect the requested language from the user's idea.
- The "language" field must contain the language used for the lyrics.
- If language is Spanish, ALL lyrics must be written in natural Spanish.
- If language is English, ALL lyrics must be written in natural English.
- Never mix languages unless the user explicitly requests it.

2. LYRICS
- Write completely original lyrics.
- Do not copy existing songs, artists or lyrics.
- The "lyrics" field must contain ONLY the lyrics.
- Never include explanations.
- Never include "Style Prompt" inside lyrics.
- Never include production instructions inside lyrics.
- Use clear song sections such as:

[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Bridge]
[Final Chorus]
[Outro]

- Make the lyrics natural, singable and emotionally coherent.
- Avoid repetitive filler.
- Check grammar and spelling before returning the result.

3. MUSIC
Create a coherent musical concept.

Consider:
- genre
- subgenre
- BPM
- rhythm
- percussion
- bass
- synths
- pads
- melodies
- vocals
- atmosphere
- energy
- dynamics
- song structure

4. STYLE PROMPT
The style_prompt is intended to be sent directly to Suno.

Create a detailed professional production prompt.

Include:
- genre and subgenre
- BPM
- rhythm
- percussion
- bass
- melodic elements
- synths
- vocals
- vocal character
- atmosphere
- emotional tone
- energy
- dynamics
- production quality
- arrangement
- transitions
- climax
- outro

The style_prompt should be detailed and descriptive, ideally close to 1000 characters without exceeding 1000 characters.

Do NOT include lyrics in style_prompt.

5. TITLE
Create a short, memorable and original title.

6. BPM
Choose an appropriate BPM for the genre and mood.

7. QUALITY CONTROL
Before returning the answer, verify:

- lyrics language matches the language field
- lyrics contain no style instructions
- lyrics contain no "Style Prompt"
- lyrics have correct spelling
- style_prompt contains only music production instructions
- style_prompt does not contain lyrics
- title is coherent with the theme
- BPM is appropriate for the genre

Return ONLY the structured data requested by the schema.
"""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": idea
                }
            ],
            format=SongSpecification.model_json_schema()
        )

        content = response.message.content

        return SongSpecification.model_validate_json(content)