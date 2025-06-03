# Dread Campaign Generator

Generate complete campaign materials for the Dread tabletop roleplaying game using LangChain and LangGraph. Creates detailed campaign settings, character questions, and scenario outlines from your prompts.

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

The generator creates a comprehensive campaign document including:

- Detailed Scenario Summary
- Character Roles & Questionnaires
  - 6 distinct character roles
  - Custom questionnaires for each role
- Three-Act Structure
  - Introduction and setup
  - Rising tension and conflicts
  - Climax and consequences
- NPCs and Events
  - Key non-player characters
  - Triggered events and their impacts
- Ending Possibilities
  - Multiple resolution paths
  - Survival and tragic outcomes
- Game Master Tips
  - Tension management
  - Pacing guidance
  - Tower pull suggestions

## Technical Details

- Uses Google's Gemini Pro model (gemini-2.5-flash-preview-05-20)
- Implements LangGraph for structured campaign generation
- Temperature: 0.7 for balanced creativity
- Docker: Python 3.11 slim, non-root user, volume mounted
- Output: Markdown format

## Example

Check out `dread_campaign_example.md` for a sample generated campaign. 