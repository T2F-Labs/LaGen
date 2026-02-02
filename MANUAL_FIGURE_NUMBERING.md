# Manual Figure Numbering System - Independent Chapters

## Overview
This document explains the **manual figure numbering system** implemented for the Symphony Book, where each chapter explicitly controls its own figure numbering independent of chapter order or other chapters.

## Problem Solved
Previously, figure numbering depended on the automatic chapter counter, which meant:
- If chapters were reordered, figure numbers would change
- If a chapter was skipped, numbering would be off
- Chapter 0 (front matter) interfered with numbering
- Figures in Chapter 3 showed as "Figure 1.1" instead of "Figure 3.1"

## Solution: Manual Counter Override

Each chapter now **explicitly sets its own chapter number** at the beginning, ensuring:
- ✅ Chapter 1 figures are always 1.1, 1.2, 1.3...
- ✅ Chapter 2 figures are always 2.1, 2.2, 2.3...
- ✅ Chapter 3 figures are always 3.1, 3.2, 3.3...
- ✅ Chapter 4 figures are always 4.1, 4.2, 4.3...
- ✅ Chapter 5 figures are always 5.1, 5.2, 5.3...

**Regardless of:**
- Chapter order in main.tex
- Whether previous chapters exist
- Whether previous chapters have figures
- Front matter structure

## Implementation

### Chapter 1 Entry (content/chapter1-new/entry.tex)
```latex
\chapter{INTRODUCTION}
\label{ch:introduction}

% MANUAL FIGURE NUMBERING FOR CHAPTER 1
% Override automatic numbering to ensure figures are always 1.x
\setcounter{chapter}{1}
\setcounter{figure}{0}
```

### Chapter 2 Entry (content/chapter2-new/entry.tex)
```latex
\chapter{SYSTEM ANALYSIS}
\label{ch:system-analysis}

% MANUAL FIGURE NUMBERING FOR CHAPTER 2
% Override automatic numbering to ensure figures are always 2.x
\setcounter{chapter}{2}
\setcounter{figure}{0}
```

### Chapter 3 Entry (content/chapter3-new/entry.tex)
```latex
\chapter{SYSTEM DESIGN}
\label{ch:system-design}

% MANUAL FIGURE NUMBERING FOR CHAPTER 3
% Override automatic numbering to ensure figures are always 3.x
\setcounter{chapter}{3}
\setcounter{figure}{0}
```

### Chapter 4 Entry (content/chapter4-new/entry.tex)
```latex
\chapter{APPENDIX}
\label{ch:appendix}

% MANUAL FIGURE NUMBERING FOR CHAPTER 4
% Override automatic numbering to ensure figures are always 4.x
\setcounter{chapter}{4}
\setcounter{figure}{0}
```

### Chapter 5 Entry (content/chapter5-new/entry.tex)
```latex
\chapter{BACK MATTERS}
\label{ch:back-matters}

% MANUAL FIGURE NUMBERING FOR CHAPTER 5
% Override automatic numbering to ensure figures are always 5.x
\setcounter{chapter}{5}
\setcounter{figure}{0}
```

## How It Works

### The Commands
1. **`\setcounter{chapter}{N}`** - Forces the chapter counter to a specific number
2. **`\setcounter{figure}{0}`** - Resets the figure counter to 0

### The Result
When LaTeX encounters a figure:
```latex
\begin{figure}[H]
\includegraphics{...}
\caption{Some caption}
\label{fig:3.1}
\end{figure}
```

It uses `\thefigure` which expands to `\thechapter.\arabic{figure}`:
- In Chapter 3: `\thechapter` = 3, `\arabic{figure}` = 1 → **Figure 3.1** ✅

### Why This Works
- Each chapter **explicitly declares** its number
- The figure counter **resets to 0** at the start of each chapter
- The `\counterwithin{figure}{chapter}` in config.tex ensures figures increment properly
- The `\renewcommand{\thefigure}{\thechapter.\arabic{figure}}` formats the display

## Benefits

### 1. Independence
Each chapter is completely independent:
```latex
% You can load chapters in ANY order:
\input{content/chapter3-new/entry.tex}  % Figures will be 3.1, 3.2, 3.3...
\input{content/chapter1-new/entry.tex}  % Figures will be 1.1, 1.2, 1.3...
\input{content/chapter5-new/entry.tex}  % Figures will be 5.1, 5.2, 5.3...
```

### 2. Predictability
Figure numbers are **hardcoded** and never change:
- Chapter 3 figures are ALWAYS 3.x
- Chapter 1 figures are ALWAYS 1.x
- No surprises, no dependencies

### 3. Flexibility
You can:
- Skip chapters (e.g., remove Chapter 2 temporarily)
- Reorder chapters in main.tex
- Work on chapters independently
- Compile individual chapters for testing

### 4. Maintainability
Clear and explicit:
- Easy to understand what chapter you're in
- Easy to debug numbering issues
- Easy to add new chapters

## Figure Numbering Reference

### Chapter 1: INTRODUCTION
- **Figure 1.1**: High-Level Overview of Symphony System
- (Add more as needed)

### Chapter 2: SYSTEM ANALYSIS
- **Figure 2.1**: (When added)
- **Figure 2.2**: (When added)

### Chapter 3: SYSTEM DESIGN
- **Figure 3.1**: H²A² Architecture
- **Figure 3.2**: System Bootstrap Process
- **Figure 3.3**: The Pit Architecture
- **Figure 3.4**: Orchestra Kit Architecture
- **Figure 3.5**: Extension Lifecycle State Machine
- **Figure 3.6**: Extension Development Workflow
- **Figure 3.7**: IPC Communication Infrastructure
- **Figure 3.8**: Melody Execution Workflow
- **Figure 3.9**: Conductor Workflow
- **Figure 3.10**: Melody Execution State Machine
- **Figure 3.11**: Overall System Activity
- **Figure 3.12**: Harmony Board Creation Process
- **Figure 3.13**: System Use Cases

### Chapter 4: APPENDIX
- **Figure 4.1**: (When added)
- **Figure 4.2**: (When added)

### Chapter 5: BACK MATTERS
- **Figure 5.1**: (When added)
- **Figure 5.2**: (When added)

## Adding New Chapters

When adding a new chapter (e.g., Chapter 6):

```latex
% content/chapter6-new/entry.tex
\chapter{NEW CHAPTER TITLE}
\label{ch:new-chapter}

% MANUAL FIGURE NUMBERING FOR CHAPTER 6
% Override automatic numbering to ensure figures are always 6.x
\setcounter{chapter}{6}
\setcounter{figure}{0}

% Chapter content...
\input{content/chapter6-new/section1.tex}
```

## Adding Figures to a Chapter

Simply use the standard LaTeX figure environment:

```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{path/to/image.png}
\caption{Your caption here}
\label{fig:3.14}  % Use chapter.number format
\end{figure}
```

The figure will automatically be numbered correctly based on the chapter counter.

## Tables Work the Same Way

Tables also use chapter-based numbering:
- Chapter 1: Table 1.1, Table 1.2, ...
- Chapter 2: Table 2.1, Table 2.2, ...
- Chapter 3: Table 3.1, Table 3.2, ...

No additional configuration needed - the `\counterwithin{table}{chapter}` in config.tex handles it.

## Compilation

After making these changes, **delete auxiliary files** and recompile:

```bash
# Delete old auxiliary files
rm -f *.aux *.log *.out *.toc *.lof *.lot

# Compile
xelatex main.tex

# If you have references
biber main
xelatex main.tex
xelatex main.tex
```

## Verification

To verify the fix:
1. Compile the document
2. Open the PDF
3. Navigate to Chapter 3
4. Check that figures show as:
   - Figure 3.1 (NOT 1.1 or 0.2) ✅
   - Figure 3.2 ✅
   - Figure 3.3 ✅
   - ... through Figure 3.13 ✅

## Technical Details

### Counter Hierarchy
LaTeX counters have a hierarchy:
- `chapter` counter (top level)
- `figure` counter (subordinate to chapter via `\counterwithin`)
- `table` counter (subordinate to chapter via `\counterwithin`)

### Manual Override
By using `\setcounter{chapter}{N}`, we:
1. Force the chapter counter to a specific value
2. Trigger the reset of subordinate counters (figure, table)
3. Ensure consistent numbering regardless of document structure

### Display Format
The display format is controlled by:
```latex
\renewcommand{\thefigure}{\thechapter.\arabic{figure}}
```
This means: "Display figures as ChapterNumber.FigureNumber"

## Troubleshooting

### Problem: Figures still show wrong numbers
**Solution**: Delete auxiliary files and recompile from scratch
```bash
rm -f *.aux *.log *.out *.toc *.lof *.lot
xelatex main.tex
```

### Problem: Chapter numbers in TOC are wrong
**Solution**: This is expected! The TOC will show the manual chapter numbers (1, 2, 3, 4, 5) which is correct.

### Problem: Want to change a chapter number
**Solution**: Just change the `\setcounter{chapter}{N}` value in that chapter's entry.tex

### Problem: Adding a new chapter between existing ones
**Solution**: 
1. Create the new chapter folder
2. Set the appropriate chapter number with `\setcounter{chapter}{N}`
3. Renumber subsequent chapters if needed
4. Update figure labels to match new chapter numbers

## Best Practices

### 1. Always Set Both Counters
```latex
\setcounter{chapter}{3}   % Set chapter number
\setcounter{figure}{0}    % Reset figure counter
```

### 2. Place at Start of Chapter
Put the counter commands immediately after `\chapter{...}` and before any content.

### 3. Use Consistent Labels
Label figures with the chapter number:
```latex
\label{fig:3.1}   % Good - matches chapter number
\label{fig:arch}  % Bad - not clear which chapter
```

### 4. Document Your Chapters
Add comments explaining the manual numbering:
```latex
% MANUAL FIGURE NUMBERING FOR CHAPTER 3
% Override automatic numbering to ensure figures are always 3.x
```

## Summary

✅ **Each chapter is now independent**
✅ **Figure numbering is explicit and predictable**
✅ **Chapter 3 figures will always be 3.1, 3.2, 3.3...**
✅ **No dependency on chapter order or previous chapters**
✅ **Easy to maintain and extend**

This manual numbering system gives you complete control over figure numbering while maintaining the professional appearance and consistency of your academic document.
