import tkinter as tk
import tkinter.messagebox
import customtkinter
from pytube import YouTube

def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)

        video = yt_object.streams.get_lowest_resolution()
        video.download()

        # Show success message
        tkinter.messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        # Show error message
        tkinter.messagebox.showerror("Error", f"Error: {e}")

# System
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x420")
app.title("Youtube Downloader")

# Adding some UI elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Running this app
app.mainloop()





