#!/usr/bin/env python3
"""
Fixes cover files to be compatible with direct inclusion in the main template.

This script:
1. Removes document structure (\documentclass, \begin{document}, \end{document})
2. Extracts needed TikZ libraries and packages
3. Adds a consistent header comment

Usage:
    python fix_covers.py
"""

import os
import re
import glob
import sys
from pathlib import Path

def process_cover_file(filename):
    """Process a cover file to make it compatible for direct inclusion."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip files that have already been processed
    if "% ========== COVER" in content and not "\\documentclass" in content:
        print(f"Skipping {filename} - already processed")
        return False
        
    # Extract cover number
    cover_num = re.search(r'cover(\d+)\.tex', filename).group(1)
    
    # Extract TikZ libraries
    tikz_libs = []
    for match in re.finditer(r'\\usetikzlibrary\{([^}]+)\}', content):
        tikz_libs.append(match.group(0))
    
    # Extract additional packages
    packages = []
    for match in re.finditer(r'\\usepackage(\[.*?\])?\{([^}]+)\}', content):
        if "config.tex" not in match.group(0):
            packages.append(match.group(0))
    
    # Extract document content
    doc_match = re.search(r'\\begin{document}(.*?)\\end{document}', content, re.DOTALL)
    if not doc_match:
        print(f"Warning: Could not find document structure in {filename}")
        return False
    
    doc_content = doc_match.group(1).strip()
    
    # Remove any \thispagestyle commands
    doc_content = re.sub(r'\\thispagestyle\{[^}]+\}', '', doc_content)
    
    # Build new content
    new_content = [
        f"% ========== COVER{cover_num}: PROFESSIONAL DESIGN ==========",
        "% Cover-specific dependencies"
    ]
    
    if tikz_libs:
        new_content.extend(tikz_libs)
    
    if packages:
        new_content.append("")
        new_content.extend(packages)
    
    new_content.append("")
    new_content.append(doc_content)
    
    # Write back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_content))
    
    print(f"Processed {filename}")
    return True

def main():
    # Process all cover files
    cover_path = Path("covers")
    if not cover_path.exists():
        print("Error: 'covers' directory not found")
        return 1
    
    cover_files = list(cover_path.glob("cover*.tex"))
    if not cover_files:
        print("No cover files found")
        return 1
    
    processed = 0
    for cover_file in cover_files:
        if process_cover_file(str(cover_file)):
            processed += 1
    
    print(f"Processed {processed} of {len(cover_files)} cover files")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 