# Project Structure

## Root Directory Layout

```
├── main.tex                    # Main document entry point with module configuration
├── config.tex                  # Core LaTeX configuration with conditional module loading
├── brand_colors.tex            # Brand color definitions and color cascade system
├── GUIDE.md                    #  LaTeX configuration guide
├── README.md                   # Project overview and quick start
└── .kiro/                      # Kiro IDE configuration and steering files
```

## Core Configuration Files

### Entry Points
- **`main.tex`** - Primary document template with module flags
- **`config.tex`** - Core configuration that loads modules conditionally
- **`brand_colors.tex`** - Centralized color definitions for consistent branding

### Module System
The project uses a modular architecture where features are loaded only when needed:

```latex
% In main.tex - Configure which modules to load
\newcommand{\EnableMathematics}{true}
\newcommand{\EnableTables}{true}
\newcommand{\EnableBoxes}{false}
```

## Directory Structure

### `/content/` - Document Content
```
content/
├── 01-introduction.tex         # Chapter/section files
├── 02-mathematics.tex          # Mathematical content examples
├── 03-tables.tex              # Table examples and formatting
└── 04-conclusion.tex           # Conclusion content
```

### `/modules/` - Feature Modules
```
modules/
├── typography-advanced.tex     # Advanced text formatting and typography
├── mathematics.tex            # Math packages and theorem environments
├── tables.tex                # Table styling and enhanced column types
├── boxes.tex                 # Callout boxes and visual elements
├── lists.tex                 # Enhanced list formatting and icons
├── code.tex                  # Code highlighting and listings
├── images.tex                # Image handling and positioning
├── algorithms.tex            # Algorithm typesetting
└── references.tex            # Bibliography and cross-referencing
```

### `/templates/` - Document Templates
```
templates/
├── template1.tex              # Modern geometric design
├── template2.tex              # Corporate sidebar design
├── template3.tex              # Minimal elegant design
└── README.md                  # Template usage documentation
```

### `/covers/` - Cover Page Designs
```
covers/
├── cover1.tex                 # Various cover page designs
├── cover2.tex                 # Independent of templates
├── cover3.tex                 # Can be mixed and matched
├── ...
└── README.md                  # Cover usage guide
```

### `/use-cases/` - Complete Examples
```
use-cases/
├── 01-cover-custom-content.tex    # Custom cover examples
├── 03-template1-custom-content.tex # Template usage examples
├── 06-modular-basic.tex           # Module configuration examples
├── 10-academic-paper.tex          # Specialized document types
└── README.md                      # Use case documentation
```

### `/examples/` - Template Demonstrations
```
examples/
├── example_use_template1.tex      # Template 1 demonstration
├── example_use_template2.tex      # Template 2 demonstration
├── example_use_template3.tex      # Template 3 demonstration
└── README.md                      # Example documentation
```

### `/scripts/` - Setup and Build Tools
```
scripts/
├── setup-xetex-env.sh            # Linux/macOS environment setup
└── setup-xetex-env.ps1           # Windows PowerShell setup
```

### `/assets/` - Static Resources
```
assets/
└── covers/                        # Cover page images and graphics
    ├── cover1.jpg
    ├── cover2.jpg
    └── ...
```

## File Naming Conventions

### Document Files
- **Main documents**: `main.tex`, `document.tex`
- **Content sections**: `01-introduction.tex`, `02-chapter-name.tex` (numbered for ordering)
- **Use cases**: `01-cover-custom.tex` (numbered with descriptive names)

### Module Files
- **Feature modules**: `module-name.tex` (kebab-case)
- **Templates**: `template1.tex`, `template2.tex` (numbered)
- **Covers**: `cover1.tex`, `cover2.tex` (numbered)

### Configuration Files
- **Core config**: `config.tex` (main configuration)
- **Brand colors**: `brand_colors.tex` (underscore for clarity)
- **Custom themes**: `my_theme.tex`, `custom_colors.tex`

## Architecture Patterns

### Modular Loading Pattern
```latex
% Define module flags before loading config
\newcommand{\EnableFeature}{true/false}
\input{config.tex}  % Loads modules based on flags
```

### Brand Color Cascade
```latex
% Define primary brand colors
\definecolor{brandPrimary}{HTML}{2563EB}
% Derived colors automatically cascade
\colorlet{accent}{brandPrimary}
```

### Template Integration
```latex
\input{config.tex}           # Load core configuration
\input{templates/template1.tex}  # Load template styling
\templateOneCover{...}       # Use template-specific commands
```

### Content Organization
- Keep content files independent of styling
- Use `\input{}` for content inclusion
- Separate structure from presentation
- Enable easy content reuse across different templates

## Best Practices

### File Organization
- Group related functionality in modules
- Keep content separate from configuration
- Use descriptive, numbered filenames for ordering
- Maintain consistent naming conventions

### Module Design
- Each module should be self-contained
- Provide fallback colors/settings if brand colors missing
- Use `\providecommand{}` for optional dependencies
- Include module loading messages for debugging

### Template Structure
- Templates should work with any brand color scheme
- Provide both cover and body styling options
- Allow mixing covers from different templates
- Include  usage examples