#!/usr/bin/env python3
"""
Systematic fix for malformed environment endings in Symphony Book LaTeX files.
Fixes \end{environment> to \end{environment} across all affected files.

This script addresses the widespread issue documented in the troubleshooting guide
under "Runaway Arguments & Malformed Endings".
"""

import os
import re
import glob

def fix_malformed_environments(file_path):
    """Fix malformed environment endings in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix malformed environment endings: \end{environment> -> \end{environment}
        content = re.sub(r'\\end\{([^}]+)>', r'\\end{\1}', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Count fixes made
            fixes = len(re.findall(r'\\end\{[^}]+>', original_content))
            print(f"✅ Fixed {fixes} malformed environment endings in {file_path}")
            return fixes
        else:
            print(f"⚪ No malformed environments found in {file_path}")
            return 0
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return 0

def main():
    """Main function to fix all affected files."""
    print("🔧 Symphony Book: Fixing Malformed Environment Endings")
    print("=" * 60)
    
    # Find all .tex files in content directory
    tex_files = glob.glob("content/**/*.tex", recursive=True)
    
    total_fixes = 0
    files_fixed = 0
    
    for file_path in sorted(tex_files):
        fixes = fix_malformed_environments(file_path)
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes
    
    print("=" * 60)
    print(f"🎯 SUMMARY:")
    print(f"   Files processed: {len(tex_files)}")
    print(f"   Files fixed: {files_fixed}")
    print(f"   Total fixes applied: {total_fixes}")
    print(f"   Status: {'✅ SUCCESS' if total_fixes > 0 else '⚪ NO ISSUES FOUND'}")
    
    if total_fixes > 0:
        print("\n📋 NEXT STEPS:")
        print("   1. Test compilation: xelatex main.tex")
        print("   2. Verify no 'Runaway argument' errors remain")
        print("   3. Check document output quality")

if __name__ == "__main__":
    main()