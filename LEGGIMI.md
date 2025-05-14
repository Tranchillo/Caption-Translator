# Caption Translator

Questo script Python ti aiuta a validare e tradurre file di caption auto-generati (ad esempio da Flux Gym o Civitai) nella lingua di tua scelta. Garantisce che tutti i file di testo siano codificati in UTF-8 e produce versioni tradotte con suffissi specifici per lingua.

## 📁 Struttura delle cartelle

```
Caption_Translator/
├── Caption_Translator.py
├── requirements.txt
├── put_here_image_and_caption/
│   ├── 001.txt
│   ├── 001.jpg / 001.png
│   ├── translation/    # Le traduzioni vengono salvate qui
│   │   ├── 001_it.txt
│   │   └── ...
│   └── ...
└── venv/ (ambiente virtuale opzionale)
```

## ⚙️ Caratteristiche

- Funziona nella cartella locale in cui è posizionato
- Assicura che tutti i file `.txt` siano codificati in UTF-8
- Traduce ogni caption nella lingua selezionata
- I file originali rimangono invariati
- Crea nuovi file come `001_it.txt`, `002_fr.txt`, ecc. nella sottocartella `translation`

## 🚀 Installazione (con ambiente virtuale)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

## 📌 Utilizzo

1. Crea un file `requirements.txt` con il seguente contenuto:
   ```
   googletrans==4.0.0-rc1
   chardet
   ```

2. Posiziona i tuoi file di caption `.txt` (e opzionalmente le immagini corrispondenti) all'interno della cartella `put_here_image_and_caption`.
3. Esegui lo script usando questo comando:

```bash
python Caption_Translator.py --lang it
```

Sostituisci `it` con il codice della lingua di destinazione desiderata (ad esempio `en`, `fr`, `de`, `es`, `zh`, ecc.).

## 📝 Output

Per ogni file come `001.txt`, un file tradotto come `001_it.txt` verrà creato nella sottocartella `translation`.

## 📄 Licenza

Libero utilizzo. Non sono richiesti API o servizi a pagamento.
