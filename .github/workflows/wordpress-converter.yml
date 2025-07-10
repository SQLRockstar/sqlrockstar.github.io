name: WordPress to Jekyll Converter

on:
  workflow_dispatch:
    inputs:
      xml_url:
        description: 'URL to WordPress XML file'
        required: true
        type: string

permissions:
  contents: write

jobs:
  convert:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: Install Python dependencies
      run: |
        pip install beautifulsoup4 lxml python-dateutil
        
    - name: Download WordPress XML
      run: |
        curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
          -o wordpress-export.xml "${{ github.event.inputs.xml_url }}"
        
    - name: Run WordPress to Jekyll converter
      run: |
        python3 wordpress_parser.py wordpress-export.xml
        
    - name: Show conversion results
      run: |
        echo "Blog structure created:"
        find blog -type f -name "*.yml" -o -name "*.html" -o -name "Gemfile" | head -10
        echo ""
        echo "Posts created:"
        find blog/_posts -name "*.markdown" | wc -l
        echo ""
        echo "Sample post:"
        find blog/_posts -name "*.markdown" | head -1 | xargs head -10
        
    - name: Commit and push changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        if git diff --staged --quiet; then
          echo "No changes to commit"
        else
          git commit -m "Convert WordPress XML to Jekyll - $(find blog/_posts -name '*.markdown' | wc -l) posts"
          git push origin main
        fi
