# LaTeX Troubleshooting Guide: Symphony Book Project

## Overview
This document provides a systematic approach to fixing common LaTeX compilation errors and warnings encountered in professional document generation systems. The solutions are based on real troubleshooting experience with the Symphony Book project.

## Critical Error Categories & Solutions

### 1. **Undefined Control Sequence Errors**

**Problem**: Commands not defined in loaded packages
```
Undefined control sequence.
./content/chapter6/chapter_cover.tex, 45
The control sequence at the end of the top line
of your error message was never \def'ed.
```

**Common Cases**:
- `\hexagon` - Not defined in standard math packages
- Custom symbols not available

**Recipe**:
1. Replace undefined symbols with standard alternatives
2. For `\hexagon`, use `\diamond` or other standard math symbols
3. Ensure required packages are loaded for custom symbols

**Example Fix**:
```latex
% OLD (problematic)
\raisebox{-0.2ex}{\Large$\hexagon$}

% NEW (working)
\raisebox{-0.2ex}{\Large$\diamond$}
```

### 2. **Missing Math Mode Errors**

**Problem**: Text appearing outside proper environments
```
Missing $ inserted.
./content/chapter8/generic-primitives-approach.tex, 105
```

**Root Cause**: Text content appearing outside `\begin{lstlisting}` or other proper environments

**Recipe**:
1. Ensure all code content is within `\begin{lstlisting}...\end{lstlisting}`
2. Check for missing `\begin{lstlisting}` statements
3. Verify environment balance

### 3. **Listings Language Errors**

**Problem**: Undefined languages in listings package
```
Package Listings Error: language toml undefined.
Package Listings Error: language javascript undefined.
Package Listings Error: language rust undefined.
Package Listings Error: language json undefined.
Package Listings Error: language typescript undefined.
```

**Recipe**:
1. Replace `language=toml` with `language=bash` for configuration files
2. Replace `language=javascript` with `language=JavaScript` (capital J)
3. Define custom languages in code module if needed
4. Ensure EnableCode=true to load language definitions

**Language Mapping**:
```latex
% Supported alternatives
language=bash        % For TOML, YAML, config files
language=JavaScript  % For JavaScript (capital J)
language=Python      % For Python
language=C           % For C/C++
language=rust        % Custom definition required
language=json        % Custom definition required
language=typescript  % Custom definition required
```

**Custom Language Definitions** (add to modules/code.tex):
```latex
% Define Rust language
\lstdefinelanguage{Rust}{
  morekeywords=[1]{as, break, const, continue, crate, else, enum, extern, false, fn, for, if, impl, in, let, loop, match, mod, move, mut, pub, ref, return, self, Self, static, struct, super, trait, true, type, unsafe, use, where, while, async, await, dyn},
  morekeywords=[2]{bool, char, f32, f64, i8, i16, i32, i64, i128, isize, str, u8, u16, u32, u64, u128, usize, Box, Vec, HashMap, String, Option, Result},
  sensitive,
  morecomment=[s]{/*}{*/},
  morecomment=[l]//,
  morestring=[b]",
  morestring=[d]'
}[keywords, comments, strings]

% Define JSON language
\lstdefinelanguage{json}{
  morekeywords=[1]{true, false, null},
  sensitive=true,
  morestring=[b]",
  comment=[l]{//},
  morecomment=[s]{/*}{*/}
}

% Define TypeScript language
\lstdefinelanguage{TypeScript}{
  morekeywords=[1]{break, continue, delete, else, for, function, if, in, new, return, this, typeof, var, void, while, with, case, catch, class, const, default, do, enum, export, extends, finally, from, implements, import, instanceof, let, static, super, switch, throw, try, await, async, interface, type, namespace, module, declare, public, private, protected, readonly, abstract},
  morekeywords=[2]{false, null, true, boolean, number, undefined, string, any, never, unknown, Array, Boolean, Date, Math, Number, String, Object, Promise},
  sensitive,
  morecomment=[s]{/*}{*/},
  morecomment=[l]//,
  morestring=[b]',
  morestring=[b]",
  morestring=[b]`
}[keywords, comments, strings]
```

### 4. **List Environment Errors**

**Problem**: `\item` commands outside list environments
```
LaTeX Error: Lonely \item--perhaps a missing list environment.
```

**Recipe**:
1. Ensure all `\item` commands are within list environments
2. Add missing `\begin{compactlist}` or `\begin{itemize}` statements
3. Check for unbalanced list environments

**Fix Pattern**:
```latex
% OLD (problematic)
\end{compactlist}
    \item \textbf{Item}: Description

% NEW (working)
\end{compactlist}

\begin{compactlist}
    \item \textbf{Item}: Description
\end{compactlist}
```

### 5. **File Path Errors**

**Problem**: Incorrect relative paths in `\input` statements
```
LaTeX Error: File `content/chapter11/capability-model.tex' not found.
```

**Recipe**:
1. Use relative paths from the current directory
2. Remove full path prefixes when already in the correct directory
3. Verify file existence and correct spelling

**Path Fix**:
```latex
% OLD (problematic from within chapter11/)
\input{content/chapter11/capability-model.tex}

% NEW (working from within chapter11/)
\input{capability-model.tex}
```

### 6. **Duplicate Label Errors**

**Problem**: Same label used in multiple locations
```
Label `subsec:evaluation-methodology' multiply defined.
```

**Recipe**:
1. Make labels unique by adding context prefixes
2. Use descriptive, specific label names
3. Search for duplicate labels before adding new ones

**Label Naming Pattern**:
```latex
% OLD (generic, likely to duplicate)
\label{subsec:evaluation-methodology}

% NEW (specific, unique)
\label{subsec:feature-comparison-methodology}
\label{subsec:competitive-analysis-methodology}
```

### 7. **"Not in outer par mode" Errors**

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

### 8. **pgfkeys Errors**

**Problem**: Unquoted parameters in tcolorbox options
```
Package pgfkeys Error: I do not know the key '/tcb/Don't Replace'
```

**Recipe**:
- Quote parameters containing special characters: `title={Don't Replace}`
- Use braces around complex parameter values

### 9. **Runaway Arguments & Malformed Endings**

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

**Common Malformed Patterns**:
```latex
% WRONG (missing closing brace)
\end{tabular>
\end{table>
\end{description>
\end{figure>

% CORRECT
\end{tabular}
\end{table}
\end{description}
\end{figure}
```

### 10. **Extra Closing Braces**

**Problem**: Extra `}` characters causing brace mismatch
```
Extra }, or forgotten \endgroup.
```

**Recipe**:
- Remove extra `}` from `\end{environment}}`
- Use systematic search: `\\end\{[^}]+\}\}`

### 11. **Package Command Dependencies**

**Problem**: Commands used before required packages are loaded
```
Undefined control sequence.
./modules/typography-advanced.tex, 99
l.99 \MakeOuterQuote{"}
LaTeX Error: Missing \begin{document}.
```

**Root Cause**: `\MakeOuterQuote` command used before csquotes package is loaded

**Recipe**:
1. Ensure package is loaded before using its commands
2. Move command calls to after package loading
3. Use conditional loading when packages are optional

**Fix Pattern**:
```latex
% OLD (problematic)
\usepackage{somepackage}
\SomeCommand{}  % In different file loaded before package

% NEW (working)
\usepackage{somepackage}
\SomeCommand{}  % After package is loaded
```

**Specific csquotes Fix**:
```latex
% In config.tex - load csquotes then configure
\usepackage[autostyle=true,english=american]{csquotes}
\MakeOuterQuote{"}  % After csquotes is loaded

% In typography module - remove the command
% \MakeOuterQuote{"}  % Comment out or remove
```

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

### 6. **Package Loading Order Warnings**

**Problem**: fvextra/csquotes loading order
```
Package fvextra Warning: csquotes should be loaded after fvextra
```

**Recipe**:
```latex
% Load csquotes after code module (which loads minted/fvextra)
\ifthenelse{\equal{\EnableCode}{true}}{
    \input{modules/code.tex}
}{}
% Then load csquotes
\usepackage[autostyle=true,english=american]{csquotes}
```

### 7. **Lettrine Spacing Warnings**

**Problem**: Drop caps don't fit on page
```
Package lettrine Warning: The dropped cap S doesn't fit on page
```

**Recipe**:
```latex
% Add vertical space before lettrine
\vspace{0.5cm}
\lettrine{S}{ymphony} continues normally...
```

### 8. **Float Specifier Warnings**

**Problem**: Float placement restrictions
```
`h' float specifier changed to `ht'
```

**Recipe**:
```latex
% Use more flexible float specifiers
\begin{table}[ht]  % Instead of [h]
\begin{figure}[htb] % Instead of [h]
```

### 9. **Hyperref Bookmark Warnings**

**Problem**: Bookmark anchor conflicts
```
Package hyperref Warning: The anchor of a bookmark and its parent's must not be the same
```

**Recipe**:
```latex
% Add spacing between section and subsection
\section{Title}
\vspace{0.3cm}
\subsection{Subtitle}
```

## Systematic Troubleshooting Process

### Phase 1: Critical Error Resolution
1. **Fix undefined control sequences** (highest priority)
2. **Fix package command dependencies** (commands before packages)
3. **Fix malformed syntax** (braces, quotes, environments)
4. **Balance environments** (begin/end pairs)
5. **Fix file path issues** (missing files, incorrect paths)

### Phase 2: Language and Environment Fixes
1. **Fix listings language issues** (undefined languages)
2. **Fix list environment problems** (lonely items)
3. **Fix math mode issues** (missing environments)
4. **Resolve duplicate labels** (make unique)
5. **Enable required modules** (code module for language definitions)

### Phase 3: Warning Cleanup
1. **Package loading order** (fvextra before csquotes)
2. **Package conflicts** (siunitx/physics, options)
3. **Typography spacing** (lettrine, drop caps)
4. **Float placement** (table/figure specifiers)
5. **Configuration warnings** (geometry, caption)

### Phase 4: Verification
1. **Environment balance check**
2. **Package dependency verification**
3. **Module loading order test**
4. **Compilation test**
5. **Warning analysis**

## Automated Fix Scripts

### Undefined Symbol Fixer
```python
def fix_undefined_symbols(content):
    # Replace common undefined symbols
    content = re.sub(r'\\hexagon', r'\\diamond', content)
    return content
```

### Listings Language Fixer
```python
def fix_listings_languages(content):
    # Fix common language issues
    content = re.sub(r'language=toml', r'language=bash', content)
    content = re.sub(r'language=javascript', r'language=JavaScript', content)
    return content
```

### List Environment Fixer
```python
def fix_list_environments(content):
    # Find lonely items and wrap in environments
    # This requires more sophisticated parsing
    return content
```

### File Path Fixer
```python
def fix_file_paths(content):
    # Fix common path issues
    content = re.sub(r'\\input\{content/chapter(\d+)/([^}]+)\}', 
                    r'\\input{\2}', content)
    return content
```

### Label Uniqueness Fixer
```python
def fix_duplicate_labels(content, context_prefix):
    # Add context prefix to labels
    content = re.sub(r'\\label\{(subsec:[^}]+)\}', 
                    rf'\\label{{{context_prefix}-\1}}', content)
    return content
```

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

### Package Command Dependencies Fixer
```python
def fix_package_dependencies(content):
    # Move commands that require packages to after package loading
    # Example: Move \MakeOuterQuote after csquotes
    content = re.sub(r'\\MakeOuterQuote\{[^}]+\}', '', content)  # Remove from modules
    return content
```

### Environment Balance Checker
```python
def check_balance(content):
    for env in ['center', 'infobox', 'alertbox', 'successbox', 'compactlist', 'lstlisting']:
        begin_count = len(re.findall(rf'\\begin\{{{env}\}}', content))
        end_count = len(re.findall(rf'\\end\{{{env}\}}', content))
        if begin_count != end_count:
            print(f"Unbalanced {env}: {begin_count} begin, {end_count} end")
```

### Module Loading Order Fixer
```python
def fix_module_loading_order(config_content):
    # Ensure proper loading sequence for packages with dependencies
    # Example: Load code module before csquotes to avoid fvextra warnings
    return config_content
```

## Prevention Best Practices

### 1. **Symbol Usage**
- Use only standard LaTeX symbols or define custom ones properly
- Check symbol availability in loaded packages
- Provide fallbacks for undefined symbols

### 2. **Environment Usage**
- Never use floating environments inside non-floating containers
- Always use `\captionof{table}{...}` for non-floating tables
- Quote complex tcolorbox parameters
- Ensure all environments are properly balanced

### 3. **Listings Configuration**
- Use supported language names (check documentation)
- Define custom languages when needed
- Test language definitions before use

### 4. **File Organization**
- Use relative paths consistently
- Verify file existence before including
- Use descriptive, unique file names

### 5. **Label Management**
- Use descriptive, context-specific labels
- Check for duplicates before adding new labels
- Follow consistent naming conventions

### 7. **Package Dependencies**
- Ensure packages are loaded before using their commands
- Move command calls to appropriate locations after package loading
- Use conditional loading for optional package features
- Check package documentation for command requirements

### 8. **Module Loading Order**
- Load packages in correct dependency order
- Handle package conflicts with proper sequencing
- Use `\PassOptionsToPackage` for early option setting
- Test module combinations for compatibility
### 9. **Syntax Checking**
- Verify brace matching
- Check environment balance
- Test compilation frequently
- Validate package command usage

## Quick Reference Commands

### Essential Packages for Fixes
```latex
\usepackage{caption}        % For \captionof
\usepackage{ifthen}         % For conditional loading
\usepackage{listings}       % For code listings
\PassOptionsToPackage{...}{hyperref}  % For option conflicts
```

### Common Replacements
```latex
% Undefined symbols
\hexagon → \diamond

% Listings languages
language=toml → language=toml (with proper definition)
language=javascript → language=JavaScript (capital J)

% File paths (from within chapter directory)
\input{content/chapter11/file.tex} → \input{file.tex}

% Table environments (inside tcolorbox)
\begin{table}[h]\centering → \begin{center}
\caption{Title} → \captionof{table}{Title}
\end{table} → \end{center}

% Float specifiers
\begin{table}[h] → \begin{table}[ht]
\begin{figure}[h] → \begin{figure}[htb]

% Package command dependencies
% In module file:
\MakeOuterQuote{"} → % Remove or comment out
% In config file after csquotes:
\usepackage{csquotes}
\MakeOuterQuote{"}  % Add after package loading

% Module enabling
\newcommand{\EnableCode}{false} → \newcommand{\EnableCode}{true}
```

## Success Metrics

### Clean Compilation Indicators
- ✅ No "Undefined control sequence" errors
- ✅ No "Missing \begin{document}" errors
- ✅ No "Missing $ inserted" errors
- ✅ No "Listings Error" messages
- ✅ No "Lonely \item" errors
- ✅ No "File not found" errors
- ✅ No "multiply defined" label errors
- ✅ No "Not in outer par mode" errors
- ✅ No "Runaway argument" errors
- ✅ No "Emergency stop" messages
- ✅ No package command dependency errors
- ✅ Proper module loading (EnableCode=true for listings)
- ✅ Minimal package warnings only
- ✅ PDF generation successful

### Warning Reduction
- ✅ Hyperref warnings eliminated/reduced
- ✅ Package conflict warnings resolved (siunitx/physics)
- ✅ Package loading order warnings fixed (fvextra/csquotes)
- ✅ Geometry warnings fixed (footskip)
- ✅ Caption warnings suppressed appropriately
- ✅ Lettrine spacing warnings resolved
- ✅ Float specifier warnings minimized
- ✅ Lineno package warnings acknowledged

## Conclusion

The key to successful LaTeX troubleshooting is systematic error categorization and targeted fixes. Most compilation failures stem from:

1. **Undefined symbols** - Use standard alternatives or define properly
2. **Package dependencies** - Load packages before using their commands
3. **Environment misuse** - Ensure proper nesting and balance
4. **Language configuration** - Enable code module and define custom languages
5. **File path issues** - Use correct relative paths
6. **Label conflicts** - Make labels unique and descriptive
7. **Module configuration** - Enable required modules (EnableCode=true for listings)
8. **Package loading order** - Load dependencies in correct sequence

Address critical errors first, then clean up warnings for a professional result.

**Remember**: Some warnings are informational and harmless. Focus on eliminating errors and critical warnings that affect functionality or output quality.

## Recent Fixes Applied (Symphony Book Project)

### Major Error Resolutions:
1. **EnableCode Module**: Changed from false to true to load language definitions
2. **JavaScript/TOML Languages**: Proper definitions added to code module
3. **csquotes/MakeOuterQuote**: Fixed package dependency order
4. **Lettrine Spacing**: Added vertical space for proper drop cap fitting
5. **Duplicate Labels**: Made all labels unique with context prefixes
6. **Float Specifiers**: Changed restrictive [h] to flexible [ht]/[htb]
7. **Package Loading Order**: csquotes after fvextra to avoid warnings

### System Improvements:
- Complete language support for JavaScript and TOML
- Proper package dependency management
- Enhanced typography with correct spacing
- Optimized warning reduction strategies
- Complete error prevention patterns

### 12. **pgfplots Axis Environment Errors**

**Problem**: Undefined axis environment for charts and graphs
```
LaTeX Error: Environment axis undefined.
./content/appendices/appendix-e/latency-benchmarks.tex, 117
Undefined control sequence.
./content/appendices/appendix-e/latency-benchmarks.tex, 127
```

**Root Cause**: pgfplots package not loaded for chart creation

**Recipe**:
1. Add pgfplots package to mathematics module
2. Set compatibility version for consistent behavior
3. Ensure EnableMathematics=true in main.tex

**Fix for modules/mathematics.tex**:
```latex
% Load pgfplots for charts and graphs
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

**Module Configuration**:
```latex
% In main.tex - ensure mathematics module is enabled
\newcommand{\EnableMathematics}{true}
```

### 13. **Article Class Chapter Commands**

**Problem**: Undefined control sequence for \chapter* in article class
```
Undefined control sequence.
./content/appendices/appendix-a/entry.tex, 2
l.2 \chapter*{Appendix A: Glossary of Terms}
```

**Root Cause**: Article document class doesn't support \chapter commands

**Recipe**:
1. Comment out \chapter* commands in article class documents
2. Use \section* for top-level divisions instead
3. Keep \addcontentsline for table of contents entries

**Fix Pattern**:
```latex
% WRONG (in article class)
\chapter*{Appendix A: Glossary of Terms}

% CORRECT (in article class)
% \chapter*{Appendix A: Glossary of Terms}
\addcontentsline{toc}{chapter}{Appendix A: Glossary of Terms}

% OR use section instead
\section*{Appendix A: Glossary of Terms}
\addcontentsline{toc}{section}{Appendix A: Glossary of Terms}
```

**Document Class Comparison**:
```latex
% Book/Report class - supports chapters
\documentclass{book}
\chapter{Chapter Title}
\chapter*{Unnumbered Chapter}

% Article class - sections only
\documentclass{article}
\section{Section Title}
\section*{Unnumbered Section}
```

### 14. **Float Specifier Warnings**

**Problem**: Restrictive float placement warnings
```
`h' float specifier changed to `ht'.
./content/appendices/appendix-e/latency-benchmarks.tex
```

**Root Cause**: `[h]` float specifier is too restrictive for LaTeX's float placement algorithm

**Recipe**:
1. Replace `[h]` with `[ht]` for tables
2. Replace `[h]` with `[htb]` for figures
3. Use more flexible placement options

**Fix Pattern**:
```latex
% RESTRICTIVE (causes warnings)
\begin{table}[h]
\begin{figure}[h]

% FLEXIBLE (no warnings)
\begin{table}[ht]
\begin{figure}[htb]
```

**Float Specifier Guide**:
- `h` = here only (too restrictive)
- `t` = top of page
- `b` = bottom of page
- `p` = separate page
- `!` = override restrictions
- `H` = exactly here (requires float package)

### 15. **Hyperref Bookmark Warnings**

**Problem**: Bookmark anchor conflicts
```
Package hyperref Warning: The anchor of a bookmark and its parent's must not be the same. Added a new anchor on input line 11.
```

**Root Cause**: Section and subsection anchors are too close together

**Recipe**:
1. Add vertical space between bookmark levels
2. Use `\vspace{0.3cm}` after main headings
3. Use `\vspace{0.2cm}` before subsections

**Fix Pattern**:
```latex
% PROBLEMATIC (anchors too close)
\addcontentsline{toc}{chapter}{Appendix A}
\section*{Overview}
\addcontentsline{toc}{section}{Overview}

% FIXED (proper spacing)
\addcontentsline{toc}{chapter}{Appendix A}
\vspace{0.3cm}
\section*{Overview}
\addcontentsline{toc}{section}{Overview}
```

### 16. **Overfull \hbox Warnings**

**Problem**: Text extends beyond margin
```
Overfull \hbox (2.23705pt too wide) in paragraph at lines 100--101
```

**Root Cause**: Long text or numbers don't fit within column width

**Recipe**:
1. Use en-dashes (--) instead of hyphens (-) for ranges
2. Break long numbers or text appropriately
3. Adjust table column specifications if needed

**Fix Pattern**:
```latex
% PROBLEMATIC (causes overfull)
3.8-10.1× improvement

% FIXED (proper typography)
3.8--10.1× improvement
```

**Table Column Adjustments**:
```latex
% If still overfull, adjust column types
\begin{tabular}{@{}lrrrp{2cm}@{}}  % p{width} for last column
```
### 17. **Table Rule Typos**

**Problem**: Undefined table rule commands
```
Undefined control sequence.
./content/chapter13/orchestration-architecture.tex, 125
l.125 \tomlrule
```

**Root Cause**: Typos in table rule commands

**Recipe**:
1. Check for common typos in table rules
2. Ensure correct booktabs package commands are used
3. Verify table environment syntax

**Common Typos and Fixes**:
```latex
% WRONG (typos)
\tomlrule → \toprule
\tabable → \tabular
\midule → \midrule
\botomrule → \bottomrule

% CORRECT (booktabs package)
\toprule    % Top rule
\midrule    % Middle rule  
\bottomrule % Bottom rule
\cmidrule   % Partial rule
```

**Standard Table Pattern**:
```latex
\begin{table}[ht]
\centering
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
\midrule
Data 1 & Data 2 & Data 3 \\
Data 4 & Data 5 & Data 6 \\
\bottomrule
\end{tabular}
\caption{Table Caption}
\end{table}
```

### 18. **Table Environment Mismatches**

**Problem**: Mismatched table environment endings
```
LaTeX Error: \begin{tabular} on input line 86 ended by \end{tabable}.
```

**Root Cause**: Typo in environment ending

**Recipe**:
1. Check that \begin{environment} matches \end{environment}
2. Look for common typos in environment names
3. Ensure proper nesting of environments

**Common Environment Mismatches**:
```latex
% WRONG (mismatched)
\begin{tabular} ... \end{tabable}
\begin{table} ... \end{tabel}
\begin{figure} ... \end{figrue}

% CORRECT (matched)
\begin{tabular} ... \end{tabular}
\begin{table} ... \end{table}
\begin{figure} ... \end{figure}
```

**Automated Check Pattern**:
```python
# Find environment mismatches
import re
content = open('file.tex').read()
begins = re.findall(r'\\begin\{([^}]+)\}', content)
ends = re.findall(r'\\end\{([^}]+)\}', content)
mismatches = set(begins) - set(ends)
print("Potential mismatches:", mismatches)
```
### 19. **"Not in outer par mode" Errors**

**Problem**: Tables inside non-floating environments
```
LaTeX Error: Not in outer par mode.
./content/chapter19/component-system-implementation.tex, 50
```

**Root Cause**: Using `\begin{table}` inside box environments (infobox, alertbox, successbox)

**Recipe**:
1. Replace `\begin{table}[h]` with `\begin{center}`
2. Remove `\centering` line
3. Replace `\caption{...}` with `\captionof{table}{...}`
4. Replace `\end{table}` with `\end{center}`
5. Ensure `caption` package is loaded

**Automated Fix Pattern**:
```latex
% WRONG (inside box environments)
\begin{infobox}
\begin{table}[h]
\centering
\begin{tabular}{...}
...
\end{tabular}
\caption{Table Title}
\end{table}
\end{infobox}

% CORRECT (using center environment)
\begin{infobox}
\begin{center}
\begin{tabular}{...}
...
\end{tabular}
\captionof{table}{Table Title}
\end{center}
\end{infobox}
```

### 20. **Runaway Arguments and Missing Braces**

**Problem**: Missing closing braces in commands
```
Runaway argument?
./content/chapter18/entry.tex, 20
{A/B Testing Data**: Preserves data for model comparison and validati\ETC.
! File ended while scanning use of \textbf .
```

**Root Cause**: Malformed `\textbf` commands with missing opening braces

**Recipe**:
1. Check for malformed `\textbf{text**` patterns
2. Fix missing opening braces: `\textbf{text}`
3. Ensure all braces are properly matched
4. Look for double asterisks `**` which indicate markdown-style formatting

**Common Patterns to Fix**:
```latex
% WRONG (missing opening brace)
\textbf{A/B Testing Data**: Description
\textbf{Feedback Integration**: Description

% CORRECT (proper braces)
\textbf{A/B Testing Data}: Description
\textbf{Feedback Integration}: Description
```

### 21. **Malformed Table Environment Syntax**

**Problem**: Incorrect table environment syntax
```
LaTeX Error: \begin{tabular} on input line 86 ended by \end{tabable}.
```

**Root Cause**: Typos in environment commands and malformed backslashes

**Recipe**:
1. Fix double backslashes: `\\begin{center}` → `\begin{center}`
2. Fix environment name typos: `\end{tabable}` → `\end{tabular}`
3. Check for missing closing braces in table endings
4. Verify proper table structure

**Common Syntax Errors**:
```latex
% WRONG (malformed syntax)
\\begin{center}           % Double backslash
\end{tabable}            % Wrong environment name
\end{table>              % Missing closing brace

% CORRECT (proper syntax)
\begin{center}           % Single backslash
\end{tabular}           % Correct environment name
\end{table}             % Proper closing brace
```

### 22. **"Too deeply nested" List Errors**

**Problem**: Excessive list nesting beyond LaTeX limits
```
LaTeX Error: Too deeply nested.
./content/chapter21/testing-strategy.tex, 76
```

**Root Cause**: Lists nested more than 4 levels deep or custom list environments not properly defined

**Recipe**:
1. Reduce list nesting to maximum 4 levels
2. Use description lists instead of nested itemize
3. Break complex lists into separate sections
4. Ensure custom list environments (compactlist, expandedlist) are properly defined

**List Nesting Limits**:
```latex
% MAXIMUM NESTING (4 levels)
\begin{itemize}
  \item Level 1
  \begin{itemize}
    \item Level 2
    \begin{itemize}
      \item Level 3
      \begin{itemize}
        \item Level 4 (maximum)
      \end{itemize}
    \end{itemize}
  \end{itemize}
\end{itemize}

% ALTERNATIVE: Use description lists
\begin{description}
  \item[Category 1] Description
  \item[Category 2] Description
\end{description}
```