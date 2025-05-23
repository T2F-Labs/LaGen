#!/usr/bin/env python3
"""
Markdown to LaTeX Converter using Jinja2 Templates

This script converts a Markdown file into a beautifully formatted LaTeX file
using a Jinja2 template. It extracts content from the markdown and structures it 
in a format suitable for rendering with the template.

Features:
  - Converts markdown headings to LaTeX sections
  - Handles code blocks with language detection
  - Processes tables with proper formatting
  - Formats lists (ordered and unordered)
  - Handles blockquotes
  - Processes inline formatting (bold, italic)
  - Extracts document metadata from the markdown
  - Embeds config.tex content directly into the output file

Usage:
    python md2tex.py input.md [output.tex] [--title "Document Title"]

Dependencies:
    - jinja2 (install via pip install jinja2)
"""

import argparse
import os
import sys
import re
import datetime
from jinja2 import Template

# Regular expressions for parsing markdown
RE_HEADING = re.compile(r'^(#{1,6})\s+(.*?)(?:\s+\{#(.*?)\})?$')
RE_CODE_BLOCK_START = re.compile(r'^```(?:\s*(\S+))?$')
RE_CODE_BLOCK_END = re.compile(r'^```\s*$')
RE_TABLE_ROW = re.compile(r'^\|(.+)\|$')
RE_TABLE_DELIMITER = re.compile(r'^\|\s*(:?-{3,}:?\s*\|)+\s*$')
RE_LIST_ITEM = re.compile(r'^(\s*)([*+-]|\d+\.)\s+(.*)$')
RE_BLOCKQUOTE = re.compile(r'^>\s*(.*?)$')
RE_HORIZONTAL_RULE = re.compile(r'^(?:\s*[-*_]){3,}\s*$')
RE_BOLD = re.compile(r'\*\*(.+?)\*\*')
RE_ITALIC = re.compile(r'\*(.+?)\*')
RE_LINK = re.compile(r'\[(.+?)\]\((.+?)\)')
RE_IMAGE = re.compile(r'!\[(.+?)\]\((.+?)\)')

def read_file(file_path):
    """Read content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

def escape_latex(text):
    """Escape LaTeX special characters."""
    chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    for char, replacement in chars.items():
        # Don't replace inside code blocks that are marked with ```
        if char in text:
            text = text.replace(char, replacement)
    return text

def parse_table(lines, start_idx):
    """Parse a markdown table and return a table object."""
    # Get header line
    header_line = lines[start_idx].strip('| \t\n')
    headers = [header.strip() for header in header_line.split('|')]
    
    # Parse alignment from delimiter line
    delim_line = lines[start_idx + 1].strip('| \t\n')
    alignments = []
    for col in delim_line.split('|'):
        col = col.strip()
        if col.startswith(':') and col.endswith(':'):
            alignments.append('center')
        elif col.endswith(':'):
            alignments.append('right')
        else:
            alignments.append('left')
    
    # Get column specs from alignments
    col_spec = ''.join(['c' if align == 'center' else 
                       'r' if align == 'right' else 
                       'l' for align in alignments])
    
    # Parse row data
    rows = []
    i = start_idx + 2
    while i < len(lines) and RE_TABLE_ROW.match(lines[i]):
        row_line = lines[i].strip('| \t\n')
        row_cells = [cell.strip() for cell in row_line.split('|')]
        # Ensure we have the right number of cells
        while len(row_cells) < len(headers):
            row_cells.append('')
        rows.append(row_cells[:len(headers)])
        i += 1
    
    # Create table object
    table = {
        'caption': 'Table',
        'column_spec': col_spec,
        'env': 'tabular',
        'use_colors': True,
        'headers': headers,
        'rows': rows,
        'has_footer': False
    }
    
    return table, i - start_idx

def parse_list(lines, start_idx):
    """Parse a markdown list and return a list object."""
    list_type = "itemize" if lines[start_idx].strip()[0] in "*+-" else "enumerate"
    items = []
    i = start_idx
    
    # Track indentation level
    base_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())
    
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            if i < len(lines) and not RE_LIST_ITEM.match(lines[i]):
                break
            continue
            
        match = RE_LIST_ITEM.match(line)
        if not match:
            break
            
        indent = len(match.group(1))
        marker = match.group(2)
        content = match.group(3)
        
        # Handle list item based on indentation
        if indent == base_indent:
            # This is a top-level item
            items.append(content)
        else:
            # This is a sub-item, add to the last item
            if not isinstance(items[-1], dict):
                items[-1] = {
                    'text': items[-1],
                    'subitems': []
                }
            items[-1]['subitems'].append(content)
        
        i += 1
    
    # Create list object
    list_obj = {
        'type': list_type,
        'items': items
    }
    
    return list_obj, i - start_idx

def parse_code_block(lines, start_idx):
    """Parse a markdown code block and return a code block object."""
    # Get language from the start line
    match = RE_CODE_BLOCK_START.match(lines[start_idx])
    language = match.group(1) if match and match.group(1) else "text"
    
    # Collect code content
    content = []
    i = start_idx + 1
    while i < len(lines) and not RE_CODE_BLOCK_END.match(lines[i]):
        content.append(lines[i])
        i += 1
    
    # Skip the closing ```
    i += 1
    
    # Create code block object
    code_block = {
        'type': "listing",
        'language': language,
        'content': '\n'.join(content)
    }
    
    return code_block, i - start_idx

def parse_blockquote(lines, start_idx):
    """Parse a markdown blockquote and return a quote object."""
    content = []
    i = start_idx
    
    while i < len(lines) and RE_BLOCKQUOTE.match(lines[i]):
        match = RE_BLOCKQUOTE.match(lines[i])
        content.append(match.group(1))
        i += 1
    
    # Create quote object
    quote = {
        'type': "display",
        'content': '\n'.join(content)
    }
    
    return quote, i - start_idx

def format_markdown_text(text):
    """Format markdown text with inline formatting."""
    # Replace bold text
    text = RE_BOLD.sub(r'\\textbf{\1}', text)
    
    # Replace italic text
    text = RE_ITALIC.sub(r'\\textit{\1}', text)
    
    # Replace links
    text = RE_LINK.sub(r'\\href{\2}{\1}', text)
    
    # Replace images
    text = RE_IMAGE.sub(r'\\includegraphics{\2} % \1', text)
    
    # Escape LaTeX special characters (except in already processed parts)
    text = escape_latex(text)
    
    return text

def extract_title_from_markdown(lines):
    """Try to extract a title from the markdown content."""
    for line in lines[:10]:  # Check first 10 lines only
        match = RE_HEADING.match(line)
        if match and len(match.group(1)) == 1:  # Only h1 headings
            return match.group(2).strip()
    return None

def parse_markdown_to_template_data(md_text, title=None):
    """Parse markdown text and convert to template data structure."""
    lines = md_text.splitlines()
    
    # Initialize template data
    data = {
        'title': title or extract_title_from_markdown(lines) or "Untitled Document",
        'author': os.environ.get('USER', 'Anonymous'),
        'date': r'\today',  # LaTeX command to insert current date
        'executive_summary': "",
        'document_classification': "Internal",
        'distribution': "General",
        'version': "1.0",
        'show_toc': True,
        'sections': []
    }
    
    # Extract executive summary if present (first paragraph after title)
    for i, line in enumerate(lines):
        if i > 0 and line.strip() and not RE_HEADING.match(line):
            data['executive_summary'] = line.strip()
            break
    
    # Process the markdown content
    i = 0
    current_section = None
    
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
            
        # Process headings
        heading_match = RE_HEADING.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            title_text = heading_match.group(2)
            label = heading_match.group(3) if heading_match.group(3) else None
            
            section = {
                'level': level,
                'title': title_text,
                'label': label,
                'content': "",
                'drop_cap': level == 1,  # Only top level sections get drop caps
                'subsections': [],
                'tables': [],
                'fancy_tables': [],
                'lists': [],
                'boxes': [],
                'code_blocks': [],
                'algorithms': [],
                'quotes': []
            }
            
            if level == 1:
                data['sections'].append(section)
                current_section = section
            elif level == 2 and current_section:
                current_section['subsections'].append(section)
            elif level == 3 and current_section and current_section['subsections']:
                current_section['subsections'][-1]['subsections'].append(section)
                
            i += 1
            continue
            
        # Process code blocks
        code_block_match = RE_CODE_BLOCK_START.match(line)
        if code_block_match:
            code_block, lines_processed = parse_code_block(lines, i)
            if current_section:
                current_section['code_blocks'].append(code_block)
            i += lines_processed
            continue
            
        # Process tables
        table_match = RE_TABLE_ROW.match(line)
        if table_match and i + 1 < len(lines) and RE_TABLE_DELIMITER.match(lines[i + 1]):
            table, lines_processed = parse_table(lines, i)
            if current_section:
                current_section['tables'].append(table)
            i += lines_processed
            continue
            
        # Process lists
        list_match = RE_LIST_ITEM.match(line)
        if list_match:
            list_obj, lines_processed = parse_list(lines, i)
            if current_section:
                current_section['lists'].append(list_obj)
            i += lines_processed
            continue
            
        # Process blockquotes
        blockquote_match = RE_BLOCKQUOTE.match(line)
        if blockquote_match:
            quote, lines_processed = parse_blockquote(lines, i)
            if current_section:
                current_section['quotes'].append(quote)
            i += lines_processed
            continue
            
        # Process horizontal rules
        if RE_HORIZONTAL_RULE.match(line):
            # We don't actually need to do anything with these in LaTeX
            i += 1
            continue
            
        # Process regular paragraph text
        paragraph_content = format_markdown_text(line)
        if current_section:
            if current_section['content']:
                current_section['content'] += "\n\n" + paragraph_content
            else:
                current_section['content'] = paragraph_content
        i += 1
            
    return data

def markdown_to_latex(md_text, template_text, config_text, output_file, title=None):
    """Convert markdown to LaTeX using Jinja2 template."""
    # Parse markdown into template data
    template_data = parse_markdown_to_template_data(md_text, title)
    
    # Create Jinja2 template
    template = Template(template_text)
    
    # Render template with data
    latex_content = template.render(**template_data)
    
    # Replace reference to config.tex with actual content
    latex_content = latex_content.replace(r'\input{config.tex}', config_text)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"LaTeX document generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to LaTeX with Jinja2 template.")
    parser.add_argument("input_file", help="Path to the input Markdown file")
    parser.add_argument("output_file", nargs="?", help="Path to the output LaTeX file (optional)")
    parser.add_argument("--title", help="Document title (optional, overrides title from Markdown)")

    args = parser.parse_args()

    # Determine output file path
    output_file_path = args.output_file
    if not output_file_path:
        output_file_path = os.path.splitext(args.input_file)[0] + ".tex"

    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Read input files
    md_text = read_file(args.input_file)
    template_text = read_file('latex_template.tex.jinja')
    config_text = read_file('config.tex')

    # Convert markdown to LaTeX
    try:
        markdown_to_latex(md_text, template_text, config_text, output_file_path, args.title)
    except Exception as e:
        print(f"Error during Markdown to LaTeX conversion: {e}", file=sys.stderr)
        import traceback
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)