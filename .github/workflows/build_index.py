import os

def generate_index_html(notebook_files, build_dir='.'):
    html_content = "<html>\n<head><title>My Jupyter Notebooks</title></head>\n<body>\n<h1>My Jupyter Notebooks</h1>\n<ul>\n"
    
    for notebook in notebook_files:
        html_content += f'<li><a href="{notebook}">{notebook}</a></li>\n'

    html_content += "</ul>\n</body>\n</html>"

    with open(os.path.join(build_dir, "index.html"), "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    build_dir = "."
    notebook_files = [os.path.join(build_dir, f) for f in os.listdir(build_dir) if f.endswith('.html')]
    generate_index_html(notebook_files)
