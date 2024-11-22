# Multilingual Documentation Translator

**Multilingual Documentation Translator** is a Python-based tool that translates documentation (e.g., `README.md`) into multiple languages using the Helsinki-NLP MarianMT models. This tool helps make documentation accessible to a global audience.

---

## Features

- Translate markdown files (`.md`) into multiple languages.
- Supports 20+ languages with pre-trained Helsinki-NLP models.
- Preserves markdown formatting in translated outputs.
- Easy integration into existing workflows.

---

## Installation

1. **Clone the Repository**  
   Clone the project to your local machine:
   ```bash
   git clone https://github.com/<your-username>/doc-multilingual-translator.git
   cd doc-multilingual-translator

2. **Install Dependencies**
   Install the required Python libraries using:
   ```pip install -r requirements.txt```

## Usage
To translate a file, use the following command:
```python translate_docs.py --input <file-path> --languages <language-codes> --output <output-dir>```

### Example
Translate README.md into Spanish (es), French (fr), German (de), and Chinese (zh), and save the output in the translations/ directory:
```python translate_docs.py --input README.md --languages es,fr,de,zh --output ./translations/
```

## Parameters

- `--input`: Path to the markdown file to be translated (e.g., `README.md`).
- `--languages`: Comma-separated list of target language codes (e.g., `es,fr,de,zh`).
- `--output`: Directory where the translated files will be saved (default: `./translations`).

## Supported Languages

Below are some of the language codes you can use in the `--languages` argument:

| Language       | Code |
|----------------|------|
| Spanish        | `es` |
| French         | `fr` |
| German         | `de` |
| Chinese        | `zh` |
| Japanese       | `ja` |
| Italian        | `it` |
| Dutch          | `nl` |
| Portuguese     | `pt` |
| Russian        | `ru` |

For a full list of supported languages, refer to the [Helsinki-NLP MarianMT Models](https://huggingface.co/models?filter=helsinki-nlp).


## Directory Structure

```plaintext
doc-multilingual-translator/
├── translate_docs.py      # Main translation script
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── input/                 # Folder for input files
└── translations/          # Folder for translated output files

