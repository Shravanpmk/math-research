# Fuzzy Soft Graphs: Literature Review, Gap Analysis and Research Roadmap

*Prepared 12 November 2026. Literature coverage: foundational work through items indexed by early November 2026.*

---

## 0. Read this first: what is verified and what is not

**Search limitations.** This report was produced in a sandbox whose network policy blocked every scholarly host: Google Scholar, Crossref, OpenAlex, Semantic Scholar, arXiv, doi.org and all publisher sites returned proxy refusals. Only a general web-search tool was available. Consequently:

1. **Your Google Scholar profile could not be opened.** Searches on the profile ID (`QFNVkx4AAAAJ`) and on the name "Shravan" combined with fuzzy/soft graph terms returned nothing attributable to you. **Step 1 (profile analysis) is therefore not done**, and I have not guessed at your publications. Section 1 says exactly what I need from you and how the ranking in Section 7 will change once I have it.
2. **No full text was read.** Every bibliographic fact below comes from search-result records (publisher landing pages, DOAJ, DBLP, MaRDI, PubMed, RePEc, Bohrium, citing papers' reference lists). I could not open a paper to check a theorem statement. Where I describe a paper's content, it is from its indexed abstract.
3. **Negative results are weak evidence.** "No paper found" means "not found by roughly forty targeted web queries", not "confirmed absent from Scopus/Web of Science/MathSciNet/zbMATH". Every novelty claim in this report must be re-checked in those databases before it goes into a manuscript.

**Evidence tags used throughout.**

| Tag | Meaning |
|---|---|
| **[V]** | Bibliographic record seen in this session's search results (title, authors, venue; DOI where given). |
| **[V‑]** | Record seen, but some field (authors, pages, or DOI) was missing or came only from a citing paper. The missing field is named. |
| **[R]** | Recalled from my own training knowledge and *not* re-verified in this session. Standard, well-known references, but check before citing. |
| **Proved here** | A statement I prove in this report; small cases are also checked by `experiments/verify_examples.py`. |
| **Conjecture / Question** | Unproved. My own hypothesis. |

---

## 1. Researcher profile analysis (Step 1): not completed

I could not access the profile, so I cannot identify your publications, co-authors, citation pattern or technical strengths. Rather than fabricate an analysis, here is what would change if you supply the list (pasting titles and venues is enough):

| If your record shows… | Then the ranking in Section 7 shifts toward… |
|---|---|
| Domination or coloring in fuzzy / fuzzy soft / intuitionistic variants | P2, P3, P4, P13 (already ranked first) |
| Connectivity, strong arcs, indices (Wiener, connectivity index) | P6, P7, P8 |
| Matrix or energy papers | P10, P11, P12 |
| Decision-making applications (MCDM, medical, supplier selection) | P16, P9, and the application tracks of Section 6 |
| Algorithms or computation | P5, P9, P17 |
| Algebraic or hyperstructure work | P1, P15 |

The roadmap below is written to stand without this information. Its ranking assumes only that you work in fuzzy soft graph theory at PhD level, as your request implies.

---

## 2. Standing notation

- $G^{*}=(V,E)$ is a finite simple graph, $n=|V|$. $A$ is a finite parameter set, $m=|A|$.
- A **fuzzy graph** on $G^{*}$ is a pair $(\sigma,\mu)$, $\sigma:V\to[0,1]$, $\mu:E\to[0,1]$, with $\mu(xy)\le\sigma(x)\wedge\sigma(y)$ (Rosenfeld [R]).
- A **fuzzy soft graph** (FSG) is $\tilde G=(G^{*},\tilde F,\tilde K,A)$ where $(\tilde F,A)$ is a fuzzy soft set over $V$, $(\tilde K,A)$ is a fuzzy soft set over $E$, and for every $e\in A$ the pair $H(e)=(\sigma_e,\mu_e)=(\tilde F(e),\tilde K(e))$ is a fuzzy graph on $G^{*}$. This is the definition of Akram–Nawaz and Mohinta–Samanta as indexed [V]. Equivalently: **an FSG is an $A$-indexed family of fuzzy graphs on one vertex set.**
- Strength of a path $P$ in layer $e$: $s_e(P)=\min_{uv\in P}\mu_e(uv)$. Strength of connectedness: $\mathrm{CONN}_e(x,y)=\max_P s_e(P)$.
- An arc $xy$ is **strong** in $H(e)$ if $\mu_e(xy)\ge \mathrm{CONN}_{H(e)-xy}(x,y)$ (Bhutani–Rosenfeld [R]; $\alpha$- and $\beta$-strong in Mathew–Sunitha's classification [R]). $S_e$ denotes the crisp **strong-arc graph** of layer $e$.
- Meet layer: $\mu_\wedge(xy)=\min_{e\in A}\mu_e(xy)$, with $\mathrm{CONN}_\wedge$ its strength of connectedness.
- $A_e=[\mu_e(v_iv_j)]$ is the adjacency matrix of layer $e$, $L_e=D_e-A_e$ its Laplacian, $\mathcal E(M)=\sum_i|\lambda_i(M)|$ the energy.

---

## 3. Literature review (Step 2)

### 3.1 Chronological map

| Period | Development | Key records |
|---|---|---|
| 1965–1999 | Fuzzy sets; fuzzy graphs; soft sets | Zadeh 1965 [R]; Rosenfeld 1975 [R]; Molodtsov 1999 [R] |
| 2001 | Fuzzy soft sets | Maji–Biswas–Roy 2001 [R] |
| 2014–2015 | Soft graphs and their operations; soft trees | Thumbakara–George 2014 [V‑]; Akram–Nawaz 2015 (Operations on soft graphs) [V‑]; Akram–Zafar 2015 [V] |
| 2015–2016 | **Fuzzy soft graphs defined** (two independent introductions); regular/irregular types; applications | Akram–Nawaz 2015 [V]; Mohinta–Samanta 2015 [V]; Akram–Nawaz 2016 [V] |
| 2016–2018 | Complements, uniform/regular types, set operations, trees, connectivity vs. complement | Al‑Masarwah–Abu Qamar 2016, 2018 [V]; Çelik 2017 [V‑]; Akram–Zafar 2017 [V‑]; Shashikala–Anil 2016 [V] |
| 2016–2021 | **Variant explosion**: intuitionistic, neutrosophic, bipolar, interval-valued, Pythagorean (Dombi), picture, type‑2, m‑polar soft variants | Shahzadi–Akram 2017, 2018; Akram–Shahzadi 2017; Shahzadi–Akram–Davvaz 2020; Chellamani et al. 2021; Shahzadi–Sarwar–Akram 2020 (all [V] or [V‑]) |
| 2017–2021 | Domination begins | Hussain–Hussain 2017 [V]; Rajeevan PhD thesis 2019 [V‑]; Karbasioun–Ameri 2021 [V] |
| 2019–2022 | Cycles, products, degrees | Shashikala–Anil 2019, 2021, 2022 [V] |
| 2021–2022 | Competition graphs and hypergraphs | Nawaz–Akram 2021/22 [V]; fuzzy soft competition hypergraphs 2022 [V‑] |
| 2023 | Coloring begins | Hussain–Farhana 2023 (two papers) [V] |
| 2024 | Degree-based topological indices in top-tier venues; soft coloring; bipolar fuzzy soft domination | Azeem et al. 2024 [V]; Anwar–Azeem–Jamil 2024 [V‑]; Hamidizadeh et al. 2024 [V]; Amin et al. 2024 [V] |
| 2025–2026 | Planar and outerplanar FSGs with image applications; FSG structures; spherical fuzzy soft competition graphs; soft-graph survey; large "uncertain graph" surveys on arXiv | Sci. Rep. 2025 and 2026 [V‑]; Amin–Fahmi 2025 [V]; Jose–George–Thumbakara 2025 [V‑]; arXiv 2411.17411, 2602.21268, 2605.23936 [V‑] |

### 3.2 Thematic comparative table: fuzzy soft graphs proper

| # | Paper | Venue, year, DOI/link | Contribution (from indexed abstract) | Limitation (my assessment) | Tag |
|---|---|---|---|---|---|
| 1 | M. Akram, S. Nawaz, *On fuzzy soft graphs* | Ital. J. Pure Appl. Math. 34 (2015) 497–514; [PDF](https://ijpam.uniud.it/online_issue/201534/44-AkramNawaz.pdf) | Defines FSGs; strong, complete, regular FSGs | Definitions and layer-wise properties; no coupled invariants | [V] |
| 2 | S. Mohinta, T. K. Samanta, *An introduction to fuzzy soft graph* | Mathematica Moravica 19(2) (2015) 35–48; doi:10.5937/matmor1502035m | Defines FSGs; union and intersection | Same | [V] |
| 3 | M. Akram, S. Nawaz, *Fuzzy soft graphs with applications* | J. Intell. Fuzzy Syst. 30(6) (2016) 3619–3632; doi:10.3233/IFS-162107 | Irregular FSG types; social- and road-network illustrations | Applications are illustrative toy examples | [V] |
| 4 | A. Al‑Masarwah, M. Abu Qamar, *Some new concepts of fuzzy soft graphs* | Fuzzy Inf. Eng. 8(4) (2016) 427–438; doi:10.1016/j.fiae.2017.01.003 | Complement and $\mu$-complement | Layer-wise | [V] |
| 5 | A. Al‑Masarwah, M. Abu Qamar, *Certain types of fuzzy soft graphs* | New Math. Nat. Comput. 14(2) (2018) 145–156; doi:10.1142/S1793005718500102 | Uniform vertex/edge FSGs; degree, total degree; regularity of complements | Layer-wise | [V] |
| 6 | Çelik, *Some operations on fuzzy soft graphs* | AIP Conf. Proc. (2017); doi:10.1063/1.4981678 | Union, intersection | Conference note. Author's given name not confirmed | [V‑] |
| 7 | M. Akram, F. Zafar, *Fuzzy soft trees* | Southeast Asian Bull. Math. (2017) | Fuzzy soft cycles, bridges, cutnodes, trees | Volume/pages not confirmed | [V‑] |
| 8 | M. Akram, F. Zafar, *Hybrid Soft Computing Models Applied to Graph Theory* (book; ch. 4 "Fuzzy Soft Graphs") | Springer, Stud. Fuzziness Soft Comput. 380 (2020); doi:10.1007/978-3-030-16020-3 | Consolidates the Akram-school definitions | Monograph of existing material | [V] |
| 9 | S. Shashikala, P. N. Anil, *Connectivity in fuzzy soft graph and its complement* | IOSR J. Math. 12(5) (2016) 95–99 | Connectivity of an FSG vs. its complement, by examples | Example-driven; venue is not selectively indexed | [V] |
| 10 | S. Shashikala, P. N. Anil, *Fuzzy soft cycles in fuzzy soft graphs* | J. New Results Sci. 8(1) (2019) 26–35 | Decomposition of complete FSGs into Hamiltonian fuzzy soft cycles | Inherits the crisp $K_n$ decomposition | [V] |
| 11 | S. Shashikala, P. N. Anil, *Some studies on products of fuzzy soft graphs* | Ratio Mathematica 41 (2021) 227–254 | Product operations | Degree bookkeeping | [V] |
| 12 | S. Shashikala, P. N. Anil, *Study of different degrees based on various operations on fuzzy soft graphs* | Ital. J. Pure Appl. Math. 47 (2022) 971–983 | Degrees under conjunction/disjunction | Same | [V] |
| 13 | R. J. Hussain, S. S. Hussain, *Domination in fuzzy soft graphs* | Int. J. Fuzzy Math. Arch. 14(2) (2017) 243–252; doi:10.22457/ijfma.v14n2a8 | First domination paper for FSGs | DOI seen in one record only | [V] |
| 14 | Rani Rajeevan, *Domination parameters in fuzzy soft graphs* (PhD thesis) | Univ. Kerala, 2019; Shodhganga handle 10603/570786 | Thesis-length treatment of domination parameters | Only the catalogue listing was seen. **Must be read before claiming novelty in any domination problem.** | [V‑] |
| 15 | A. Karbasioun, R. Ameri, *Total and secure domination for corona product of two fuzzy soft graphs* | Fuzzy Inf. Eng. (2021); doi:10.1080/16168658.2021.1915456 | Dominating, total and secure total dominating sets in coronas | One product, three parameters | [V] |
| 16 | R. Jahir Hussain, S. Afya Farhana, *Fuzzy chromatic number of fuzzy soft cycle and complete fuzzy soft graphs* | AIP Conf. Proc. (2023); doi:10.1063/5.0114372 | Fuzzy soft colouring; chromatic numbers of two classes; bounds | Two graph classes | [V] |
| 17 | R. Jahir Hussain, S. Afya Farhana, *Fuzzy dominator coloring on fuzzy soft graphs* | Ratio Mathematica 48 (2023); doi:10.23755/rm.v48i0.1153 | Dominator colouring on paths, cycles, complete and complete bipartite FSGs | Class-by-class values | [V] |
| 18 | *Bounds on fuzzy dominator chromatic number of fuzzy soft bipartite graphs* | Ratio Mathematica (2023) | Sharp bounds for bipartite FSGs | Authors not shown in the records I saw | [V‑] |
| 19 | M. Azeem, S. Anwar, M. K. Jamil, M. Saeed, M. Deveci, *Topological numbers of fuzzy soft graphs and their application* | Inf. Sci. 667 (2024) 120468; doi:10.1016/j.ins.2024.120468 | Two Sombor-type numbers for FSG families | Degree-based only; one index DBLP lists the fourth author as M. H. Saeed | [V] |
| 20 | S. Anwar, M. Azeem, M. K. Jamil, *Topological numbers of fuzzy soft graphs and their applications in globalizing the world by mutual trade* | Appl. Soft Comput. 159 (2024) 111642 | Zagreb-type numbers; trade-corridor application | DOI not confirmed | [V‑] |
| 21 | H. S. Nawaz, M. Akram, *Oligopolistic competition among the wireless internet service providers of Malaysia using fuzzy soft graphs* | J. Appl. Math. Comput. (2021 online; issue 2022) 855–890; doi:10.1007/s12190-021-01514-z | Fuzzy soft (economic) competition graphs | Digraph-based; no optimisation theory | [V] |
| 22 | *Decision-making methods based on fuzzy soft competition hypergraphs* | Complex Intell. Syst. 8(3) (2022) 2325–2348; doi:10.1007/s40747-022-00646-4 | $k$-competition and neighbourhood hypergraphs; algorithms for competition strength | Authors not shown in the records I saw | [V‑] |
| 23 | *A fuzzy soft planar graph with application in image segmentation* | Sci. Rep. (2025); doi:10.1038/s41598-025-02880-5 | Fuzzy soft multigraphs, planarity, faces | Authors not confirmed | [V‑] |
| 24 | *Image contraction through fuzzy soft outerplanar graph structures* | Sci. Rep. 16 (2026) 9779; [link](https://www.nature.com/articles/s41598-026-37570-3) | Outerplanar FSGs; duals of fuzzy soft planar graphs | Authors not confirmed; DOI inferred from URL | [V‑] |
| 25 | U. Amin, A. Fahmi, *Fuzzy soft graph structure with application* | Bol. Soc. Paran. Mat. 43 (2025) 1–39; doi:10.5269/bspm.76660 | Generalises FSGs to graph structures; courier-selection example | Definitional | [V] |
| 26 | Kalaiarasi, Mahalakshmi et al., *Fuzzy soft tri‑partite graphs and its complement* | Seen only as a ResearchGate listing | Tripartite FSGs | Venue not confirmed | [V‑] |

### 3.3 Variants (hybrid membership models)

| Variant | Record | Tag |
|---|---|---|
| Intuitionistic fuzzy soft | S. Shahzadi, M. Akram, *Intuitionistic fuzzy soft graphs with applications*, J. Appl. Math. Comput. 55 (2017) 369–392 (DOI not confirmed); *Graphs in an intuitionistic fuzzy soft environment*, Axioms 7(2) (2018) 20, doi:10.3390/axioms7020020; *Edge regular intuitionistic fuzzy soft graphs*, J. Intell. Fuzzy Syst. (2016), doi:10.3233/JIFS-16120 | [V‑], [V], [V‑] |
| Neutrosophic soft | M. Akram, S. Shahzadi, *Neutrosophic soft graphs with application*, J. Intell. Fuzzy Syst. 32(1) (2017) 841–858, doi:10.3233/JIFS-16090; Hussain–Hussain–Smarandache, *Domination number in neutrosophic soft graphs*, Neutrosophic Sets Syst. (2019) | [V], [V‑] |
| Bipolar fuzzy soft | *A new multiple criteria decision-making method based on bipolar fuzzy soft graphs*, Iran. J. Fuzzy Syst. ([article 4116](https://ijfs.usb.ac.ir/article_4116.html)), authors not shown in the record; U. Amin, A. Fahmi, N. Yaqoob, A. Farid, M. A. S. Hassan, *Domination in bipolar fuzzy soft graphs*, J. Intell. Fuzzy Syst. 46(3) (2024) 6369–6382, doi:10.3233/JIFS-236485 | [V‑], [V] |
| Interval-valued fuzzy soft | *Interval-valued fuzzy soft graphs*, Topol. Algebra Appl. (2017), doi:10.1515/taa-2017-0004 (author names garbled in the record) | [V‑] |
| Pythagorean fuzzy soft | G. Shahzadi, M. Akram, B. Davvaz, J. Intell. Fuzzy Syst. 38(4) (2020) 4977–4991, doi:10.3233/JIFS-191610; M. Akram, G. Shahzadi, *Decision-making approach based on Pythagorean Dombi fuzzy soft graphs*, Granul. Comput., doi:10.1007/s41066-020-00224-4; Nawaz–Akram, *Inter-specific competition among trees in Pythagorean fuzzy soft environment*, Complex Intell. Syst. (2021), doi:10.1007/s40747-021-00470-2 | [V] |
| Picture fuzzy soft | P. Chellamani, D. Ajay, S. Broumi, T. A. A. Ligori, *An approach to decision-making via picture fuzzy soft graphs*, Granul. Comput. (2021), doi:10.1007/s41066-021-00282-2 | [V] |
| Type‑2 fuzzy soft | S. Shahzadi, M. Sarwar, M. Akram, *Decision-making approach with fuzzy type‑2 soft graphs*, J. Math. (2020), doi:10.1155/2020/8872446 | [V] |
| m‑polar soft fuzzy | Ramkumar–Sridevi line, Ratio Mathematica (2023), incl. *Domination in m‑polar soft fuzzy graphs* (authors not shown in that record) | [V‑] |
| Spherical fuzzy soft | *Spherical fuzzy soft competition graphs with application*, doi:10.1007/s12190-024-02286-y (2025) | [V‑] |
| Fuzzy hypersoft | *Representation of fuzzy hypersoft set in graphs*, Palestine J. Math. 12(1) (2023) 836–847 | [V‑] |
| Soft expert, complex | Titles appear only inside reference lists of arXiv surveys; not independently confirmed | not verified |
| q‑rung orthopair fuzzy soft graphs | **No record found** under that title | gap candidate, low value |

### 3.4 Neighbouring literature that the proposals rely on

| Topic | Record | Tag |
|---|---|---|
| Soft graph colouring | K. Hamidizadeh, R. Manaviyat, S. Mirvakili, B. Davvaz, *Application of soft sets to graph coloring*, Comput. Appl. Math. 43 (2024) 214, doi:10.1007/s40314-024-02738-y | [V] |
| Soft graph matrices | Thenge, Reddy, Jain, *Adjacency and incidence matrix of a soft graph*, Commun. Math. Appl. 11(1) (2020) | [V] |
| Soft graph survey | J. Jose, B. George, R. K. Thumbakara, *Soft graphs: a comprehensive survey*, New Math. Nat. Comput. 21(3) (2025) | [V‑] |
| Fuzzy connectivity | *Node connectivity and arc connectivity of a fuzzy graph*, Inf. Sci. 180 (2010), doi:10.1016/j.ins.2009.10.006 (Mathew–Sunitha [R]); *Generalized fuzzy graph connectivity parameters with application to human trafficking*, Mathematics 8(3) (2020) 424 | [V] |
| Connectivity and Wiener indices of fuzzy graphs | Binu–Mathew–Mordeson, Fuzzy Sets Syst. 2019 and 2020 | [R] |
| Fuzzy graph energy | Anjali–Mathew 2013 [R]; Sharbaf–Fayazi, *Laplacian energy of a fuzzy graph*, Iran. J. Math. Chem. (2014) [V]; *Energy of Pythagorean fuzzy graphs with applications*, Mathematics 6(8) (2018) 136, doi:10.3390/math6080136 [V] | mixed |
| Energy of fuzzy soft *sets* (singular values) | Int. J. Fuzzy Syst. 21(2) (2019) 35–49 (authors not shown in record) | [V‑] |
| Fuzzy colouring | Muñoz et al., *Coloring fuzzy graphs* (Omega) [V‑]; Gong–Zhang, Axioms 2022 [V‑]; Mahapatra–Samanta–Pal, *Applications of edge colouring of fuzzy graphs*, Informatica 31(2) (2020) 313–330, doi:10.15388/20-INFOR403 [V] | mixed |
| Fuzzy domination | Somasundaram–Somasundaram 1998 [R]; Manjusha–Sunitha, J. Intell. Fuzzy Syst. 27 (2014), doi:10.3233/IFS-141277 [V]; *Strong domination index in fuzzy graphs*, arXiv:2307.10409 [V‑] | mixed |
| Factor (simultaneous) domination in crisp graphs | Brigham–Dutton, *Factor domination in graphs*, Discrete Math. 86 (1990) 127–136 | [R] |
| Robust discrete optimisation with scenarios | Kouvelis–Yu (1997 book); Yu–Yang, *On the robust shortest path problem*, Comput. Oper. Res. 25 (1998) | [R] |
| Fuzzy graph neural models | *Enhancing link prediction with fuzzy graph attention networks…*, arXiv:2411.07482; "soft graph neural network" definitions in arXiv:2602.21268 | [V‑] |

### 3.5 Sources I could not access

Google Scholar (profile and citation counts), Scopus, Web of Science, MathSciNet, zbMATH, all publisher full texts, the Rajeevan thesis, and the arXiv surveys' text. Citation counts are therefore omitted rather than estimated.

---

## 4. State of the art (Step 3)

### 4.1 Maturity by direction

| Direction | Definitions | Theorems | Algorithms / complexity | Applications | Maturity |
|---|---|---|---|---|---|
| Basic types (regular, complete, strong, complement) | Stable | Many, layer-wise | None needed | Toy | Saturated |
| Set operations and products | Stable | Degree formulae | None | None | Saturated |
| Trees, cycles, bridges, cutnodes | Present | Layer-wise transfers | None | None | Shallow |
| Connectivity | Example-level | Few | None found | None | **Immature** |
| Domination | Several papers and one thesis | Class values, corona | None found | None | Developing |
| Colouring | Two to three papers since 2023 | Class values and bounds | None found | None | **Early** |
| Degree-based topological indices | Two 2024 papers | Formulae for families | Direct computation | Trade | Developing |
| Distance/connectivity-based indices | **None found** | None | None | None | **Open** |
| Spectral (energy, Laplacian) | **None found** for FSGs (exists for fuzzy graphs and for fuzzy soft *sets*) | None | None | None | **Open** |
| Planarity | 2025–2026 papers | Present | Image pipelines | Image segmentation | Developing |
| Competition (hyper)graphs | Present | Present | Scoring procedures | Markets | Developing |
| Isomorphism, automorphisms, enumeration | **None found** | None | None | None | Open |
| Metric dimension, labeling, Hamiltonicity | None found (one Hamiltonian decomposition note) | None | None | None | Open |
| Optimisation (paths, trees, flows, matching) | **None found** | None | None | None | **Open** |
| Machine learning on FSGs | Definitions inside surveys only | None | None | None | Open |
| Decision-making | Many procedures across variants | No axiomatics or stability results found | Score-and-rank | Illustrative | Wide but shallow |

### 4.2 Critical assessment

Three observations shape everything that follows.

**(a) Most published FSG theory is layer-wise.** Because an FSG is a family $\{H(e)\}_{e\in A}$ of fuzzy graphs, a statement of the form "property $\mathcal P$ holds in $\tilde G$ iff it holds in every $H(e)$" carries no information beyond fuzzy graph theory. From the indexed abstracts, the regularity, complement, operation, tree and degree results are of this form. This is the field's main weakness, and a referee at a strong journal will raise it.

**(b) The parameter set has no structure in the existing theory.** Parameters are never weighted, ordered, reduced, or made to interact, although soft set theory itself has a developed parameter-reduction literature. The mathematically new content of an FSG can only come from **coupling across parameters**.

**(c) Variant proliferation has outpaced depth.** Replacing $[0,1]$ by intuitionistic, Pythagorean, picture, spherical or neutrosophic grades multiplies papers without creating new graph theory. Extending to yet another membership model is the lowest-value direction available, and I recommend against it.

One structural remark that deserves care in any manuscript: an FSG is formally an edge-weighted **multiplex (multilayer) network** with a shared vertex set. Multilayer-network science (Kivelä et al. 2014 [R]) already studies coupled invariants. A serious FSG paper should cite that literature and state what the fuzzy (max–min) semantics add; Sections 5 and 7 are written with that in mind.

---

## 5. Research gaps and original problems (Steps 4 and 5)

### 5.1 Genuine gaps versus solved or trivial problems

| Area | Already done (do not repeat) | Trivial by layer-wise reduction | Genuine gap |
|---|---|---|---|
| Operations | Union, intersection, products, complements, degree formulae | Further products' degree formulae | Behaviour of *coupled* invariants under products (P2, P6) |
| Connectivity | Bridges/cutnodes per layer; connectivity vs. complement examples | "Connected iff every layer connected" | Consensus connectivity (P6), all-layer separators (P8) |
| Domination | Basic, total, secure-total (corona), dominator colouring on classes; bipolar and neutrosophic versions; a thesis | Per-layer domination numbers | Simultaneous and $k$-of-$m$ domination, existence of independent versions, complexity (P2–P5) |
| Colouring | Chromatic numbers of cycles/complete FSGs; soft colouring of soft graphs | Colour each layer separately | Multi-threshold and conflict-minimising colouring (P13) |
| Spectral | Nothing for FSGs | Tuple of layer energies | Energy deficit, optimal weighting, tensor spectra (P10–P12) |
| Indices | Sombor/Zagreb type (degree-based) | More degree-based indices | Connectivity/Wiener-type coupled indices (P7) |
| Optimisation | Nothing found | — | Robust path/tree/matching dichotomy (P9) |
| Uncertainty modelling | Many membership variants | New membership variants | Random FSGs (P18); parameter reduction (P4) |
| Machine learning | Definitions only | — | FS‑GNN with t‑norm aggregation (P17) |
| Decision-making | Many scoring procedures | New numerical examples | Axiomatics and stability (P16) |
| Network analysis | Toy social/road examples | — | Vulnerability (P8), centrality via P6, P11 |

### 5.2 Two foundational facts used repeatedly

**Lemma 2.1 (realisability of strong-arc graphs). Proved here.** Let $G^{*}$ be connected and $S$ a spanning subgraph of $G^{*}$. There is a fuzzy graph on $G^{*}$ with full support whose strong-arc graph is exactly $S$ if and only if $S$ is connected.

*Proof.* ($\Leftarrow$) Put $\sigma\equiv1$, $\mu=1$ on $E(S)$ and $\mu=\tfrac12$ on $E\setminus E(S)$. Arcs of $S$ have the maximum possible weight, so they are strong. For $xy\notin E(S)$, $S\subseteq G^{*}-xy$ is connected, so $\mathrm{CONN}_{G-xy}(x,y)=1>\tfrac12$ and $xy$ is not strong. ($\Rightarrow$) Every edge $uv$ of a maximum spanning tree $T$ satisfies $\mu(uv)=\mathrm{CONN}(u,v)$, hence is strong; so $T\subseteq S$ and $S$ is connected (this is the Bhutani–Rosenfeld strong-path theorem [R]). $\square$

**Corollary 2.2. Proved here.** For connected $G^{*}$ and any connected spanning subgraphs $S_1,\dots,S_m$ of $G^{*}$ there is an FSG over $A=\lbrace e_1,\dots,e_m\rbrace$ with $S_{e_i}=S_i$ for all $i$. Hence every invariant of an FSG that depends only on $(S_e)_{e\in A}$ ranges over exactly the values attained by $m$-tuples of connected spanning subgraphs of $G^{*}$.

**Remark 2.3 (generic layers are trees). Proved here.** If the weights $\mu_e(uv)$, $uv\in E$, are pairwise distinct, then $S_e$ is exactly the unique maximum spanning tree of $H(e)$. (A non-tree edge is strictly weaker than every edge on its tree path, so it is not strong; a tree edge is the strictly heaviest edge across its fundamental cut, so it is strong.) Strong-arc graphs with cycles therefore arise only from ties, which is where the "$\beta$-strong" arcs live.

This corollary is a **triviality filter**: any proposed "strong-arc" invariant of FSGs is a crisp invariant of tuples of connected spanning subgraphs, and its novelty must be judged in that setting.

### 5.3 Problem statements

Each problem gives: setting; question; novelty evidence; expected contribution; strategy; validation; difficulty (1–5), feasibility, publication potential. "Novelty evidence" always carries the caveat of Section 0.

---

#### P1. Separability: which FSG invariants are genuinely soft?

- **Definitions.** Call an invariant $I$ of FSGs **separable** if there are a fuzzy-graph invariant $I_0$ and a symmetric function $\Phi$ with $I(\tilde G)=\Phi\big((I_0(H(e)))_{e\in A}\big)$ for all $\tilde G$. Call it **coupled** otherwise.
- **Question.** Give a usable criterion for separability, and classify the invariants in the existing FSG literature (degrees, regularity, domination, chromatic numbers, Sombor/Zagreb numbers, planarity values) as separable or coupled.
- **Novelty.** No such classification was found. The observation behind it is implicit in the definition but, as far as I could see, not stated or exploited.
- **Contribution.** A short structural paper with (i) a formal criterion (e.g., $I$ is separable iff it is invariant under independent relabelling of each layer's weights that preserves each $I_0$-fibre); (ii) a table auditing the literature; (iii) the first catalogue of coupled invariants (those of P2, P6, P8, P10).
- **Strategy.** Category-style formulation: FSGs as functors from the discrete category $A$ to fuzzy graphs on $G^{*}$; separable invariants factor through the product. Coupledness is shown by exhibiting two FSGs with equal multisets of layers' $I_0$-values but different $I$.
- **Validation.** The examples in P3 and P6 already witness coupledness of simultaneous independent domination and the consensus gap.
- **Difficulty 2. Feasibility high. Potential:** a positioning paper; suitable as the opening chapter of a thesis. The audit must be done from full texts, which I could not read.

---

#### P2. Simultaneous (factor) domination in fuzzy soft graphs

- **Definitions.** $D\subseteq V$ is a **simultaneous strong dominating set** of $\tilde G$ if $D$ dominates $S_e$ for every $e\in A$. $\gamma_{\mathrm{sim}}(\tilde G)$ is the minimum $|D|$; the weighted version minimises $\sum_{v\in D}\max_e\sigma_e(v)$.
- **Proved here (elementary bounds).** $\max_e\gamma(S_e)\le\gamma_{\mathrm{sim}}(\tilde G)\le\min\lbrace\sum_e\gamma(S_e),\ \gamma(\bigcap_eS_e)\rbrace$, where isolated vertices of $\bigcap_e S_e$ count in the dominating set.
- **Reduction.** By Corollary 2.2, $\gamma_{\mathrm{sim}}$ over FSGs on $G^{*}$ equals the factor domination number (Brigham–Dutton [R]) over tuples of *connected spanning* subgraphs of $G^{*}$. The crisp literature treats factorings of $K_n$ (edge-disjoint factors); here factors overlap, must be connected, and live in a host graph $G^{*}$.
- **Questions.** (a) Determine $\Gamma_m(G^{*})=\max\gamma_{\mathrm{sim}}$ over all FSGs on $G^{*}$ with $m$ parameters, for paths (trivial: all layers equal $G^{*}$), cycles, complete graphs, complete bipartite graphs, grids. (b) **Question P2.1:** does $\Gamma_m(K_n)/n$ converge for fixed $m$; is the limit $c_m<1$; and does $c_m\to1$ as $m\to\infty$? (For $m$ Hamiltonian-path layers a random-set-plus-repair argument gives an upper bound strictly below $n$; I have not verified more than this heuristic.) (c) Characterise FSGs with $\gamma_{\mathrm{sim}}=\max_e\gamma(S_e)$.
- **Novelty.** Published FSG domination (items 13–15, 17–18 of Table 3.2; bipolar and neutrosophic analogues) is, by abstract, per-layer. Simultaneous domination was not found. **Risk:** the Rajeevan thesis is unread.
- **Strategy.** For cycles, each layer is $C_n$ or $C_n$ minus an edge; this gives a clean extremal problem solvable by a covering argument. For $K_n$, use probabilistic layers (random spanning trees) for lower bounds and the union-of-dominating-sets bound refined by a greedy/alteration argument for upper bounds.
- **Validation.** Exhaustive search for $n\le 9$, $m\le3$ (the script already brute-forces $\gamma_{\mathrm{sim}}$); ILP for larger instances.
- **Difficulty 3. Feasibility high. Potential:** Discrete Applied Mathematics / Fuzzy Sets and Systems level if the extremal results are sharp.

---

#### P3. Existence of simultaneous independent dominating sets

- **Definition.** $D$ is a simultaneous independent dominating set if it dominates every $S_e$ and is independent in $\bigcup_eS_e$.
- **Example 3.1. Proved here.** On $V=\lbrace a,b,c\rbrace$, $G^{*}=K_3$, take $S_1=$ path $a\!-\!b\!-\!c$ and $S_2=$ path $b\!-\!a\!-\!c$ (realisable by Lemma 2.1). Independent sets of the union are singletons, and no singleton dominates both layers. So such a set **need not exist**, in contrast with every single graph, where maximal independent sets always dominate.
- **Questions.** (a) Characterise FSGs admitting one. (b) **Conjecture P3.1:** deciding existence is NP-complete already for $m=2$. (c) Does the domination chain $ir\le\gamma\le i\le\beta\le\Gamma\le IR$ (Cockayne–Hedetniemi–Miller [R]) have a simultaneous analogue on the class where all six parameters are defined?
- **Novelty.** Not found for FSGs. The crisp factor-domination literature should be checked for "independent factor domination".
- **Strategy.** NP-hardness via reduction from exact cover or from independent dominating set in a gadget where layer 2 forces independence constraints. Sufficient condition: a common perfect code.
- **Validation.** Enumerate all pairs of connected spanning subgraphs for $n\le7$ and tabulate the existence frequency.
- **Difficulty 3. Feasibility high. Potential:** good; a counterexample-driven paper that referees find convincing.

---

#### P4. $k$-of-$m$ robust domination and parameter reducts

- **Definitions.** $D$ is **$(k,m)$-dominating** if every $v\notin D$ has a neighbour in $D$ in at least $k$ of the graphs $S_e$; $\gamma_k$ is the minimum size ($\gamma_m=\gamma_{\mathrm{sim}}$; $\gamma_1=\gamma(\bigcup_eS_e)$). A **$\gamma$-reduct** is a minimal $B\subseteq A$ with $\gamma_{\mathrm{sim}}(\tilde G|_B)=\gamma_{\mathrm{sim}}(\tilde G)$.
- **Questions.** (a) Is $k\mapsto\gamma_k$ convex, or can its increments be arbitrary non-negative integers? (b) Complexity of finding a minimum $\gamma$-reduct. **Conjecture P4.1:** it is $\Sigma_2^p$-hard in general and NP-hard even when domination numbers are given by an oracle. (c) Relationship between $\gamma$-reducts and classical soft-set parameter reducts (Chen et al. 2005 [R]).
- **Novelty.** Parameter reduction has not been connected to graph invariants of FSGs in anything I found.
- **Strategy.** $\gamma_1\le\dots\le\gamma_m$ is immediate; build gadget families realising prescribed increment sequences; reduce hitting set to reduct computation.
- **Validation.** Small-case enumeration; ILP formulations $\sum_e y_{v,e}\ge k(1-x_v)$, $y_{v,e}\le\sum_{u\in N_e(v)}x_u$.
- **Difficulty 3–4. Feasibility medium–high. Potential:** strong link to decision-support (which criteria matter for coverage).

---

#### P5. Parameterized complexity of simultaneous domination

- **Setting.** Input size $O(m(n+|E|))$.
- **Facts.** NP-hard for $m=1$. Polynomial when $G^{*}$ is a tree (all layers coincide by Lemma 2.1).
- **Questions.** (a) Show fixed-parameter tractability in $\mathrm{tw}(G^{*})+m$ by dynamic programming with per-vertex states "in $D$" or "set of layers in which already dominated" (expected running time $(2^m+1)^{O(\mathrm{tw})}\,\mathrm{poly}$; to be proved). (b) **Question P5.1:** is the problem W[1]-hard parameterised by treewidth alone when $m$ is part of the input? (c) Approximation: is the greedy $O(\log(nm))$ ratio tight?
- **Novelty.** No complexity result of any kind was found for FSGs.
- **Strategy.** Standard tree-decomposition DP; hardness via multicoloured clique with one layer per colour pair; set-cover reduction for inapproximability.
- **Validation.** Implement the DP and compare with ILP on cactus and series–parallel hosts.
- **Difficulty 4. Feasibility medium (needs algorithmic background). Potential:** Theoretical Computer Science / Algorithmica-adjacent venues, or Discrete Applied Mathematics.

---

#### P6. Consensus connectivity and the consensus gap

- **Definition.** $\Delta(x,y)=\min_{e}\mathrm{CONN}_e(x,y)-\mathrm{CONN}_\wedge(x,y)$ and $\Delta(\tilde G)=\sum_{x<y}\Delta(x,y)$.
- **Proved here.**
  1. $\Delta(x,y)\ge0$ (for every path $P$, $\min_es_e(P)\le\mathrm{CONN}_e$).
  2. **Example 6.1** ($\Delta>0$). On the 4‑cycle $abcd$ let $\mu_1=(1,1,1,\tfrac12)$ and $\mu_2=(\tfrac12,1,1,1)$ on $(ab,bc,cd,da)$. Then $\mathrm{CONN}_1(a,b)=\mathrm{CONN}_2(a,b)=1$ but $\mathrm{CONN}_\wedge(a,b)=\tfrac12$.
  3. If all layers share a common maximum spanning tree, then $\Delta\equiv0$.
  4. **Example 6.2** (the converse fails). On a triangle let $\mu_1=(1,0.9,0.8)$ and $\mu_2=(0.1,0.2,0.3)$ on $(xy,yz,xz)$. Then $\mu_\wedge=\mu_2$ and $\Delta\equiv0$, but the unique maximum spanning trees are $\lbrace xy,yz\rbrace$ and $\lbrace yz,xz\rbrace$.
  5. Pointwise: $\Delta(x,y)=0$ iff $x,y$ are connected in the crisp graph $\lbrace uv:\mu_e(uv)\ge t\ \forall e\rbrace$ with $t=\min_e\mathrm{CONN}_e(x,y)$. Hence $\Delta$ is computable in polynomial time.
  6. **Proposition 6.3** ($m=2$). $\sup\Delta(x,y)=1$ simultaneously for all pairs is approached on $G^{*}$ iff $G^{*}$ has two edge-disjoint spanning trees. (Take $\mu_i=1$ on $T_i$ and $\varepsilon$ elsewhere; conversely the high-weight spanning trees of the two layers cannot share an edge.)
  7. **Remark 6.4.** For $m=3$ the triangle already achieves gap $1-\varepsilon$ on all pairs, though it has no two edge-disjoint spanning trees. A bridge of $G^{*}$ lies in every spanning tree, so its endpoints always have gap near 0 in the extremal regime.
- **Questions.** (a) Characterise $\Delta\equiv0$ structurally (it is strictly weaker than a common maximum spanning tree). (b) Define $\tau(G^{*})$ as the least number of spanning trees of $G^{*}$ with empty common intersection; this is the least $m$ for which the gap can approach 1 on every pair. Then $\tau=2$ iff two edge-disjoint spanning trees exist, $\tau=\infty$ iff $G^{*}$ has a bridge, and $\tau(C_n)=n$ (each spanning tree of a cycle omits one edge), so $\tau$ is unbounded on bridgeless graphs. **Observation:** the complements of spanning trees are the bases of the cographic matroid $M^{*}(G^{*})$, so $\tau(G^{*})$ is its covering number, and Edmonds' matroid covering theorem [R] gives $\tau(G^{*})=\max_{\emptyset\ne X\subseteq E}\lceil |X|/r^{*}(X)\rceil$ with $r^{*}(X)=|X|-r(E)+r(E\setminus X)$. The formula should be re-derived carefully in the manuscript; the open part is its graph-theoretic interpretation and the non-extremal regime in (c). (c) For $m<\tau(G^{*})$, determine $\sup\Delta(\tilde G)$ over FSGs on $G^{*}$ with $m$ parameters (how many pairs can have gap near 1), in terms of tree-packing data (Nash‑Williams–Tutte [R]).
- **Novelty.** Connectivity in FSGs is treated only layer-wise in what I found (items 7, 9). The meet-layer comparison was not found.
- **Strategy.** Maximum-spanning-tree exchange arguments; matroid union for (b) and (c).
- **Validation.** `verify_examples.py` checks items 2, 4 and Remark 6.4. Exhaustive computation of $\tau$ and of the $m<\tau$ suprema for $n\le8$.
- **Difficulty 3. Feasibility high. Potential:** high; clean statements, classical tools, a real application reading (Section 6).

---

#### P7. Coupled connectivity and Wiener-type indices

- **Definitions.** Consensus connectivity index $CI_\wedge(\tilde G)=\sum_{x<y}\sigma_\wedge(x)\sigma_\wedge(y)\mathrm{CONN}_\wedge(x,y)$, and layer indices $CI_e$ as in Binu–Mathew–Mordeson [R]. Analogous Wiener index using strong geodesics common to all layers.
- **Questions.** (a) Sharp inequalities between $CI_\wedge$ and $\min_eCI_e$, with equality characterised via P6. (b) Extremal FSGs for $CI_\wedge$ on a fixed host with prescribed layer indices. (c) Behaviour under Cartesian, tensor and lexicographic products of FSGs (the product layers were defined by Shashikala–Anil [V]). (d) Parameter criticality: classify $e\in A$ as *index-reducing, neutral* according to $CI_\wedge(\tilde G|_{A-e})$ versus $CI_\wedge(\tilde G)$, mirroring connectivity-enhancing/reducing nodes for fuzzy graphs.
- **Novelty.** Only degree-based FSG indices were found (items 19–20). Connectivity-based ones were not.
- **Strategy.** $CI_\wedge\le\min_eCI_e$ always holds (since $\sigma_\wedge\le\sigma_e$ and $\mathrm{CONN}_\wedge\le\mathrm{CONN}_e$); equality needs one layer that is minimal on every pair, which is stronger than $\Delta\equiv0$. Product formulae via $\mathrm{CONN}$ in products of fuzzy graphs.
- **Validation.** Compute on real multiplex transport data (Section 6.2).
- **Difficulty 2–3. Feasibility high. Potential:** medium–high (Information Sciences published the degree-based analogue).

---

#### P8. All-layer separators and vulnerability

- **Definitions.** $X\subseteq V$ is an **all-layer separator** if $S_e-X$ is disconnected (or trivial) for every $e$; $\kappa_\forall$ is the minimum size. $\kappa_\exists=\min_e\kappa(S_e)$.
- **Proved here.** $\max_e\kappa(S_e)\le\kappa_\forall\le\kappa(\bigcup_eS_e)$.
- **Questions.** (a) Complexity of $\kappa_\forall$. **Conjecture P8.1:** NP-hard for $m=2$ (each layer may be separated along a different cut, so no single max-flow certificate applies). (b) A Menger/Whitney-type inequality: relate $\kappa_\forall$, the analogous edge parameter, and minimum simultaneous degree. (c) Fuzzy weighting: minimise $\sum_{v\in X}\max_e\sigma_e(v)$.
- **Novelty.** Not found for FSGs; related notions exist for multilayer networks and must be cited.
- **Strategy.** Hardness from vertex cover via layers that are stars-plus-paths; ILP with one cut-indicator system per layer.
- **Validation.** Random and real multiplex instances; compare $\kappa_\forall$ with both bounds.
- **Difficulty 4. Feasibility medium. Potential:** high for cybersecurity/infrastructure framing.

---

#### P9. A bottleneck/sum dichotomy for robust optimisation on FSGs

- **Setting.** Read parameters as scenarios or criteria. For a combinatorial family $\mathcal F$ of edge sets (paths $x$–$y$, spanning trees, perfect matchings), compare
  - **bottleneck–maximin:** $\max_{F\in\mathcal F}\min_{e\in A}\min_{uv\in F}\mu_e(uv)$;
  - **sum–maximin:** $\max_{F\in\mathcal F}\min_{e\in A}\sum_{uv\in F}\mu_e(uv)$.
- **Theorem 9.1. Proved here.** The bottleneck–maximin problem on $\tilde G$ equals the bottleneck problem on the single fuzzy graph $\mu_\wedge$, because the two minima commute. Hence it is polynomial whenever the single-layer bottleneck problem is (paths, spanning trees, matchings).
- **Contrast [R].** The sum versions with two or more discrete scenarios are NP-hard for shortest path and assignment (Kouvelis–Yu; Yu–Yang).
- **Questions.** (a) Map the frontier between these extremes for objectives built from continuous Archimedean t‑norms (product, Łukasiewicz) in place of $\min$ along a path: **Conjecture P9.1:** maximin strongest path is NP-hard for the product t‑norm with $m=2$ (it is a two-scenario shortest path after taking logarithms, so this should follow from [R]; the proof must handle the restriction to weights in $(0,1]$). (b) For Sugeno–Weber or nilpotent t‑norms, where path strength saturates at 0, is there a pseudo-polynomial algorithm? (c) Ordered weighted averaging across parameters: complexity as a function of the OWA weight vector.
- **Novelty.** No optimisation results for FSGs were found. The dichotomy explains *why* max–min semantics are computationally privileged, which is a publishable conceptual point.
- **Strategy.** Reductions from two-scenario robust shortest path; label-setting algorithms with Pareto pruning for small $m$.
- **Validation.** `verify_examples.py` brute-forces Theorem 9.1 on random instances. Benchmark Pareto label-setting against ILP on road networks with multi-criteria edge data.
- **Difficulty 3. Feasibility high. Potential:** high (Fuzzy Sets and Systems; European J. Oper. Res. if the t‑norm classification is complete).

---

#### P10. Energy deficit of a fuzzy soft graph

- **Definitions.** For a weight vector $w$ in the simplex, $A_w=\sum_ew_eA_e$ and $\delta_w(\tilde G)=\sum_ew_e\mathcal E(A_e)-\mathcal E(A_w)$.
- **Proved here.**
  1. $\delta_w\ge0$, since energy of a symmetric matrix is its nuclear norm.
  2. $\delta_w=0$ iff there is a symmetric $W$ with spectral norm $\le1$ and $\langle W,A_e\rangle=\mathcal E(A_e)$ for all $e$ with $w_e>0$ (dual-norm certificate).
  3. Per layer, $2\sqrt{\sum_{i<j}\mu_e(v_iv_j)^2}\le\mathcal E(A_e)\le\sqrt{2n\sum_{i<j}\mu_e(v_iv_j)^2}$. (The lower bound uses $\mathrm{tr}A_e=0$; the upper bound is the McClelland/Cauchy–Schwarz bound, known for fuzzy graphs.)
  4. Strictness: two layers each a single edge, $ab$ and $bc$, give $\mathcal E=2+2$ separately and $2\sqrt2$ for the sum.
  5. If the $A_e$ commute, then $\delta_w=0$ iff on every common eigenvector the eigenvalues of the layers in the support of $w$ have weakly the same sign. This can fail even for very regular layers: the two perfect matchings $\lbrace 01,23\rbrace$ and $\lbrace 12,30\rbrace$ of $C_4$ commute, each has energy 4, and their half-sum has energy 2.
- **Questions.** (a) Characterise $\delta_w=0$ combinatorially for FSGs (the certificate in 2 is analytic). For Cayley/circulant layers on an abelian group, item 5 turns this into a sign condition on character sums; classify the connection sets that satisfy it. (b) Sharp upper bound on $\delta_w$ in terms of $n$, $m$ and layer Frobenius norms; extremal FSGs. (c) Is $\delta$ a meaningful "disagreement among criteria" measure? Compare with the consensus gap of P6.
- **Novelty.** No FSG energy paper was found; energies exist for fuzzy graphs and (via singular values) for fuzzy soft sets. A paper that only lists layer energies would be separable in the sense of P1 and weak. The deficit is coupled.
- **Strategy.** Ky Fan inequalities; simultaneous diagonalisation; majorisation.
- **Validation.** Random FSGs (the script checks items 1 and 3 on 300 instances) and structured families (circulant layers commute, so everything is explicit).
- **Difficulty 3. Feasibility high. Potential:** MATCH / Linear Algebra Appl. for theory; Information Sciences with an application.

---

#### P11. Optimal parameter weighting for algebraic connectivity

- **Definition.** $L_w=\sum_ew_eL_e$; $a(w)=\lambda_2(L_w)$.
- **Proved here.** $a$ is concave on the simplex, so $a(w)\ge\sum_ew_e\lambda_2(L_e)$, and $\max_wa(w)$ is a convex (semidefinite) program. The maximum can strictly exceed every single layer: layers $\lbrace ab\rbrace$ and $\lbrace bc\rbrace$ on three vertices have $\lambda_2=0$, while $w=(\tfrac12,\tfrac12)$ gives $\lambda_2=\tfrac12$.
- **Questions.** (a) Closed forms for $w^{*}$ for structured families (two spanning trees; circulant layers). (b) Sparsity: bound the support size of an optimal $w^{*}$. **Question P11.1:** is there always an optimal $w^{*}$ whose support size is bounded by a function of the multiplicity $r$ of $\lambda_2(L_{w^{*}})$ alone (a Carathéodory-type argument on the optimality conditions suggests about $r(r+1)/2+1$; unproved)? (c) Interpretation of $w^{*}$ as data-driven criteria weights, replacing subjective weights in FSG decision models.
- **Novelty.** Not found for FSGs. Related: Ghosh–Boyd on growing well-connected graphs [R]; the multiplex-network literature on supra-Laplacians. Novelty lies in the FSG decision-making interpretation and the sparsity question.
- **Strategy.** SDP duality; subgradient of $\lambda_2$ is $\big(x^{\top}L_ex\big)_e$ for a Fiedler vector $x$.
- **Validation.** CVXPY experiments on multiplex datasets; compare rankings under $w^{*}$ and under uniform weights.
- **Difficulty 3. Feasibility high. Potential:** high; bridges theory and applications.

---

#### P12. Tensor spectral theory for FSGs

- **Definition.** $\mathcal A\in\mathbb R^{n\times n\times m}$ with frontal slices $A_e$. Candidate energies: sum of singular values of the mode‑3 unfolding; t‑product (tubal) nuclear norm; HOSVD core norms.
- **Questions.** Which tensor energy is (i) invariant under FSG isomorphism (vertex and parameter relabelling), (ii) coupled in the sense of P1, (iii) bounded by Koolen–Moulton-type inequalities? Note that the t‑product depends on parameter order, so it fails (i) unless parameters are cyclically ordered (which is natural for temporal FSGs only).
- **Novelty.** Not found.
- **Strategy.** Establish invariance first; then bounds via unfolding ranks.
- **Validation.** Numerical comparison of candidate energies as discriminators of non-isomorphic FSGs.
- **Difficulty 4. Feasibility medium. Potential:** medium; risk of being definitional unless a sharp theorem emerges.

---

#### P13. Multi-threshold and conflict-minimising colouring

- **Definitions.** For thresholds $\alpha=(\alpha_e)_{e\in A}$ let $G^{\alpha}=\bigcup_e\lbrace uv:\mu_e(uv)\ge\alpha_e\rbrace$ and $\chi(\alpha)=\chi(G^{\alpha})$. The **chromatic profile** is the monotone step function $\chi:[0,1]^m\to\mathbb N$. For $k$ colours, the **conflict cost** of $c:V\to[k]$ is $\max_e\sum_{c(u)=c(v)}\mu_e(uv)$.
- **Proved here.** $\max_e\chi_e(\alpha_e)\le\chi(\alpha)\le\prod_e\chi_e(\alpha_e)$ (product colouring).
- **Questions.** (a) Size of the Pareto frontier $\lbrace\alpha:\chi(\alpha)\le k\rbrace$: how many maximal elements can it have as a function of $n,m$? (b) Complexity and approximation of minimum conflict cost for fixed $k$ (a min–max multi-layer $k$-cut). (c) Which FSGs attain the product upper bound?
- **Novelty.** Existing FSG colouring (items 16–18) gives class values. The relation to *soft colouring* of Hamidizadeh et al. [V] must be checked from full text before claiming novelty; their notion unifies vertex, edge and hypergraph colouring and may overlap with (a).
- **Strategy.** Frontier size via antichains in the product of the layers' weight orders; SDP relaxations for (b).
- **Validation.** Frequency-assignment style instances (parameters = time slots or bands).
- **Difficulty 3. Feasibility medium–high. Potential:** medium–high.

---

#### P14. Metric dimension with vector-valued distances

- **Definitions.** $d_e$ = strong-geodesic distance in layer $e$. $W\subseteq V$ **resolves** $\tilde G$ if for all $x\ne y$ there are $w\in W$ and $e\in A$ with $d_e(x,w)\ne d_e(y,w)$; $\beta_\exists$ is the minimum size. The all-layer version requires $W$ to resolve each layer; $\beta_\forall$.
- **Proved here.** $\beta_\exists\le\min_e\beta(S_e)$ and $\max_e\beta(S_e)\le\beta_\forall\le\sum_e\beta(S_e)$.
- **Questions.** (a) How small can $\beta_\exists$ be relative to $\min_e\beta(S_e)$? Determine $\min\beta_\exists$ over two-parameter FSGs on $K_n$ whose layers both have metric dimension at least $k$. (b) Complexity of $\beta_\exists$. By Remark 2.3, generic layers are trees, whose metric dimension is known in closed form, so tree layers are the natural first case.
- **Novelty.** Not found for FSGs (metric dimension exists only in non-peer-reviewed fuzzy/neutrosophic preprints, per the search).
- **Difficulty 3. Feasibility medium. Potential:** medium; sensor/landmark placement applications.

---

#### P15. Isomorphism, automorphisms and enumeration

- **Definitions.** An isomorphism $\tilde G\to\tilde G'$ is a pair of bijections $(f:V\to V',\ \varphi:A\to A')$ with $\sigma'_{\varphi(e)}\circ f=\sigma_e$ and $\mu'_{\varphi(e)}(f(u)f(v))=\mu_e(uv)$. $\mathrm{Aut}(\tilde G)\le\mathrm{Aut}(G^{*})\times\mathrm{Sym}(A)$.
- **Questions.** (a) FSG isomorphism is GI-complete (expected to be routine: encode layers and weights by gadgets). (b) Which subgroups of $\mathrm{Aut}(G^{*})\times\mathrm{Sym}(A)$ arise? A Frucht-type theorem for FSGs. (c) Count FSGs with weights in a finite chain up to isomorphism (Pólya/Burnside).
- **Novelty.** No FSG isomorphism paper was found (weak/co-weak isomorphism exist for fuzzy and other variants).
- **Difficulty 2–3. Feasibility high. Potential:** medium; algebraic flavour.

---

#### P16. Axiomatics and stability of FSG decision rules

- **Setting.** The FSG decision procedures in the literature (Table 3.3) score alternatives from layer adjacency data and rank them. Model: alternatives $=V$, criteria $=A$, a rule $R$ maps $\tilde G$ to a weak order on $V$.
- **Questions.** (a) Characterise the standard "sum of memberships/choice value" rule by axioms (anonymity over parameters, neutrality over vertices, monotonicity, consistency under parameter-set union). (b) **Stability theorem to prove:** if $\lVert\mu_e-\mu'_e\rVert_\infty\le\varepsilon$ for all $e$, then a degree-sum rule preserves every strict preference whose score margin exceeds $2\varepsilon m(n-1)$. (This is immediate from the triangle inequality; the research question is the sharp constant for each rule and the analogous statement for spectral rules via Davis–Kahan.) (c) Rank reversal: which rules are immune to adding a dominated alternative?
- **Novelty.** No axiomatic or stability analysis was found among FSG decision papers.
- **Strategy.** Social-choice characterisation techniques (Young's axioms for scoring rules).
- **Validation.** Monte-Carlo perturbation of published numerical examples (which requires the full texts).
- **Difficulty 3. Feasibility high. Potential:** high in decision-science journals; raises the standard of the application literature.

---

#### P17. Fuzzy soft graph neural networks

- **Definition.** Layer update $h_v^{(t+1)}=\phi\Big(h_v^{(t)},\ \bigoplus_{e\in A}\rho_e\big(\bigotimes_{u\in N_e(v)}T(\mu_e(uv),\psi(h_u^{(t)}))\big)\Big)$ with $T$ a (learnable, parametric) t‑norm, $\bigotimes$ a permutation-invariant aggregator and $\bigoplus$ an aggregator over parameters with attention weights $w_e$.
- **Questions.** (a) Expressive power relative to the multiplex 1‑WL test; does max–min aggregation strictly reduce or change it? (b) Does sparsity regularisation on $w$ recover parameter reducts (P4)? (c) Does a bottleneck-aggregating network learn $\mathrm{CONN}_\wedge$ exactly (algorithmic alignment)?
- **Novelty.** Only definitions were found (inside arXiv surveys). Relational GCNs (Schlichtkrull et al. [R]) are the obvious baseline and cover the crisp multi-relational case; novelty must come from fuzzy aggregators and the theory in (a)–(c).
- **Validation.** Node classification and link prediction on multiplex benchmarks; ablate t‑norms; compare with R‑GCN and multiplex GAT baselines.
- **Difficulty 4. Feasibility medium (needs ML engineering). Potential:** high visibility, high competition.

---

#### P18. Random fuzzy soft graphs

- **Model.** $\mathcal G(n,m,F)$: host $K_n$; $\mu_e(uv)$ i.i.d. with distribution $F$ on $[0,1]$, independent across $e$.
- **Questions.** (a) By Remark 2.3, for continuous $F$ each $S_e$ is almost surely the maximum spanning tree of its layer, so $\gamma_{\mathrm{sim}}$ is the simultaneous domination number of $m$ independent random minimum-spanning-tree-type trees of $K_n$, and it is linear in $n$. **Conjecture P18.1:** $\gamma_{\mathrm{sim}}/n\to c_m$ almost surely, with $c_m$ strictly increasing in $m$. For discrete $F$ (ties), determine the density of $S_e$. (b) Distribution of the consensus gap: for continuous $F$, show $\mathrm{CONN}_\wedge$ and $\min_e\mathrm{CONN}_e$ concentrate and find the limit of their difference. (c) Threshold for existence of simultaneous independent dominating sets (P3).
- **Novelty.** Not found; a 2020s paper on topological indices of "fuzzy random graphs" exists [V‑] but not for FSGs.
- **Strategy.** $\mathrm{CONN}$ in a weighted complete graph is governed by the connectivity threshold of $G(n,p)$: $\mathrm{CONN}_e\approx F^{-1}(1-\log n/n)$; for the meet layer replace $F$ by the distribution of the minimum of $m$ copies.
- **Validation.** Simulation to $n=10^4$.
- **Difficulty 4. Feasibility medium. Potential:** medium–high; gives null models for the applications.

---

### 5.4 Summary table

| # | Problem | Coupled? | Difficulty | Feasibility | Novelty confidence* | Publication potential |
|---|---|---|---|---|---|---|
| P1 | Separability audit | meta | 2 | High | Medium–high | Medium |
| P2 | Simultaneous domination | Yes | 3 | High | Medium (thesis unread) | High |
| P3 | Independent version: existence | Yes | 3 | High | Medium | High |
| P4 | $k$-of-$m$ domination, reducts | Yes | 3–4 | Medium–high | Medium–high | High |
| P5 | Parameterized complexity | Yes | 4 | Medium | High | High |
| P6 | Consensus gap | Yes | 3 | High | Medium–high | High |
| P7 | Coupled indices | Yes | 2–3 | High | Medium–high | Medium–high |
| P8 | All-layer separators | Yes | 4 | Medium | Medium | High |
| P9 | Bottleneck/sum dichotomy | Yes | 3 | High | Medium–high | High |
| P10 | Energy deficit | Yes | 3 | High | Medium–high | High |
| P11 | Optimal weighting, $\lambda_2$ | Yes | 3 | High | Medium | High |
| P12 | Tensor spectra | Yes | 4 | Medium | Medium | Medium |
| P13 | Multi-threshold colouring | Yes | 3 | Medium–high | Medium (check soft colouring) | Medium–high |
| P14 | Metric dimension | Yes | 3 | Medium | Medium–high | Medium |
| P15 | Isomorphism/enumeration | n/a | 2–3 | High | Medium | Medium |
| P16 | Decision-rule axiomatics | n/a | 3 | High | Medium–high | High |
| P17 | FS‑GNN | Yes | 4 | Medium | Medium | High, competitive |
| P18 | Random FSGs | Yes | 4 | Medium | High | Medium–high |

\*Confidence that the problem is unpublished, given only web-search evidence. None is "certain".

---

## 6. Sector-wise applications (Step 6)

In every sector the modelling step is the same: vertices are entities, **parameters are criteria, scenarios, time windows or expert opinions**, and $\mu_e(uv)$ grades the relation $uv$ under $e$. What changes is which coupled invariant answers the sector's question. Dataset names are from memory [R]; confirm availability and licences.

| Sector | Model | Formulation | Solution method | Validation |
|---|---|---|---|---|
| **Healthcare** | $V$ = hospitals/clinics; $A$ = specialties or emergency types; $\mu_e(uv)$ = graded ability of $u$ to serve $v$'s catchment for $e$ (travel time, capacity) | Facility coverage for all specialties: $\gamma_{\mathrm{sim}}$ (P2); "at least $k$ specialties": $\gamma_k$ (P4); which specialties drive cost: $\gamma$-reducts | ILP; FPT dynamic programming on road-network tree decompositions (P5) | Compare with per-specialty planning; sensitivity to membership perturbation (P16). Data: open hospital-location and travel-time data; MIMIC-type clinical data are access-controlled |
| **Transportation** | $V$ = stations; $A$ = modes or time-of-day/weather scenarios; $\mu_e$ = reliability of a link | Most reliable route under every scenario = bottleneck–maximin path (Theorem 9.1, polynomial); additive travel-time robustness is NP-hard (P9) | Widest-path on $\mu_\wedge$; Pareto label-setting for sum objectives | Multiplex transport networks (e.g., the London multiplex, European air-transport multiplex [R]); report consensus gap $\Delta$ (P6) as a measure of how much reliability is lost by requiring one route for all scenarios |
| **Cybersecurity** | $V$ = hosts; $A$ = protocols/privilege levels/attack classes; $\mu_e$ = exploitability or trust | Smallest host set whose removal disconnects every layer: $\kappa_\forall$ (P8); monitor placement: $\gamma_{\mathrm{sim}}$ or $\beta_\exists$ (P14) | ILP; greedy with approximation guarantee (P5c) | Attack-graph corpora and intrusion datasets (e.g., CIC‑IDS2017 [R]) converted to host graphs; compare against single-layer baselines |
| **Social networks** | $V$ = users; $A$ = relation types or platforms | Influence that holds across all relation types: paths in $\mu_\wedge$; community robustness: energy deficit $\delta_w$ and optimal $w^{*}$ (P10, P11); learning: FS‑GNN (P17) | Spectral clustering on $L_{w^{*}}$; GNN training | Multiplex social datasets (e.g., CS‑Aarhus [R]); metrics: NMI/ARI against ground truth, link-prediction AUC |
| **Finance** | $V$ = institutions/assets; $A$ = exposure types or market regimes; $\mu_e$ = normalised exposure or tail dependence | Contagion channels that persist across regimes: $\mathrm{CONN}_\wedge$; systemic nodes: all-layer separators (P8); regime-weighting that maximises/minimises connectivity (P11) | Max–min closure; SDP | Public interbank/trade multiplex data (e.g., FAO trade multiplex [R]); backtest systemic-importance rankings against realised stress events |
| **Environmental systems** | $V$ = monitoring sites/habitat patches; $A$ = pollutants or species; $\mu_e$ = transport/dispersal strength | Sensor placement resolving all pollutants: $\beta_\exists$, $\gamma_{\mathrm{sim}}$; corridor design robust across species: bottleneck–maximin spanning tree (P9) | Polynomial for bottleneck objectives | River-network and air-quality monitoring data; hold-out prediction error at unmonitored sites |
| **Decision-support** | $V$ = alternatives; $A$ = criteria/experts; digraph layers of graded preference | Ranking rules with proven stability margins (P16); data-driven criteria weights $w^{*}$ (P11); criteria reduction (P4) | Scoring rules; SDP | Re-run published FSG decision examples; report stability radius and rank-reversal behaviour, which existing papers do not report |

**Experimental protocol common to all sectors.** (1) State how memberships are obtained from data (normalisation formula), since results depend on it; (2) compare against the single-layer aggregate (average layer) and against per-layer analysis; (3) report sensitivity to $\pm\varepsilon$ perturbations of $\mu$; (4) use a random FSG null model (P18) to judge whether an observed value is unusual.

---

## 7. Execution roadmap for the top five (Step 7)

### 7.1 Ranking

Scores are 1–5. "Alignment" is provisional because Step 1 is missing; it is scored against a generic fuzzy soft graph background.

| Rank | Problem(s) | Originality | Depth | Feasibility | Alignment (provisional) | Total |
|---|---|---|---|---|---|---|
| 1 | **P2 + P3** Simultaneous domination and existence of independent versions | 4 | 4 | 5 | 5 | 18 |
| 2 | **P6 (+P7)** Consensus gap and coupled connectivity indices | 4 | 4 | 5 | 4 | 17 |
| 3 | **P10 + P11** Energy deficit and optimal parameter weighting | 4 | 4 | 4 | 4 | 16 |
| 4 | **P9** Bottleneck/sum dichotomy | 4 | 3 | 5 | 3 | 15 |
| 5 | **P16** Axiomatics and stability of decision rules | 4 | 3 | 5 | 3 | 15 |

P1 is not ranked as a separate paper; it is the framing that the introduction of each paper should use. P5, P8 and P17 are stronger in principle but need algorithmic or ML expertise I cannot presume.

### 7.2 Rank 1: simultaneous domination (P2 + P3)

- **Methodology.** Reduce to tuples of connected spanning subgraphs (Corollary 2.2); solve extremal questions host by host; then complexity.
- **Initial lemmas (proved in this report).** Lemma 2.1; Corollary 2.2; the bounds in P2; Example 3.1.
- **Candidate theorems (to prove).**
  - T1. Exact $\Gamma_m(C_n)$ for all $m,n$. (Layers are $C_n$ or Hamiltonian paths of $C_n$; expect $\lceil n/3\rceil$ plus a correction bounded by the number of distinct deleted edges.)
  - T2. Bounds $c\,n\le\Gamma_2(K_n)\le C\,n$ with explicit constants; lower bound via two "comb-like" spanning trees with complementary leaf structure.
  - T3. NP-completeness of the existence problem in P3 for $m=2$.
  - T4. A sufficient condition for existence: the layers admit a common efficient dominating set.
- **Proof directions.** T1 by a discharging/covering count on the cycle. T2 lower bound: a set dominating a spanning tree must hit every closed neighbourhood of its leaves' supports; choose two trees whose support-vertex sets are disjoint. T3 from 3‑SAT with a variable gadget in layer 1 and a clause gadget in layer 2.
- **Computational experiments.** Extend `verify_examples.py`: enumerate all pairs/triples of connected spanning subgraphs of small hosts; tabulate $\Gamma_m$; ILP (e.g., OR‑Tools) to $n\approx200$.
- **Datasets and metrics.** Multiplex transport/healthcare coverage instances; metrics: $\gamma_{\mathrm{sim}}/\max_e\gamma_e$ (price of simultaneity), run time, optimality gap of greedy.
- **90-day plan.**

| Days | Work | Deliverable |
|---|---|---|
| 1–10 | Read Hussain–Hussain 2017, the Rajeevan thesis, Karbasioun–Ameri 2021, Brigham–Dutton 1990 and its citing papers; fix definitions | Two-page novelty memo; go/no-go |
| 11–30 | Prove T1; computational tables for small hosts | Section draft + data |
| 31–50 | T2 bounds; T4 | Section draft |
| 51–70 | T3 hardness proof; ILP experiments | Section draft + plots |
| 71–85 | Application case study (coverage) | Section draft |
| 86–90 | Assemble and internally review | Submission-ready manuscript |

### 7.3 Rank 2: consensus gap (P6 + P7)

- **Initial lemmas (proved here).** Items 1–5 of P6; Proposition 6.3; Remark 6.4.
- **Candidate theorems.** T1. Structural characterisation of $\Delta\equiv0$ (target form: for every threshold $t$, the components of $\lbrace\mu_\wedge\ge t\rbrace$ coincide with the common refinement of components of $\lbrace\mu_e\ge t\rbrace$ restricted appropriately; to be made precise). T2. $\tau(G^{*})$ via the cographic covering number, with a graph-theoretic reading, and the suprema for $m<\tau$. T3. $CI_\wedge\le\min_eCI_e$ with a characterisation of equality. T4. Product formulae for $\mathrm{CONN}_\wedge$ under Cartesian products.
- **Proof directions.** Threshold-graph (level-set) calculus: every statement about $\mathrm{CONN}$ is a statement about components of level graphs, which converts T1 into lattice statements about partitions. T2 via Edmonds' covering theorem and matroid union.
- **Experiments.** All-pairs $\Delta$ by Floyd–Warshall max–min closure (already implemented); $\tau$ by exhaustive search for $n\le8$, then SAT/ILP.
- **Datasets and metrics.** Multiplex transport; metrics: mean gap, fraction of zero-gap pairs, gap versus number of layers.
- **90-day plan.** Days 1–10 literature check (multilayer "path-based" connectivity; tree packing/covering for $\tau$); 11–35 T1 and T3; 36–55 T2 and the $m<\tau$ regime; 56–70 T4 and indices; 71–85 data study; 86–90 assembly.

### 7.4 Rank 3: spectral coupling (P10 + P11)

- **Initial lemmas (proved here).** Items 1–5 of P10; concavity and the strict-improvement example in P11.
- **Candidate theorems.** T1. Combinatorial conditions for $\delta_w=0$, starting from commuting (Cayley) layers. T2. Sharp bound $\delta_w\le f(n,m)\max_e\lVert A_e\rVert_F$ and extremal FSGs. T3. Closed-form $w^{*}$ for two-tree and circulant families. T4. Support bound for $w^{*}$ (Question P11.1).
- **Proof directions.** T1: common eigenbasis plus sign agreement gives a certificate $W=\sum\mathrm{sgn}(\lambda_i)x_ix_i^{\top}$. T2: Ky Fan norm inequalities; equality cases from orthogonal supports. T4: optimality conditions of the SDP; rank of the dual certificate.
- **Experiments.** CVXPY for $w^{*}$; random and real multiplex layers; compare $\delta$ with $\Delta$ of P6 as disagreement measures.
- **Metrics.** $\delta_w/\sum w_e\mathcal E(A_e)$; $\lambda_2(L_{w^{*}})/\max_e\lambda_2(L_e)$; support size of $w^{*}$; clustering quality using $L_{w^{*}}$.
- **90-day plan.** Days 1–10 literature (fuzzy graph energy; multiplex supra-Laplacian; Laplacian weight optimisation); 11–30 T1; 31–50 T2; 51–65 T3; 66–78 T4 or its refutation; 79–90 experiments and writing.

### 7.5 Rank 4: dichotomy (P9)

- **Initial lemma (proved here).** Theorem 9.1.
- **Candidate theorems.** T1. NP-hardness of maximin strongest path under the product t‑norm, $m=2$. T2. Classification for continuous Archimedean t‑norms: strict ⇒ NP-hard; nilpotent ⇒ status to be determined. T3. FPT/pseudo-polynomial algorithm when weights come from a chain of size $q$.
- **Proof directions.** Logarithmic transformation to two-scenario shortest path [R]; for T3, dynamic programming over $q^{m}$ strength vectors.
- **Experiments.** Road networks with multi-criteria reliabilities; Pareto label-setting versus ILP.
- **90-day plan.** Days 1–10 literature (robust and multi-objective shortest path); 11–30 T1; 31–55 T2; 56–70 T3 and code; 71–90 experiments and writing.

### 7.6 Rank 5: decision-rule theory (P16)

- **Initial lemma.** The $2\varepsilon m(n-1)$ stability margin (immediate).
- **Candidate theorems.** T1. Axiomatic characterisation of the choice-value rule. T2. Sharp stability radius for degree, closeness-type and spectral (Perron vector) rules. T3. Rank-reversal classification.
- **Experiments.** Re-analyse numerical examples from the FSG decision papers of Table 3.3 (needs their full texts); Monte-Carlo perturbations.
- **Metrics.** Stability radius; Kendall $\tau$ under perturbation; frequency of rank reversal.
- **90-day plan.** Days 1–15 collect and encode published examples; 16–40 T1; 41–60 T2; 61–75 T3; 76–90 experiments and writing.

---

## 8. Publication strategy (Step 8)

### 8.1 Journal targets

Check current indexing and scope on each journal's site before submitting; indexing status changes, and I could not verify it in this session.

| Paper | First choice | Realistic alternatives |
|---|---|---|
| P2+P3 | Discrete Applied Mathematics; Fuzzy Sets and Systems | Discrete Mathematics, Algorithms and Applications; AKCE Int. J. Graphs Comb.; J. Appl. Math. Comput. |
| P6+P7 | Fuzzy Sets and Systems; Information Sciences | Int. J. Fuzzy Systems; Comput. Appl. Math.; Soft Computing |
| P10+P11 | Linear Algebra and its Applications (theory-heavy version); Information Sciences (with application) | MATCH Commun. Math. Comput. Chem.; Comput. Appl. Math. |
| P9 | Fuzzy Sets and Systems; European J. Oper. Res. (if classification is complete) | Networks; Soft Computing; Fuzzy Optim. Decis. Mak. |
| P16 | Fuzzy Optim. Decis. Mak.; Information Sciences | Expert Systems with Applications; Applied Soft Computing; Granular Computing |
| P5, P8 | Discrete Applied Mathematics; Theoretical Computer Science | J. Comb. Optim. |
| P17 | IEEE Trans. Fuzzy Systems | Neural Networks; Knowledge-Based Systems |

The existing FSG literature sits largely in mid-tier venues, with exceptions in Information Sciences, Applied Soft Computing and Scientific Reports. Coupled-invariant results with real proofs are a credible route into the first-choice column.

### 8.2 Working titles

1. *Simultaneous domination in fuzzy soft graphs: realisability, extremal values and complexity*
2. *When do criteria agree? The consensus gap of a fuzzy soft graph*
3. *Energy deficit and optimal parameter weighting in fuzzy soft graphs*
4. *Max–min is easy, sum is hard: robust optimisation on fuzzy soft graphs*
5. *Stability and axioms for decision rules on fuzzy soft graphs*
6. *What is soft about fuzzy soft graphs? Separable and coupled invariants* (short note or thesis chapter)

### 8.3 A coherent multi-paper programme

**Thesis statement:** *the mathematical content of fuzzy soft graph theory lies in invariants that couple parameters; these invariants are computable or provably hard in ways determined by max–min semantics, and they answer robust multi-criteria questions that layer-wise analysis cannot.*

| Phase | Months | Papers | Dependency |
|---|---|---|---|
| Foundations | 0–3 | P1 note; literature audit from full texts | none |
| Combinatorial core | 3–9 | P2+P3; P6+P7 | Lemma 2.1; level-set calculus |
| Spectral and optimisation | 9–15 | P10+P11; P9 | P6 (for comparison of disagreement measures) |
| Algorithms and decisions | 15–21 | P5 or P8; P16 | P2, P11 |
| Outlook | 21–24 | P18 or P17; thesis writing | all |

Connected projects: an open-source Python package for FSGs (data structure, max–min closure, strong arcs, coupled invariants, ILP models) grown from `experiments/verify_examples.py`; a curated benchmark of FSGs built from multiplex datasets with documented membership constructions.

### 8.4 Before any submission

1. Obtain and read items 13–18 of Table 3.2 and the Rajeevan thesis (domination, colouring).
2. Search Scopus, Web of Science, MathSciNet and zbMATH for each working title's key phrase and for the multilayer-network equivalents ("multiplex domination", "simultaneous domination", "factor domination", "multilayer connectivity").
3. Confirm every [R] and [V‑] reference against the publisher record.
4. Reconcile definitions (strong-arc domination versus other conventions; scalar cardinality versus counting) with those already used for FSGs so that results are comparable.

---

## 9. Reproducibility

`experiments/verify_examples.py` (Python 3, NumPy) checks, by brute force or on random instances: Lemma 2.1 (300 random hosts); Remark 2.3 (200 random layers); $\tau(C_n)=n$ for $n\le6$; item 5 of P10; Examples 3.1, 6.1, 6.2; Remark 6.4; the bounds in P2 (200 random layer families); items 1, 3, 4 of P10 and the concavity claim of P11 (300 random FSGs); the example in P11; Theorem 9.1 (100 random instances). It prints `all checks passed`. These checks support the small claims marked "Proved here"; they are not evidence for any conjecture.

---

## 10. References

Tags as in Section 0. Entries marked [R] were not re-verified in this session.

**Fuzzy soft graphs and variants**

1. M. Akram, S. Nawaz. On fuzzy soft graphs. *Ital. J. Pure Appl. Math.* 34 (2015) 497–514. https://ijpam.uniud.it/online_issue/201534/44-AkramNawaz.pdf [V]
2. S. Mohinta, T. K. Samanta. An introduction to fuzzy soft graph. *Mathematica Moravica* 19(2) (2015) 35–48. doi:10.5937/matmor1502035m [V]
3. M. Akram, S. Nawaz. Fuzzy soft graphs with applications. *J. Intell. Fuzzy Syst.* 30(6) (2016) 3619–3632. doi:10.3233/IFS-162107 [V]
4. A. Al‑Masarwah, M. Abu Qamar. Some new concepts of fuzzy soft graphs. *Fuzzy Inf. Eng.* 8(4) (2016) 427–438. doi:10.1016/j.fiae.2017.01.003 [V]
5. A. Al‑Masarwah, M. Abu Qamar. Certain types of fuzzy soft graphs. *New Math. Nat. Comput.* 14(2) (2018) 145–156. doi:10.1142/S1793005718500102 [V]
6. Çelik. Some operations on fuzzy soft graphs. *AIP Conf. Proc.* (2017). doi:10.1063/1.4981678 [V‑: given name, volume]
7. M. Akram, F. Zafar. Fuzzy soft trees. *Southeast Asian Bull. Math.* (2017). [V‑: volume, pages]
8. M. Akram, F. Zafar. *Hybrid Soft Computing Models Applied to Graph Theory.* Stud. Fuzziness Soft Comput. 380, Springer, 2020. doi:10.1007/978-3-030-16020-3 [V]
9. S. Shashikala, P. N. Anil. Connectivity in fuzzy soft graph and its complement. *IOSR J. Math.* 12(5) (2016) 95–99. [V]
10. S. Shashikala, P. N. Anil. Fuzzy soft cycles in fuzzy soft graphs. *J. New Results Sci.* 8(1) (2019) 26–35. [V]
11. S. Shashikala, P. N. Anil. Some studies on products of fuzzy soft graphs. *Ratio Mathematica* 41 (2021) 227–254. [V]
12. S. Shashikala, P. N. Anil. Study of different degrees based on various operations on fuzzy soft graphs. *Ital. J. Pure Appl. Math.* 47 (2022) 971–983. [V]
13. R. J. Hussain, S. S. Hussain. Domination in fuzzy soft graphs. *Int. J. Fuzzy Math. Arch.* 14(2) (2017) 243–252. doi:10.22457/ijfma.v14n2a8 [V]
14. R. Rajeevan. *Domination parameters in fuzzy soft graphs.* PhD thesis, University of Kerala, 2019. Shodhganga handle 10603/570786. [V‑: listing only]
15. A. Karbasioun, R. Ameri. Total and secure domination for corona product of two fuzzy soft graphs. *Fuzzy Inf. Eng.* (2021). doi:10.1080/16168658.2021.1915456 [V]
16. R. Jahir Hussain, S. Afya Farhana. Fuzzy chromatic number of fuzzy soft cycle and complete fuzzy soft graphs. *AIP Conf. Proc.* (2023). doi:10.1063/5.0114372 [V]
17. R. Jahir Hussain, S. Afya Farhana. Fuzzy dominator coloring on fuzzy soft graphs. *Ratio Mathematica* 48 (2023). doi:10.23755/rm.v48i0.1153 [V]
18. Bounds on fuzzy dominator chromatic number of fuzzy soft bipartite graphs. *Ratio Mathematica* (2023). [V‑: authors]
19. M. Azeem, S. Anwar, M. K. Jamil, M. Saeed, M. Deveci. Topological numbers of fuzzy soft graphs and their application. *Inf. Sci.* 667 (2024) 120468. doi:10.1016/j.ins.2024.120468 [V]
20. S. Anwar, M. Azeem, M. K. Jamil. Topological numbers of fuzzy soft graphs and their applications in globalizing the world by mutual trade. *Appl. Soft Comput.* 159 (2024) 111642. [V‑: DOI]
21. H. S. Nawaz, M. Akram. Oligopolistic competition among the wireless internet service providers of Malaysia using fuzzy soft graphs. *J. Appl. Math. Comput.* (2021/2022) 855–890. doi:10.1007/s12190-021-01514-z [V]
22. Decision-making methods based on fuzzy soft competition hypergraphs. *Complex Intell. Syst.* 8(3) (2022) 2325–2348. doi:10.1007/s40747-022-00646-4 [V‑: authors]
23. A fuzzy soft planar graph with application in image segmentation. *Sci. Rep.* (2025). doi:10.1038/s41598-025-02880-5 [V‑: authors]
24. Image contraction through fuzzy soft outerplanar graph structures. *Sci. Rep.* 16 (2026) 9779. https://www.nature.com/articles/s41598-026-37570-3 [V‑: authors]
25. U. Amin, A. Fahmi. Fuzzy soft graph structure with application. *Bol. Soc. Paran. Mat.* 43 (2025) 1–39. doi:10.5269/bspm.76660 [V]
26. U. Amin, A. Fahmi, N. Yaqoob, A. Farid, M. A. S. Hassan. Domination in bipolar fuzzy soft graphs. *J. Intell. Fuzzy Syst.* 46(3) (2024) 6369–6382. doi:10.3233/JIFS-236485 [V]
27. S. Shahzadi, M. Akram. Intuitionistic fuzzy soft graphs with applications. *J. Appl. Math. Comput.* 55 (2017) 369–392. [V‑: from a citing paper; DOI]
28. S. Shahzadi, M. Akram. Graphs in an intuitionistic fuzzy soft environment. *Axioms* 7(2) (2018) 20. doi:10.3390/axioms7020020 [V]
29. M. Akram, S. Shahzadi. Neutrosophic soft graphs with application. *J. Intell. Fuzzy Syst.* 32(1) (2017) 841–858. doi:10.3233/JIFS-16090 [V]
30. G. Shahzadi, M. Akram, B. Davvaz. Pythagorean fuzzy soft graphs with applications. *J. Intell. Fuzzy Syst.* 38(4) (2020) 4977–4991. doi:10.3233/JIFS-191610 [V; exact title wording to be confirmed]
31. M. Akram, G. Shahzadi. Decision-making approach based on Pythagorean Dombi fuzzy soft graphs. *Granul. Comput.* doi:10.1007/s41066-020-00224-4 [V]
32. H. S. Nawaz, M. Akram. Inter-specific competition among trees in Pythagorean fuzzy soft environment. *Complex Intell. Syst.* (2021). doi:10.1007/s40747-021-00470-2 [V]
33. P. Chellamani, D. Ajay, S. Broumi, T. A. A. Ligori. An approach to decision-making via picture fuzzy soft graphs. *Granul. Comput.* (2021). doi:10.1007/s41066-021-00282-2 [V]
34. S. Shahzadi, M. Sarwar, M. Akram. Decision-making approach with fuzzy type‑2 soft graphs. *J. Math.* (2020). doi:10.1155/2020/8872446 [V]
35. A new multiple criteria decision-making method based on bipolar fuzzy soft graphs. *Iran. J. Fuzzy Syst.* https://ijfs.usb.ac.ir/article_4116.html [V‑: authors, year]
36. Interval-valued fuzzy soft graphs. *Topol. Algebra Appl.* (2017). doi:10.1515/taa-2017-0004 [V‑: authors]
37. Representation of fuzzy hypersoft set in graphs. *Palestine J. Math.* 12(1) (2023) 836–847. [V‑: authors]
38. Spherical fuzzy soft competition graphs with application. (2025). doi:10.1007/s12190-024-02286-y [V‑: authors]
39. R. J. Hussain, S. S. Hussain, F. Smarandache. Domination number in neutrosophic soft graphs. *Neutrosophic Sets Syst.* (2019). [V‑: volume]

**Soft graphs**

40. R. K. Thumbakara, B. George. Soft graphs. *Gen. Math. Notes* 21(2) (2014) 75–86. [V‑: from citing papers]
41. M. Akram, S. Nawaz. Operations on soft graphs. *Fuzzy Inf. Eng.* 7 (2015) 423–449. doi:10.1016/j.fiae.2015.11.003 [V‑: DOI from a citing paper]
42. M. Akram, F. Zafar. On soft trees. *Bul. Acad. Ştiinţe Repub. Mold. Mat.* 2015, no. 2, 82–95. [V]
43. Thenge, Reddy, Jain. Adjacency and incidence matrix of a soft graph. *Commun. Math. Appl.* 11(1) (2020). [V]
44. K. Hamidizadeh, R. Manaviyat, S. Mirvakili, B. Davvaz. Application of soft sets to graph coloring. *Comput. Appl. Math.* 43 (2024) 214. doi:10.1007/s40314-024-02738-y [V]
45. J. Jose, B. George, R. K. Thumbakara. Soft graphs: a comprehensive survey. *New Math. Nat. Comput.* 21(3) (2025). [V‑: pages, DOI]

**Fuzzy graphs (background)**

46. Node connectivity and arc connectivity of a fuzzy graph. *Inf. Sci.* 180 (2010). doi:10.1016/j.ins.2009.10.006 [V; authors S. Mathew, M. S. Sunitha per [R]]
47. Generalized fuzzy graph connectivity parameters with application to human trafficking. *Mathematics* 8(3) (2020) 424. [V‑: authors]
48. S. R. Sharbaf, F. Fayazi. Laplacian energy of a fuzzy graph. *Iran. J. Math. Chem.* (2014). [V]
49. Energy of Pythagorean fuzzy graphs with applications. *Mathematics* 6(8) (2018) 136. doi:10.3390/math6080136 [V‑: authors]
50. O. T. Manjusha, M. S. Sunitha. Notes on domination in fuzzy graphs. *J. Intell. Fuzzy Syst.* 27 (2014). doi:10.3233/IFS-141277 [V]
51. R. Mahapatra, S. Samanta, M. Pal. Applications of edge colouring of fuzzy graphs. *Informatica* 31(2) (2020) 313–330. doi:10.15388/20-INFOR403 [V]
52. Strong domination index in fuzzy graphs. arXiv:2307.10409. [V‑: authors]
53. An edge-centric perspective of Roman domination in fuzzy graphs through strong neighborhoods. arXiv:2408.13260. [V‑: authors]
54. Enhancing link prediction with fuzzy graph attention networks and dynamic negative sampling. arXiv:2411.07482. [V‑: authors]
55. Surveys seen by title only: arXiv:2411.17411; arXiv:2602.21268; arXiv:2605.23936. [V‑: authors]

**Classical and methodological references (recalled, not re-verified)**

56. L. A. Zadeh. Fuzzy sets. *Inf. Control* 8 (1965) 338–353. [R]
57. A. Rosenfeld. Fuzzy graphs. In *Fuzzy Sets and Their Applications*, Academic Press, 1975, 77–95. [R]
58. D. Molodtsov. Soft set theory: first results. *Comput. Math. Appl.* 37 (1999) 19–31. [R]
59. P. K. Maji, R. Biswas, A. R. Roy. Fuzzy soft sets. *J. Fuzzy Math.* 9 (2001) 589–602. [R]
60. K. R. Bhutani, A. Rosenfeld. Strong arcs in fuzzy graphs. *Inf. Sci.* 152 (2003) 319–322. [R]
61. S. Mathew, M. S. Sunitha. Types of arcs in a fuzzy graph. *Inf. Sci.* 179 (2009) 1760–1768. [R]
62. A. Somasundaram, S. Somasundaram. Domination in fuzzy graphs I. *Pattern Recognit. Lett.* 19 (1998) 787–791. [R]
63. M. Binu, S. Mathew, J. N. Mordeson. Connectivity index of a fuzzy graph and its application to human trafficking. *Fuzzy Sets Syst.* 360 (2019) 117–136; Wiener index of a fuzzy graph and application to illegal immigration networks. *Fuzzy Sets Syst.* 384 (2020) 132–147. [R]
64. N. Anjali, S. Mathew. Energy of a fuzzy graph. *Ann. Fuzzy Math. Inform.* 6 (2013) 455–465. [R]
65. R. C. Brigham, R. D. Dutton. Factor domination in graphs. *Discrete Math.* 86 (1990) 127–136. [R]
66. E. J. Cockayne, S. T. Hedetniemi, D. J. Miller. Properties of hereditary hypergraphs and middle graphs. *Canad. Math. Bull.* 21 (1978) 461–468. [R]
67. P. Kouvelis, G. Yu. *Robust Discrete Optimization and Its Applications.* Kluwer, 1997. [R]
68. G. Yu, J. Yang. On the robust shortest path problem. *Comput. Oper. Res.* 25 (1998) 457–468. [R]
69. D. Chen, E. C. C. Tsang, D. S. Yeung, X. Wang. The parameterization reduction of soft sets and its applications. *Comput. Math. Appl.* 49 (2005) 757–763. [R]
70a. J. Edmonds. Minimum partition of a matroid into independent subsets. *J. Res. Nat. Bur. Standards* 69B (1965) 67–72. [R]
70. C. St. J. A. Nash‑Williams. Edge-disjoint spanning trees of finite graphs. *J. London Math. Soc.* 36 (1961) 445–450; W. T. Tutte, same journal, 221–230. [R]
71. A. Ghosh, S. Boyd. Growing well-connected graphs. *Proc. 45th IEEE CDC* (2006). [R]
72. M. Kivelä et al. Multilayer networks. *J. Complex Netw.* 2 (2014) 203–271. [R]
73. M. Schlichtkrull et al. Modeling relational data with graph convolutional networks. *ESWC* 2018. [R]
