# Access Remedies for Cross-Border Mergers in Network Industries

**Author:** Muhammad Adil Saleem  
**Primary affiliation:** School of Economics and Finance, Xi'an Jiaotong University, China  
**Second affiliation:** Pakhtunkhwa Economic Policy Research Institute (PEPRI), Abdul Wali Khan University, Mardan, Pakistan  
**Corresponding email:** adilsaleem233@gmail.com  

## Working paper status

This repository contains the working-paper package for:

> **Access Remedies for Cross-Border Mergers in Network Industries**

The paper develops a competition-economics model of access and interoperability remedies for cross-border mergers in network industries. The repository is intended to provide a timestamped authorship record, store the working-paper source files, and make the paper package reproducible.

## Repository contents

```text
paper/
  Access_Remedies_Working_Paper.pdf      # Compiled working-paper PDF
  Access_Remedies_Working_Paper.tex      # Main LaTeX source
  references.bib                         # Bibliography database

figures/
  figure_1_welfare_comparison.pdf
  figure_2_welfare_difference.pdf
  figure_3_access_quality_threshold.pdf
  figure_4_entrant_cost_threshold.pdf

code/
  generate_figures.py                    # Python code used to generate figures

docs/
  REPOSITORY_UPLOAD_GUIDE.md             # Suggested GitHub upload/release steps
  RELEASE_NOTES_v0.1.md                  # Notes for initial working-paper release

LICENSE                                  # All rights reserved license notice
AUTHORS.md                               # Author and affiliation information
CITATION.cff                             # Citation metadata for GitHub
CHANGELOG.md                             # Version history
.gitignore                               # LaTeX/Python temporary file exclusions
```

## How to compile the paper

From the repository root, run:

```bash
cd paper
pdflatex Access_Remedies_Working_Paper.tex
bibtex Access_Remedies_Working_Paper
pdflatex Access_Remedies_Working_Paper.tex
pdflatex Access_Remedies_Working_Paper.tex
```

The compiled output is:

```text
paper/Access_Remedies_Working_Paper.pdf
```

## How to regenerate figures

From the repository root, run:

```bash
python code/generate_figures.py
```

The script generates the PDF figures used in the paper.

## Suggested citation

Saleem, Muhammad Adil. 2026. *Access Remedies for Cross-Border Mergers in Network Industries*. Working paper.

## Copyright and reuse

Copyright (c) 2026 Muhammad Adil Saleem. All rights reserved.

No part of this working paper, including the text, equations, figures, tables, source files, and associated materials, may be reproduced, distributed, modified, or used in derivative works without the prior written permission of the author, except for brief quotations with proper citation for scholarly review or academic discussion.

This repository is not distributed under an open-source license.
