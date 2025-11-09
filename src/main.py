from classes.Assistent import BioAssistent, Article
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="secret.env")
article_1 = Article()
article_1.content = '''
# 🧬 IGF1 Gene / Protein Overview

- **Gene Symbol / Name:** IGF1 (insulin like growth factor 1)
- **Protein Name:** Insulin-like growth factor 1
- **Identifiers:**
  - UniProt ID: [P05019](https://www.uniprot.org/uniprotkb/P05019/entry)
  - KEGG ID: [hsa:3479](https://www.kegg.jp/entry/hsa:3479)
  - Gene ID (NCBI): [3479](https://www.ncbi.nlm.nih.gov/gene/3479)
  - HGNC ID: [HGNC:5464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5464)
  - Ensembl ID: [ENSG00000017427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000017427)
  - OMIM ID: [147440](https://omim.org/entry/147440)
  - RefSeqGene ID: [NG_011713.1](https://www.ncbi.nlm.nih.gov/nuccore/NG_011713.1)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprotkb/P05019/entry)  
  - [Protein (RefSeq)](https://www.ncbi.nlm.nih.gov/protein/NP_000609.1)  
  - [mRNA (RefSeq)](https://www.ncbi.nlm.nih.gov/nuccore/NM_000618.5)  
  - [Gene (RefSeqGene)](https://www.ncbi.nlm.nih.gov/nuccore/NG_011713.1)

---

# 🔬 Structure and Functional Domains

- **Protein Length:** 195 amino acids (canonical precursor), mature IGF-1 chain: 70 amino acids (positions 49–118)
- **Key Domains / Motifs:**
  - B domain (49–77): IGFBP binding surface and receptor interaction
  - C domain (78–89): Linker region
  - A domain (90–110): Critical for receptor binding
  - D domain (111–118): C-terminal extension
  - Disulfide bonds: Cys54–Cys96, Cys66–Cys109, Cys95–Cys100 (structural stabilization)
- **Functional Roles:** Mediates growth and development through insulin-like growth factor receptor binding; regulates cell proliferation, survival, and metabolism via PI3K-Akt signaling pathway
- **Post-Translational Modifications (PTMs):**
  - Signal peptide cleavage (positions 1–21)
  - Propeptide processing (positions 22–48)
  - Disulfide bond formation critical for tertiary structure
- **Orthologs / Paralogs:**
  - *C. elegans*: SKN-1 (35% identity)
  - *Drosophila*: CncC (32% identity)
  - Mouse: IGF1 (98% identity)

---

# ⚙️ Sequence-to-Function Relationships

| Interval | Type of Modification | Experimental Effect | Functional Outcome | Source |
|-----------|---------------------|---------------------|--------------------|--------|
| 84–85     | R84E/R85E mutation  | Disrupted integrin binding | Suppressed IGF1 signaling and tumorigenesis | UniProt |
| 54–96     | Disulfide bond (Cys54–Cys96) | Structural stabilization | Proper folding and receptor binding | NCBI |
| 66–109    | Disulfide bond (Cys66–Cys109) | Structural stabilization | Functional ligand conformation | NCBI |
| 95–100    | Disulfide bond (Cys95–Cys100) | Structural stabilization | Receptor binding interface integrity | NCBI |

### 🧬 Clinically Significant Variants (gnomAD / ClinVar)

> "No pathogenic or likely pathogenic variants reported in gnomAD v4.1.0 for this gene."

While ClinVar contains several pathogenic variants (e.g., frameshift c.34_37del, splice donor c.220+1G>T), none are present in gnomAD v4.1.0, suggesting extreme rarity in the general population. These variants are associated with insulin-like growth factor I deficiency (OMIM: 147440).

---

# 🧠 4. Pathways and Functional Networks

- **KEGG Pathways:**
  - [PI3K-Akt signaling pathway](https://www.kegg.jp/pathway/hsa04151): Central to IGF1 function in cell survival, growth, and metabolism
  - [Dilated cardiomyopathy](https://www.kegg.jp/pathway/hsa05414): IGF1 contributes to cardiac remodeling and function
  - [EGFR tyrosine kinase inhibitor resistance](https://www.kegg.jp/pathway/hsa01521): Cross-talk with EGFR signaling in cancer therapy resistance
- **Interaction Partners:**
  - IGF1R (receptor)
  - IGFBPs (binding proteins)
  - Integrins (via RGD motif)
  - IRS1/2 (downstream signaling)

---

# 🧓 5. Longevity and Aging Associations

| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| Mouse (liver-specific) | IGF1 knockout | ↑ Lifespan in females (16.1%), ↓ in males (8.3%) | OpenGenes |
| *Drosophila* | Dilp2-GAL4-driven reduction | ↑ Lifespan (10.5% males, 33.5% females) | OpenGenes |
| Mouse (heart-specific) | IGF1 overexpression | Improved calcium homeostasis, ↓ apoptosis | PMID: 35616058 |
| Human centenarians | IGF-1:p.Ile91Leu variant | Attenuated IGF-1 signaling, exceptional longevity | PMID: 40133344 |

**Key Findings:**
- Sex-dependent effects: Females generally benefit more from reduced IGF1 signaling
- Tissue-specificity: Liver-specific knockout improves metabolic health but heart-specific overexpression enhances cardiac aging resilience
- Mitochondrial dependence: Pro-longevity effects require intact mitochondrial genome (PMID: 40501628)
- Therapeutic potential: IGF-1-X10 plasmid counteracts age-related muscle atrophy (PMID: 35838121)

---

# 💊 6. Small Molecule and Drug Interactions

- **Masoprocol:** Listed in KEGG but no direct mechanistic link to IGF1 established
- **Sulforaphane:** Indirectly enhances IGF1 signaling through Nrf2 activation (cross-pathway interaction)
- **2-O-β-D-Glucopyranosyl ascorbic acid:** Modulates IIS pathway to extend *C. elegans* lifespan (PMID: 40509403)
- **Mechano-growth factor (MGF) E-domain peptide:** Preserves cardiac function during aging (PMID: 23712705)

---

# 🌍 7. Evolutionary Conservation

- **Domain Conservation:** B and A domains highly conserved across vertebrates (70–90% identity)
- **Ortholog Functions:**
  - *C. elegans* SKN-1: Regulates oxidative stress response and longevity
  - *Drosophila* CncC: Mediates stress resistance and developmental growth
  - Mouse IGF1: Nearly identical function in growth and metabolism
- **Longevity Mechanism Conservation:** Reduced IGF1 signaling extends lifespan in invertebrates and mammals, though sex-specific effects vary

---

# 📚 8. References

## Primary Databases
- UniProt: [P05019](https://www.uniprot.org/uniprotkb/P05019/entry)
- KEGG: [hsa:3479](https://www.kegg.jp/entry/hsa:3479)
- NCBI Gene: [3479](https://www.ncbi.nlm.nih.gov/gene/3479)
- OMIM: [147440](https://omim.org/entry/147440)
- gnomAD: [ENSG00000017427](https://gnomad.broadinstitute.org/gene/ENSG00000017427)

## Key Publications
- Rinderknecht & Humbel (1978). *J Biol Chem* 253(8):2769–2776. PMID: 632300
- PMID: 40133344 - IGF-1 variants in human longevity
- PMID: 35616058 - Cardiac IGF1R signaling in aging
- PMID: 35838121 - IGF-1-X10 for muscle aging
- PMID: 37941907 - Laron syndrome insights

## OpenGenes Resources
- [IGF1 Longevity Associations](https://opengenes.org/gene/IGF1)
- [IGF1R-IRS2-UCP2 haplotype](https://doi.org/10.1007/s11357-011-9210-z)
- [rs2229765 longevity association](https://doi.org/10.1186/1471-2318-9-19)
'''
article_1.source = "IGF1"

article_2 = Article()
article_2.content = '''
bservations: # 🧬 NFE2L2 (NRF2) Longevity Sequence-to-Function Knowledge Base

## 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** NFE2L2 (Nuclear factor erythroid 2-like 2)
- **Protein Name:** Nuclear factor erythroid 2-related factor 2
- **Identifiers:**
  - UniProt ID: |Q16236](https://www.uniprot.org/uniprotkb/Q16236/entry)
  - KEGG ID: |hsa:4780](https://www.kegg.jp/entry/hsa:4780)
  - Gene ID (NCBI): |4780](https://www.ncbi.nlm.nih.gov/gene/4780)
  - HGNC ID:
|HGNC:7782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:77
82)
  - Ensembl ID:
|ENSG00000116044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG000001
16044)
  - OMIM ID: |600492](https://omim.org/entry/600492)
  - RefSeqGene ID:
|NG_029882.1](https://www.ncbi.nlm.nih.gov/nuccore/NG_029882.1)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - |Protein (UniProt)](https://www.uniprot.org/uniprotkb/Q16236/entry)  
  - |Protein (RefSeq)](https://www.ncbi.nlm.nih.gov/protein/NP_006155.2)  
  - |mRNA (RefSeq)](https://www.ncbi.nlm.nih.gov/nuccore/NM_006164.5)  
  - |Gene (RefSeqGene)](https://www.ncbi.nlm.nih.gov/nuccore/NG_029882.1)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 605 amino acids (canonical isoform)
- **Key Domains / Motifs:**
  - bZIP domain (497–560): Mediates DNA binding and heterodimerization with
small Maf proteins
  - ETGE motif (79–82): High-affinity KEAP1 interaction site
  - DLG motif (29–31): Mediates KEAP1 interaction
  - Disordered regions (334–449, 571–605): Contain polar residue bias
  - Transactivation region (591–596): Mediates interaction with CHD6
- **Functional Roles:**
  - Master regulator of antioxidant response elements (ARE)
  - Mediates cellular defense against oxidative stress, inflammation, and
electrophilic insults
  - Regulates proteostasis via unfolded protein response (UPR)
- **Post-Translational Modifications (PTMs):**
  - Phosphorylation: S40 (PKC-mediated, promotes nuclear translocation), S215
  - Acetylation: K596/K599 (enhances nuclear localization; deacetylated by
SIRT1)
  - Glycation: K462/K472/K487 (impairs dimerization; reversed by FN3K)
- **Orthologs / Paralogs:**
  - *C. elegans*: SKN-1 (45% identity)
  - *Drosophila*: CncC (42% identity)
  - *Mus musculus*: Nfe2l2 (95% identity)

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval | Type of Modification | Experimental Effect | Functional Outcome |
Source |
|-----------|---------------------|---------------------|--------------------|--
------|
| 29–31 | DLG motif mutation | KEAP1 binding loss | Constitutive NRF2 activation
| UniProt |
| 79–82 | ETGE motif mutation | Abolished KEAP1 binding | Enhanced antioxidant
response | UniProt |
| 80 | T80K substitution | Increased protein abundance | Enhanced
transcriptional activity | UniProt |
| 497–560 | bZIP domain deletion | Loss of DNA binding | Impaired ARE activation
| NCBI |
| 591–596 | Transactivation region mutation | CHD6 interaction loss | Reduced
transcriptional activation | UniProt |

### 🧬 Clinically Significant Variants (gnomAD / ClinVar)
> "No pathogenic or likely pathogenic variants reported in gnomAD v4.1.0 for
this gene."

**Gene-Associated Diseases (OMIM / NCBI):**
- Immunodeficiency, developmental delay, and hypohomocysteinemia (IMDDHH)
- Hepatocellular carcinoma (via KEAP1-NRF2 pathway dysregulation)
- Neurodegenerative disorders (Alzheimer's, Parkinson's)

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - |hsa05418: Fluid shear stress and
atherosclerosis](https://www.kegg.jp/pathway/hsa05418): NRF2 activation protects
endothelial cells from oxidative damage
  - |hsa04141: Protein processing in endoplasmic
reticulum](https://www.kegg.jp/pathway/hsa04141): Regulates UPR during ER stress
- **Interaction Partners:**
  - KEAP1 (primary negative regulator)
  - MAFF, MAFG, MAFK (dimerization partners)
  - CHD6 (transcriptional co-activator)
  - SIRT1 (deacetylates NRF2)

---

## 🧓 5. Longevity and Aging Associations
| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| *C. elegans* (skn-1) | Forsythoside A | ↑ Mitophagy, ↓ chondrocyte senescence
| PMID: 39383631 |
| Hutchinson-Gilford progeria | Progerin inhibition | Restored NRF2 activity, ↓
oxidative stress | PMID: 27259148 |
| Mouse (Klotho-deficient) | Klotho supplementation | Prevented heart failure, ↓
cardiac aging | PMID: 33334122 |
| Human cardiomyocytes | LncRNA UCA1 overexpression | ↓ Oxidative stress, ↓
ferroptosis | PMID: 39538055 |
| Mouse (UVB-exposed skin) | Salvianolic acid B | ↓ Fibroblast senescence, ↑
skin repair | PMID: 38820663 |
| Mouse (intervertebral discs) | Pyrroloquinoline quinone | ↓ Disc degeneration,
↑ Wnt5a expression | PMID: 38780001 |

**Key Mechanisms:**
- NRF2 decline with age contributes to inflammaging and SASP
- Regulates chaperone-mediated autophagy via LAMP2A (PMID: 29950142)
- Nrf2/Wnt/β-catenin axis decline drives Parkinson's neurodegeneration (PMID:
32863224)

---

## 💊 6. Small Molecule and Drug Interactions
- **Omaveloxolone** (KEGG D10964): Activates NRF2 pathway by mimicking oxidative
stress
- **Sulforaphane**: Disrupts KEAP1-NRF2 binding → nuclear translocation
- **Dimethyl fumarate**: Activates NRF2 → upregulates antioxidant enzymes
- **Pyrroloquinoline quinone (PQQ)**: Dissociates KEAP1-NRF2 complex → ↑ Wnt5a
expression
- **Cynarin**: Inhibits NLRP3 inflammasome via NRF2/ROS axis (PMID: 39340662)

---

## 🌍 7. Evolutionary Conservation
- **Conserved domains:** bZIP domain (100% conservation in vertebrates)
- **Ortholog functions:**
  - *C. elegans* SKN-1: Regulates oxidative stress resistance and longevity
  - *Drosophila* CncC: Mediates detoxification and stress response
  - *Mus musculus* Nfe2l2: Critical for aging-related cardioprotection
- **Longevity conservation:** NRF2/SKN-1 pathway extends lifespan in
invertebrates when activated

---

## 📚 8. References
### Primary Databases
- UniProt: |Q16236](https://www.uniprot.org/uniprotkb/Q16236/entry)
- KEGG: |hsa:4780](https://www.kegg.jp/entry/hsa:4780)
- NCBI Gene: |4780](https://www.ncbi.nlm.nih.gov/gene/4780)
- OMIM: |600492](https://omim.org/entry/600492)
- gnomAD:
|ENSG00000116044](https://gnomad.broadinstitute.org/gene/ENSG00000116044)

### Key Publications
1. Moi P., et al. (1994). *Proc Natl Acad Sci U S A* 91(21):9926–9930. PMID:
7937919
2. Forsythoside A mechanism: PMID: 39383631
3. Progeria-NRF2 link: PMID: 27259148
4. Klotho-NRF2 cardiac aging: PMID: 33334122
5. ERK5-NRF2 atherosclerosis: PMID: 37264926
6. NRF2 in chaperone-mediated autophagy: PMID: 29950142
7. NRF2-HO-1 inflammaging: PMID: 39380993

### Additional Resources
- Reactome: |R-HSA-9755511
(KEAP1-NFE2L2)](https://reactome.org/content/detail/R-HSA-9755511)
- PDB Structures: |2FLU](https://www.rcsb.org/structure/2FLU),
|7O7B](https://www.rcsb.org/structure/7O7B),
|7X5E](https://www.rcsb.org/structure/7X5E)
'''
article_2.source = "NRF2"


assistent = BioAssistent()
assistent.add_many_articles([article_1, article_2])


print(assistent.process_user_issue("What are the main functions of the NRF2 protein in the cellular antioxidant response?"))
print(assistent.process_user_issue("What is the role of IGF1 in regulating growth and metabolism, and through which signaling pathway is it implemented?"))
print(assistent.process_user_issue("How can the interaction or cross-talk between the NRF2 and IGF1 pathways affect aging and longevity?"))