import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import webbrowser
import pyautogui
import time

# Web URLs for each AI tool
ai_urls = {
    "ChatGPT": "https://chat.openai.com",
    "Claude": "https://claude.ai",
    "CoPilot": "https://copilot.microsoft.com",
    "Grok": "https://x.ai",
    "Custom": ""  # Will be asked
}

def open_or_focus_web_ai(tool, prompt_text):
    url = ai_urls.get(tool, "")
    if tool == "Custom" or not url:
        url = simpledialog.askstring("Custom AI URL", "Enter the URL of the AI interface:")
        if not url:
            return

    # Open the browser to the AI tool
    webbrowser.open_new_tab(url)

    # Wait and inject after a delay
    root.after(5000, lambda: inject_to_browser(prompt_text))  # Wait 5s for browser to load

def inject_to_browser(prompt_text):
    time.sleep(0.5)
    pyautogui.write(prompt_text, interval=0.01)
    pyautogui.press("enter")


# Generate final prompt
def generate_prompt():
    vision = vision_input.get("1.0", tk.END).strip()
    style = style_var.get()
    tone = tone_input.get()
    features = features_input.get("1.0", tk.END).strip()
    constraints = constraints_input.get("1.0", tk.END).strip()
    avoid = avoid_input.get("1.0", tk.END).strip()
    lang = code_lang_var.get()

    if not vision or not style:
        messagebox.showwarning("Missing Info", "Vision and Style are required.")
        return

    lang_line = f"Preferred language: {lang}" if style == "Code" and lang else ""

    prompt = f"""You are to generate a {style.lower()} based on the following vision:

"{vision}"

{lang_line}
Desired tone: {tone if tone else 'default/neutral'}
Key features to include: {features if features else 'N/A'}
Constraints: {constraints if constraints else 'None'}
Avoid: {avoid if avoid else 'Nothing'}

Respond in the style of a polished {style.lower()}, formatted and structured as if ready for immediate use.
"""
    final_prompt_output.delete("1.0", tk.END)
    final_prompt_output.insert(tk.END, prompt)

# Save prompt to file
def save_prompt():
    prompt = final_prompt_output.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Nothing to save", "Generate a prompt first.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        messagebox.showinfo("Saved", "Prompt saved successfully.")

# Placeholder for inject functionality
def inject_prompt():
    tool = injection_var.get()
    prompt = final_prompt_output.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("No prompt", "Generate a prompt first.")
        return
    open_or_focus_web_ai(tool, prompt)


# Handle style dropdown selection
def toggle_lang_selector(event):
    selected = style_var.get()
    if selected == "Code":
        # Pack it directly before the submit_btn
        code_lang_frame.pack(fill=tk.X, pady=(0, 10), before=submit_btn)
    else:
        code_lang_frame.pack_forget()

# Main window
root = tk.Tk()
root.title("VisionSmith - Prompt Forge UI")
root.geometry("800x750")
root.configure(padx=20, pady=20)

# Vision Input
tk.Label(root, text="🧠 What do you want to create? (Vision Input)", font=("Arial", 12, "bold")).pack(anchor="w")
vision_input = tk.Text(root, height=5, wrap=tk.WORD)
vision_input.pack(fill=tk.X, pady=(0, 10))

# Output Style
tk.Label(root, text="🎨 Select Output Style", font=("Arial", 12)).pack(anchor="w")
style_var = tk.StringVar()
style_dropdown = ttk.Combobox(root, textvariable=style_var, values=[
    "Code", "Blog Post", "Vlog Script", "Agent", "Story", "Song", "Business Plan", "Lesson Plan"
], state="readonly")
style_dropdown.pack(fill=tk.X, pady=(0, 10))
style_dropdown.bind("<<ComboboxSelected>>", toggle_lang_selector)

# Code language selector frame - define it here, but don't pack it initially.
# It will be packed by toggle_lang_selector when "Code" is selected.
code_lang_var = tk.StringVar()
code_lang_frame = tk.Frame(root) # Create the frame

code_lang_label = tk.Label(code_lang_frame, text="💻 Preferred Programming Language")
code_lang_dropdown = ttk.Combobox(code_lang_frame, textvariable=code_lang_var, values=[
    "Python", "JavaScript", "HTML/CSS", "C#", "TypeScript", "React", "Node.js", "PHP", "Go"
], state="readonly")

code_lang_label.pack(anchor="w")
code_lang_dropdown.pack(fill=tk.X)

# Submit Button - this needs to be defined BEFORE the call to pack() that uses it as 'before'
submit_btn = tk.Button(root, text="Generate Prompt", command=generate_prompt, bg="#4CAF50", fg="white")
submit_btn.pack(pady=(0, 20), ipadx=10)

# Additional Fields
tk.Label(root, text="Tone / Personality (e.g., funny, serious, dark, hopeful)").pack(anchor="w")
tone_input = tk.Entry(root)
tone_input.pack(fill=tk.X)

tk.Label(root, text="Key Features / Must-Haves (What features, elements, or themes should it include?)").pack(anchor="w")
features_input = tk.Text(root, height=3)
features_input.pack(fill=tk.X)

tk.Label(root, text="Constraints / Rules (Any rules, limits, or technical/logistical constraints?)").pack(anchor="w")
constraints_input = tk.Text(root, height=3)
constraints_input.pack(fill=tk.X)

tk.Label(root, text="Avoid / Exclusions (What should it definitely NOT include or do?)").pack(anchor="w")
avoid_input = tk.Text(root, height=3)
avoid_input.pack(fill=tk.X, pady=(0, 15))

# Final Prompt Output
tk.Label(root, text="📝 Final Prompt", font=("Arial", 12, "bold")).pack(anchor="w")
final_prompt_output = tk.Text(root, height=10, wrap=tk.WORD)
final_prompt_output.pack(fill=tk.BOTH, expand=True)

# Save / Inject Options
btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, pady=10)

save_btn = tk.Button(btn_frame, text="💾 Save Prompt", command=save_prompt)
save_btn.pack(side=tk.LEFT, padx=5)

injection_var = tk.StringVar(value="ChatGPT")
injection_dropdown = ttk.Combobox(btn_frame, textvariable=injection_var, values=[
    "ChatGPT", "Claude", "CoPilot", "Grok", "Custom"
], state="readonly")
injection_dropdown.pack(side=tk.LEFT, padx=5)

inject_btn = tk.Button(btn_frame, text="🚀 Inject Prompt", command=inject_prompt)
inject_btn.pack(side=tk.LEFT, padx=5)

# Run the app
root.mainloop()