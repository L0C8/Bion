import os
import zipfile
import shutil
import tempfile
from bs4 import BeautifulSoup

def apply_bionic(text):
    def bold_word(word):
        if len(word) <= 2:
            return word
        cutoff = max(1, len(word) // 3)
        return f"<b>{word[:cutoff]}</b>{word[cutoff:]}"
    
    result = []
    for token in text.split():
        if token.isalpha():
            result.append(bold_word(token))
        else:
            result.append(token)
    return " ".join(result)

def build_bionic_epub(input_path, output_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(input_path, 'r') as zin:
            zin.extractall(tmpdir)

        # Walk through and modify content files
        for root, dirs, files in os.walk(tmpdir):
            for file in files:
                if file.endswith(('.xhtml', '.html')):
                    full_path = os.path.join(root, file)
                    with open(full_path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f, 'html.parser')

                    for tag in soup.find_all(['p', 'span', 'div', 'li']):
                        if tag.string:
                            tag.string.replace_with(BeautifulSoup(apply_bionic(tag.string), 'html.parser'))

                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

        # Create output EPUB
        with zipfile.ZipFile(output_path, 'w') as zout:
            for foldername, subfolders, filenames in os.walk(tmpdir):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, tmpdir)
                    zout.write(file_path, arcname)
