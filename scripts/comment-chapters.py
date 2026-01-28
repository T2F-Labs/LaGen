#!/usr/bin/env python3
"""
Simple LaTeX Chapter Commenter - One Time Run
Just comments out all \chapter*{} statements. No bullshit.
"""

import os
import re
from pathlib import Path

def main():
    print("🔧 Commenting out all \\chapter*{} statements...")
    
    # Find all .tex files in content/ directory only
    tex_files = []
    content_dir = Path('content')
    if content_dir.exists():
        for tex_file in content_dir.rglob("*.tex"):
            tex_files.append(tex_file)
    else:
        print("❌ content/ directory not found!")
        return
    
    print(f"📁 Found {len(tex_files)} .tex files")
    
    # Pattern to match \chapter*{...} statements
    chapter_pattern = re.compile(r'^(\s*)(\\chapter\*\{[^}]*\})', re.MULTILINE)
    
    total_changes = 0
    files_modified = 0
    
    # Process each file
    for file_path in tex_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if no chapter statements
            if '\\chapter*' not in content:
                continue
            
            # Comment out chapter statements
            def replace_chapter(match):
                indent = match.group(1)
                chapter_cmd = match.group(2)
                return f"{indent}% {chapter_cmd}"
            
            modified_content = chapter_pattern.sub(replace_chapter, content)
            changes = len(chapter_pattern.findall(content))
            
            if changes > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"✓ {file_path}: commented out {changes} chapter statement(s)")
                total_changes += changes
                files_modified += 1
                
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")
    
    print(f"\n🎉 Done! Modified {files_modified} files, commented out {total_changes} chapter statements")
    print("💡 Use git to rollback if needed")

if __name__ == "__main__":
    main()