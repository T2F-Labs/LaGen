# Template Examples

This directory contains example files demonstrating how to use the professional document templates. These examples provide ready-to-use document structures with minimal required customization.

## Available Example Files

### 1. Template 1: Modern Geometric Design
`example_use_template1.tex` - A project proposal document showcasing:
- Dynamic geometric background pattern
- Professional cover page
- Styled sections and lists
- Custom table formatting

### 2. Template 2: Corporate Sidebar Design
`example_use_template2.tex` - A strategic analysis document featuring:
- Professional sidebar with brand color
- Subtle pattern in the content area
- Corporate-style cover page
- Structured content organization

### 3. Template 3: Minimal Elegant Design
`example_use_template3.tex` - An annual report document demonstrating:
- Clean gradient background
- Elegant corner flourishes
- Sophisticated minimal cover page
- Professional data presentation

### 4. Theme Example
`example_theme.tex` - Shows how to create custom color themes for your documents.

## How to Use These Examples

1. **Review the examples** to understand the document structure and organization
2. **Copy the example** that best fits your needs as a starting point
3. **Replace the content** with your own while keeping the structural elements
4. **Compile** using XeLaTeX:
   ```
   xelatex your_document.tex
   ```

## Template Structure

All template examples follow this general structure:

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[margin=0.8in]{geometry}

% Load the core configuration with brand colors
\input{config.tex}

% Load the template
\input{templates/template1.tex}  % Change to template2.tex or template3.tex as needed

% Begin the document
\begin{document}

% Create the cover page using the template's macro
\templateOneCover{TITLE}{Subtitle}{Year}{Recipient}{Author}  % Use the appropriate template macro

% Apply the template's table style
\templateOneTable  % Use the appropriate template table style

% Document content follows...
\section{First Section}
Content...

\end{document}
```

## Customizing the Examples

### Changing Colors

1. Create a custom brand colors file based on `brand_colors.tex`
2. Modify the brand colors to match your requirements
3. Load your custom colors file in your document

Example:
```latex
% Create my_colors.tex with:
\definecolor{brandPrimary}{HTML}{00796B}     % Teal
\definecolor{brandSecondary}{HTML}{004D40}   % Dark Teal
\definecolor{brandAccent}{HTML}{FFA000}      % Amber

% Then in your document:
\input{config.tex}
\input{my_colors.tex}
\input{templates/template1.tex}
```

### Modifying Templates

For more extensive customization:

1. Copy the template file to create your own variant
2. Modify the background, cover page, or styling elements
3. Use your custom template in your document

Example:
```latex
% Create my_template.tex based on template1.tex
% Then in your document:
\input{config.tex}
\input{my_template.tex}
```

## Requirements

These examples require:
- A LaTeX distribution with XeLaTeX
- The "Inter" font family (or modify the font in config.tex)
- Required LaTeX packages (automatically installed by most LaTeX distributions) 