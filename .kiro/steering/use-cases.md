# LaTeX Use Cases Documentation

This directory contains comprehensive examples demonstrating every combination of covers, templates, brand colors, and modular configurations for the LaGen LaTeX system.

## 📁 Directory Structure

```
use-cases/
├── 01-cover-custom-content.tex      # Custom cover with personal styling
├── 02-cover-brand-colors.tex        # Custom cover using brand color system
├── 03-template1-custom-content.tex  # Template 1 with custom content
├── 04-template2-brand-colors.tex    # Template 2 with brand integration
├── 05-template3-minimal.tex         # Template 3 elegant minimal design
├── 06-modular-basic.tex             # Basic module configuration
├── 07-modular-selective.tex         # Selective module loading
├── 08-modular-full.tex              # Full feature configuration
├── 09-cover-template-hybrid.tex     # Hybrid custom cover + template body
├── 10-academic-paper.tex            # Academic paper optimization
├── 11-business-report.tex           # Business report configuration
└── README.md                        # This documentation
```

## 🎯 Use Case Categories

### **Cover Designs**

| Use Case | File | Description | Compile Time |
|----------|------|-------------|--------------|
| **Custom Cover** | `01-cover-custom-content.tex` | Pure custom styling without templates | 8-12s |
| **Brand Cover** | `02-cover-brand-colors.tex` | Custom cover leveraging brand color system | 10-15s |
| **Hybrid Cover** | `09-cover-template-hybrid.tex` | Custom cover + template body styling | 15-20s |

### **Template Configurations**

| Template | File | Style | Best For |
|----------|------|-------|----------|
| **Template 1** | `03-template1-custom-content.tex` | Modern Geometric | Marketing, presentations |
| **Template 2** | `04-template2-brand-colors.tex` | Corporate Sidebar | Business reports, proposals |
| **Template 3** | `05-template3-minimal.tex` | Minimal Elegant | Academic papers, clean docs |

### **Modular Loading Strategies**

| Configuration | File | Modules Enabled | Compile Time | Use Case |
|---------------|------|-----------------|--------------|----------|
| **Basic** | `06-modular-basic.tex` | Boxes only | 8-12s | Quick drafts, Overleaf free |
| **Selective** | `07-modular-selective.tex` | Math, Tables, Boxes, Lists | 15-25s | Balanced functionality |
| **Full** | `08-modular-full.tex` | All modules | 25-35s | Feature-rich documents |

### **Specialized Configurations**

| Document Type | File | Optimized For | Key Features |
|---------------|------|---------------|--------------|
| **Academic** | `10-academic-paper.tex` | Research papers | Math, algorithms, references |
| **Business** | `11-business-report.tex` | Corporate reports | Tables, charts, professional styling |

## 🚀 Quick Start Guide

### 1. **Choose Your Base Configuration**

```latex
% Basic setup for any use case
\documentclass[11pt,a4paper]{article}
\usepackage{ifthen}

% Configure modules based on your needs
\newcommand{\EnableMathematics}{true/false}
\newcommand{\EnableTables}{true/false}
% ... other modules

% Load configuration
\input{config.tex}
```

### 2. **Select Cover/Template Approach**

**Option A: Custom Cover**
```latex
% Define your own cover command
\newcommand{\customCover}[5]{%
  % Custom styling here
}
```

**Option B: Use Template**
```latex
% Load template
\input{templates/template1.tex}

% Use template cover
\templateOneCover{Title}{Subtitle}{Year}{To}{By}
```

**Option C: Hybrid Approach**
```latex
% Load template for body styling
\input{templates/template2.tex}

% Define custom cover using template colors
\newcommand{\hybridCover}[5]{%
  % Custom layout with template colors
}
```

### 3. **Add Your Content**
```latex
\begin{document}
% Cover page
\customCover{...} % or \templateOneCover{...}

% Content sections
\input{content/01-introduction.tex}
\input{content/02-main-content.tex}
% ... more sections
\end{document}
```

#### Note on Content Organization
Content files can be chapters, standalone pages, or granular sections. Covers and templates define the outer shell of the document; your content files are independent and do not need to be part of the cover page.

Common patterns:
- Chapters: `01-introduction.tex`, `02-methods.tex`, `03-results.tex`
- Standalone pages: `10-appendix-a.tex`, `20-acknowledgements.tex`

You can also use `\include{...}` for chapter-length units to enforce page breaks and keep auxiliary files separate:

```latex
% Example: mixing \input and \include
\begin{document}
  % Cover
  \templateOneCover{...}

  % Chapters as separate units
  \include{content/01-introduction}
  \include{content/02-methods}

  % Smaller sections
  \input{content/03-results-section-a.tex}
  \input{content/03-results-section-b.tex}
\end{document}
```

## ⚡ Performance Optimization

### **Compilation Time Guidelines**

| Configuration | Time | Memory | Overleaf Free Plan |
|---------------|------|--------|--------------------|
| Basic (boxes only) | 8-12s | Low | ✅ Excellent |
| Selective (3-4 modules) | 15-25s | Medium | ✅ Good |
| Full (all modules) | 25-35s | High | ⚠️ May timeout |

### **Module Selection Strategy**

1. **Start Basic**: Begin with minimal modules
2. **Add Selectively**: Enable only needed features
3. **Test Compilation**: Verify performance on target platform
4. **Optimize**: Disable unused modules

## 🎨 Brand Color Integration

All use cases demonstrate proper brand color usage:

```latex
% Brand colors automatically loaded from brand_colors.tex
\textcolor{brandPrimary}{Primary elements}
\textcolor{brandSecondary}{Secondary elements}  
\textcolor{brandAccent}{Highlights and accents}
\textcolor{brandTertiary}{Subsections and warnings}
```

### **Color Cascade System**
The system automatically derives UI colors from your brand colors:
- Table headers use `brandPrimary`
- Borders use `brandPrimary!20`
- Success elements use `brandAccent`
- Section numbers use brand color hierarchy

## 📋 Module Reference

| Module | Purpose | When to Enable |
|--------|---------|----------------|
| **AdvancedTypography** | Drop caps, advanced fonts | Professional documents |
| **Mathematics** | Equations, theorems | Academic, technical papers |
| **Tables** | Enhanced table formatting | Data-heavy documents |
| **Boxes** | Info/warning/success boxes | All documents (recommended) |
| **Lists** | Enhanced list styling | Structured content |
| **Code** | Syntax highlighting | Technical documentation |
| **Images** | Advanced image handling | Visual-heavy documents |
| **Algorithms** | Pseudocode formatting | Computer science papers |
| **References** | Bibliography management | Academic papers |

## 🔧 Customization Examples

### **Custom Colors**
```latex
% Override brand colors in brand_colors.tex
\definecolor{brandPrimary}{HTML}{YOUR_COLOR}
\definecolor{brandSecondary}{HTML}{YOUR_COLOR}
```

### **Custom Cover Elements**
```latex
% Add custom graphics
\begin{tikzpicture}
  \fill[brandPrimary] (0,0) rectangle (2,1);
  \node[white] at (1,0.5) {Custom Element};
\end{tikzpicture}
```

### **Module Combinations**
```latex
% Academic configuration
\newcommand{\EnableMathematics}{true}
\newcommand{\EnableAlgorithms}{true}
\newcommand{\EnableReferences}{true}

% Business configuration  
\newcommand{\EnableTables}{true}
\newcommand{\EnableBoxes}{true}
\newcommand{\EnableImages}{true}
```

## 🎯 Best Practices

1. **Performance First**: Start with basic configuration
2. **Brand Consistency**: Use brand color system throughout
3. **Template Selection**: Choose template based on document purpose
4. **Content Organization**: Use content/ directory for sections
5. **Testing**: Always test compilation time on target platform

## 📞 Support

For questions or issues:
1. Check this documentation first
2. Review the specific use case file
3. Test with basic configuration
4. Verify module requirements

Each use case file is fully documented and ready to compile!
