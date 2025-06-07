# LaTeX Document Generator

![LaTeX](https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)

A powerful system for generating professional LaTeX documents programmatically using Python and Jinja2 templating, with enhanced typography and formatting capabilities.

## 📋 Overview

This project provides a flexible template system that lets you generate beautiful LaTeX documents from structured data. Perfect for:

- Creating customized reports from data analysis
- Generating documentation with consistent formatting
- Automating the production of academic papers
- Creating professional white papers and technical documents
- Producing multi-page tables and complex mathematical content

## ✨ Key Features

- **Full LaTeX Integration**: Leverage LaTeX's powerful typesetting capabilities
- **Programmatic Generation**: Create documents from Python data structures
- **Rich Elements**: Support for tables, lists, code blocks, algorithms, callout boxes, and more
- **Professional Styling**: Beautiful pre-designed styling with customization options
- **Drop Cap Support**: Elegant typography with first-letter drop caps
- **Modular Structure**: Organize content in sections and subsections
- **Flexible References**: Generate bibliographies automatically
- **Beautiful Tables**: Styled tables with colored headers and alternating rows
- **Code Highlighting**: Syntax highlighting for multiple programming languages
- **Multi-page Tables**: Support for tables that span multiple pages
- **Advanced Math**: Professional mathematical typesetting with AMS packages
- **Units & Numbers**: Proper formatting of units and numbers with siunitx
- **Brand Consistency**: Letterspacing and font scaling for brand names
- **Better Page Control**: Enhanced float placement and management
- **Professional Pagination**: "Page X of Y" numbering and advanced headers/footers
- **Advanced Image Handling**: Professional image formatting with shapes, fallbacks, and effects
- **Comprehensive Lists**: Task lists, priority lists, and custom styling options
- **Semantic Box Styling**: Info, alert, and success boxes with visual cues

## 📖 Documentation

This project includes comprehensive documentation to help you get the most out of the LaTeX template system:

- **GUIDE.md**: [Complete LaTeX configuration guide](./GUIDE.md) with detailed explanations of all available features and usage examples
- **dev.md**: Development guidelines for maintaining and extending the system
- **INSTRUCTIONS.md**: Basic usage instructions and examples

The [`GUIDE.md`](./GUIDE.md) file provides an extensive reference for all LaTeX configuration options available in `config.tex`, including:

- Font and encoding options
- Page layout settings
- Color schemes and typography
- Section styling and header/footer configuration
- Advanced mathematical typesetting features
- Box and callout styling
- List formatting options
- Table configuration
- Code listing setup
- Algorithm formatting
- Advanced image handling with various shapes and styles

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/latex-document-generator.git
cd latex-document-generator

# Install dependencies
pip install jinja2
```

You'll also need a LaTeX distribution with XeLaTeX:
- **Windows**: [MiKTeX](https://miktex.org/download)
- **macOS**: [MacTeX](https://www.tug.org/mactex/)
- **Linux**: `sudo apt-get install texlive-full`

## 🚀 Quick Start

1. Create your data structure in Python:

```python
data = {
    "title": "Project Analysis Report",
    "author": "Jane Smith",
    "executive_summary": "This report analyzes the performance of our recent project...",
    "company_name": "Lagen",
    "document_version": "1.0.3",
    "document_status": "Final",
    "document_classification": "Internal Use",
    "sections": [
        {
            "level": 1,
            "title": "Introduction",
            "content": "This document provides analysis of...",
            "drop_cap": True
        },
        # More sections...
    ]
}
```

2. Generate the LaTeX document:

```python
from jinja2 import Template

# Load the template
with open('latex_template.tex.jinja', 'r') as f:
    template = Template(f.read())

# Render the template with your data
latex_output = template.render(**data)

# Write the output to a file
with open('output.tex', 'w') as f:
    f.write(latex_output)
```

3. Compile the LaTeX document:

```bash
xelatex output.tex
```

## 📚 Advanced Features

### Professional Typography and Branding

Use our enhanced typography features to maintain brand consistency:

```latex
% Define your brand elements
\newcommand{\companyName}{Lagen}
\newcommand{\companyTagline}{Professional Document Systems}

% Use the brand elements in text with proper letterspacing
Our \brandname{\companyName} system helps you...
The \productname{Lagen Documentation System} provides...
```

### Multi-page Tables

Create tables that span across multiple pages with consistent headers:

```latex
\begin{longtable}{p{2cm}p{4cm}p{3cm}p{4cm}}
\caption{Project Timeline and Milestones} \\
\rowcolor{headerbg}
\textcolor{headertext}{\textbf{Date}} &
\textcolor{headertext}{\textbf{Milestone}} &
\textcolor{headertext}{\textbf{Responsible}} &
\textcolor{headertext}{\textbf{Deliverables}} \\
\toprule
\endfirsthead

% Header for continuation pages
\multicolumn{4}{c}{\tablename\ \thetable{} -- continued from previous page} \\
\rowcolor{headerbg}
\textcolor{headertext}{\textbf{Date}} &
\textcolor{headertext}{\textbf{Milestone}} &
\textcolor{headertext}{\textbf{Responsible}} &
\textcolor{headertext}{\textbf{Deliverables}} \\
\toprule
\endhead

% Footer for all pages except the last
\midrule \multicolumn{4}{r}{Continued on next page} \\
\endfoot

% Footer for the last page
\bottomrule
\endlastfoot

% Table contents
2023-01-15 & Project Initiation & Project Manager & Project charter \\
% Additional rows...
\end{longtable}
```

### Professional Numerical and Unit Formatting

Format measurements consistently with proper units:

```latex
The battery capacity is \SI{5000}{\milli\ampere\hour}
The budget is \SI{2500000}{\USD} for the first phase
```

### Enhanced Column Types

Use predefined column types for better table formatting:

```latex
\begin{tabularx}{\textwidth}{L{3cm}C{5cm}R{2cm}N}
% L = left-aligned with specified width
% C = centered with specified width
% R = right-aligned with specified width
% N = right-aligned, automatically sized (for numbers)
\end{tabularx}
```

### Mathematical Typesetting

Create professional-looking equations with advanced math packages:

```latex
\begin{align}
E &= mc^2 \\
F &= G\frac{m_1 m_2}{r^2} \\
\nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t}
\end{align}
```

### Advanced Image Handling

Create professional image presentations with various shapes and styles:

```latex
% Image with rounded corners
\roundedImage{images/profile.jpg}{4cm}{10pt}{Team Member}{Profile Not Available}

% Circular image (perfect for profile pictures)
\circularImage{images/avatar.png}{3cm}{CEO Portrait}{Avatar Not Available}

% Image with drop shadow effect
\shadowImage{images/product.jpg}{6cm}{Product Showcase}{Image Not Available}
```

## 📖 Examples

The repository includes example data structures and their output PDFs:

- `examples/simple_report.py` - Basic report with sections and subsections
- `examples/data_analysis.py` - Data analysis report with tables and charts
- `examples/technical_document.py` - Technical document with code samples and algorithms
- `examples/multi_page_tables.py` - Report with tables spanning multiple pages
- `examples/mathematical_report.py` - Document with advanced mathematical content

## 📂 Project Structure

```
.
├── latex_template.tex         # Main template file
├── config.tex                 # LaTeX configuration and styling
├── GUIDE.md                   # Comprehensive LaTeX configuration guide
├── dev.md                     # Development guidelines and standards
├── covers/                    # Optional cover page designs
│   ├── cover1.tex             # Modern cover design
│   └── cover2.tex             # Traditional cover design
├── examples/                  # Example Python data and output PDFs
├── INSTRUCTIONS.md            # Basic usage instructions
└── README.md                  # This file
```

## 🖨️ Output Examples

The template produces professionally styled documents with elements like:

- Title page with document metadata
- Optional cover pages with branding
- Executive summary in a styled box
- Table of contents with proper formatting
- Section headings with optional drop caps
- Multi-page professional tables
- Mathematical equations and formulas with proper spacing
- Callout boxes for important information
- Code listings with syntax highlighting
- Algorithm descriptions with proper mathematical notation
- Cross-references and proper citations
- Professional image handling with various shapes and effects
- Task and priority lists with custom styling

## ⚙️ Customization

You can customize the look and feel of your documents by modifying `config.tex`. This includes:

- Colors and branding
- Fonts and typography
- Spacing and layout
- Special environment styling
- Mathematical styling and number formatting
- Table layouts and designs
- Header and footer formatting
- Image presentation styles
- List formatting and styling

For detailed customization options, refer to the [comprehensive configuration guide](./GUIDE.md).

## 🆕 Recent Updates

- Added comprehensive `GUIDE.md` documentation for all LaTeX configuration options
- Fixed package loading conflicts between `graphicx` and `adjustbox`
- Enhanced image handling with various shapes, styles, and fallback mechanisms
- Added development guidelines in `dev.md`
- Improved tabular environments with compatibility fixes
- Enhanced mathematical typesetting section with additional examples
- Added custom list styles including task lists and priority indicators

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- LaTeX project for their amazing typesetting system
- Jinja2 team for the powerful templating engine
- All contributors and users of this project 