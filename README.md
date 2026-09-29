<div align="center">

# The Sovereignty Gap in Yorùbá NLP: Orthographic Integrity, Contextual Disambiguation, and Linguistic Data Sovereignty

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10892345-blue.svg)](https://doi.org/10.5281/zenodo.10892345)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Benchmark](https://img.shields.io/badge/Benchmark-YorTIB--200-success.svg)](data/yortib_200.json)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Peer--Reviewed%20%2F%20Reproducible-brightgreen.svg)](#)

<p align="center">:README.md`:
```markdown
<div align="center">

# The Sovereignty Gap in Yorùbá NLP: Orthographic Integrity, Contextual Disambiguation, and Linguistic Data Sovereignty

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10892345-blue.svg)](https://doi.org/10.5281/zenodo.10892345)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Benchmark](https://img.shields.io/badge/Benchmark-YorTIB--200-success.svg)](data/yortib_200.json)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Peer--Reviewed%20%2F%20Reproducible-brightgreen.svg)](#)

<p align="center">
  <b>An empirical audit demonstrating why diacritic flattening is not data cleaning—it is epistemic flattening.</b>
</p>

---

### Graphical Abstract

![Graphical Abstract](Figures/Graphical%20abstract.png)

</div>

---

## 📌 Executive Summary

Tonal and subdot diacritics in Yorùbá orthography are not decorative accents; they are foundational, morphemic determinants of lexical semantics and syntactic grammatical class. Standard multi-lingual Natural Language Processing (NLP) pipelines routinely strip or normalize these diacritics under the guise of "noise removal" or token vocabulary consolidation. 

This repository houses the **YorTIB-200** (*Yorùbá Tone & Meaning Integrity Benchmark*) dataset and reproducible01$).* | *Figure 4: Consistent across-the-board disambiguation failure in flattened text vs. sovereign retention across all 7 domains.* |

</div>

---

## 📊 Summary of Empirical Results

All evaluations were conducted in a strictly controlled, paired setting over $N = 200$ naturalistic sentence contexts.

| Semantic Category | $N$ | Baseline Accuracy (Unmarked) | Sovereign Accuracy (Preserved) | $\Delta$ (Accuracy Gap) | McNemar Significance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Everyday Vocabulary** | 48 | 22.9% (0.229) | 100.0% (1.000) | **+77.1 pp** | $p < 0.001$ |
| **Agriculture** | 18 | 27.8% (0.278) | 100.0% (1.000) | **+72.2 pp** | $p < 0.001$ |
| **Transportation** | 11 | 36.4% (0.364) | 100.0% (1.000) | **+63.6 pp** | $p < 0.001$ |
| **Medicine & Healing** | 10 | 20.0% (0.200) | 100.0% (1.000) | **+80.0 pp** | $p < 0.001$ |
| **Spiritual Concepts** | 57 | 43.9% (0.439) | 100.0% (1.000) | **+56.1 pp** | $p < 0.001$ |
| **Moral / Philosophical Concepts** | 29 | 48.3% (0.483) | 100.0% (1.000) | **+51.7 pp** | $p < 0.001$ |
| **Ontological Concepts** | 27 | 59.3% (0.593) | 96.3% (0.963) | **+37.0 pp** | $p < 0.001$ |
| **Overall Dataset (Aggregate)** | **200** | **38.5% (0.385)** | **99.5% (0.995)** | **+61.0 pp** | **$p = 3.76 \times 10^{-37}$** |

### Statistical Rigor
- **McNemar Test:** Paired $\chi^2$ test confirms statistical divergence at $p = 3.76 \times 10^{-37}$.
- **Bootstrap 95% Confidence Interval:** $[0.535, 0.675]$ (computed over 1,000 paired bootstrap iterations).
- **Contingency Matrix:**
  - Sovereign Correct & Baseline Correct: **77**
  - Sovereign Correct & Baseline Incorrect: **122**
  - Sovereign Incorrect & Baseline Correct: **0**
  - Sovereign Incorrect & Baseline Incorrect: **1**

---

## 📁 Repository Structure

```text
Yoruba-Sovereignty-Gap/
├── README.md                          # Repository documentation & publication report
├── LICENSE                            # MIT Open Source License
├── requirements.txt                   # Environment dependencies
├── Figures/                           # High-resolution publication figures & assets
│   ├── README.md                      # Figure captions, alt-text, and resolution details
│   ├── Graphical abstract.png         # Graphical Abstract banner
│   ├── Figure_1.jpg                   # YorTIB-200 Benchmark Dataset
│   ├── Figure_2.jpg                   # Representation Conditions & Evaluation
│   ├── Figure_3.jpg                   # Overall Results & McNemar Contingency
│   └── Figure_4.jpg                   # Performance Across Semantic Categories
├── data/
│   ├── yortib_200.json                # Primary curated benchmark (200 instances)
│   ├── prediction_filled_baseline.csv # Model inferences under unmarked condition
│   ├── prediction_filled_sovereign.csv# Model inferences under preserved condition
│   └── prediction_filled_paired.csv   # Paired instance-level prediction matrix
├── scripts/
│   ├── evaluate.py                    # Replication script (McNemar, Bootstrap CI, Metrics)
│   └── populate_predictions.py       # Template parsing & inference verification pipeline
└── reports/
    └── gold_audit_report.xlsx         # Complete data audit report and statistical summary
