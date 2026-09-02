# SOLARA Agent 🎵

SOLARA is an AI-powered music creation agent that transforms natural-language ideas into structured song specifications and prepares them for music generation through the Suno API.

The project is being developed as an MVP focused on learning and applying AI Engineering concepts such as LLM integration, structured outputs, prompt engineering, API integration, and agent architecture.

## Current Architecture

```text
User Idea
    │
    ▼
MusicAgent
    │
    ▼
Llama 3 (Local)
    │
    ▼
Ollama
    │
    ▼
SongSpecification
    │
    ▼
SunoClient
    │
    ▼
Suno API
```

## Current Features

* Local Llama 3 inference through Ollama
* Natural language → structured song specification
* Pydantic data validation
* Automatic lyrics generation
* Automatic musical style generation
* Genre, mood, BPM and theme generation
* Vocal gender and energy definition
* Suno API client
* Suno API authentication
* Suno API credit checking
* Suno payload generation

## Example

Input:

```text
Quiero una canción Afro House sensual y emocional
sobre dos personas que se encuentran durante una noche
de verano frente al mar.
```

SOLARA generates a structured specification:

```json
{
  "title": "Mar de Luna",
  "genre": "Afro House",
  "mood": "Romantic, Elegant, Profound, and Danceable",
  "bpm": 123,
  "language": "Spanish",
  "theme": "Summer Night by the Sea",
  "vocal_gender": "Female",
  "energy": "Building and Climaxing"
}
```

It also generates original lyrics and a production style prompt suitable for Suno.

## Tech Stack

* Python
* Ollama
* Llama 3
* Pydantic
* Suno API
* httpx
* python-dotenv

## Project Structure

```text
solara-agent/
│
├── app/
│   ├── agents/
│   │   └── music_agent.py
│   │
│   ├── services/
│   │   └── suno.py
│   │
│   └── main.py
│
├── test_agent.py
├── test_suno.py
├── test_payload.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd solara-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and run Ollama

Make sure Ollama is installed and the required model is available:

```bash
ollama list
```

Example:

```bash
ollama run llama3:latest
```

### 6. Configure environment variables

Create a `.env` file:

```env
SUNO_API_KEY=your_suno_api_key
```

Never commit `.env` to GitHub.

## Testing

Test the local Llama agent:

```bash
python test_agent.py
```

Test the Suno API connection:

```bash
python test_suno.py
```

Test the Suno payload generation:

```bash
python test_payload.py
```

## Roadmap

* [x] Connect Ollama
* [x] Connect Llama 3
* [x] Create MusicAgent
* [x] Create structured SongSpecification
* [x] Integrate Pydantic validation
* [x] Connect Suno API
* [x] Build Suno payload
* [ ] Generate songs through Suno
* [ ] Track Suno generation tasks
* [ ] Retrieve generated audio
* [ ] Add quality validation
* [ ] Create FastAPI interface
* [ ] Add song history
* [ ] Add multiple music styles
* [ ] Improve prompt engineering
* [ ] Evaluate Llama vs Qwen
* [ ] Build production-ready agent architecture

## Learning Goals

This project is also a practical AI Engineering learning project.

The main concepts being explored are:

* LLM applications
* Local LLM inference
* Ollama
* Structured outputs
* Pydantic
* Prompt engineering
* Agent architecture
* API integration
* Validation
* Async programming
* AI application architecture
* Evaluation and experimentation

## Status

🚧 MVP in development.

The current version successfully transforms a natural-language music idea into a structured song specification using a locally running Llama model.
