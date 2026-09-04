def build_correction_prompt(validation_error: str) -> str:
    return f"""
Your previous song specification failed validation.

VALIDATION ERROR:
{validation_error}

Generate a completely corrected SongSpecification.

CRITICAL CORRECTIONS:

1. LYRICS

- If lyrics are too short, generate complete lyrics.
- Lyrics must contain at least 200 characters.
- Lyrics must contain meaningful content.
- Lyrics must contain multiple song sections.

Use:

[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Bridge]
[Final Chorus]
[Outro]

Never put production instructions inside lyrics.

Never write:

"(distorted synths)"
"(drums)"
"(bass)"
"(instrumental)"

or any other production direction inside lyrics.

2. STYLE PROMPT

- Maximum 1000 characters.
- Contains ONLY musical production information.
- Do NOT include lyrics.
- Do NOT write "Style Prompt".
- Do NOT use labels such as:
  "Energy:"
  "Vocals:"
  "Instrumental:"
  "vocal_gender:"

3. VOCALS

The user did NOT explicitly request an instrumental song.

Therefore:

- NEVER use vocal_gender="instrumental"
  unless the user's original request explicitly asks for
  an instrumental track or no vocals.

If vocal_gender is:

male
female
duet

then lyrics MUST contain complete lyrics.

If vocal_gender is instrumental:

lyrics MUST be empty.

4. LANGUAGE

Lyrics must match the requested language.

5. FINAL CHECK

Correct every validation error before returning the result.

Return ONLY valid JSON matching the SongSpecification schema.
"""