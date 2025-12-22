# Technology Stack

## Core Technologies

- **LaTeX Engine**: XeTeX (required for advanced font features via fontspec)
- **Document Class**: Standard LaTeX article class
- **Build System**: XeLaTeX compiler with optional latexmk automation
- **Font System**: fontspec package for OpenType/TrueType font support
- **Template Engine**: Jinja2 (Python) for programmatic document generation

## Key LaTeX Packages

### Core Configuration
- `geometry` - Page layout and margins
- `xcolor` - Color management and brand color system
- `fontspec` - Modern font handling (XeTeX/LuaTeX)
- `ifthen` - Conditional module loading

### Modular Features (Loaded on Demand)
- **Typography**: `microtype`, `soul`, `lettrine`, `csquotes`, `ragged2e`
- **Mathematics**: `amsmath`, `amssymb`, `mathtools`, `siunitx`, `physics`, `amsthm`
- **Tables**: `booktabs`, `tabularx`, `longtable`, `multirow`, `array`
- **Boxes**: `tcolorbox`, `tikz`, `fontawesome5`
- **Code**: `listings`, `minted` (requires Python Pygments)
- **Images**: `graphicx`, `adjustbox`, `eso-pic`
- **Algorithms**: `algorithm`, `algorithmic`
- **References**: `biblatex`, `hyperref`, `cleveref`

## Build Commands

### Compilation

```bash
# Basic compilation (single pass)
xelatex main.tex

# Full compilation with references
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex

# Using latexmk (automated)
latexmk -xelatex main.tex

# With shell escape (for minted code highlighting)
xelatex -shell-escape main.tex
```

### Environment Setup

```bash
# Linux/macOS setup
bash scripts/setup-xetex-env.sh --create-latexmkrc

# Windows setup
powershell scripts/setup-xetex-env.ps1 -CreateLatexmkrc

# Full installation with all packages
bash scripts/setup-xetex-env.sh --full --install-pygments --create-latexmkrc
```

### Common Options

- `--full` - Install complete TeX Live scheme (large download)
- `--install-pygments` - Install Python Pygments for minted syntax highlighting
- `--create-latexmkrc` - Generate latexmkrc configuration file

## Compilation Performance

Module loading affects compilation time:
- **Basic** (minimal modules): 8-12 seconds
- **Selective** (common modules): 15-25 seconds  
- **Full** (all modules): 25-35 seconds

## Font Requirements

The default configuration uses the "Inter" font family. Ensure required fonts are installed or modify `config.tex` to use available system fonts.

## Python Integration

While the core system is pure LaTeX, Python/Jinja2 can be used for:
- Programmatic document generation from data
- Template variable substitution
- Dynamic content generation

Python is optional unless using the `minted` package for advanced code highlighting.
