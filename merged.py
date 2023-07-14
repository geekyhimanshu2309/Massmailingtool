# import pandas as pd
# import smtplib as sm
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import tkinter as tk
# from tkinter import filedialog

# def send_emails():
#     sender_email = sender_entry.get()
#     context = context_entry.get("1.0", tk.END)
#     attachment_file = file_path_entry.get()

#     # Read email addresses from Excel file
#     data = pd.read_excel(attachment_file)
#     email_col = data.get("email")
#     list_of_emails = list(email_col)

#     try:
#         server = sm.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, "enterpassword")
        
#         for recipient_email in list_of_emails:
#             message = MIMEMultipart("alternative")
#             message['Subject'] = "This is a test message"
#             message["From"] = sender_email
#             message["To"] = recipient_email

#             html = '''
#                 <html>
#                 <head>
#                 </head>
#                 <body>
#                 <h1>{}</h1>
#                 <p>{}</p>
#                 <button style="padding:20px;background:green;color:white;">Verify</button>
#                 </body>
#                 </html>
#             '''.format(context, sender_email)

#             text = MIMEText(html, "html")
#             message.attach(text)
#             server.sendmail(sender_email, recipient_email, message.as_string())
        
#         server.quit()
#         print("Message has been sent to the emails")
#     except Exception as e:
#         print(e)

# def open_file():
#     global file_path
#     file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
#     file_path_entry.delete(0, tk.END)
#     file_path_entry.insert(0, file_path)
#     data_frame = pd.read_excel(file_path)
#     print(data_frame)

# # Create a new Tkinter window
# window = tk.Tk()

# # Create form labels
# sender_label = tk.Label(window, text="Sender Email Address:")
# sender_label.pack()

# # Create form input fields
# sender_entry = tk.Entry(window)
# sender_entry.pack()

# context_label = tk.Label(window, text="Context:")
# context_label.pack()

# context_entry = tk.Text(window, height=5, width=30)
# context_entry.pack()

# file_path_label = tk.Label(window, text="Email File:")
# file_path_label.pack()

# file_path_entry = tk.Entry(window, width=50)
# file_path_entry.pack()

# # Create buttons
# open_file_button = tk.Button(window, text="Open File", command=open_file)
# open_file_button.pack()

# send_button = tk.Button(window, text="Send Email", command=send_emails)
# send_button.pack()

# # Run the Tkinter event loop
# window.mainloop()
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import filedialog

def send_emails():
    sender_email = sender_entry.get()
    password = password_entry.get()
    context = context_entry.get("1.0", tk.END)

    # Read email addresses from Excel file
    attachment_file = file_path_entry.get()
    data = pd.read_excel(attachment_file)
    email_col = data.get("email")
    list_of_emails = list(email_col)

    try:
        server = sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        for recipient_email in list_of_emails:
            message = MIMEMultipart("alternative")
            message['Subject'] = "This is a test message"
            message["From"] = sender_email
            message["To"] = recipient_email

            html = '''
                <html>
                <head>
                </head>
                <body>
                <h1>{}</h1>
                <p>{}</p>
                <button style="padding:20px;background:green;color:white;">Verify</button>
                </body>
                </html>
            '''.format(context, sender_email)

            text = MIMEText(html, "html")
            message.attach(text)

            # Add attachments
            attachment_files = attachment_files_entry.get("1.0", tk.END).splitlines()
            for attachment_file in attachment_files:
                with open(attachment_file, "rb") as file:
                    attachment = MIMEApplication(file.read())
                    attachment.add_header(
                        "Content-Disposition",
                        "attachment",
                        filename=attachment_file.split("/")[-1]  # Extracting just the file name
                    )
                    message.attach(attachment)

            server.sendmail(sender_email, recipient_email, message.as_string())

        server.quit()
        print("Message has been sent to the emails")
    except Exception as e:
        print(e)

def open_email_file():
    global email_file_path
    email_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, email_file_path)
    data_frame = pd.read_excel(email_file_path)
    print(data_frame)

def open_attachment_files():
    attachment_files = filedialog.askopenfilenames()
    attachment_files_entry.delete("1.0", tk.END)
    for file_path in attachment_files:
        attachment_files_entry.insert(tk.END, file_path + "\n")

# Create a new Tkinter window
window = tk.Tk()

# Create form labels
sender_label = tk.Label(window, text="Sender Email Address:")
sender_label.pack()

# Create form input fields
sender_entry = tk.Entry(window)
sender_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")  # Entry field for password, text hidden as *
password_entry.pack()

context_label = tk.Label(window, text="Context:")
context_label.pack()

context_entry = tk.Text(window, height=10, width=50)
context_entry.pack()

attachment_label = tk.Label(window, text="Attachments:")
attachment_label.pack()

attachment_files_entry = tk.Text(window, height=5, width=30)
attachment_files_entry.pack()

email_file_label = tk.Label(window, text="Email File:")
email_file_label.pack()

file_path_entry = tk.Entry(window, width=50)
file_path_entry.pack()

# Create buttons
open_email_file_button = tk.Button(window, text="Open Email File", command=open_email_file)
open_email_file_button.pack()

open_attachment_files_button = tk.Button(window, text="Open Attachment Files", command=open_attachment_files)
open_attachment_files_button.pack()

send_button = tk.Button(window, text="Send Email", command=send_emails)
send_button.pack()

# Run the Tkinter event loop
window.mainloop()
