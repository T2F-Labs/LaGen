# Cover System for LaTeX Templates

This directory contains cover page designs for the Lagen document system.

## How to Use Covers

To use a cover in your document, set the `\covertype` command in your main document:

```latex
\newcommand{\covertype}{1}  % Use cover1.tex
```

Valid values:
- `none` - No cover (default)
- `1`, `2`, `3`, etc. - Corresponds to cover1.tex, cover2.tex, etc.

## Available Cover Designs

### Cover 1: Modern Gradient Design
![Cover 1](https://via.placeholder.com/400x200/3b82f6/FFFFFF?text=Modern+Gradient)

**Style:** Bold, contemporary design with gradient backgrounds and floating geometric shapes.

**Best for:** Marketing materials, product documentation, innovation reports, and presentations that need visual impact.

**Features:**
- Gradient blue background with semi-transparent geometric elements
- Large prominent title with ample whitespace
- Centered summary box with platform/focus area details
- Modern, clean typography with clear hierarchy

**Feeling:** Dynamic, forward-thinking, innovative, and professional.

### Cover 2: Minimal Circle Design
![Cover 2](https://via.placeholder.com/400x200/f8fafc/000000?text=Minimal+Circle)

**Style:** Clean and elegant with circular motifs and structured layout.

**Best for:** Corporate communications, business reports, proposals, and formal documents.

**Features:**
- White background with minimal decorative elements
- Concentric circles as a focal point
- Structured layout with clear sections
- Color-coded rule lines to guide reading

**Feeling:** Professional, structured, trustworthy, and approachable.

### Cover 3: Modern Corporate Design
![Cover 3](https://via.placeholder.com/400x200/f8fafc/1e293b?text=Modern+Corporate)

**Style:** Clean corporate layout with accent bar and structured information presentation.

**Best for:** Annual reports, corporate guidelines, business proposals, and formal business documentation.

**Features:**
- White background with horizontal accent bar at top
- Corporate header area with company and department information
- Large document title with clear subtitle
- Segmented decorative element below title
- Classification information in a structured footer

**Feeling:** Professional, authoritative, precise, and corporate.

### Cover 4: Elegant Academic Design
![Cover 4](https://via.placeholder.com/400x200/ffffff/1e293b?text=Elegant+Academic)

**Style:** Refined academic layout with traditional elements and formal structure.

**Best for:** Research papers, academic publications, dissertations, and scholarly reports.

**Features:**
- Classic horizontal rule borders
- Centered title and author information
- Abstract box with formal academic structure
- Keywords section
- Subtle dot pattern at the bottom 

**Feeling:** Scholarly, authoritative, traditional, and credible.

### Cover 5: Technical Blueprint Design
![Cover 5](https://via.placeholder.com/400x200/f8fafc/3b82f6?text=Technical+Blueprint)

**Style:** Technical schematic-inspired layout with grid patterns and precise measurements.

**Best for:** Technical specifications, engineering documents, software documentation, and detailed technical reports.

**Features:**
- Blueprint-like grid background
- Technical header with document IDs and revision information
- Status banner
- Technical details block with document metadata
- Linear pattern in the content area
- Corner markers and frame elements for technical appearance

**Feeling:** Technical, precise, detailed, and systematic.

### Cover 6: Creative Gradient Design
![Cover 6](https://via.placeholder.com/400x200/60a5fa/FFFFFF?text=Creative+Gradient)

**Style:** Dynamic, artistic design with gradient background and organic elements.

**Best for:** Creative presentations, design portfolios, marketing content, and innovative reports.

**Features:**
- Vibrant gradient background
- Random decorative circle pattern
- Curved decorative elements
- Wave pattern under title
- Modern drop-shadow effects
- Circular brand element at bottom

**Feeling:** Creative, energetic, modern, and visually engaging.

## Creating New Covers

To create a new cover:

1. Create a new file named `coverX.tex` (where X is the next available number)
2. Add a header comment with `% ========== COVERX: DESCRIPTION ==========`
3. Include any required TikZ libraries or packages at the top
4. Define any additional placeholder commands you need
5. Design your cover content
6. Avoid using document structure elements like `\documentclass`, `\begin{document}`, `\end{document}`

### Available Placeholder Variables

All cover files have access to these predefined placeholder variables:

- `\TitlePlaceholder` - Document title
- `\SubtitlePlaceholder` - Document subtitle
- `\SummaryTitlePlaceholder` - Summary title
- `\SummaryTextPlaceholder` - Summary text
- `\PlatformsList` - List of platforms
- `\FocusList` - List of focus areas
- `\FocusItemOne` through `\FocusItemFour` - Individual focus items
- `\AuthorPlaceholder` - Author name
- `\DatePlaceholder` - Document date
- `\ClassificationPlaceholder` - Document classification
- `\DistributionPlaceholder` - Distribution information
- `\VersionPlaceholder` - Document version
- `\StatusPlaceholder` - Document status
- `\ClassificationLevelPlaceholder` - Confidentiality level

### Cover Template

```latex
% ========== COVERN: DESCRIPTION ==========
% Cover-specific dependencies
\usetikzlibrary{positioning,shapes.geometric}

% Provide any additional placeholder commands
\providecommand{\CustomPlaceholder}{Default Value}

% Your cover design here
\begin{tikzpicture}[remember picture,overlay]
    % Your TikZ content
\end{tikzpicture}

% Title section
% ...

% Summary section
% ...

% Footer information 
% ...
```

## Fixing Existing Cover Files

If you have cover files designed with document structure elements, use the provided script:

```bash
python tools/fix_covers.py
```

This will process all cover files and make them compatible with the direct inclusion approach. 