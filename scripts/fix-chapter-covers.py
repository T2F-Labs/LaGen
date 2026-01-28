#!/usr/bin/env python3
"""
Fix Chapter Cover Page Breaks
Adds \newpage at the beginning of chapter cover files from chapters 5-25
to ensure each chapter starts on a new page.
"""

import os
import re

def fix_chapter_cover(chapter_num):
    """Fix a single chapter cover file by adding \newpage at the beginning."""
    cover_file = f"content/chapter{chapter_num}/chapter_cover.tex"
    
    if not os.path.exists(cover_file):
        print(f"⚠️  Chapter {chapter_num} cover file not found: {cover_file}")
        return False
    
    try:
        # Read the current content
        with open(cover_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if \newpage is already at the beginning
        if content.strip().startswith('\\newpage'):
            print(f"✅ Chapter {chapter_num} already has \\newpage at the beginning")
            return True
        
        # Find the first comment line (should be the chapter header comment)
        lines = content.split('\n')
        first_comment_idx = -1
        
        for i, line in enumerate(lines):
            if line.strip().startswith('%') and 'CHAPTER' in line.upper() and 'COVER' in line.upper():
                first_comment_idx = i
                break
        
        if first_comment_idx == -1:
            print(f"⚠️  Could not find chapter header comment in {cover_file}")
            return False
        
        # Insert \newpage before the first comment
        lines.insert(first_comment_idx, '\\newpage')
        lines.insert(first_comment_idx + 1, '')  # Add blank line after \newpage
        
        # Write the modified content back
        modified_content = '\n'.join(lines)
        
        with open(cover_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print(f"✅ Fixed Chapter {chapter_num} - added \\newpage")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing Chapter {chapter_num}: {e}")
        return False

def main():
    """Fix all chapter covers from 5 to 25."""
    print("🔧 Fixing chapter cover page breaks...")
    print("=" * 50)
    
    success_count = 0
    total_count = 0
    
    # Process chapters 5-25
    for chapter_num in range(5, 26):
        total_count += 1
        if fix_chapter_cover(chapter_num):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 Summary: {success_count}/{total_count} chapters fixed successfully")
    
    if success_count == total_count:
        print("🎉 All chapter covers now start on new pages!")
    else:
        print(f"⚠️  {total_count - success_count} chapters had issues")

if __name__ == "__main__":
    main()