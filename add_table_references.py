#!/usr/bin/env python3
"""
Script to add references before all tables in chapter 6 files
"""

import re

# Define table references to add (table caption -> reference text)
table_refs = {
    # multi-agent-implementation.tex
    'Consensus Decision Making Implementation': 'Consensus-based decision making for collective agent decisions, as shown in Table~\\ref{tab:consensus-decision-making}:',
    'Agent Redundancy and Recovery Implementation': 'Critical system functions are protected through strategic redundancy, as detailed in Table~\\ref{tab:agent-redundancy-recovery}:',
    'Individual Agent Performance Metrics': 'Each agent is evaluated across multiple performance dimensions, as shown in Table~\\ref{tab:individual-agent-performance}:',
    'Collaboration Pattern Performance Comparison': 'Our evaluation across 500 development tasks demonstrates the relative strengths of each pattern, as shown in Table~\\ref{tab:collaboration-pattern-performance}:',
    
    # database-implementation.tex
    'Hybrid Architecture Workload Distribution': 'The hybrid architecture distributes workloads based on operation characteristics, as shown in Table~\\ref{tab:hybrid-workload-distribution}:',
    'Hybrid Configuration Performance Comparison': 'Performance evaluation demonstrates the effectiveness of our hybrid approach, as shown in Table~\\ref{tab:hybrid-performance-comparison}:',
    'Content Deduplication Analysis': 'Content-addressable storage provides significant space savings through deduplication, as demonstrated in Table~\\ref{tab:content-deduplication-analysis}:',
    'Quality Assessment Framework': 'Our quality scoring framework evaluates artifacts across multiple dimensions, as shown in Table~\\ref{tab:quality-assessment-framework}:',
    'Predictive Allocation Performance': 'The predictive allocation system demonstrates significant performance improvements, as shown in Table~\\ref{tab:predictive-allocation-performance}:',
    'Search Performance Metrics': 'The search implementation achieves excellent performance across all query types, as demonstrated in Table~\\ref{tab:search-performance-metrics}:',
    'Cache Invalidation Strategies': 'We implement multiple cache invalidation strategies based on data characteristics, as shown in Table~\\ref{tab:cache-invalidation-strategies}:',
    'Database Performance Results': 'Our comprehensive performance evaluation demonstrates excellent results across all metrics, as shown in Table~\\ref{tab:database-performance-results}:',
    
    # ui-implementation.tex
    'Cognitive Load Comparison': 'Our implementation focuses on reducing cognitive load through intelligent interface design, as shown in Table~\\ref{tab:cognitive-load-comparison}:',
    'Harmony Board Component Architecture': 'The Harmony Board implements a node-based visual programming interface with multiple components, as detailed in Table~\\ref{tab:harmony-board-architecture}:',
    'Artifact Quality Visualization Methods': 'Visual representation of generated artifact quality uses multiple visualization techniques, as shown in Table~\\ref{tab:artifact-quality-visualization}:',
    'UI Performance Metrics': 'Optimization strategies ensure smooth UI performance, as demonstrated in Table~\\ref{tab:ui-performance-metrics}:',
    'Common Interaction Patterns': 'Analysis of user interaction patterns reveals optimization opportunities, as shown in Table~\\ref{tab:common-interaction-patterns}:',
    
    # testing-deployment.tex
    'Quality Monitoring Automation': 'Real-time quality monitoring with intelligent alerting is implemented across all dimensions, as shown in Table~\\ref{tab:quality-monitoring-automation}:',
    'Cross-Platform Deployment Performance': 'Adaptive deployment ensures consistent behavior across platforms, as demonstrated in Table~\\ref{tab:cross-platform-deployment}:',
    'Distribution Channel Performance': 'We implement four distribution channels with varying characteristics, as shown in Table~\\ref{tab:distribution-channel-performance}:',
    'Distribution Strategy Effectiveness': 'Our distribution strategies demonstrate significant improvements over traditional approaches, as shown in Table~\\ref{tab:distribution-strategy-effectiveness}:',
    
    # implementation-evaluation.tex
    'Evaluation Methodology Overview': 'Our evaluation framework assesses five key dimensions using multiple methodologies, as shown in Table~\\ref{tab:evaluation-methodology}:',
    'Core Performance Benchmarks': 'Core system performance exceeds design targets across all metrics, as demonstrated in Table~\\ref{tab:core-performance-benchmarks}:',
    'IDE Performance Comparison': 'Symphony outperforms traditional and AI-enhanced IDEs across key metrics, as shown in Table~\\ref{tab:ide-performance-comparison}:',
    'Productivity Impact Measurement': 'Measured productivity improvements across development tasks demonstrate significant gains, as shown in Table~\\ref{tab:productivity-impact}:',
    'Scalability Test Results': 'System maintains performance under increasing load, as demonstrated in Table~\\ref{tab:scalability-test-results}:',
    'Training System Effectiveness': 'FQT methodology achieves superior learning outcomes compared to traditional approaches, as shown in Table~\\ref{tab:training-system-effectiveness}:',
}

def add_reference_before_table(content, table_caption, reference_text):
    """Add reference text before a table"""
    # Find the pattern: some text before table
    # Look for the line before \begin{center} that comes before the table
    
    # Pattern to find table with this caption
    pattern = r'([^\n]*)\n\n\\begin\{center\}\n\\begin\{tabular\}[^\n]*\n\\toprule\n.*?\\captionof\{table\}\{' + re.escape(table_caption) + r'\}'
    
    def replace_func(match):
        before_text = match.group(1)
        full_match = match.group(0)
        
        # Check if reference already exists
        if '~\\ref{' in before_text:
            return full_match
        
        # Replace the line before table with reference text
        return full_match.replace(before_text, reference_text.rstrip(':'))
    
    return re.sub(pattern, replace_func, content, flags=re.DOTALL)

# Process each file
files_to_process = {
    'content/chapter6-new/multi-agent-implementation.tex': [
        'Consensus Decision Making Implementation',
        'Agent Redundancy and Recovery Implementation',
        'Individual Agent Performance Metrics',
        'Collaboration Pattern Performance Comparison'
    ],
    'content/chapter6-new/database-implementation.tex': [
        'Hybrid Architecture Workload Distribution',
        'Hybrid Configuration Performance Comparison',
        'Content Deduplication Analysis',
        'Quality Assessment Framework',
        'Predictive Allocation Performance',
        'Search Performance Metrics',
        'Cache Invalidation Strategies',
        'Database Performance Results'
    ],
    'content/chapter6-new/ui-implementation.tex': [
        'Cognitive Load Comparison',
        'Harmony Board Component Architecture',
        'Artifact Quality Visualization Methods',
        'UI Performance Metrics',
        'Common Interaction Patterns'
    ],
    'content/chapter6-new/testing-deployment.tex': [
        'Quality Monitoring Automation',
        'Cross-Platform Deployment Performance',
        'Distribution Channel Performance',
        'Distribution Strategy Effectiveness'
    ],
    'content/chapter6-new/implementation-evaluation.tex': [
        'Evaluation Methodology Overview',
        'Core Performance Benchmarks',
        'IDE Performance Comparison',
        'Productivity Impact Measurement',
        'Scalability Test Results',
        'Training System Effectiveness'
    ]
}

for filepath, tables in files_to_process.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        for table_caption in tables:
            if table_caption in table_refs:
                new_content = add_reference_before_table(content, table_caption, table_refs[table_caption])
                if new_content != content:
                    content = new_content
                    modified = True
                    print(f'  ✓ Added reference for: {table_caption}')
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✅ Updated: {filepath}\n')
        else:
            print(f'⚠️  No changes: {filepath}\n')
            
    except Exception as e:
        print(f'❌ Error processing {filepath}: {e}\n')

print('Done!')
