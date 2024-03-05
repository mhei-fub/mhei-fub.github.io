import yaml

def parse_yaml_to_html(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    html_menu = '<div class="menu"><div class="accordion">'
    
    for item in data['Menu']:
        for title, content in item.items():
            # Check if the content is a string (direct link)
            if isinstance(content, str):
                # Special handling for 'Home' to point to 'index.html'
                if title == 'Home':
                    html_menu += f'<div class="contentBox"><div class="label"><a href="index.html">Home</a></div><div class="content"></div></div>'
                else:
                    html_menu += f'<div class="contentBox"><div class="label"><a href="{content}">{title}</a></div><div class="content"></div></div>'
            # If the content is a dictionary, it has submenu items
            elif isinstance(content, dict):
                html_menu += f'<div class="contentBox"><div class="label">{title}</div><div class="content">'
                for sub_item in content:
                    for sub_title, sub_link in sub_item.items():
                        html_menu += f'<a href="{sub_link}">{sub_title}</a>'
                html_menu += '</div></div>'
            # If the content is a list, indicating nested submenus
            elif isinstance(content, list):
                html_menu += f'<div class="contentBox"><div class="label">{title}</div><div class="content">'
                for sub_item in content:
                    for sub_title, sub_link in sub_item.items():
                        html_menu += f'<a href="{sub_link}">{sub_title}</a>'
                html_menu += '</div></div>'
    
    html_menu += '</div><button class="button" id="Btn"><i class=\'bx bx-menu bx-burst\' style=\'color:#54d82d\' ></i></button></div>'
    
    return html_menu

def update_js_script(js_file, html_menu):
    with open(js_file, 'r+') as file:
        lines = file.readlines()
        if lines:
            lines[0] = f'const menu = `{html_menu}`;\n'
        else:
            lines = [f'const menu = `{html_menu}`;\n']
        file.seek(0)
        file.writelines(lines)
        file.truncate()

yaml_file = 'menu.yaml'
js_file = 'script.js'

html_menu = parse_yaml_to_html(yaml_file)
update_js_script(js_file, html_menu)
