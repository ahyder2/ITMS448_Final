#Programmed by Desmond Mair

import tkinter as tk
from Reddit_Scraper import ScrapeReddit
from Twitter_Scraper import scrapeTwitter

#Function for the exit button
def close_app():
    window.destroy()

def run_twitter_scrape():
    scrapeTwitter()

def run_reddit_scrape():
    strSubreddit = str(subinputstr_entry.get())
    strKey = str(subkeystr_entry.get())

    ScrapeReddit(strSubreddit, strKey)

window = tk.Tk()

#Setting up the sections for the GUI
window.title("Web Scraper Tool 1.0 (ITMS448 OSINT PROJECT")
window.resizable("false", "false")
frameHeader = tk.Frame(master = window, borderwidth = 2, pady = 2)
centerFrame = tk.Frame(window, borderwidth = 2, pady = 2)
bottomFrame = tk.Frame(window, borderwidth = 2, pady = 2)
frameHeader.grid(row = 0, column = 0)
centerFrame.grid(row = 1, column = 0)
bottomFrame.grid(row = 2, column = 0)

#This is the header, where the title of the program resides
header = tk.Label(frameHeader, text = "Twitter/Reddit Web Scraper", bg = 'gray', fg = 'black', height = '3', width = '50', font = ("Helvetica 16 bold"))
header.grid(row = 0, column = 0)

#Frame for the input
frame_main1 = tk.Label(centerFrame, borderwidth = 2, relief = 'sunken')
frame_main2 = tk.Label(centerFrame, borderwidth = 2, relief = 'sunken')

subinput = tk.Label(frame_main1, text = "Subreddit: ")
subkey = tk.Label(frame_main2, text = "Key: ")

subinputstr = tk.StringVar()
subkeystr = tk.StringVar()

subinputstr_entry = tk.Entry(frame_main1, textvariable = subinputstr, width = 10)
subkeystr_entry = tk.Entry(frame_main2, textvariable = subkeystr, width = 10)

frame_main1.pack(fill = 'x', pady = 2)
frame_main2.pack(fill = 'x', pady = 2)
subinput.pack(side = "left")
subinputstr_entry.pack(side = "right", padx = 1)
subkey.pack(side = "left")
subkeystr_entry.pack(side = "right", padx = 1)

#Button to run the Twitter Scraper
button_run1 = tk.Button(bottomFrame, text = "Twitter", command = run_twitter_scrape(), bg = 'light blue', fg = 'black', relief = 'raised', width = 10, font = ('Helvetica 9 bold'))
button_run1.grid(column = 0, row = 0, sticky = 'w', padx = 100, pady = 2)

#Button to run the Reddit Scraper
button_run2 = tk.Button(bottomFrame, text = "Reddit", command = run_reddit_scrape(), bg = 'red', fg = 'black', relief = 'raised', width = 10, font = ('Helvetica 9 bold'))
button_run2.grid(column = 1, row = 0, sticky = 'w', padx = 100, pady = 2)

#Exit button
button_run3 = tk.Button(bottomFrame, text = "Exit", command = close_app, bg = 'dark red', fg = 'white', relief = 'raised', width = 10, font = ('Helvetica 9 bold'))
button_run3.grid(column = 2, row = 0, sticky = 'w', padx = 100, pady = 2)

window.mainloop()
