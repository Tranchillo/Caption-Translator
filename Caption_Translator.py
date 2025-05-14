import os
import chardet
from googletrans import Translator
import argparse

# Percorso della cartella contenente immagini e caption
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_FOLDER = os.path.join(WORK_DIR, "put_here_image_and_caption")
TRANSLATION_FOLDER = os.path.join(TARGET_FOLDER, "translation")  # Sottocartella per le traduzioni

# Estensioni immagini supportate
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']

# Verifica e converte file in UTF-8 se necessario
def ensure_utf8(filepath):
    with open(filepath, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    if encoding.lower() != 'utf-8':
        with open(filepath, 'r', encoding=encoding, errors='ignore') as f:
            content = f.read()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[INFO] Converted to UTF-8: {filepath}")
    else:
        print(f"[OK] Already UTF-8: {filepath}")

# Traduci caption
def translate_caption(content, target_lang):
    translator = Translator()
    try:
        translated = translator.translate(content, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"[ERROR] Translation failed: {e}")
        return None

# Crea la cartella per le traduzioni se non esiste
if not os.path.exists(TRANSLATION_FOLDER):
    os.makedirs(TRANSLATION_FOLDER)

# Processa tutti i file .txt nella cartella
def process_captions(lang_code):
    if not os.path.exists(TARGET_FOLDER):
        print(f"[ERROR] Folder not found: {TARGET_FOLDER}")
        return

    files = [f for f in os.listdir(TARGET_FOLDER) if f.lower().endswith('.txt')]
    print(f"[INFO] Found {len(files)} caption files.")

    for filename in files:
        full_path = os.path.join(TARGET_FOLDER, filename)
        ensure_utf8(full_path)

        with open(full_path, 'r', encoding='utf-8') as f:
            original_text = f.read().strip()

        translated_text = translate_caption(original_text, lang_code)
        if translated_text:
            name, ext = os.path.splitext(filename)
            output_file = os.path.join(TRANSLATION_FOLDER, f"{name}_{lang_code}.txt")  # Salvataggio nella sottocartella 'translation'
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write(translated_text)
            print(f"[SUCCESS] Translated: {filename} -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate and validate captions in UTF-8.")
    parser.add_argument("--lang", type=str, required=True, help="Target language code (e.g. it, en, fr, es)")
    args = parser.parse_args()

    print(f"[START] Processing captions in folder: {TARGET_FOLDER}")
    process_captions(args.lang)
    print("[DONE] All files processed.")
