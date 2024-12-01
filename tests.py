import sys
import os

# Append the parent directory of 'Markdown_renderer' to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Markdown_renderer'))
sys.path.append(parent_dir)

# Main tests begin here
import markdownrenderer as md  # Import the module

mymarkdown = """
# This is sick

Here is some more markdown with a list:

- Item 1
- Item 2
- Item 3
"""

md.render(mymarkdown)

mymarkdown2 = """
# My second markdown

- Another list
- With more items
"""

md.render(mymarkdown2)
