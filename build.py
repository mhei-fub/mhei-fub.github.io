import os
from bs4 import BeautifulSoup

def read_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError:
        print(f"Error reading file: {file_path}")
        return None

def generate_nav_link(filename, title):
    if filename == 'index.html':
        return f'<a href="/">{title}</a>'
    else:
        return f'<a href="{filename}">{title}</a>'

def sort_links(item):
    filename, title = item
    return '' if title == 'Home' else title

def update_script_js(nav_links_str):
    try:
        with open('script.js', 'r') as file:
            lines = file.readlines()
        lines[0] = f'const menu = `{nav_links_str}`;\n'
        with open('script.js', 'w') as file:
            file.writelines(lines)
    except IOError:
        print("Error updating script.js")

menu_start = "<div class=\"navbar\"><button class=\"arrow\" id=\"Btn\"><div class=\"arrow-bar arrow-bar1\"></div><div class=\"arrow-bar arrow-bar2\"></div></button></div><div class=\"menu\" id=\"menu\">"

pages = {}

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            contents = read_html_file(file_path)
            if contents:
                soup = BeautifulSoup(contents, 'html.parser')
                title = soup.title.string if soup.title else "No title"
                pages[file] = title

sorted = dict(sorted(pages.items(), key=sort_links))
links = [generate_nav_link(filename, title) for filename, title in sorted.items()]
menu = ''.join([menu_start, ''.join(links), "</div>"])

update_script_js(menu)