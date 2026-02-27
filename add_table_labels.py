#!/usr/bin/env python3
"""
Script to add labels to all tables in chapter 6 files
"""

import re
import os

# Define files to process
files = [
    'content/chapter6-new/multi-agent-implementation.tex',
    'content/chapter6-new/database-implementation.tex',
    'content/chapter6-new/ui-implementation.tex',
    'content/chapter6-new/testing-deployment.tex',
    'content/chapter6-new/implementation-evaluation.tex'
]

# Table name to label mapping
table_labels = {
    # multi-agent-implementation.tex
    'Enhancer-Prompt Agent Performance': 'tab:enhancer-prompt-performance',
    'Communication Protocol Stack': 'tab:communication-protocol-stack',
    'Consensus Decision Making Implementation': 'tab:consensus-decision-making',
    'Agent Redundancy and Recovery Implementation': 'tab:agent-redundancy-recovery',
    'Individual Agent Performance Metrics': 'tab:individual-agent-performance',
    'Collaboration Pattern Performance Comparison': 'tab:collaboration-pattern-performance',
    
    # database-implementation.tex
    'Hybrid Architecture Workload Distribution': 'tab:hybrid-workload-distribution',
    'Hybrid Configuration Performance Comparison': 'tab:hybrid-performance-comparison',
    'Content Deduplication Analysis': 'tab:content-deduplication-analysis',
    'Quality Assessment Framework': 'tab:quality-assessment-framework',
    'Predictive Allocation Performance': 'tab:predictive-allocation-performance',
    'Search Performance Metrics': 'tab:search-performance-metrics',
    'Cache Invalidation Strategies': 'tab:cache-invalidation-strategies',
    'Database Performance Results': 'tab:database-performance-results',
    
    # ui-implementation.tex
    'Cognitive Load Comparison': 'tab:cognitive-load-comparison',
    'Harmony Board Component Architecture': 'tab:harmony-board-architecture',
    'Artifact Quality Visualization Methods': 'tab:artifact-quality-visualization',
    'UI Performance Metrics': 'tab:ui-performance-metrics',
    'Common Interaction Patterns': 'tab:common-interaction-patterns',
    
    # testing-deployment.tex
    'Quality Monitoring Automation': 'tab:quality-monitoring-automation',
    'Cross-Platform Deployment Performance': 'tab:cross-platform-deployment',
    'Distribution Channel Performance': 'tab:distribution-channel-performance',
    'Distribution Strategy Effectiveness': 'tab:distribution-strategy-effectiveness',
    
    # implementation-evaluation.tex
    'Evaluation Methodology Overview': 'tab:evaluation-methodology',
    'Core Performance Benchmarks': 'tab:core-performance-benchmarks',
    'IDE Performance Comparison': 'tab:ide-performance-comparison',
    'Productivity Impact Measurement': 'tab:productivity-impact',
    'Scalability Test Results': 'tab:scalability-test-results',
    'Training System Effectiveness': 'tab:training-system-effectiveness',
}

def add_labels_to_file(filepath):
    """Add labels to tables in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all \captionof{table}{...} and add label if not present
    pattern = r'\\captionof\{table\}\{([^}]+)\}'
    
    def replace_caption(match):
        table_name = match.group(1)
        caption_text = match.group(0)
        
        # Check if label already exists after this caption
        next_chars = content[match.end():match.end()+100]
        if '\\label{' in next_chars:
            return caption_text  # Label already exists
        
        # Get label for this table
        label = table_labels.get(table_name)
        if label:
            return f'{caption_text}\n\\label{{{label}}}'
        else:
            print(f'Warning: No label defined for table: {table_name}')
            return caption_text
    
    new_content = re.sub(pattern, replace_caption, content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'Processed: {filepath}')

# Process all files
for filepath in files:
    if os.path.exists(filepath):
        add_labels_to_file(filepath)
    else:
        print(f'File not found: {filepath}')

print('\nDone! Labels added to all tables.')
print('\nNow you need to manually add references like "as shown in Table~\\ref{tab:xxx}" before each table.')
