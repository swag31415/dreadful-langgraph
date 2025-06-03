# Dread Campaign Generator

Generate complete campaign materials for the Dread tabletop roleplaying game using LangChain and LangGraph. Creates campaign settings, character questions, and scenario outlines from your prompts.

## Quick Start

1. Clone the repository
2. Create `.env` with your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
3. Run with Docker Compose:
   ```bash
   docker compose up
   ```

## Alternative Installation

### Local Setup
```bash
pip install -r requirements.txt
python dread_campaign_generator.py
```

### Direct Docker
```bash
docker build -t dread-campaign-generator .
docker run --env-file .env -v $(pwd):/app dread-campaign-generator
```

## Usage

1. Run the application
2. Enter your campaign prompt when prompted, e.g.:
   ```
   A horror campaign set in an abandoned amusement park where the rides come to life at night, and the park's former owner's ghost seeks to trap visitors forever.
   ```
3. Find your generated campaign in `dread_campaign.md`

## Output Format

- Campaign Setting
- Character Creation Questions
- Scenario Outline
- Game Master Notes

## Technical Notes

- Uses Google's Gemini Pro model
- Temperature: 0.7 for balanced creativity
- Docker: Python 3.11 slim, non-root user, volume mounted
- Output: Markdown format 