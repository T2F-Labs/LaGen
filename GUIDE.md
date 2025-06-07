# LaTeX Configuration Guide

This guide explains the features and usage of the `config.tex` file, which provides a comprehensive LaTeX setup for professional document creation.

## Table of Contents

- [Font and Encoding](#font-and-encoding)
- [Page Layout](#page-layout)
- [Colors](#colors)
- [Typography](#typography)
- [Advanced Text Features](#advanced-text-features)
- [Section Styling](#section-styling)
- [Headers and Footers](#headers-and-footers)
- [Table of Contents](#table-of-contents)
- [Advanced Reference Management](#advanced-reference-management)
- [Mathematical Typesetting](#mathematical-typesetting)
- [Page Break Control](#page-break-control)
- [Boxes and Callouts](#boxes-and-callouts)
- [Lists](#lists)
- [Tables](#tables)
- [Code Listings](#code-listings)
- [Algorithms](#algorithms)
- [Icon Boxes](#icon-boxes)
- [Title Page](#title-page)
- [Document Metadata](#document-metadata)
- [Advanced Image Handling](#advanced-image-handling)

## Font and Encoding

### Overview

This section configures font setup and character encoding for your document, using XeTeX/LuaTeX engines for modern font handling.

### Packages

- `inputenc` & `fontenc`: Basic character encoding
- `lmodern`: Latin Modern font family
- `fontspec`: Modern font handling (for XeTeX/LuaTeX)
- `setspace`: Line spacing control
- `xcolor`: Color management
- `microtype`: Typography refinements
- `scalefnt`: Font scaling utilities

### Features

- **Main Font Setup**: Using the "Inter" font family with various weights
- **Letter Spacing Control**: Fine control of space between characters 
- **Brand Consistency**: Special macros for consistent branding

### Usage

```latex
% Set your preferred font
\setmainfont{YourFont}[
    UprightFont = *-Regular,
    BoldFont = *-Bold,
    ItalicFont = *-Italic,
    BoldItalicFont = *-BoldItalic,
    LetterSpace = 3.0
]

% Use branded text macros
\brandname{Company} produces the \productname{Product}
```

## Page Layout

### Overview

Controls the overall document dimensions, margins, and spacing.

### Packages

- `geometry`: Page dimensions and margins
- `placeins`: Float placement control
- `flafter`: Ensures floats appear after references
- `fixltx2e`: Bug fixes for LaTeX kernel

### Features

- Professional margin settings
- Float control to improve document flow
- Customizable page dimensions

### Usage

```latex
% Adjust margins as needed
\geometry{
    top=1in,
    bottom=1in,
    left=1in,
    right=1in
}
```

## Colors

### Overview

Defines a comprehensive color palette for consistent styling throughout your document.

### Features

- **Text Colors**: Primary, secondary, and accent colors
- **Semantic Colors**: Success, warning, and background colors
- **Functional Colors**: For tables, code blocks, and UI elements

### Usage

```latex
% Use defined colors
{\color{accent}This text is in accent color}

% Define your own colors
\definecolor{mycolor}{HTML}{FF5733}
```

## Typography

### Overview

Fine-tunes the spacing and appearance of text for improved readability.

### Packages

- `microtype`: Advanced typography adjustments
- `parskip`: Paragraph spacing control

### Features

- Zero paragraph indentation with controlled spacing between paragraphs
- Microtypography improvements for professional appearance

### Usage

The settings work automatically, but you can adjust spacing:

```latex
\setlength{\parskip}{10pt} % More space between paragraphs
```

## Advanced Text Features

### Overview

Provides specialized typography tools for professional document appearance.

### Packages

- `lettrine`: Creates drop caps at section beginnings
- `csquotes`: Smart quotation handling
- `nowidow`: Prevents orphaned lines
- `needspace`: Controls page breaks

### Features

- **Drop Caps**: Elegant large initial letters
- **Smart Quotes**: Proper quotation marks
- **Widow Control**: Prevents single lines at page breaks

### Usage

```latex
% Create a drop cap
\lettrine{T}{his} paragraph begins with a drop cap...

% Use proper quotes
"This text has properly formatted quotation marks"

% Block quotation
\begin{displayquote}
This is a block quotation with proper formatting.
\end{displayquote}
```

## Section Styling

### Overview

Customizes the appearance of headings at various levels.

### Packages

- `titlesec`: Heading customization

### Features

- Color-coordinated section headings
- Custom spacing before and after headings
- Decorative elements (horizontal rule below sections)

### Usage

Section styling is applied automatically to standard LaTeX sectioning commands:

```latex
\section{My Section}
\subsection{My Subsection}
\subsubsection{My Subsubsection}
```

## Headers and Footers

### Overview

Configures the content displayed at the top and bottom of each page.

### Packages

- `fancyhdr`: Header and footer customization
- `lastpage`: Provides total page count

### Features

- Document title in the header
- Page numbers with total page count
- Customizable content areas (left, center, right)

### Usage

```latex
% Customize header content
\fancyhead[L]{Your Custom Left Header}
\fancyhead[R]{Your Custom Right Header}
\fancyfoot[C]{Your Custom Footer}
```

## Table of Contents

### Overview

Styles the table of contents for improved navigation and appearance.

### Packages

- `tocloft`: Table of contents customization

### Features

- Dotted leaders between entries and page numbers
- Custom fonts and colors for different TOC levels
- Controlled spacing between entries

### Usage

The TOC styling is applied automatically when you use:

```latex
\tableofcontents
```

## Advanced Reference Management

### Overview

Provides tools for sophisticated bibliography management and cross-referencing.

### Packages

- `biblatex`: Advanced bibliography management
- `hyperref`: PDF features and hyperlinks
- `nameref`: Reference by name
- `varioref`: Page-aware references
- `cleveref`: Intelligent cross-references

### Features

- **Bibliography**: Customizable citation and reference styles
- **Hyperlinks**: Clickable links and PDF bookmarks
- **Cross-References**: Smart references to figures, tables, sections, etc.

### Usage

```latex
% Cite a reference
\cite{key}

% Reference a section
\nameref{sec:introduction}

% Smart cross-reference
\cref{fig:example}
```

## Mathematical Typesetting

### Overview

Provides comprehensive tools for typesetting mathematical content with precision and elegance.

### Packages

- `amsmath`: Advanced math environments and commands
- `amssymb`: Extended mathematical symbols
- `fixmath`: Corrects typography issues in math mode
- `siunitx`: Consistent formatting of numbers and units

### Features

- **Math Environments**: Equations, align, gather, multline, etc.
- **Symbol Collection**: Comprehensive mathematical symbols
- **Unit Formatting**: Consistent and correct display of units
- **Custom Units**: Predefined units (USD, hour, year)

### Usage

```latex
% Basic equation
\begin{equation}
  E = mc^2
\end{equation}

% Aligned equations
\begin{align}
  a &= b + c \\
  d &= e + f
\end{align}

% Numbers with units
\SI{5.2}{\kilo\gram}
\SI{42}{\metre\per\second}
\SI{1500}{\USD}
\SI{2.5}{\hour}
\SI{3}{\year}

% Define your own units
\DeclareSIUnit\myunit{mu}
```

### Tips for Mathematical Typesetting

- Use `align` instead of `eqnarray` for aligned equations
- Use `\text{}` for text within math mode
- Use `\left( ... \right)` for automatically sized parentheses
- Use the `siunitx` package consistently for all measurements and units

## Page Break Control

### Overview

Provides tools to control page breaks for better document flow.

### Packages

- `afterpage`: Execute commands after the current page

### Usage

```latex
% Insert a page break after the current content finishes
\afterpage{\clearpage}
```

## Boxes and Callouts

### Overview

Creates visually distinct boxes for highlighting important content.

### Packages

- `tikz`: Drawing and effects
- `tcolorbox`: Advanced box creation

### Features

- **Info Boxes**: For general information
- **Alert Boxes**: For warnings and cautions
- **Success Boxes**: For positive highlights
- **Logo Boxes**: With icons and visual elements

### Usage

```latex
% Basic info box
\begin{infobox}
Important information goes here.
\end{infobox}

% Info box with title
\begin{infobox}[title=Note]
Important information with a title.
\end{infobox}

% Alert box for warnings
\begin{alertbox}
Warning or caution information.
\end{alertbox}

% Success box for positive information
\begin{successbox}
Success or positive information.
\end{successbox}
```

## Lists

### Overview

The configuration provides extensive list customization options for creating professional, hierarchical, and visually appealing lists. From basic bullet points to task-oriented lists with icons, the setup allows for a wide range of list presentations.

### Packages

- `enumitem`: Advanced list customization
- `fontawesome5`: Icon integration for modern list items (already loaded in Icon Boxes section)
- `tikz`: Custom bullet styling (already loaded in Boxes section)

### Features

- **Hierarchical Styling**: Distinct formatting for each nesting level
- **Color-Coded Lists**: Visual hierarchy through consistent color schemes
- **Custom Icons**: Task-oriented and priority-based list markers
- **Task Lists**: Pre-configured environments for completed, pending, and failed tasks
- **Priority Indicators**: High, medium, and low priority item styling
- **Spacing Control**: Compact and expanded list variants
- **TikZ Bullets**: Custom geometric bullet points
- **Description Lists**: Enhanced styling for term-definition pairs

### Usage

#### Basic Lists

```latex
% Standard bullet list with hierarchical styling
\begin{itemize}
    \item First level item
    \begin{itemize}
        \item Second level item
        \begin{itemize}
            \item Third level item with small square bullet
        \end{itemize}
    \end{itemize}
\end{itemize}

% Standard numbered list with hierarchical styling
\begin{enumerate}
    \item First level uses colored numbers
    \begin{enumerate}
        \item Second level uses letters in parentheses
        \begin{enumerate}
            \item Third level uses roman numerals
        \end{enumerate}
    \end{enumerate}
\end{enumerate}

% Description list for term-definition pairs
\begin{description}
    \item[API] Application Programming Interface
    \item[UI/UX] User Interface and User Experience
    \item[CI/CD] Continuous Integration and Continuous Deployment
\end{description}
```

#### Task-Oriented Lists

```latex
% Completed tasks
\begin{tasklist}
    \item Project requirements finalized
    \item Design mockups approved
    \item Initial development phase completed
\end{tasklist}

% Pending tasks
\begin{pendingtask}
    \item Integration testing in progress
    \item Documentation updates underway
    \item Client feedback incorporation
\end{pendingtask}

% Failed or cancelled tasks
\begin{failedtask}
    \item Legacy system migration (cancelled)
    \item Optional feature implementation (postponed)
    \item Third-party integration (incompatible)
\end{failedtask}
```

#### Priority-Based Lists

```latex
% High priority items
\begin{highpriority}
    \item Security vulnerability patch
    \item Critical performance issue
    \item Deadline-sensitive deliverable
\end{highpriority}

% Medium priority items
\begin{mediumpriority}
    \item Feature enhancement request
    \item Minor bug fixes
    \item Documentation improvements
\end{mediumpriority}

% Low priority items
\begin{lowpriority}
    \item UI refinements
    \item Optional optimizations
    \item Future planning items
\end{lowpriority}
```

#### Custom List Styling

```latex
% Use TikZ bullets for custom geometric styling
\begin{itemize}[label=\tikzbullet{accent}]
    \item Custom bullet with accent color
    \item Professional geometric styling
    \begin{itemize}[label=\tikzbullet{success}]
        \item Nested level with different color
        \item Consistent geometric appearance
    \end{itemize}
\end{itemize}

% Create lists with custom FontAwesome icons
\begin{itemize}[label=\color{primary}\faBookmark]
    \item Custom bookmark icon for key points
    \item Tailored visual indicators
\end{itemize}

% Modify spacing for specific lists
\begin{itemize}[itemsep=8pt, label=\color{success}\faArrowRight]
    \item Increased spacing between items
    \item For better readability
\end{itemize}
```

#### Spacing Variants

```latex
% Compact list for dense information
\begin{compactlist}
    \item Minimal spacing between items
    \item Space-efficient presentation
    \item Ideal for appendices or dense references
\end{compactlist}

% Expanded list for emphasis
\begin{expandedlist}
    \item Generous spacing between items
    \item Enhanced readability
    \item Draws attention to content
\end{expandedlist}
```

#### Advanced Customization

```latex
% One-off customization for specific lists
\begin{itemize}[
    label=\color{warning}\faStar,
    leftmargin=25pt,
    itemsep=6pt,
    font=\bfseries
]
    \item Custom formatting for special emphasis
    \item Combines multiple customization options
    \item Tailored to specific document sections
\end{itemize}

% Roman numeral list with custom formatting
\begin{enumerate}[
    label=\color{primary}\Roman*.,
    font=\bfseries,
    leftmargin=30pt
]
    \item Major document section
    \item With custom Roman numerals
    \item And enhanced visibility
\end{enumerate}
```

### Tips for Professional Lists

- **Color Consistency**: Match list colors with your document's color scheme
- **Visual Hierarchy**: Use different bullet styles to indicate hierarchy
- **Icon Meaning**: Choose icons that intuitively represent item types or categories
- **Balanced Spacing**: Adjust spacing based on content density and document style
- **Mixed Approaches**: Combine different list types (e.g., icons for top level, regular bullets for nested items)

## Tables

### Overview

Provides tools for creating professional tables with advanced features.

### Packages

- `booktabs`: Professional table rules
- `tabularx`: Flexible width tables
- `longtable`: Multi-page tables
- `array`: Enhanced column types
- `multirow`: Spanning multiple rows

### Features

- **Column Types**: Left (L), Center (C), Right (R), and auto-width (X)
- **Multi-page Tables**: Tables that can span multiple pages
- **Row Colors**: Alternating row colors for readability
- **Cell Spanning**: Cells that span multiple rows or columns

### Usage

```latex
% Basic table with booktabs rules
\begin{tabular}{lcc}
    \toprule
    Item & Quantity & Price \\
    \midrule
    Widget & 5 & \$10 \\
    Gadget & 3 & \$15 \\
    \bottomrule
\end{tabular}

% Table with custom column types
\begin{tabularx}{\textwidth}{L{2cm}C{3cm}R{2cm}>{\raggedleft\arraybackslash}X}
    Header 1 & Header 2 & Header 3 & Header 4 \\
    Content & Content & Content & Content \\
\end{tabularx}

% Multi-page table
\begin{longtable}{lll}
    \caption{My Long Table} \\
    \toprule
    Col 1 & Col 2 & Col 3 \\
    \midrule
    \endhead
    % Table content...
    \bottomrule
\end{longtable}
```

## Code Listings

### Overview

Provides tools for displaying source code with syntax highlighting.

### Packages

- `listings`: Basic code display
- `minted`: Advanced syntax highlighting (requires Python)

### Features

- Syntax highlighting for various languages
- Line numbering
- Custom styling (colors, fonts, frames)

### Usage

```latex
% Basic code listing
\begin{lstlisting}[language=Python]
def hello_world():
    print("Hello, world!")
\end{lstlisting}

% Advanced syntax highlighting with minted
\begin{minted}{javascript}
function helloWorld() {
    console.log("Hello, world!");
}
\end{minted}
```

## Algorithms

### Overview

Provides tools for displaying algorithms and pseudocode.

### Packages

- `algorithm2e`: Algorithm environment

### Features

- Structured algorithm display
- Line numbering
- Keywords for control structures

### Usage

```latex
\begin{algorithm}[H]
    \SetAlgoLined
    \KwData{Input data $X$}
    \KwResult{Output $Y$}
    Initialize $Y$\;
    \For{each $x \in X$}{
        Process $x$\;
        \If{condition is met}{
            Update $Y$\;
        }
    }
    \Return{$Y$}\;
    \caption{My Algorithm}
\end{algorithm}
```

## Advanced Image Handling

### Overview

The configuration provides sophisticated image handling capabilities with various shapes, styles, and fallback mechanisms. These features enable elegant, professional image presentation with graceful handling of missing images.

### Packages

- `graphicx`: Basic image inclusion
- `adjustbox`: Enhanced image positioning
- `tikz`: Advanced image manipulation
- `varwidth`: Variable-width text containers

### Features

- **Fallback Mechanism**: Displays placeholder when images are missing
- **Shape Options**: Rectangular, rounded, circular, and custom shapes
- **Visual Effects**: Frames, shadows, and decorative elements
- **Responsive Images**: Full-width and proportionally scaled images
- **Special Features**: Zoom effects and image grids

### Usage

#### Basic Image Handling

```latex
% Basic image with fallback text
\imageWithFallback[scale=1.2]{images/photo.jpg}{5cm}{Image Not Available}

% Standard rectangular image with caption
\rectImage{images/diagram.png}{8cm}{System Architecture}{Diagram Not Available}
```

#### Shaped Images

```latex
% Image with rounded corners
\roundedImage{images/profile.jpg}{4cm}{10pt}{Team Member}{Profile Not Available}

% Circular image (perfect for profile pictures)
\circularImage{images/avatar.png}{3cm}{CEO Portrait}{Avatar Not Available}
```

#### Enhanced Visual Styling

```latex
% Image with drop shadow effect
\shadowImage{images/product.jpg}{6cm}{Product Showcase}{Image Not Available}

% Image with custom colored frame
\framedImage{images/chart.pdf}{7cm}{accent}{Quarterly Results}{Chart Not Available}
```

#### Responsive Images

```latex
% Full-width image that scales with the document
\fullwidthImage{images/banner.jpg}{3cm}{Website Banner}{Banner Image Not Available}
```

#### Advanced Features

```latex
% Image with magnified section
\zoomedImage{images/circuit.jpg}{8cm}{2}{3}{1}{4}{Circuit Detail}{Circuit Diagram Not Available}

% 2x2 grid of related images
\imageGrid{images/spring.jpg}{images/summer.jpg}{images/fall.jpg}{images/winter.jpg}{10cm}{Seasonal Changes}{Season Images Not Available}
```

### Tips for Professional Image Handling

- **Consistent Sizing**: Maintain consistent image dimensions for similar content
- **Appropriate Shapes**: Use shapes that complement the image content (e.g., circular for portraits)
- **Alt Text**: Always provide descriptive alt text for accessibility and fallbacks
- **Resolution**: Use appropriate resolution images (not too large or too small)
- **Captions**: Add informative captions to give context to images

## Icon Boxes

### Overview

Creates visually enhanced boxes with icons for better visual communication.

### Packages

- `fontawesome5`: Icon collection
- `awesomebox`: Icon-enhanced boxes
- `bclogo`: Logo-enhanced boxes

### Features

- Various icon styles (information, warning, tip)
- Color-coded boxes with matching icons
- Visual hierarchy for important information

### Usage

```latex
% Icon box with fontawesome
\awesomebox[teal]{2pt}{\faLightbulb}{teal}{This is a tip with an icon.}

% Warning box
\awesomebox[orange]{2pt}{\faExclamationTriangle}{orange}{This is a warning.}

% Logo box
\bclogo[logo=\bcattention]{This is an attention box.}
```

## Title Page

### Overview

Customizes the appearance of the title page for a professional first impression.

### Packages

- `titling`: Title page customization

### Features

- Controlled spacing
- Color coordination
- Decorative elements

### Usage

Title page styling is applied automatically when you use:

```latex
\maketitle
```

## Document Metadata

### Overview

Sets document information for PDF properties and title page.

### Features

- Title and subtitle
- Author information
- Date (current or specific)
- PDF metadata

### Usage

```latex
\title{Main Title\\[0.3em]Subtitle}
\author{Author Name}
\date{January 1, 2023} % Specific date or \today
```

---

This guide covers the core features of the `config.tex` file. For more detailed usage examples, refer to the `latex_template.tex` file. 