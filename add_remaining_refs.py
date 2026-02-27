#!/usr/bin/env python3
import re

# Mapping of (file, search_text, replacement_text)
replacements = [
    # database-implementation.tex
    ('content/chapter6-new/database-implementation.tex', 
     'The hybrid architecture distributes workloads based on operation characteristics:\n\n\\begin{center}',
     'The hybrid architecture distributes workloads based on operation characteristics, as shown in Table~\\ref{tab:hybrid-workload-distribution}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'Performance evaluation demonstrates the effectiveness of our hybrid approach:\n\n\\begin{center}',
     'Performance evaluation demonstrates the effectiveness of our hybrid approach, as shown in Table~\\ref{tab:hybrid-performance-comparison}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'Content-addressable storage provides significant space savings through deduplication:\n\n\\begin{center}',
     'Content-addressable storage provides significant space savings through deduplication, as demonstrated in Table~\\ref{tab:content-deduplication-analysis}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'Our quality scoring framework evaluates artifacts across multiple dimensions:\n\n\\begin{center}',
     'Our quality scoring framework evaluates artifacts across multiple dimensions, as shown in Table~\\ref{tab:quality-assessment-framework}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'The predictive allocation system demonstrates significant performance improvements:\n\n\\begin{center}',
     'The predictive allocation system demonstrates significant performance improvements, as shown in Table~\\ref{tab:predictive-allocation-performance}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'The search implementation achieves excellent performance across all query types:\n\n\\begin{center}',
     'The search implementation achieves excellent performance across all query types, as demonstrated in Table~\\ref{tab:search-performance-metrics}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'We implement multiple cache invalidation strategies based on data characteristics:\n\n\\begin{center}',
     'We implement multiple cache invalidation strategies based on data characteristics, as shown in Table~\\ref{tab:cache-invalidation-strategies}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/database-implementation.tex',
     'Our comprehensive performance evaluation demonstrates excellent results across all metrics:\n\n\\begin{center}',
     'Our comprehensive performance evaluation demonstrates excellent results across all metrics, as shown in Table~\\ref{tab:database-performance-results}:\n\n\\begin{center}'),
    
    # ui-implementation.tex
    ('content/chapter6-new/ui-implementation.tex',
     'Our implementation focuses on reducing cognitive load through intelligent interface design:\n\n\\begin{center}',
     'Our implementation focuses on reducing cognitive load through intelligent interface design, as shown in Table~\\ref{tab:cognitive-load-comparison}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/ui-implementation.tex',
     'The Harmony Board implements a node-based visual programming interface:\n\n\\begin{center}',
     'The Harmony Board implements a node-based visual programming interface with multiple components, as detailed in Table~\\ref{tab:harmony-board-architecture}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/ui-implementation.tex',
     'Visual representation of generated artifact quality:\n\n\\begin{center}',
     'Visual representation of generated artifact quality uses multiple visualization techniques, as shown in Table~\\ref{tab:artifact-quality-visualization}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/ui-implementation.tex',
     'Optimization strategies for smooth UI performance:\n\n\\begin{center}',
     'Optimization strategies ensure smooth UI performance, as demonstrated in Table~\\ref{tab:ui-performance-metrics}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/ui-implementation.tex',
     'Analysis of user interaction patterns reveals optimization opportunities:\n\n\\begin{center}',
     'Analysis of user interaction patterns reveals optimization opportunities, as shown in Table~\\ref{tab:common-interaction-patterns}:\n\n\\begin{center}'),
    
    # implementation-evaluation.tex
    ('content/chapter6-new/implementation-evaluation.tex',
     'Our evaluation framework assesses five key dimensions:\n\n\\begin{center}',
     'Our evaluation framework assesses five key dimensions using multiple methodologies, as shown in Table~\\ref{tab:evaluation-methodology}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/implementation-evaluation.tex',
     'Core system performance exceeds design targets:\n\n\\begin{center}',
     'Core system performance exceeds design targets across all metrics, as demonstrated in Table~\\ref{tab:core-performance-benchmarks}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/implementation-evaluation.tex',
     'Symphony outperforms traditional and AI-enhanced IDEs:\n\n\\begin{center}',
     'Symphony outperforms traditional and AI-enhanced IDEs across key metrics, as shown in Table~\\ref{tab:ide-performance-comparison}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/implementation-evaluation.tex',
     'Measured productivity improvements across development tasks:\n\n\\begin{center}',
     'Measured productivity improvements across development tasks demonstrate significant gains, as shown in Table~\\ref{tab:productivity-impact}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/implementation-evaluation.tex',
     'System maintains performance under increasing load:\n\n\\begin{center}',
     'System maintains performance under increasing load, as demonstrated in Table~\\ref{tab:scalability-test-results}:\n\n\\begin{center}'),
    
    ('content/chapter6-new/implementation-evaluation.tex',
     'Comparative evaluation against traditional training approaches shows significant improvements:\n\n\\begin{center}',
     'FQT methodology achieves superior learning outcomes compared to traditional approaches, as shown in Table~\\ref{tab:training-system-effectiveness}:\n\n\\begin{center}'),
]

for filepath, old_text, new_text in replacements:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✓ Updated: {filepath}')
        else:
            print(f'⚠ Not found in {filepath}: {old_text[:50]}...')
    except Exception as e:
        print(f'✗ Error: {filepath}: {e}')

print('\n✅ Done!')
