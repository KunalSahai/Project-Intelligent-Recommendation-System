import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import wikipedia

def search_wikipedia(query):
    try:
        # Set language (optional)
        wikipedia.set_lang("en")
        
        # Search for the query
        results = wikipedia.search(query)
        
        if results:
            # Get the most relevant article
            page = wikipedia.page(results[0])
            
            # Return title and summary
            return page.title, page.summary
        else:
            return "No results found for the query.", None
    except wikipedia.exceptions.DisambiguationError as e:
        return "Disambiguation Error: Please specify your query further.", None
    except wikipedia.exceptions.PageError as e:
        return "Page not found. Please try a different query.", None
    except Exception as e:
        return "An error occurred while processing your request.", None

def search():
    query = entry.get()
    title, summary = search_wikipedia(query)
    if summary is None:
        messagebox.showinfo("Intelligent Recommendation System", title)
    else:
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Title: {title}\n\nSummary: {summary}")
        output_text.config(state="disabled")

# Create a Tkinter window
window = tk.Tk()
window.title("Intelligent Recommendation System")

# Create frames
input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

output_frame = ttk.Frame(window)
output_frame.pack(pady=10)

# Create input widgets
label = ttk.Label(input_frame, text="Enter your search query:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(input_frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

button = ttk.Button(input_frame, text="Search", command=search)
button.grid(row=0, column=2, padx=5, pady=5)

# Create output widgets
output_text = tk.Text(output_frame, wrap="word", height=10, width=70)
output_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)
output_text.config(state="disabled")

scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=output_text.yview)
scrollbar.pack(side="right", fill="y")

output_text.config(yscrollcommand=scrollbar.set)

# Run the Tkinter event loop
window.mainloop()