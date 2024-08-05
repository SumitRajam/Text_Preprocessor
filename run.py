import tkinter as tk
from tkinter import scrolledtext
from functions import tokenize_text, check_voices, lemmatize_text, stem_text, tag_text, extract_clauses, process_text1

def process_text(action):
    """Process the text input based on the selected action."""
    user_input = entry.get().strip()  # Get user input and remove extra spaces
    if not user_input:
        show_message("Please enter input text.", fg="red")
        return
    actions = {
        'tokenize': tokenize_text,
        'stem': stem_text,
        'lemmatize': lemmatize_text,
        'pos': tag_text,
        'tenses': process_text1,
        'clauses': extract_clauses,
        'voices': check_voices
    }
    if action in actions:
        func = actions[action]
        output = func(user_input)
        print(f"Debug Output:\n{output}")  # Debug: Print output to console
        output_text.config(state=tk.NORMAL)  # Make text widget editable to insert text
        output_text.delete(1.0, tk.END)  # Clear the previous output
        output_text.insert(tk.END, output)  # Insert the new output
        output_text.config(state=tk.DISABLED)  # Make text widget non-editable

def generate_test_text():
    """Populate the entry widget with sample text."""
    sample_text = (
        "Apple announced a new iPhone model with advanced camera features. "
        "The United States government is investigating the recent cyberattack. "
        "Due to heavy rainfall, several flights have been delayed at Mumbai airport."
    )
    entry.delete(0, tk.END)  # Clear the existing text
    entry.insert(0, sample_text)  # Insert the sample text

def reset_all():
    """Clear the input field and output area, and show instructions."""
    entry.delete(0, tk.END)  # Clear the entry widget
    output_text.config(state=tk.NORMAL)  # Make text widget editable to clear text
    output_text.delete(1.0, tk.END)  # Clear the output text
    show_instructions()  # Show instructions or information

def show_instructions():
    """Display usage instructions or information about the model."""
    instructions = (
        "Welcome to the Text Processing Tool!\n\n"
        "1. Enter your text in the input field.\n"
        "2. Click 'Generate Test Text' to use sample text.\n"
        "3. Select a processing action (e.g., Tokenize, Stem) to analyze the text.\n"
        "4. Click 'Reset' to clear the input and output.\n\n"
        "Instructions will be displayed here."
    )
    show_message(instructions, fg="black")  # Show instructions in the output area

def show_message(message, fg="black"):
    """Display a message in the output area."""
    output_text.config(state=tk.NORMAL)  # Make text widget editable to insert text
    output_text.delete(1.0, tk.END)  # Clear previous content
    output_text.insert(tk.END, message)  # Insert message
    output_text.config(state=tk.DISABLED)  # Make text widget non-editable

# Create the main window
root = tk.Tk()
root.title("Text Preprocesser")
root.geometry("800x500")  # Initial size of the window

# Set the minimum size for the window
root.minsize(780, 500)

# Create an Entry widget for user input
entry_label = tk.Label(root, text="Enter text for processing:")
entry_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

entry = tk.Entry(root, width=60)
entry.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

# Create a Button to generate test text
generate_button = tk.Button(root, text="Generate Test Text", command=generate_test_text)
generate_button.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

# Create a Button to reset all fields
reset_button = tk.Button(root, text="Reset", command=reset_all)
reset_button.grid(row=1, column=2, padx=10, pady=5, sticky='ew')

# Create a Frame for the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

# Create buttons for different functionalities
buttons = [
    ('Tokenize', 'tokenize'),
    ('Stem', 'stem'),
    ('Lemmatize', 'lemmatize'),
    ('POS Tagging', 'pos'),
    ('Tenses', 'tenses'),
    ('Clauses', 'clauses'),
    ('Voices', 'voices')
]

# Calculate minimum button width for display
button_min_width = max(len(text) for text, _ in buttons) * 10  # Approximate width

for i, (text, action) in enumerate(buttons):
    button = tk.Button(button_frame, text=text, width=button_min_width, command=lambda a=action: process_text(a))
    button.grid(row=0, column=i, padx=5, pady=5)

# Create a Frame to contain the Text widget and scrollbar
output_frame = tk.Frame(root)
output_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=20, sticky='nsew')

# Create a ScrolledText widget for displaying the output
output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=20, width=90, state=tk.DISABLED)
output_text.grid(row=0, column=0, sticky='nsew')

# Configure grid weights for responsive resizing
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
output_frame.grid_rowconfigure(0, weight=1)
output_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(tuple(range(len(buttons))), weight=1)  # Equal weight for each button column

# Show instructions when the application starts
show_instructions()

# Start the Tkinter event loop
root.mainloop()
