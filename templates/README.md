# LaTeX Document Templates

This directory contains a collection of professionally designed LaTeX templates that work with our brand color system and configuration.

## Available Templates

### Template 1: Modern Geometric Design
A sleek, modern template featuring geometric patterns and a professional cover page design. Ideal for project proposals, whitepapers, and technical reports.

**Key Features:**
- Dynamic geometric background using brand colors
- Professionally styled cover page
- Custom table styling with brand colors
- Footer with brand color accents

### Template 2: Corporate Sidebar Design
A professional corporate template featuring a colored sidebar and subtle patterns for official business documents. Perfect for business reports, strategic analyses, and formal presentations.

**Key Features:**
- Elegant sidebar with brand color
- Subtle pattern in the content area
- Professional cover page
- Custom table styling with brand colors
- Header and footer design with page numbers

### Template 3: Minimal Elegant Design
A clean, minimalist template with subtle gradients and thin lines for a sophisticated appearance. Ideal for annual reports, academic papers, and formal documentation.

**Key Features:**
- Subtle gradient background
- Elegant corner flourishes
- Thin line decorations
- Sophisticated cover page
- Clean table styling

## How to Use the Templates

Each template can be easily integrated into your documents:

1. **Include the configuration files:**
   ```latex
   \input{config.tex}  % Loads the core configuration with brand colors
   ```

2. **Load your chosen template:**
   ```latex
   \input{templates/template1.tex}  % For Template 1
   % OR
   \input{templates/template2.tex}  % For Template 2
   % OR
   \input{templates/template3.tex}  % For Template 3
   ```

3. **Generate the cover page** using the template's macro:
   ```latex
   % For Template 1
   \templateOneCover{MAIN TITLE}{Subtitle}{Year}{Recipient}{Preparer}
   
   % For Template 2
   \templateTwoCover{MAIN TITLE}{Subtitle}{Year}{Recipient}{Preparer}
   
   % For Template 3
   \templateThreeCover{MAIN TITLE}{Subtitle}{Year}{Recipient}{Preparer}
   ```

4. **Apply table styling** (optional):
   ```latex
   % For Template 1
   \templateOneTable
   
   % For Template 2
   \templateTwoTable
   
   % For Template 3
   \templateThreeTable
   ```

## Example Usage

Example files demonstrating how to use each template are provided in the root directory:

- `example_use_template1.tex` - Shows Template 1 in use
- `example_use_template2.tex` - Shows Template 2 in use
- `example_use_template3.tex` - Shows Template 3 in use

## Customization

All templates automatically use your brand colors from `config.tex` and `brand_colors.tex`. To customize the appearance:

1. Modify your brand colors in `brand_colors.tex`
2. Create a custom theme file (see `example_theme.tex` for reference)

## Required Packages

These templates require the following LaTeX packages:
- `geometry`
- `xcolor`
- `tikz`
- `eso-pic`
- `lipsum` (for example documents only)
- `tabularx` (for tables in example documents) 