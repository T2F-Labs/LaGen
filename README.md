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

## 🧱 Content Structure
Content lives in the `content/` directory and can be organized as chapters, standalone pages, or granular sections. Covers and templates define the shell of the document; your content files are independent and do not need to be part of the cover page.

Typical patterns:
- Chapters: `01-introduction.tex`, `02-methods.tex`, `03-results.tex`
- Single pages/sections: `10-appendix-a.tex`, `20-acknowledgements.tex`

How to include:
```latex
\begin{document}
  % Cover (optional)
  % \templateOneCover{...} or \customCover{...}

  % Content loaded on its own pages
  \input{content/01-introduction.tex}
  \input{content/02-chapter.tex}
  % or, to force page breaks between major units
  \include{content/03-results} % uses its own .tex and inserts clear pages
\end{document}
```

## 📖 Documentation

This project includes comprehensive documentation to help you get the most out of the LaTeX template system:

- **GUIDE.md**: [Complete LaTeX configuration guide](./GUIDE.md) with detailed explanations of all available features and usage examples
- **dev.md**: Development guidelines for maintaining and extending the system
