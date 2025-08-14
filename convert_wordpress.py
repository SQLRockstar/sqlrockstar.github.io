#!/usr/bin/env python3
"""
WordPress XML to GitHub Pages (Jekyll) Markdown Converter
GitHub Actions version
"""

import xml.etree.ElementTree as ET
import re
import html
from datetime import datetime
import os
import html2text


def clean_filename(title):
    """Convert title to a clean filename suitable for Jekyll."""
    # Remove HTML tags and decode entities
    title = re.sub(r'<[^>]+>', '', title)
    title = html.unescape(title)
    
    # Convert to lowercase and replace spaces/special chars with hyphens
    title = re.sub(r'[^\w\s-]', '', title)
    title = re.sub(r'[-\s]+', '-', title).strip('-').lower()
    
    return title[:50]  # Limit length


def parse_wordpress_content(content):
    """Parse WordPress content and convert to Markdown."""
    if not content:
        return ""
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Convert WordPress blocks and HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    h.ignore_emphasis = False
    
    # Handle WordPress blocks - convert to plain HTML first
    # Remove WordPress block comments
    content = re.sub(r'<!-- wp:[^>]+ -->', '', content)
    content = re.sub(r'<!-- /wp:[^>]+ -->', '', content)
    
    # Convert CDATA sections
    content = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', content, flags=re.DOTALL)
    
    # Convert to markdown
    markdown_content = h.handle(content)
    
    # Clean up extra newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    return markdown_content.strip()


def extract_post_data(item):
    """Extract relevant data from a WordPress XML item."""
    # Extract basic information
    title = item.find('title').text if item.find('title') is not None else "Untitled"
    title = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', title, flags=re.DOTALL)
    
    link = item.find('link').text if item.find('link') is not None else ""
    
    pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
    if pub_date:
        try:
            # Parse WordPress date format
            date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
            jekyll_date = date_obj.strftime("%Y-%m-%d")
            jekyll_time = date_obj.strftime("%Y-%m-%d %H:%M:%S %z")
        except:
            jekyll_date = pub_date[:10]  # Fallback
            jekyll_time = pub_date
    else:
        jekyll_date = "2023-01-01"
        jekyll_time = "2023-01-01 00:00:00 +0000"
    
    creator = item.find('.//{http://purl.org/dc/elements/1.1/}creator')
    author = creator.text if creator is not None else "admin"
    
    # Extract content
    content_elem = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded')
    content = content_elem.text if content_elem is not None else ""
    
    # Extract WordPress specific fields
    post_type = item.find('.//{http://wordpress.org/export/1.2/}post_type')
    post_type = post_type.text if post_type is not None else "post"
    
    status = item.find('.//{http://wordpress.org/export/1.2/}status')
    status = status.text if status is not None else "publish"
    
    # Extract categories and tags
    categories = []
    tags = []
    
    for category in item.findall('.//{http://wordpress.org/export/1.2/}category'):
        domain = category.get('domain', '')
        nicename = category.get('nicename', '')
        if domain == 'category':
            categories.append(nicename)
        elif domain == 'post_tag':
            tags.append(nicename)
    
    return {
        'title': title,
        'link': link,
        'date': jekyll_date,
        'datetime': jekyll_time,
        'author': author,
        'content': content,
        'post_type': post_type,
        'status': status,
        'categories': categories,
        'tags': tags
    }


def create_jekyll_post(post_data, output_dir):
    """Create a Jekyll-compatible Markdown file."""
    if post_data['status'] != 'publish':
        print(f"Skipping '{post_data['title']}' - not published")
        return None
    
    # Create filename
    clean_title = clean_filename(post_data['title'])
    
    # Determine output location and filename based on post type
    if post_data['post_type'] == 'post':
        post_dir = os.path.join(output_dir, '_posts')
        filename = f"{post_data['date']}-{clean_title}.md"
    else:
        # For pages, use a cleaner structure
        post_dir = output_dir
        filename = f"{clean_title}.md"
    
    # Determine layout based on post type
    layout = 'post' if post_data['post_type'] == 'post' else 'page'
    
    # Create front matter
    front_matter = [
        '---',
        f'layout: {layout}',
        f'title: "{post_data["title"].replace('"', '\\"')}"',
        f'date: {post_data["datetime"]}',
        f'author: {post_data["author"]}'
    ]
    
    if post_data['categories']:
        front_matter.append(f'categories: [{", ".join([f'"{cat}"' for cat in post_data["categories"]])}]')
    
    if post_data['tags']:
        front_matter.append(f'tags: [{", ".join([f'"{tag}"' for tag in post_data["tags"]])}]')
    
    if post_data['link']:
        front_matter.append(f'original_url: {post_data["link"]}')
    
    front_matter.append('---')
    front_matter.append('')  # Empty line after front matter
    
    # Convert content to markdown
    markdown_content = parse_wordpress_content(post_data['content'])
    
    # Combine front matter and content
    full_content = '\n'.join(front_matter) + markdown_content
    
    # Ensure output directory exists
    os.makedirs(post_dir, exist_ok=True)
    
    # Write file
    filepath = os.path.join(post_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Created: {filepath}")
    return filepath


def convert_wordpress_xml(xml_file, output_dir):
    """Main function to convert WordPress XML to Jekyll posts."""
    try:
        print(f"Converting WordPress XML: {xml_file}")
        print(f"Output directory: {output_dir}")
        print("-" * 50)
        
        # Parse XML
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Find all items (posts/pages)
        items = root.findall('.//item')
        
        converted_count = 0
        skipped_count = 0
        
        for item in items:
            post_data = extract_post_data(item)
            
            # Skip certain post types
            if post_data['post_type'] in ['attachment', 'nav_menu_item', 'custom_css']:
                skipped_count += 1
                continue
            
            result = create_jekyll_post(post_data, output_dir)
            if result:
                converted_count += 1
            else:
                skipped_count += 1
        
        print(f"\nConversion complete!")
        print(f"Converted: {converted_count} posts/pages")
        print(f"Skipped: {skipped_count} items")
        
        return converted_count > 0
        
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False


if __name__ == "__main__":
    xml_file = "data/thomaslarock.WordPress.2005-2025-PAGES.xml"
    output_dir = "."  # Current directory (repo root)
    
    if not os.path.exists(xml_file):
        print(f"Error: XML file '{xml_file}' not found")
        exit(1)
    
    success = convert_wordpress_xml(xml_file, output_dir)
    if not success:
        exit(1)
