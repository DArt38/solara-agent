from agents.music_agent import MusicAgent
from llm.ollama_provider import OllamaProvider


llm = OllamaProvider(
    model="qwen3.6:latest"
)

agent = MusicAgent(llm=llm)

song = agent.create_song_specification(
    "Crea una canción de Drum and Bass oscura y cinematográfica con voz de mujer"
    "sobre una ciudad futurista durante una persecución nocturna. "
    "Debe ser intensa, agresiva y electrónica."
)

print(song.model_dump_json(indent=2))