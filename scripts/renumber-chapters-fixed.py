#!/usr/bin/env python3
"""
Fixed Chapter Renumbering Script for Symphony Book
==================================================

This script properly renumbers chapters after chapter 6 was removed.
It handles directory renaming and content updates separately and safely.

Usage: python scripts/renumber-chapters-fixed.py
"""

import os
import re
import shutil
import sys
from pathlib import Path
import tempfile

def main():
    """Main renumbering function"""
    print("Symphony Book Chapter Renumbering Script (Fixed)")
    print("=" * 55)
    
    # Confirm with user
    response = input("This will renumber chapters 7-26 to 6-25. Continue? (y/N): ")
    if response.lower() != 'y':
        print("Aborted.")
        return
    
    content_dir = Path("content")
    if not content_dir.exists():
        print("Error: content/ directory not found. Run from project root.")
        return
    
    # Step 1: Create mapping of old to new chapter numbers
    chapter_mapping = {}
    for old_num in range(7, 27):  # chapters 7-26
        new_num = old_num - 1     # become chapters 6-25
        chapter_mapping[old_num] = new_num
    
    print(f"Chapter mapping: {chapter_mapping}")
    
    # Step 2: Rename directories using temporary names first to avoid conflicts
    print("\nStep 1: Renaming chapter directories...")
    
    # First pass: rename to temporary names
    temp_mapping = {}
    for old_num in range(7, 27):
        old_dir = content_dir / f"chapter{old_num}"
        if old_dir.exists():
            temp_name = f"temp_chapter_{old_num}"
            temp_dir = content_dir / temp_name
            print(f"  Temp rename: {old_dir} -> {temp_dir}")
            shutil.move(str(old_dir), str(temp_dir))
            temp_mapping[old_num] = temp_dir
        else:
            print(f"  Warning: {old_dir} does not exist")
    
    # Second pass: rename from temp names to final names
    for old_num, new_num in chapter_mapping.items():
        if old_num in temp_mapping:
            temp_dir = temp_mapping[old_num]
            final_dir = content_dir / f"chapter{new_num}"
            print(f"  Final rename: {temp_dir} -> {final_dir}")
            shutil.move(str(temp_dir), str(final_dir))
    
    # Step 3: Update file contents
    print("\nStep 2: Updating file contents...")
    
    # Find all .tex files in the project
    tex_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(Path(root) / file)
    
    print(f"Found {len(tex_files)} .tex files to process")
    
    # Update each file
    updated_count = 0
    for tex_file in tex_files:
        if update_file_contents(tex_file, chapter_mapping):
            updated_count += 1
    
    print(f"Updated {updated_count} files")
    
    print("\nStep 3: Verification...")
    verify_renumbering(content_dir)
    
    print("\nChapter renumbering completed successfully!")
    print("Please review the changes and test compilation.")

def update_file_contents(file_path, chapter_mapping):
    """Update chapter references in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update patterns for each old->new mapping
        for old_num, new_num in chapter_mapping.items():
            # Pattern 1: \label{chap:chapterX} -> \label{chap:chapterY}
            content = re.sub(
                rf'\\label\{{chap:chapter{old_num}\}}',
                rf'\\label{{chap:chapter{new_num}}}',
                content
            )
            
            # Pattern 2: \ref{chap:chapterX} -> \ref{chap:chapterY}
            content = re.sub(
                rf'\\ref\{{chap:chapter{old_num}\}}',
                rf'\\ref{{chap:chapter{new_num}}}',
                content
            )
            
            # Pattern 3: content/chapterX/ -> content/chapterY/
            content = re.sub(
                rf'content/chapter{old_num}/',
                rf'content/chapter{new_num}/',
                content
            )
            
            # Pattern 4: Chapter X references in text (be more specific)
            content = re.sub(
                rf'\bChapter {old_num}\b',
                rf'Chapter {new_num}',
                content
            )
            
            # Pattern 5: CHAPTER X in covers and headers
            content = re.sub(
                rf'\bCHAPTER {old_num}\b',
                rf'CHAPTER {new_num}',
                content
            )
            
            # Pattern 6: chapter{old_num} in comments (be more specific)
            content = re.sub(
                rf'\bchapter{old_num}\b',
                rf'chapter{new_num}',
                content
            )
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated: {file_path}")
            return True
        return False
    
    except Exception as e:
        print(f"  Error updating {file_path}: {e}")
        return False

def verify_renumbering(content_dir):
    """Verify the renumbering was successful"""
    print("Verifying chapter directories exist:")
    
    # Check that we have chapters 0-5 and 6-25 (no chapter6 gap)
    expected_chapters = list(range(0, 26))  # 0-25 = 26 chapters total
    
    missing_chapters = []
    extra_chapters = []
    
    for i in expected_chapters:
        chapter_dir = content_dir / f"chapter{i}"
        if not chapter_dir.exists():
            missing_chapters.append(i)
    
    # Check for any unexpected chapter directories
    for item in content_dir.iterdir():
        if item.is_dir() and item.name.startswith("chapter"):
            try:
                chapter_num = int(item.name.replace("chapter", ""))
                if chapter_num not in expected_chapters:
                    extra_chapters.append(chapter_num)
            except ValueError:
                pass
    
    if missing_chapters:
        print(f"  Warning: Missing chapters: {missing_chapters}")
    
    if extra_chapters:
        print(f"  Warning: Unexpected chapters: {extra_chapters}")
    
    if not missing_chapters and not extra_chapters:
        print("  ✓ All expected chapters (0-25) are present")
    
    # Verify we have exactly 26 chapters (0-25)
    chapter_dirs = [d for d in content_dir.iterdir() 
                   if d.is_dir() and d.name.startswith("chapter")]
    print(f"  Total chapters found: {len(chapter_dirs)}")
    
    # List the chapters we have
    chapter_nums = []
    for d in chapter_dirs:
        try:
            num = int(d.name.replace("chapter", ""))
            chapter_nums.append(num)
        except ValueError:
            pass
    
    chapter_nums.sort()
    print(f"  Chapters present: {chapter_nums}")

if __name__ == "__main__":
    main()