# EForce Export for Excel (Berndt-Auswertung)

This Python script processes EForce results from the MEDINA FEA software for Berndt-Auswertung and exports the data to Excel in a structured format.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Notes](#notes)
- [License](#license)

## Introduction

This script automates the extraction and processing of EForce results from MEDINA FEA software. It is specifically designed for Berndt-Auswertung and exports the data to Excel for further analysis.

## Prerequisites

Before using the script, ensure you have the following:

- MEDINA FEA software installed.
- EForce.eforce file generated through the UCI PRINT command.
- EForce_array.in with Element IDs (EID) sorted.
- LF.in with load cases (T=?) specified.
- SET_ID_FN.in and SET_ID_FNS.in with Set IDs sorted.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/akshaykumargn/bash2pyt.git

2. Navigate to the script directory:

```bash
cd eforce-export

3. Run the script:

```bash
bash2py.py

##File Structure

The script generates the following files:

    EForce_NID_MON_ZUG_SCHUB.csv: CSV file containing forces categorized by Montage, Zug (Tension), and Schub (Shear).

    FN_FNS_fin_[LF].csv: CSV file containing processed FN (normal forces) and FNS (contact forces) data for each specified load case (LF).

    README.md: Documentation file.

Please refer to the script for additional temporary files created during execution.
Notes

    This script is designed for a specific use case and may require adjustments for different scenarios.

##License

This project is licensed under the MIT License - see the LICENSE file for details.
