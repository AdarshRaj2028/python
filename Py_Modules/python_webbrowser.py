"""
WEB BROWSER MODULE COMPLETE REFERENCE GUIDE

****Running this will open different web pages in your browser for demonstration****

Core Purpose & Key Strength:
- Programmatically open web pages using the system's default browser.
- Simple, zero-dependency way to launch URLs.
- Cross-platform compatibility (works on Windows, macOS, Linux).
- Built into the Python standard library, so no installation is needed.

Learning Path:
Start with basic webbrowser.open() → Differentiate open_new() vs. open_new_tab() → Build dynamic URLs with f-strings → Integrate into simple applications.

ESSENTIAL FUNCTIONS TO MASTER:

1. The Core Function: webbrowser.open()
"""

import webbrowser

# webbrowser.open(url, new=0, autoraise=True)
# - url: The website address to open.
# - new: Controls where to open the URL.
#   - 0: Opens in the same browser window (default, might be a new tab).
#   - 1: Opens in a NEW browser window.
#   - 2: Opens in a NEW browser tab. (Same as webbrowser.open_new_tab(url)) -> Preffered.
# - autoraise: If True (default), raises the window.

# Example: Open a page in the most convenient way (usually a new tab)
# webbrowser.open("https://docs.python.org/3/")

"""
2. Specific Target Functions (Shortcuts):
"""

# webbrowser.open_new(url)
# - A convenient shortcut for webbrowser.open(url, new=1).
# - Use when you want to guarantee a new window.
# webbrowser.open_new("https://www.google.com")

# webbrowser.open_new_tab(url)
# - A shortcut for webbrowser.open(url, new=2).
# - This is often the most predictable and user-friendly option.
# webbrowser.open_new_tab("https://github.com")
print()

"""
KEY METHODS COMPARISON:

open() vs open_new() vs open_new_tab():
- The behavior can sometimes depend on your OS and browser settings,
- but open_new() and open_new_tab() are more explicit requests.
"""

# Let's see them in action. Uncomment one at a time to test.
python_docs = "https://docs.python.org/3/library/webbrowser.html"

# print("Testing open()... (might be a tab or window)")
# webbrowser.open(python_docs)

# print("Testing open_new()... (should be a new window)")
# webbrowser.open_new(python_docs)

# print("Testing open_new_tab()... (should be a new tab)")
# webbrowser.open_new_tab(python_docs)
print()

"""
COMMON GOTCHAS & SOLUTIONS:

1. It's a "Fire and Forget" Module:
"""
# ❌ Wrong Assumption: Thinking you can control the browser after opening.
# The webbrowser module cannot read page content, click buttons,
# close tabs, or interact with the website in any way. It only launches the URL.

# ✅ Solution: For browser automation (clicking, filling forms), you need a more
# powerful library like Selenium. For reading web page content, you need
# libraries like `requests` and `BeautifulSoup`.

"""
2. It's Non-Blocking:
"""
# Your Python script DOES NOT wait for the user to close the browser.
# It opens the URL and immediately continues executing the rest of the code.

print("This line prints immediately after the browser is launched.")
# webbrowser.open("https://www.google.com")
print("The script doesn't wait and has already moved on to this line.")
print()

"""
ADVANCED INTEGRATION:

With f-strings for Dynamic URLs:
"""
# This is the most common and powerful way to use webbrowser.
# You can build URLs based on user input or program data.

def search_pypi(package_name):
    """Opens the PyPI page for a given package."""
    if package_name:
        url = f"https://pypi.org/project/{package_name}/"
        webbrowser.open_new_tab(url)
        print(f"Opened PyPI page for '{package_name}'")
    else:
        print("No package name provided.")

# Uncomment to test the dynamic URL builder
# search_pypi("requests")
# search_pypi("numpy")

"""
With urllib.parse for Complex URLs:
"""
# For URLs with special characters or complex query parameters,
# `urllib.parse.urlencode` ensures the URL is formatted correctly.
from urllib.parse import urlencode

def open_Maps(location):
    """Opens Google Maps for a given location."""
    params = {"q": location}
    query_string = urlencode(params)
    url = f"https://www.google.com/maps?{query_string}"
    webbrowser.open_new_tab(url)
    print(f"Opening map for '{location}'")

# Uncomment to test
# open_Maps("Eiffel Tower, Paris, France")
# open_Maps("Kolkata, West Bengal")
print()

"""
PRACTICE PROJECTS:

1. Multi-Search Tool:
   - Takes a single search term and opens it on Google, Wikipedia, and GitHub.

2. Python Documentation Helper:
   - Asks for a Python module name and opens its official documentation page.

3. Automated Task Launcher:
   - A script that opens all the websites you need for your daily work (e.g., email, project management tool, news).

QUICK REFERENCE TABLE:

Function              | Behavior                                       | Use Case
----------------------|------------------------------------------------|----------------------------------
webbrowser.open(url)  | Opens in default browser (might be new tab)    | General purpose, simple opening.
webbrowser.open_new(url)| Requests a NEW BROWSER WINDOW                  | When you need to force a separate window.
webbrowser.open_new_tab(url)| Requests a NEW BROWSER TAB                 | Most common and predictable choice.

MEMORY AID:

"BOT" - Browser Opening Trio:
- B: Browser is the target.
- O: open() is the general-purpose tool.
- T: open_new_Tab() is your most reliable choice for tabs.

Remember: This module is for OPENING pages, not CONTROLLING them.

CONCEPT SUMMARY FOR REVISION:

Core Purpose: To programmatically open a URL in the user's default browser.
Key Strength: Simple, built-in, cross-platform. No installation needed.

Essential Functions to Master:
1. webbrowser.open(url) - General opener.
2. webbrowser.open_new(url) - Forces a new window.
3. webbrowser.open_new_tab(url) - Best practice for opening a new tab.

Common Gotchas:
- It's a "fire-and-forget" tool; it cannot control or read the web page.
- Your script continues to execute immediately after launching the browser.
- Use f-strings or urllib.parse to build dynamic URLs from variables or user input.
"""