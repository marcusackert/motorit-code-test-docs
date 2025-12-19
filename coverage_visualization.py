import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set up matplotlib for better visualization
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
sns.set_style("whitegrid")

def create_coverage_analysis_charts():
    """Create comprehensive code coverage analysis charts"""
    
    # Coverage data from analysis
    components = [
        'Program.cs',
        'ExplanationHelper.cs', 
        'TollCalculatorFactory',
        'TollCalculatorOptions',
        'Repository Classes',
        'Data Access Classes',
        'Entity Classes', 
        'DateTimeHelper',
        'TollFeeHelper',
        'StandardCalculatorStrategy',
        'TollCalculator',
        'Abstract Classes'
    ]
    
    coverage_data = [0, 0, 20, 10, 30, 20, 40, 70, 80, 90, 90, 10]
    
    priority_levels = [
        'CRITICAL', 'CRITICAL', 'CRITICAL', 'HIGH', 'HIGH',
        'MEDIUM', 'HIGH', 'MEDIUM', 'MEDIUM', 'WELL-COVERED',
        'WELL-COVERED', 'MEDIUM'
    ]
    
    # Color scheme
    colors = {
        'CRITICAL': '#FF4444',
        'HIGH': '#FF8800', 
        'MEDIUM': '#FFCC00',
        'WELL-COVERED': '#44AA44'
    }
    
    component_colors = [colors[priority] for priority in priority_levels]
    
    # Chart 1: Component Coverage Overview
    plt.figure(figsize=(14, 10))
    y_positions = np.arange(len(components))
    bars = plt.barh(y_positions, coverage_data, color=component_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    # Add percentage labels
    for i, (bar, percentage) in enumerate(zip(bars, coverage_data)):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                f'{percentage}%', va='center', fontweight='bold')
    
    plt.yticks(y_positions, components)
    plt.xlabel('Coverage Percentage (%)')
    plt.title('Motorit.CodeTest - Code Coverage by Component\n', fontsize=16, fontweight='bold')
    plt.xlim(0, 105)
    plt.grid(axis='x', alpha=0.3)
    
    # Add legend
    legend_handles = [plt.Rectangle((0,0),1,1, facecolor=color, alpha=0.8, edgecolor='black') 
                     for color in colors.values()]
    plt.legend(legend_handles, colors.keys(), title='Priority Level', loc='lower right')
    
    plt.tight_layout()
    plt.savefig('component_coverage_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Chart 2: Coverage Distribution Pie Charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Coverage ranges distribution
    coverage_ranges = ['No Coverage\n(0%)', 'Low Coverage\n(1-30%)', 'Medium Coverage\n(31-60%)', 
                      'Good Coverage\n(61-80%)', 'Excellent Coverage\n(81-100%)']
    range_counts = [2, 5, 1, 2, 2]
    range_colors = ['#FF4444', '#FF8800', '#FFCC00', '#88CC88', '#44AA44']
    
    ax1.pie(range_counts, labels=coverage_ranges, colors=range_colors, autopct='%1.0f%%', 
           startangle=90, textprops={'fontsize': 10})
    ax1.set_title('Distribution by Coverage Range', fontsize=14, fontweight='bold')
    
    # Priority distribution  
    priority_counts = [3, 3, 4, 2]
    priority_labels = list(colors.keys())
    priority_colors = list(colors.values())
    
    ax2.pie(priority_counts, labels=priority_labels, colors=priority_colors, autopct='%1.0f%%',
           startangle=90, textprops={'fontsize': 10})
    ax2.set_title('Distribution by Priority Level', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('coverage_distribution_charts.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Chart 3: Architecture Layer Analysis
    plt.figure(figsize=(14, 8))
    
    layers = ['Application\nLayer', 'Factory\nLayer', 'Configuration\nLayer', 'Debug\nLayer',
              'Data Access\nLayer', 'Entity\nLayer', 'Helper\nLayer', 'Business Logic\nLayer']
    
    covered_percentages = [0, 20, 10, 0, 25, 40, 75, 90]
    uncovered_percentages = [100 - c for c in covered_percentages]
    
    x_positions = np.arange(len(layers))
    width = 0.6
    
    bars_covered = plt.bar(x_positions, covered_percentages, width, label='Covered', 
                          color='#44AA44', alpha=0.8)
    bars_uncovered = plt.bar(x_positions, uncovered_percentages, width, 
                           bottom=covered_percentages, label='Uncovered', 
                           color='#FF4444', alpha=0.8)
    
    # Add percentage labels
    for i, (covered, uncovered) in enumerate(zip(covered_percentages, uncovered_percentages)):
        if covered > 5:
            plt.text(x_positions[i], covered/2, f'{covered}%', ha='center', va='center', 
                    fontweight='bold', color='white')
        if uncovered > 5:
            plt.text(x_positions[i], covered + uncovered/2, f'{uncovered}%', ha='center', va='center',
                    fontweight='bold', color='white')
    
    plt.ylabel('Coverage Percentage (%)')
    plt.title('Code Coverage by Architecture Layer', fontsize=16, fontweight='bold')
    plt.xticks(x_positions, layers, rotation=45, ha='right')
    plt.legend()
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('layer_coverage_analysis.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Chart 4: Coverage vs Impact Matrix
    plt.figure(figsize=(12, 10))
    
    impact_scores = [10, 8, 7, 6, 8, 5, 7, 6, 6, 9, 9, 4]  # System impact (1-10)
    
    scatter = plt.scatter(coverage_data, impact_scores, 
                         c=component_colors, s=200, alpha=0.7, edgecolors='black', linewidth=1)
    
    # Add component labels
    for i, component in enumerate(components):
        plt.annotate(component, (coverage_data[i], impact_scores[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    plt.xlabel('Coverage Percentage (%)')
    plt.ylabel('System Impact Score (1-10)')
    plt.title('Coverage vs Impact Analysis\n(Top-left quadrant shows critical gaps)', 
             fontsize=14, fontweight='bold')
    
    # Add quadrant dividers
    plt.axvline(x=50, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    
    # Add quadrant labels
    plt.text(25, 9.5, 'HIGH IMPACT\nLOW COVERAGE\n(CRITICAL)', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE0E0', alpha=0.9),
            fontsize=11, fontweight='bold')
    plt.text(75, 9.5, 'HIGH IMPACT\nGOOD COVERAGE\n(MAINTAIN)', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#E0FFE0', alpha=0.9),
            fontsize=11, fontweight='bold')
    plt.text(25, 1.5, 'LOW IMPACT\nLOW COVERAGE\n(CONSIDER)', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFFCC', alpha=0.9),
            fontsize=11, fontweight='bold')
    plt.text(75, 1.5, 'LOW IMPACT\nGOOD COVERAGE\n(OPTIMAL)', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#E0F0FF', alpha=0.9),
            fontsize=11, fontweight='bold')
    
    plt.xlim(-5, 105)
    plt.ylim(0, 11)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('coverage_impact_matrix.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Chart 5: Testing Implementation Roadmap
    plt.figure(figsize=(14, 8))
    
    phases = ['Phase 1:\nCritical Gaps', 'Phase 2:\nHigh Priority', 
              'Phase 3:\nMedium Priority', 'Phase 4:\nOptimization']
    phase_components = [
        ['Program.cs', 'ExplanationHelper', 'TollCalculatorFactory'],
        ['TollCalculatorOptions', 'Repository Classes', 'Entity Classes'],
        ['Data Access Classes', 'Helper Edge Cases', 'Abstract Classes'],
        ['Performance Tests', 'Integration Tests', 'Documentation']
    ]
    
    effort_percentages = [40, 30, 20, 10]
    phase_colors = ['#FF4444', '#FF8800', '#FFCC00', '#44AA44']
    
    y_positions = np.arange(len(phases))
    bars = plt.barh(y_positions, effort_percentages, color=phase_colors, alpha=0.8, 
                   edgecolor='black', linewidth=1)
    
    # Add effort labels and component details
    for i, (bar, components, effort) in enumerate(zip(bars, phase_components, effort_percentages)):
        plt.text(effort/2, bar.get_y() + bar.get_height()/2, 
                f'{effort}% effort', ha='center', va='center', 
                fontweight='bold', color='white', fontsize=11)
        
        components_text = ' • '.join(components)
        plt.text(effort + 2, bar.get_y() + bar.get_height()/2, 
                components_text, ha='left', va='center', fontsize=9)
    
    plt.yticks(y_positions, phases)
    plt.xlabel('Estimated Effort Distribution (%)')
    plt.title('Testing Implementation Roadmap', fontsize=16, fontweight='bold')
    plt.xlim(0, 100)
    
    plt.tight_layout()
    plt.savefig('testing_implementation_roadmap.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ All code coverage analysis charts created successfully!")
    print("\n📊 Generated Chart Files:")
    print("1. component_coverage_chart.png - Individual component coverage breakdown")
    print("2. coverage_distribution_charts.png - Coverage range and priority distributions") 
    print("3. layer_coverage_analysis.png - Architecture layer analysis")
    print("4. coverage_impact_matrix.png - Coverage vs system impact matrix")
    print("5. testing_implementation_roadmap.png - Phased testing strategy")
    print("\n📈 Summary: Charts show 45-50% overall coverage with critical gaps in application and debug layers")

if __name__ == "__main__":
    create_coverage_analysis_charts()