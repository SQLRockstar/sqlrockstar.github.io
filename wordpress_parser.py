#!/usr/bin/env python3
"""
WordPress XML to Jekyll Converter
Converts WordPress XML export to Jekyll blog posts
"""

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import os
import sys
from datetime import datetime
from dateutil import parser as date_parser
import argparse

def create_directory_structure():
    """Create the blog directory structure"""
    directories = [
        'blog/_posts',
        'blog/assets/images'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_jekyll_config():
    """Create Jekyll configuration file"""
    config_content = """title: Thomas LaRock's Blog
description: Database and technology insights
baseurl: "/blog"
url: "https://sqlrockstar.github.io"
permalink: /:year/:month/:day/:title/

plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag

markdown: kramdown
highlighter: rouge
theme: minima
"""
    
    with open('blog/_config.yml', 'w', encoding='utf-8') as f:
        f.write(config_content)
    print("Created Jekyll config file")

def create_index_page():
    """Create Jekyll index page"""
    index_content = """---
layout: home
title: Blog
---
"""
    
    with open('blog/index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Created index page")

def create_gemfile():
    """Create Gemfile for Jekyll"""
    gemfile_content = """source "https://rubygems.org"
gem "jekyll", "~> 4.3.0"
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end
"""
    
    with open('blog/Gemfile', 'w', encoding='utf-8') as f:
        f.write(gemfile_content)
    print("Created Gemfile")

def clean_title(title):
    """Clean title for YAML front matter"""
    if not title:
        return "Untitled"
    
    # Escape quotes and special characters for YAML
    title = title.replace('"', '\\"').replace("'", "\\'")
    return title

def create_slug(title, post_name=None):
    """Create URL slug from title or post name"""
    if post_name:
        return post_name
    
    # Create slug from title
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    
    # Ensure slug is not empty
    if not slug:
        slug = 'untitled'
    
    return slug

def parse_date(date_string):
    """Parse WordPress date string"""
    if not date_string:
        return '2024-01-01', '2024-01-01 00:00:00'
    
    try:
        date_obj = date_parser.parse(date_string)
        date_str = date_obj.strftime('%Y-%m-%d')
        time_str = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        return date_str, time_str
    except:
        return '2024-01-01', '2024-01-01 00:00:00'

def clean_content(content):
    """Clean HTML content"""
    if not content:
        return ''
    
    # Use BeautifulSoup to clean HTML
    soup = BeautifulSoup(content, 'html.parser')
    return str(soup)

def format_yaml_array(items):
    """Format array for YAML front matter"""
    if not items:
        return '[]'
    
    # Clean and quote each item
    clean_items = []
    for item in items:
        if item and item.strip():
            # Escape quotes in the item
            clean_item = item.strip().replace('"', '\\"')
            clean_items.append(f'"{clean_item}"')
    
    return '[' + ', '.join(clean_items) + ']'

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML and create Jekyll posts"""
    print(f"Parsing WordPress XML: {xml_file}")
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(f"XML parsed successfully. Root tag: {root.tag}")
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return 0
    
    # Define namespaces
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
    
    posts_created = 0
    
    # Find all items (posts)
    items = root.findall('.//item')
    print(f"Found {len(items)} items in XML")
    
    for item in items:
        try:
            # Get post type
            post_type = item.find('wp:post_type', namespaces)
            if post_type is None or post_type.text != 'post':
                continue
            
            # Get post status
            status = item.find('wp:status', namespaces)
            if status is None or status.text != 'publish':
                continue
            
            # Get post data
            title_elem = item.find('title')
            title_text = title_elem.text if title_elem is not None else 'Untitled'
            clean_title_text = clean_title(title_text)
            
            # Get content
            content_elem = item.find('content:encoded', namespaces)
            content_text = content_elem.text if content_elem is not None else ''
            clean_content_text = clean_content(content_text)
            
            # Get date
            pub_date_elem = item.find('pubDate')
            pub_date_text = pub_date_elem.text if pub_date_elem is not None else None
            date_str, time_str = parse_date(pub_date_text)
            
            # Get slug
            post_name_elem = item.find('wp:post_name', namespaces)
            post_name = post_name_elem.text if post_name_elem is not None else None
            slug = create_slug(title_text, post_name)
            
            # Get categories
            categories = []
            for category in item.findall('category'):
                if category.get('domain') == 'category' and category.text:
                    cat_name = category.text.strip()
                    if cat_name:
                        categories.append(cat_name)
            
            # Get tags
            tags = []
            for tag in item.findall('category'):
                if tag.get('domain') == 'post_tag' and tag.text:
                    tag_name = tag.text.strip()
                    if tag_name:
                        tags.append(tag_name)
            
            # Create Jekyll post
            filename = f"{date_str}-{slug}.markdown"
            filepath = f"blog/_posts/{filename}"
            
            # Create front matter
            front_matter = f"""---
layout: post
title: "{clean_title_text}"
date: {time_str}
categories: {format_yaml_array(categories)}
tags: {format_yaml_array(tags)}
---

{clean_content_text}
"""
            
            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(front_matter)
            
            posts_created += 1
            print(f"Created post: {filename}")
            
        except Exception as e:
            print(f"Error processing item: {e}")
            continue
    
    print(f"Successfully created {posts_created} posts")
    return posts_created

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Convert WordPress XML to Jekyll posts')
    parser.add_argument('xml_file', help='Path to WordPress XML file')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.xml_file):
        print(f"Error: XML file '{args.xml_file}' not found")
        sys.exit(1)
    
    print("Starting WordPress to Jekyll conversion...")
    
    # Create directory structure
    create_directory_structure()
    
    # Create Jekyll files
    create_jekyll_config()
    create_index_page()
    create_gemfile()
    
    # Parse XML and create posts
    posts_created = parse_wordpress_xml(args.xml_file)
    
    print(f"\nConversion complete!")
    print(f"Posts created: {posts_created}")
    print(f"Blog directory: ./blog/")
    print(f"Posts directory: ./blog/_posts/")

if __name__ == '__main__':
    main()
