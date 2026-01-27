# LaTeX Troubleshooting Guide: Symphony Book Project

## Overview
This document provides a systematic approach to fixing common LaTeX compilation errors and warnings encountered in professional document generation systems. The solutions are based on real troubleshooting experience with the Symphony Book project.

## Critical Error Categories & Solutions

### 1. **"Not in outer par mode" Errors**

**Problem**: Tables inside tcolorbox environments cause compilation failure
```
LaTeX Error: Not in outer par mode.
./content/chapter2/symphony-vision.tex, 39
```

**Root Cause**: Floating environments (`table`) cannot be used inside non-floating environments (`tcolorbox`, `minipage`)

**Recipe**:
1. Replace `\begin{table}[h]\centering` with `\begin{center}`
2. Replace `\caption{...}` with `\captionof{table}{...}`
3. Replace `\end{table}` with `\end{center}`
4. Add `\usepackage{caption}` to preamble

**Automated Fix**:
```python
# Replace table environments with center environments
content = re.sub(r'\\begin\{table\}\[h\]\s*\n\s*\\centering', r'\\begin{center}', content)
content = re.sub(r'\\caption\{([^}]+)\}', r'\\captionof{table}{\1}', content)
content = re.sub(r'\\end\{table\}', r'\\end{center}', content)
```

### 2. **pgfkeys Errors**

**Problem**: Unquoted parameters in tcolorbox options
```
Package pgfkeys Error: I do not know the key '/tcb/Don't Replace'
```

**Recipe**:
- Quote parameters containing special characters: `title={Don't Replace}`
- Use braces around complex parameter values

### 3. **Runaway Arguments & Malformed Endings**

**Problem**: Missing closing braces in environment endings
```
Runaway argument?
./content/chapter3/competitive-analysis.tex, 221
```

**Recipe**:
1. Check for malformed `\end{...>` (missing closing brace)
2. Fix with `\end{...}`
3. Verify all environments are properly balanced

**Automated Check**:
```python
# Find malformed endings
malformed = re.findall(r'\\end\{[^}]*>', content)
# Fix them
content = re.sub(r'\\end\{([^}]+)>', r'\\end{\1}', content)
```

### 4. **Extra Closing Braces**

**Problem**: Extra `}` characters causing brace mismatch
```
Extra }, or forgotten \endgroup.
```

**Recipe**:
- Remove extra `}` from `\end{environment}}`
- Use systematic search: `\\end\{[^}]+\}\}`

## Warning Resolution Recipes

### 1. **Hyperref Bookmarks Warning**

**Problem**: Duplicate bookmarks option
```
Package hyperref Warning: Option `bookmarks' has already been used
```

**Recipe**:
```latex
% Use \PassOptionsToPackage before loading
\PassOptionsToPackage{bookmarks=true}{hyperref}
\usepackage{hyperref}
```

### 2. **Biblatex Conflicting Options**

**Problem**: Option conflicts
```
Package biblatex Warning: Conflicting options. '<namepart>inits' conflicts with 'uniquename=full'
```

**Recipe**:
```latex
\usepackage[
    uniquename=init,  % Add explicit resolution
    giveninits=true
]{biblatex}
```

### 3. **Siunitx Physics Conflict**

**Problem**: Package command conflicts
```
Package siunitx Warning: Detected the "physics" package: omitting definition of \qty
```

**Recipe**:
```latex
\AtBeginDocument{\RenewCommandCopy\qty\SI}
```

### 4. **Caption hypcap Warnings**

**Problem**: hypcap ignored for \captionof
```
Package caption Warning: The option `hypcap=true' will be ignored
```

**Recipe**:
```latex
\usepackage{caption}
\captionsetup[table]{hypcap=false}
```

### 5. **Fancyhdr Footskip Warning**

**Problem**: Insufficient footer space
```
Package fancyhdr Warning: \footskip is too small
```

**Recipe**:
```latex
\geometry{footskip=50pt}  % Increase from default 40pt
```

## Systematic Troubleshooting Process

### Phase 1: Critical Error Resolution
1. **Fix table environments** (highest priority)
2. **Fix malformed syntax** (braces, quotes)
3. **Balance environments** (begin/end pairs)

### Phase 2: Warning Cleanup
1. **Package conflicts** (options, loading order)
2. **Configuration warnings** (geometry, caption)
3. **Compatibility issues** (siunitx/physics)

### Phase 3: Verification
1. **Environment balance check**
2. **Compilation test**
3. **Warning analysis**

## Automated Fix Scripts

### Table Environment Fixer
```python
def fix_tables(content):
    # Convert table to center environments
    content = re.sub(r'\\begin\{table\}\[h\]\s*\n\s*\\centering', r'\\begin{center}', content)
    content = re.sub(r'\\caption\{([^}]+)\}', r'\\captionof{table}{\1}', content)
    content = re.sub(r'\\end\{table\}', r'\\end{center}', content)
    return content
```

### Brace Fixer
```python
def fix_braces(content):
    # Fix extra closing braces
    content = re.sub(r'\\end\{([^}]+)\}\}', r'\\end{\1}', content)
    # Fix malformed endings
    content = re.sub(r'\\end\{([^}]+)>', r'\\end{\1}', content)
    return content
```

### Environment Balance Checker
```python
def check_balance(content):
    for env in ['center', 'infobox', 'alertbox', 'successbox']:
        begin_count = len(re.findall(rf'\\begin\{{{env}\}}', content))
        end_count = len(re.findall(rf'\\end\{{{env}\}}', content))
        if begin_count != end_count:
            print(f"Unbalanced {env}: {begin_count} begin, {end_count} end")
```

## Prevention Best Practices

### 1. **Environment Usage**
- Never use floating environments inside non-floating containers
- Always use `\captionof{table}{...}` for non-floating tables
- Quote complex tcolorbox parameters

### 2. **Module Loading**
- Use `\PassOptionsToPackage` for early option setting
- Load packages in correct order (hyperref last)
- Handle package conflicts explicitly

### 3. **Syntax Checking**
- Verify brace matching
- Check environment balance
- Test compilation frequently

## Quick Reference Commands

### Essential Packages for Fixes
```latex
\usepackage{caption}        % For \captionof
\usepackage{ifthen}         % For conditional loading
\PassOptionsToPackage{...}{hyperref}  % For option conflicts
```

### Common Replacements
```latex
% OLD (problematic)
\begin{table}[h]
\centering
...
\caption{Title}
\end{table}

% NEW (working)
\begin{center}
...
\captionof{table}{Title}
\end{center}
```

## Success Metrics

### Clean Compilation Indicators
- ✅ No "Not in outer par mode" errors
- ✅ No "Runaway argument" errors  
- ✅ No "Emergency stop" messages
- ✅ Minimal package warnings only
- ✅ PDF generation successful

### Warning Reduction
- ✅ Hyperref warnings eliminated/reduced
- ✅ Package conflict warnings resolved
- ✅ Geometry warnings fixed
- ✅ Caption warnings suppressed appropriately

## Conclusion

The key to successful LaTeX troubleshooting is systematic error categorization and targeted fixes. Most compilation failures stem from fundamental LaTeX limitations (like floating environments in non-floating contexts) rather than complex package issues. Address critical errors first, then clean up warnings for a professional result.

**Remember**: Some warnings are informational and harmless. Focus on eliminating errors and critical warnings that affect functionality or output quality.