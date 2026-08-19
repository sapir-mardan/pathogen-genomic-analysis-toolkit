# Pathogen Island Detection Toolkit

<img width="1445" alt="image" src="https://github.com/sapir-mardan/pathogen-genomic-analysis-toolkit/assets/92859243/dfeb5e92-4695-4132-9de8-f8a93a0406e3">

## Description

An easy-to-use pipeline interface designed for genomic sequence analysis. With Python and bash scripts that integrates seamlessly, it runs various bioinformatics tasks utilizing both tools. 
The program creates BLAST database, performs BLAST searches and parse the results to an output in a user-friendly format.  
  
Developed as part of a university project, it aims to identify and analyze specific pathogen genes of interest in novel *Yersinia* bacterial strains. It can be run to the specific pathogen genes or **any genes of interest by the user**. It also has the functionality to retrive sequence from FASTA file by an ID.  

### Output Example (parsed BLAST results)
<img width="1094" alt="image" src="https://github.com/sapir-mardan/pathogen-genomic-analysis-toolkit/assets/92859243/f6024d8e-c95c-4ba5-9a91-b23f2c124fd7">

### Main Features:
The assigment asked to use BLAST spesifically in commend line. I have combined my experience with Python to enhance the functionality of the pipeline.
  
**Key Bash Script Features:**
  - Create BLAST database from FASTA files and perform BLAST searches.
  - Retrieve protein sequences from NCBI protein database.
  - Automatically removes intermediate files to keep the directory clean and organized.
  
**Key Python Script Features:**  
  - Use of Biopython Modules For Various Tasks (SeqIO, Entrez, NCBIXML).
  - Retrieve protein sequences from NCBI.
  - Sequence Retrieval from FASTA Files. 
  - Parse and process BLAST results and save output in a user-friendly format.

## Table of Contents

- [Project Background](#project-background)
- [Features](#features)
- [Installation & Requirements](#installation-and-requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Background

This toolkit was developed to support biologists in their research with data analyses and tools developments. They have recently isolated and sequenced a new strain of Yersinia bacteria and they suspect that 4 genes are involved in a new phenotype observed in their samples. The assignment involved preprocessing genomic data, performing sequence alignment, and visualizing the results to determine if pathogen islands are present in the given strains. 

The 4 genes were referenced from a scientific article and termed yRz1 yRz elyY holY:

Katharina Springer et al. "Activity of a Holin-Endolysin System in the Insecticidal Pathogenicity Island of Yersinia enterocolitica." *Journal of Bacteriology*, edited by Victor J. DiRita, Michigan State University. DOI: [10.1128/JB.00180-18](https://doi.org/10.1128/JB.00180-18)

## Features

This all-in-one solution operates from a single file, utilizing a collection of Python functions stored in a separate script. No coding experience is necessary – just follow the straightforward installation process and instructions to unlock a range of tasks related to gene analysis effortlessly. When executing the program, you'll be greeted by an intuitive menu presenting the following options: 


- **Gene Detection**: Determine if four specific pathogenic genes are present in the new *Yersinia* strains using BLASTP. For a detailed description of the output statistics, see [output_description.md]([Output_Description.md](https://github.com/sapir-mardan/pathogen-genomic-analysis-toolkit/blob/main/Output_Description.md)).
- **Protein Search**: Analyze and determine the presence of any protein is in any strain, and output the results in a format similar to 'Gene Detection' option.
- **Sequence Retrieval**: Retrieve specific protein sequences by ID from a FASTA files.

## Installation and Requirements

**Requirements**
BLAST, edirect, python3 and the following libraries:
Biopython (Bio)  
sys  
pandas  
os  
datetime  

**Important note:** If you are using pre-installed BLAST and/or edirect, make sure the directory of the programs are part of your system PATH. See installation bash script for more details.  
e.g., ```
      export PATH=$PATH:/directory/to/blast/bin/path
      ```

**Installation**
1. Clone the repository and change into the project directory:
    ```bash
    git clone https://github.com/sapir-mardan/pathogen-genomic-analysis-toolkit.git
    cd pathogen-genomic-analysis-toolkit
    ```
2. Change into the project directory:
    ```bash
    cd pathogen-genomic-analysis-toolkit
    ```
3. Run the installation script to download blast and edirect to your computer (linux/mac):
   ```bash
    ./install_blast_edirect.sh
    ```
   If needed make script executable:
    ```bash
    chmod +x install_blast_edirect
    ```
4. Download required libraries:
   ```bash
   pip install -r requirements.txt
   ```
If there are no errors, the installation is successful.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/sapir-mardan/pathogen-genomic-analysis-toolkit
cd pathogen-genomic-analysis-toolkit
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python program_functions.py
```

Follow the on-screen menu to:
- Retrieve statistics about the presence of 4 pathogenic genes in new *Yersinia* strains
- Retrieve statistics about any protein of your own against NCBI database
- Retrieve protein sequences based on IDs from a FASTA file

## My Role

**Biopython integration:** FASTA parsing with `SeqIO.parse()`, sequence dictionary construction and lookup  
**Data processing:** CSV enhancement (adding headers to BLAST tabular output), pandas DataFrame manipulation  
**File handling:** Validation, error handling, user prompts  
**Testing:** Unit tests covering core functions (pytest)

Bash BLAST wrapper and menu structure co-authored with partner.

## Contribution 

Contributions are welcome!

**Acknowledgements:**    
**Sapir Mardan** developed the Python and Bash script for the program structure and execution.

**Angela Hsu** developed code for Bash script, specifically for running BLAST and ensured Windows compatibility.

**Nicole Flores** and **Matthew Raj** provided valuable assistance throughout various sections of this project not presented here. Their help is greatly appreciated.

**University of Bristol** for their support and resources throughout this project.

## License

This project is licensed under the MIT License.

