import markdown
import sys
import os
from bs4 import BeautifulSoup

def convert_md_to_html(md_file_path, html_output_path, css_file_path='styles.css'):
    """
    Converts a single Markdown file to an HTML file and links a CSS stylesheet.
    The paths for the MD file, HTML output, and CSS file are passed as arguments.
    """
    try:
        # Read the Markdown content
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert Markdown to HTML body
        html_body = markdown.markdown(md_content)

        # Create a complete HTML document
        title = os.path.basename(md_file_path).replace('.md', '').replace('-', ' ').title()
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{os.path.relpath(css_file_path, os.path.dirname(html_output_path))}">
</head>
<body>
    {html_body}
</body>
</html>
"""
        # Use BeautifulSoup to format the HTML
        soup = BeautifulSoup(html_template, 'html.parser')

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(html_output_path) or '.', exist_ok=True)

        # Write the final HTML content to the output file
        with open(html_output_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Successfully converted '{md_file_path}' to '{html_output_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{md_file_path}' or '{css_file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_md_file> <output_html_file>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    
    convert_md_to_html(md_file, html_file)
