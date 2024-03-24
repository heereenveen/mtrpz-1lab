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

def preformatted(lines):
    preformatted_indexes = [i for i, element in enumerate(lines) if element == '```']

    if len(preformatted_indexes) % 2 != 0:
        raise ValueError("invalid markdown: there is a beginning among the markup elements, but no end")

    couple_preformatted_indexes = [preformatted_indexes[i:i+2] for i in range(0, len(preformatted_indexes), 2)]

    html_lines = []
    for i in couple_preformatted_indexes:
        start_index_preformatted, end_index_preformatted = i[0], i[1]
        array = lines[start_index_preformatted : end_index_preformatted + 1]
        array[0], array[-1] = '<pre>', '</pre>'
        html_lines.extend(array)
    return html_lines

with open(input_file, 'r', encoding='utf-8') as md_file:
    md_lines = md_file.read().splitlines()
    print(md_lines)
    html_lines = []

    html_lines.extend(paragraphs(md_lines))
    html_lines.extend(preformatted(md_lines))
    
    print(html_lines)