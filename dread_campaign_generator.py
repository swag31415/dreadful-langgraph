from typing import TypedDict, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph
from dotenv import load_dotenv
import os
import operator

# Load environment variables
load_dotenv()

# Define the state type for our graph
class CampaignState(TypedDict):
    campaign_prompt: str
    scenario_summary: str
    character_roles: Annotated[str, operator.add]
    act_structure: Annotated[str, operator.add]
    npcs_and_events: Annotated[str, operator.add]
    ending_possibilities: Annotated[str, operator.add]
    gm_tips: Annotated[str, operator.add]
    final_output: str

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-preview-05-20",
    temperature=0.7
)

def generate_scenario_summary(state: CampaignState) -> CampaignState:
    """Generate a detailed scenario summary."""
    print("Generating scenario summary...")
    prompt = f"""Based on the following campaign prompt, create a detailed scenario summary for a Dread RPG campaign:
    
    {state['campaign_prompt']}
    
    Create a 1-2 paragraph summary that:
    1. Sets the tone and genre
    2. Establishes the core conflict
    3. Creates an immediate sense of dread
    4. Hints at the horror elements without revealing too much
    
    Format it in a clear, engaging way that would hook players immediately."""
    
    response = llm.invoke(prompt)
    state['scenario_summary'] = response.content
    print("✓ Scenario summary generated")
    return state

def generate_character_roles(state: CampaignState) -> CampaignState:
    """Generate character roles and questionnaires."""
    print("Generating character roles and questionnaires...")
    prompt = f"""Based on this Dread campaign scenario:
    
    {state['scenario_summary']}
    
    Generate 6 distinct character roles, each with their own custom questionnaire. For each role:
    1. Create a brief role description (1-2 sentences)
    2. Generate 13-15 questions following this structure:
       - 1-2 factual/setup questions
       - 3-5 skill/background questions
       - 3-5 personality/motivation questions
       - 2-3 horror hooks/secrets
    
    Format each role and its questions in a clear, structured way.
    All questions should invite storytelling and create tension."""
    
    response = llm.invoke(prompt)
    print("✓ Character roles and questionnaires generated")
    return {"character_roles": response.content}

def generate_act_structure(state: CampaignState) -> CampaignState:
    """Generate the three-act structure."""
    print("Generating act structure...")
    prompt = f"""Based on this Dread campaign scenario:
    
    {state['scenario_summary']}
    
    Create a detailed three-act structure that includes:
    
    Act I: Introduction
    - Setting and atmosphere details
    - Character dynamics to establish
    - Initial tension points
    - When to introduce first tower pulls
    
    Act II: Rising Tension
    - Inciting incident details
    - Key tower pull moments
    - Secret reveals and character conflicts
    - Ways to increase distrust
    
    Act III: Climax & Consequences
    - Critical tower pull moments
    - Moral dilemmas to present
    - Character death/disappearance triggers
    - Ways to maintain tension
    
    Format each act in a clear, structured way with specific moments and triggers."""
    
    response = llm.invoke(prompt)
    print("✓ Act structure generated")
    return {"act_structure": response.content}

def generate_npcs_and_events(state: CampaignState) -> CampaignState:
    """Generate NPCs and key events."""
    print("Generating NPCs and events...")
    prompt = f"""Based on this Dread campaign scenario:
    
    {state['scenario_summary']}
    
    Create:
    1. Key NPCs (3-5)
       - Name and brief description
       - Motivation
       - Relationship to players
       - Potential secrets
    
    2. Key Events (5-7)
       - Trigger conditions
       - Description
       - Impact on story
       - Tower pull opportunities
    
    Format in a clear, structured way that's easy to reference during play."""
    
    response = llm.invoke(prompt)
    print("✓ NPCs and events generated")
    return {"npcs_and_events": response.content}

def generate_ending_possibilities(state: CampaignState) -> CampaignState:
    """Generate possible endings."""
    print("Generating ending possibilities...")
    prompt = f"""Based on this Dread campaign scenario:
    
    {state['scenario_summary']}
    
    Create 3-4 possible endings that:
    1. Feel like natural conclusions to the horror story
    2. Account for different survival scenarios
    3. Include both tragic and ambiguous outcomes
    4. Tie into character secrets and motivations
    
    For each ending, include:
    - Trigger conditions
    - Key moments
    - Final tower pull opportunities
    - Resolution details
    
    Format in a clear, structured way."""
    
    response = llm.invoke(prompt)
    print("✓ Ending possibilities generated")
    return {"ending_possibilities": response.content}

def generate_gm_tips(state: CampaignState) -> CampaignState:
    """Generate specific GM tips for this scenario."""
    print("Generating GM tips...")
    prompt = f"""Based on this Dread campaign scenario:
    
    {state['scenario_summary']}
    
    Create specific GM tips that include:
    1. How to maintain tension
    2. When to slow down time
    3. How to handle player secrets
    4. Ways to adapt to player choices
    5. Specific horror elements to emphasize
    6. How to use the tower effectively
    
    Format as clear, actionable advice."""
    
    response = llm.invoke(prompt)
    print("✓ GM tips generated")
    return {"gm_tips": response.content}

def format_final_output(state: CampaignState) -> CampaignState:
    """Format all the generated content into a final campaign document."""
    print("Formatting final output...")
    final_output = f"""# DREAD CAMPAIGN: {state['campaign_prompt']}

## Scenario Summary
{state['scenario_summary']}

## Character Roles & Questionnaires
{state['character_roles']}

## Act Structure
{state['act_structure']}

## NPCs and Events
{state['npcs_and_events']}

## Ending Possibilities
{state['ending_possibilities']}

## Game Master Tips
{state['gm_tips']}

## Physical Requirements
- Jenga tower
- Character questionnaires (printed)
- Player sheets
- Optional: ambient music, lighting, props
"""
    state['final_output'] = final_output
    print("✓ Final output formatted")
    return state

def create_campaign_graph() -> StateGraph:
    """Create the LangGraph for campaign generation."""
    # Create the graph
    graph = StateGraph(CampaignState)
    
    # Add nodes
    graph.add_node("generate_scenario_summary", generate_scenario_summary)
    graph.add_node("generate_character_roles", generate_character_roles)
    graph.add_node("generate_act_structure", generate_act_structure)
    graph.add_node("generate_npcs_and_events", generate_npcs_and_events)
    graph.add_node("generate_ending_possibilities", generate_ending_possibilities)
    graph.add_node("generate_gm_tips", generate_gm_tips)
    graph.add_node("format_final_output", format_final_output)
    
    # Add edges from scenario summary to all parallel branches
    graph.add_edge("generate_scenario_summary", "generate_character_roles")
    graph.add_edge("generate_scenario_summary", "generate_act_structure")
    graph.add_edge("generate_scenario_summary", "generate_npcs_and_events")
    graph.add_edge("generate_scenario_summary", "generate_ending_possibilities")
    graph.add_edge("generate_scenario_summary", "generate_gm_tips")
    
    # Add edges from all parallel branches to final formatting
    # The reducers in the state definition will handle combining the results
    graph.add_edge("generate_character_roles", "format_final_output")
    graph.add_edge("generate_act_structure", "format_final_output")
    graph.add_edge("generate_npcs_and_events", "format_final_output")
    graph.add_edge("generate_ending_possibilities", "format_final_output")
    graph.add_edge("generate_gm_tips", "format_final_output")
    
    # Set entry point
    graph.set_entry_point("generate_scenario_summary")
    
    return graph

def generate_campaign(campaign_prompt: str) -> str:
    """Generate a complete Dread campaign from a prompt."""
    # Initialize the state
    initial_state = {
        "campaign_prompt": campaign_prompt,
        "scenario_summary": "",
        "character_roles": "",
        "act_structure": "",
        "npcs_and_events": "",
        "ending_possibilities": "",
        "gm_tips": "",
        "final_output": ""
    }
    
    # Create and run the graph
    graph = create_campaign_graph()
    result = graph.compile().invoke(initial_state)
    
    return result['final_output']

if __name__ == "__main__":
    if not os.path.exists("prompt.txt"):
        print("Error: prompt.txt not found. Please create a prompt.txt file with your campaign prompt.")
        exit(1)
    with open("prompt.txt", "r") as f:
        prompt = f.read().strip()
    print("Using campaign prompt from prompt.txt file.")
    campaign = generate_campaign(prompt)
    
    # Save to file
    with open("dread_campaign.md", "w") as f:
        f.write(campaign)
    
    print("Campaign generated and saved to 'dread_campaign.md'") 