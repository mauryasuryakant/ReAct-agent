import webbrowser
import subprocess

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opened YouTube"

def youtube_search(query):
    import webbrowser
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searched YouTube for {query}"

def open_url(url):
    import webbrowser
    webbrowser.open(url)
    return f"Opened URL: {url}"

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searched Google for {query}"

def create_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File '{filename}' created"


# 🚫 Restricted command execution
def run_command(cmd):
    return "run_command is restricted. Use other tools."