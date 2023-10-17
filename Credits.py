import tkinter as tk

# Create a new tkinter window
window = tk.Tk()
window.title("Thank You Credits")

# Set the window size and position it in the center of the screen
window.geometry("400x300")
window.eval('tk::PlaceWindow . center')

# Function to close the window
def close_window():
    window.destroy()

# Create a frame to hold the content and set its background color
content_frame = tk.Frame(window, bg="lightgray")
content_frame.pack(fill=tk.BOTH, expand=True)

# Create a "Thank You" label with a larger font
thank_you_label = tk.Label(content_frame, text="Thank You For Playing Our Game ", font=("Helvetica", 24))
thank_you_label.pack(pady=20)

# Create a label for contributors
contributors_label = tk.Label(content_frame, text="Special thanks to our contributors:")
contributors_label.pack()

# Create a list of contributors
contributors = [
    "JoshuaJ",
    "TerrorFusion",
]

for contributor in contributors:
    contributor_label = tk.Label(content_frame, text=contributor)
    contributor_label.pack()

# Create a "Close" button
close_button = tk.Button(content_frame, text="Close", command=close_window)
close_button.pack(pady=20)

# Run the tkinter main loop
window.mainloop()