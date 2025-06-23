# prompt_forge.py

def build_prompt(vision, language, tone, constraints, avoid):
    # Core template
    prompt = f"""Create a {tone.lower()} {language} script that fulfills the following vision:

{vision.strip()}

Requirements:
- Use {language}, and follow best practices.
- Include: {constraints if constraints else 'No additional constraints provided.'}
- Avoid: {avoid if avoid else 'None specified.'}

Ensure the output is clean, well-structured, and production-ready unless otherwise stated.
"""

    return prompt


if __name__ == "__main__":
    print("\n--- Vision-to-Code Prompt Forge ---\n")

    vision = input("What do you want to build? (Vision)\n> ")
    language = input("Preferred language or tech?\n> ")
    tone = input("How should the code behave or feel? (e.g., stealthy, fast, slick)\n> ")
    constraints = input("Any rules, limits, or requirements?\n> ")
    avoid = input("What should it absolutely NOT do?\n> ")

    print("\n--- Generated Prompt ---\n")
    final_prompt = build_prompt(vision, language, tone, constraints, avoid)
    print(final_prompt)
