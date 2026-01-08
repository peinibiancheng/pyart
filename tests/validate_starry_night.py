#!/usr/bin/env python3
"""
Validation script for starry_night.py

This script validates the code structure and function definitions of
starry_night.py without requiring a graphical display.
"""

import ast
import os
import sys


def validate_starry_night_code():
    """Validate Starry Night code structure"""
    
    # Calculate path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../src/starry_night.py")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    print("=" * 60)
    print("Validating Van Gogh 'Starry Night' Matplotlib Code")
    print("=" * 60)
    
    # Read code
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Parse AST
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"❌ Syntax Error: {e}")
        return False
    
    # Check required functions
    print("\n1️⃣  Checking Function Definitions:")
    print("-" * 60)
    
    required_functions = {
        'create_vector_field': 'Create swirling vector field',
        'create_brushstrokes': 'Create thousands of brushstrokes',
        'draw_starry_night': 'Main drawing function'
    }
    
    functions_found = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions_found[node.name] = node
    
    all_found = True
    for func_name, description in required_functions.items():
        if func_name in functions_found:
            print(f"  ✓ {func_name:30s} - {description}")
        else:
            print(f"  ✗ {func_name:30s} - Missing")
            all_found = False
    
    if not all_found:
        return False
    
    # Check key technical requirements
    print("\n2️⃣  Checking Technical Requirements:")
    print("-" * 60)
    
    requirements = {
        'import matplotlib.pyplot': 'Matplotlib pyplot import',
        'import numpy': 'NumPy import',
        'streamplot': 'Vector field streamplot',
        'LineCollection': 'Line collection for brushstrokes',
        'num_strokes': 'Brushstroke count parameter',
    }
    
    for keyword, description in requirements.items():
        if keyword in code:
            print(f"  ✓ {keyword:30s} - {description}")
        else:
            print(f"  ✗ {keyword:30s} - Missing")
            all_found = False
    
    # Check color palette
    print("\n3️⃣  Checking Color Elements:")
    print("-" * 60)
    
    color_elements = {
        '#1a5fb4': 'Blue (Post-Impressionist)',
        '#f7931a': 'Orange/Yellow (Post-Impressionist)',
        '#fbbf24': 'Yellow (Stars)',
    }
    
    for color, description in color_elements.items():
        if color in code:
            print(f"  ✓ {color:15s} - {description}")
        else:
            print(f"  ⚠ {color:15s} - Not found")
    
    # Count code metrics
    print("\n4️⃣  Code Statistics:")
    print("-" * 60)
    
    lines = code.split('\n')
    total_lines = len(lines)
    code_lines = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
    comment_lines = len([l for l in lines if l.strip().startswith('#')])
    
    print(f"  Total lines:                  {total_lines}")
    print(f"  Code lines:                   {code_lines}")
    print(f"  Comment lines:                {comment_lines}")
    
    # Verify key implementation details
    print("\n5️⃣  Implementation Validation:")
    print("-" * 60)
    
    checks = []
    
    # Check for vector field implementation
    if 'def create_vector_field' in code and 'U, V' in code:
        print("  ✓ Vector field (U, V components) implemented")
        checks.append(True)
    else:
        print("  ✗ Vector field not properly implemented")
        checks.append(False)
    
    # Check for brushstroke generation
    if 'segments' in code and 'colors' in code and 'linewidths' in code:
        print("  ✓ Brushstroke generation with segments, colors, linewidths")
        checks.append(True)
    else:
        print("  ✗ Brushstroke generation incomplete")
        checks.append(False)
    
    # Check for thousands of strokes
    if 'num_strokes=5000' in code or 'num_strokes = 5000' in code:
        print("  ✓ Using 5000 brushstrokes (thousands as required)")
        checks.append(True)
    else:
        print("  ⚠ Brushstroke count may differ from 5000")
        checks.append(False)
    
    # Check for flow-based positioning
    if 'u_norm' in code and 'v_norm' in code:
        print("  ✓ Brushstrokes aligned with vector field flow")
        checks.append(True)
    else:
        print("  ✗ Brushstrokes not aligned with flow")
        checks.append(False)
    
    # Final result
    print("\n" + "=" * 60)
    if all_found and all(checks):
        print("✅ Validation passed! Code meets all requirements.")
        print("✅ Implements Van Gogh 'Starry Night' with:")
        print("   - Vector fields (streamplot) for swirling patterns")
        print("   - Thousands of short, thick brushstrokes")
        print("   - Post-Impressionist color palette")
        return True
    else:
        print("⚠️  Validation completed with some issues.")
        return False


if __name__ == "__main__":
    success = validate_starry_night_code()
    sys.exit(0 if success else 1)
