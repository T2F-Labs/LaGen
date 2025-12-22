# Quick Usage Guide

## How to Use Templates and Covers

### Option 1: Use a Template (Recommended)

Templates include both cover page and document styling. Uncomment ONE template line in `main.tex`:

```latex
\newcommand{\UseTemplate}{template1}  % Modern geometric design
% \newcommand{\UseTemplate}{template2}  % Corporate sidebar design  
% \newcommand{\UseTemplate}{template3}  % Minimal elegant design
```

### Option 2: Use a Standalone Cover

If you don't want template styling, use just a cover. Uncomment ONE cover line:

```latex
% \newcommand{\UseCover}{cover1}   % Modern gradient design
% \newcommand{\UseCover}{cover2}   % Professional layout
% \newcommand{\UseCover}{cover3}   % Clean minimal design
```

### Customize Cover Content

Update these variables in `main.tex`:

```latex
\newcommand{\CoverTitle}{Your Document Title}
\newcommand{\CoverSubtitle}{Document Subtitle}
\newcommand{\CoverYear}{2024}
\newcommand{\CoverRecipient}{Recipient Name}
\newcommand{\CoverPreparer}{Author Name}
```

### Enable/Disable Modules

Set modules to `true` or `false` based on what you need:

```latex
\newcommand{\EnableMathematics}{true}   % For equations
\newcommand{\EnableTables}{true}        % For tables
\newcommand{\EnableBoxes}{true}         % For info boxes
\newcommand{\EnableCode}{false}         % For code blocks
```

## Quick Examples

### Academic Paper
```latex
\newcommand{\UseTemplate}{template3}    % Minimal elegant
\newcommand{\EnableMathematics}{true}
\newcommand{\EnableReferences}{true}
\newcommand{\EnableAlgorithms}{true}
```

### Business Report  
```latex
\newcommand{\UseTemplate}{template2}    % Corporate sidebar
\newcommand{\EnableTables}{true}
\newcommand{\EnableBoxes}{true}
\newcommand{\EnableImages}{true}
```

### Technical Document
```latex
\newcommand{\UseTemplate}{template1}    % Modern geometric
\newcommand{\EnableCode}{true}
\newcommand{\EnableMathematics}{true}
\newcommand{\EnableTables}{true}
```

## Compilation

```bash
xelatex main.tex
```

That's it! Your document will be generated with the selected template/cover and enabled modules.