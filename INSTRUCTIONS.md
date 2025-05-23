# 📝 LaTeX Document Generator (Jinja2 Template)

This repository provides a powerful and flexible **Jinja2 template** for generating LaTeX documents programmatically using structured Python data.

## 🚀 Features

-   Full support for complex LaTeX document generation
    
-   Modular sections with support for subsections, tables, lists, callout boxes, algorithms, quotes, code blocks, and references
    
-   Configurable metadata, classification levels, and document distribution
    
-   Drop-in Python integration with `jinja2.Template`
    
-   Flexible table formatting with colored headers and alternating rows
    
-   Enhanced box types with icons and logos
    
-   Advanced algorithm support with function definitions
    
-   Code highlighting with both listings and minted packages

* * *

## 📦 Template Variables

### 📄 Document Metadata

Variable | Type | Description
-------- | ---- | -----------
`title` | `str` | Document title
`author` | `str` | Author's name
`date` | `str` | Document date (defaults to `\today`)
`executive_summary` | `str` | Executive summary text
`document_classification` | `str` | Classification level
`distribution` | `str` | Distribution information
`version` | `str` | Document version
`show_toc` | `bool` | Show table of contents (default `True`)

* * *

### 📚 Sections

Each section object may include:

-   `level`: Section depth (`1`, `2`, or `3`)
    
-   `title`: Section title
    
-   `label`: (optional) LaTeX cross-reference label
    
-   `content`: Main section content
    
-   `drop_cap`: Use drop cap for first paragraph (`bool`)
    
-   `subsections`: List of subsection objects
    
-   `tables`, `fancy_tables`, `lists`, `boxes`, `code_blocks`, `algorithms`, `quotes`: Respective content blocks
    
-   `afterpage`: Content to display on the next page

* * *

### 📊 Table Objects

#### Standard Tables

```json
{
  "caption": "My Table",
  "label": "tab:my_table",
  "column_spec": "lrrr",
  "env": "tabular",
  "use_colors": true,
  "headers": ["Column 1", "Column 2", "Column 3"],
  "rows": [
    ["A", "B", "C"], 
    ["D", "E", "F"]
  ],
  "has_footer": true,
  "footer_rows": [
    ["Total", "X", "Y"]
  ]
}
```

#### Fancy Tables (in tcolorbox)

```json
{
  "title": "📊 Data Analysis Results",
  "title_bg": "accent",
  "column_spec": ">{\raggedright\\arraybackslash\\bfseries}X >{\raggedright\\arraybackslash}X c c",
  "headers": ["Category", "Description", "Value", "Status"],
  "rows": [
    ["Project A", "Implementation phase", "95%", "Complete"],
    ["Project B", "Analysis phase", "45%", "In progress"]
  ]
}
```

* * *

### 📝 List Objects

-   `type`: `"itemize"` or `"enumerate"`
    
-   `items`: List of string items or objects with `subitems` property

Example with nested lists:

```json
{
  "type": "itemize",
  "items": [
    "First level item",
    {
      "text": "Item with subitems",
      "subitems": ["Subitem 1", "Subitem 2"]
    }
  ]
}
```

* * *

### 📦 Box Objects

Field | Type | Description
----- | ---- | -----------
`type` | `str` | `"info"`, `"success"`, `"alert"`, `"awesome"`, `"bclogo"`
`title` | `str` | Optional box title (for info boxes)
`content` | `str` | Box content
`color` | `str` | Color name (for awesome boxes)
`icon` | `str` | FontAwesome icon name (for awesome boxes)
`logo` | `str` | Logo command (for bclogo boxes)

* * *

### 💻 Code Block Objects

-   `type`: `"listing"` or `"minted"`
    
-   `language`: Programming language (e.g., `python`)
    
-   `caption`: (optional) Code caption
    
-   `label`: (optional) Reference label
    
-   `options`: (optional) Additional options for minted
    
-   `content`: Code text
    

* * *

### 📐 Algorithm Objects

-   `caption`: Algorithm title
    
-   `label`: Reference label
    
-   `data`: Input data description
    
-   `result`: Output result description
    
-   `in`: Alternative input description
    
-   `out`: Alternative output description
    
-   `functions`: List of function objects with `name` and `display` properties
    
-   `content`: Algorithm steps
    

* * *

### 💬 Quote Objects

-   `type`: `"inline"` or `"display"`
    
-   `content`: Quoted text
    

* * *

### 📚 References

#### Bibliography:

```json
{
  "type": "bibliography",
  "bib_file": "references.bib",
  "title": "Bibliography",
  "filecontents": "Inline BibTeX content (optional)"
}
```

#### Manual:

```json
{
  "type": "manual",
  "title": "References:",
  "items": [
    {
      "title": "Reference Title",
      "url": "https://example.com",
      "description": "Short description"
    }
  ]
}
```

* * *

### 📎 Appendices

-   `title`, `label`, `content`
    

* * *

## 🧪 Example Usage in Python

```python
from jinja2 import Template

template_data = {
    "title": "My Document",
    "author": "John Doe",
    "executive_summary": "This document describes...",
    "sections": [
        {
            "level": 1,
            "title": "Introduction",
            "content": "This is the introduction...",
            "drop_cap": True
        },
        {
            "level": 1,
            "title": "Analysis",
            "content": "Our analysis shows...",
            "fancy_tables": [
                {
                    "title": "📊 Performance Results",
                    "headers": ["Category", "Score", "Status"],
                    "rows": [
                        ["System A", "95%", "Excellent"],
                        ["System B", "78%", "Good"],
                    ]
                }
            ],
            "boxes": [
                {
                    "type": "info",
                    "title": "Key Insight",
                    "content": "Our findings indicate..."
                }
            ]
        }
    ]
}

with open('latex_template.tex.jinja', 'r') as f:
    template = Template(f.read())

latex_output = template.render(**template_data)

# Write output to file
with open('output.tex', 'w') as f:
    f.write(latex_output)
```

## 🔍 Full Example

For a complete working example with advanced features, see the `examples` directory.

* * *

## 🛠️ Dependencies

-   Python 3.x
    
-   Jinja2: `pip install jinja2`
    
-   LaTeX distribution with XeLaTeX (for compilation)
    

* * *

## 🛠️ Compilation

To compile the generated LaTeX file:

```bash
xelatex output.tex
biber output  # If using bibliography
xelatex output.tex
xelatex output.tex  # Run twice for cross-references
```

* * *

## 📄 License

This template is provided under the MIT License. See `LICENSE` for details.

* * *

## 🙌 Contributing

Feel free to fork and submit PRs to extend features or fix bugs. Contributions are welcome!