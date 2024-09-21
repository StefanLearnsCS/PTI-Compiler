# Transformer Package Compiler (Creo Parametric Drawings)

#### This project automates the process of creating various parts packages for transformers based on user input. It processes part lists, organizes files, and compiles folders based on specific package types (Tank, Clamp, or Unit Assembly)

## Features

* Generates Steel Supplier, Purchased Parts, Pressboard, Gasket, TX2, and other transformer component packages.
* Automates folder creation and file compilation based on selected options.
* Cleans raw data and organizes parts lists into specific categories.
* Supports multiple transformer types: Tank, Clamp, and UA.

## Prerequisites

#### Before you run the project (main.py), ensure you have the following Python packages installed:
```python
pip install os PyPDF2 pdfplumber
```

## Installation

#### 1. Clone the repository:
```bash
git clone https://github.com/StefanLearnsCS/PTI-Compiler.git
cd PTI-Compiler
```

#### 2. Ensure all required modules (ReadList, GetDirectory, DataCleanse, etc.) are present.

## Usage

#### To run the program, simply execute the main.py file:
```bash
python main.py
```

### Input Prompts
#### The script will ask for user inputs in the terminal, such as:
* SO Number: A unique identifier for the transformer (i.e. 20216).
* Package Type: Select from Tank, Clamp, or Unit Assembly.
* Additional package-specific options for gaskets, pressboards, structural steel, etc.

#### Depending on the transformer type, you may be prompted for part list files (e.g., "SM-21043-TA" or "UA-21043"). The program will automatically generate folders and compile the necessary files.

