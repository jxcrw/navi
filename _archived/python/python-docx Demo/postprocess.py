#!/usr/bin/python
"""Postprocess a patent case."""
# Jak Crow
# Created: 2017/11/20

import os
import re
import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import ftfy
import pyperclip

# https://stackoverflow.com/questions/34779724/python-docx-replace-string-in-paragraph-while-keeping-style
document = Document('16P01077_US_EN [PAD] - コピー.docx')
for p in document.paragraphs:
    if 'lta' in p.text:
        inline = p.runs
        # Loop added to work with runs (strings with same style)
        for i in range(len(inline)):
            print(inline[i].text)
            if 'lta' in inline[i].text:
                text = inline[i].text.replace('lta', 'kthxwtfbbq')
                inline[i].text = text

document.save('16P01077_US_EN [PAD]_postprocessed.docx')
