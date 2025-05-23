# LaTeX Document Generator

![LaTeX](https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)

A powerful system for generating professional LaTeX documents programmatically using Python and Jinja2 templating.

## 📋 Overview

This project provides a flexible template system that lets you generate beautiful LaTeX documents from structured data. Perfect for:

- Creating customized reports from data analysis
- Generating documentation with consistent formatting
- Automating the production of academic papers
- Creating professional white papers and technical documents

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

## 📚 Documentation

For full documentation of all template features and options, see [INSTRUCTIONS.md](INSTRUCTIONS.md).

## 📖 Examples

The repository includes example data structures and their output PDFs:

- `examples/simple_report.py` - Basic report with sections and subsections
- `examples/data_analysis.py` - Data analysis report with tables and charts
- `examples/technical_document.py` - Technical document with code samples and algorithms

## 📂 Project Structure

```
.
├── latex_template.tex.jinja  # Main template file
├── config.tex               # LaTeX configuration and styling
├── examples/                # Example Python data and output PDFs
├── INSTRUCTIONS.md          # Detailed documentation
└── README.md                # This file
```

## 🖨️ Output Examples

The template produces professionally styled documents with elements like:

- Title page with document metadata
- Executive summary in a styled box
- Table of contents with proper formatting
- Section headings with optional drop caps
- Professional tables with colored headers
- Callout boxes for important information
- Code listings with syntax highlighting
- Algorithm descriptions with proper mathematical notation
- Cross-references and proper citations

## ⚙️ Customization

You can customize the look and feel of your documents by modifying `config.tex`. This includes:

- Colors and branding
- Fonts and typography
- Spacing and layout
- Special environment styling

## 🔍 Advanced Features

- **Bibliography Support**: Automatic bibliography generation with BibTeX
- **Custom Boxes**: Several styled box types for different content needs
- **Algorithm Layout**: Professional algorithm display with pseudocode
- **Icon Integration**: FontAwesome icons in callout boxes
- **Cross-referencing**: Smart referencing of sections, figures, and tables

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