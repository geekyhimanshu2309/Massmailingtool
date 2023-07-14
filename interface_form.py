import tkinter as tk

def submit_form():
    # Function to handle the form submission
    # You can access the form inputs and perform any desired actions here
    context = context_entry.get()
    email = email_entry.get()
    
    # Example: Print the form inputs
    print("Context:", context)
    print("Email:", email)

# Create a new Tkinter window
window = tk.Tk()

# Create form labels
context_label = tk.Label(window, text="Context:")
context_label.pack()  # Display the label

# Create form input fields
context_entry = tk.Entry(window)
context_entry.pack()  # Display the input field

email_label = tk.Label(window, text="Email:")
email_label.pack()  # Display the label

email_entry = tk.Entry(window)
email_entry.pack()  # Display the input field

# Create submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()  # Display the button

# Run the Tkinter event loop
window.mainloop()
