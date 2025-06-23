# creator_forge.py

def build_prompt(project_type, vision, medium, tone, features, constraints, avoid):
    prompt = f"""You are to assist in creating a {project_type.lower()} using the following creative vision:

"{vision.strip()}"

Target medium/platform: {medium if medium else 'Not specified'}
Desired tone/energy: {tone if tone else 'Neutral/default'}
Key features or elements to include:
- {features if features else 'No specific features provided.'}

Constraints or rules:
- {constraints if constraints else 'None'}

What to avoid:
- {avoid if avoid else 'Nothing specific to avoid'}

Please generate a structured, thoughtful starting point or execution plan for this {project_type.lower()}, respecting the tone and platform context. Respond as if the user is about to begin building this right away.
"""
    return prompt


if __name__ == "__main__":
    print("\n--- Creator Forge: Broad Prompt Generator ---\n")

    project_type = input("What do you want to make? (e.g., agent, story, app, song, podcast, etc.)\n> ")
    vision = input("Describe your creative vision or idea\n> ")
    medium = input("Preferred medium/platform? (e.g., web, mobile, novel, voice, AR, etc.)\n> ")
    tone = input("What tone or vibe should it have? (e.g., funny, serious, dark, hopeful)\n> ")
    features = input("What features, elements, or themes should it include?\n> ")
    constraints = input("Any rules, limits, or technical/logistical constraints?\n> ")
    avoid = input("What should it definitely NOT include or do?\n> ")

    print("\n--- Generated Creative Prompt ---\n")
    final_prompt = build_prompt(project_type, vision, medium, tone, features, constraints, avoid)
    print(final_prompt)
