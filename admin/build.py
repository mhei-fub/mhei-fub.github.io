import yaml
import os

def read_menu(yaml_file):
    menu_data = []
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
        for item_idx, item in enumerate(data):
            for title, content in item.items():
                if item_idx == 0 and isinstance(content, str):
                    filename = 'index.html'
                else:
                    filename = title.lower().replace(" ", "-") + ".html"
                if isinstance(content, str):
                    menu_data.append((title, filename, content, None))
                elif isinstance(content, list) or isinstance(content, dict):
                    group_title = title
                    for sub_item in content:
                        for sub_title, sub_link in sub_item.items():
                            sub_filename = sub_title.lower().replace(" ", "-") + ".html"
                            menu_data.append(
                                (sub_title, sub_filename, sub_link, group_title))
    return menu_data


def build_menu(menu_data):
    menu_html = '''const menu = `<div class="menu"><div class="accordion">'''
    current_group = None

    for idx, (title, filename, link, group_title) in enumerate(menu_data):

        if group_title != current_group:
            if current_group is not None:
                menu_html += '</div>'
            if group_title:
                menu_html += f'''<div class="contentBox"><div class="label">{
                    group_title}</div>'''
                current_group = group_title

        if group_title:
            menu_html += f'''<div class="content"><a href="{
                filename}">{title}</a></div>'''
        else:
            menu_html += f'''<div class="contentBox"><div class="label"><a href="{
                filename}">{title}</a></div><div class="content"></div></div>'''

    menu_html += f'''</div></div><button class="button" id="Btn"><i class="bx bx-menu bx-burst" style="color: #54d82d"></i></button>`;'''

    script_js_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'script.js')
    with open(script_js_path, 'r') as file:
        script_js_content = file.read()

    script_js_content = menu_html + '\n' + \
        script_js_content.split('\n', 1)[1]

    with open(script_js_path, 'w') as file:
        file.write(script_js_content)
    return menu_html


def build_files(template_html, menu_data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    output_directory = os.path.join(parent_directory, '..')

    for filename in os.listdir(output_directory):
        if filename.endswith('.html') and filename != 'apaf.html':
            file_path = os.path.join(output_directory, filename)
            os.remove(file_path)

    with open(template_html, 'r') as file:
        template_content = file.read()

    for title, filename, link, group_title in menu_data:
        if group_title:
            link_text = f'{title}'
        else:
            link_text = title
        output_content = template_content.format(
            title=link_text, link=f'<iframe src="{link}"></iframe>')

        output_file_path = os.path.join(output_directory, filename)
        with open(output_file_path, 'w') as file:
            file.write(output_content)
    

def main():
    menu_data = read_menu('menu.yaml')
    build_files('template.html', menu_data)
    build_menu(menu_data)


if __name__ == '__main__':
    main()
