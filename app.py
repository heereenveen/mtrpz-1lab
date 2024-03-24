import re
import os

def paragraphs(lines):
    paragraph_indexes = [i for i, element in enumerate(lines) if element == '']
    html_lines = []
    for i in paragraph_indexes:
        array = md_lines[i - 1 : i + 2]
        array.remove('')
        paragraphed_lines = ["<p>" + line + "</p>" for line in array]
        html_lines.extend(paragraphed_lines)
        
    bold(html_lines)
    italic(html_lines)
    monospaced(html_lines)
    
    return list(set(html_lines))

def bold(lines):
    for i in range(len(lines)):
        lines[i] = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', lines[i])
    
def italic(lines):
    for i in range(len(lines)):
        lines[i] = re.sub(r'_(.+?)_', r'<em>\1</em>', lines[i])

def monospaced(lines):
    for i in range(len(lines)):
        lines[i] = re.sub(r'`(.+?)`', r'<tt>\1</tt>', lines[i])