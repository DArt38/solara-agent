from agents.music_agent import MusicAgent


agent = MusicAgent()

song = agent.create_song_specification(
    "Quiero una canción Afro House sensual y emocional "
    "sobre dos personas que se encuentran durante una noche "
    "de verano frente al mar. La canción debe sentirse "
    "romántica, elegante, profunda y bailable."
)

print(song.model_dump_json(indent=2))