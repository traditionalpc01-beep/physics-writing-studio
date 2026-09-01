# Provenance (auto-generated)

generated: 2026-07-21

- n_observation_rows: 657
- n_adversarial_rows: 30

- writing_rules.tsv: {'rows': 85, 'distilled_added': 25, 'prior_retained': 60}
- phrase_bank.tsv: {'rows': 134, 'distilled_added': 12, 'prior_retained': 122}
- anti_ai_patterns.tsv: {'rows': 135, 'distilled_added': 3, 'prior_retained': 132}
- domain_register.tsv: {'rows': 46, 'distilled_added': 24, 'prior_retained': 22}
- sentence_stats_by_domain.tsv: {'rows': 24}

### Deterministic AI distillation (v3, 412 unique papers)
- Source: MiniMax-M3 per-paper observation of .evidence_packet.md files (415 JSONL records, 412 unique DOIs)
- Driver: distillation/v2/scripts/deterministic_distill.py (LCS-based quote validation, ratio >= 0.5)
- Aggregator: distillation/v2/scripts/aggregate_deterministic.py
- Output: 5 TSVs (gap_transitions 1668 rows, opener_distribution 10488, cross_section_linkers 1670, hedge_verbs 124, results_discussion_openers 4864)
- Spot-check: distillation/v2/scripts/spot_check_quotes.py - 18/18 (100%) verified against original .evidence_packet.md


### Domain seed v2.1.0 (physics_optoelectronics, generated 2026-08-31)
- writing_rules.tsv: {'rows': 95, 'domain_seed_added': 10 (R2000-R2009)}
- phrase_bank.tsv: {'rows': 145, 'domain_seed_added': 11 (P2000-P2010)}
- domain_register.tsv: {'rows': 47, 'domain_seed_added': 1 (physics_optoelectronics)}
- domain_metrics_physics.tsv: {'rows': 12, 'domain_seed_added': 12 (new file, Rule 1a metric vocabulary)}
- anti_ai_patterns.tsv: no row change; state_of_art why-column now carries the physics_optoelectronics exception (R2008)
- prompts/system_writer.txt: 4x duplicated rhythm table deduped to 1; Domain Register Notes section added; Rule 1a device-metric bullet added
- scripts/distill_physics_corpus.py added: deterministic 5-TSV increment distiller for future corpus runs (keep count >= 3, hand spot-check before merging)


### Physics corpus distillation v2.1.1 (physics_optoelectronics, generated 2026-08-31)
- corpus: 27 OA Nature-family papers (Nature Communications 16, Light: Science & Applications 8, Nature 1, Nature Electronics 1, Nature Materials 1; 2022-2026), published full text, subagent-collected into workspace qled-corpus/
- driver: scripts/distill_physics_corpus.py + count-increment merge (opener-class appends thresholded at paper_count>=2; gap/linker rows are representative first sentences per (paper, section, pivot), consistent with the pc=1-dominant live distribution)
- spot-check vs corpus: gap templates 25/25 verified; linkers 14/15 (1 miss = chemical purity listing with masked digits)
- increments: opener_distribution +220 (+29 rows count-incremented), gap_transitions +227, hedge_verbs +8 (+27 incremented), cross_section_linkers +97, results_discussion_openers +23
- domain_register: physics_optoelectronics 0 -> 27 papers (distilled); R2000-R2009 / P2000-P2010 remain evidence=domain_seed (expert-curated, unchanged)


### Physics corpus rounds v2.2.0 (physics_optoelectronics, generated 2026-08-31)
- corpus: 111 OA Nature-family papers total. Round r1 (general QLED/micro-LED/OLED/semiconductor, 50 papers);
  round B (NiOx HIL / SAM-dipole / work-function / charge balance, 19); round C (TMO physics / oxide doping /
  solution oxide films / alternative HTLs, 19); round D (inverted & flagship QLED / QD-film interface /
  PeLED hole side / oxide surface passivation, 23). Direction recalibrated against the user's local
  reference corpus (NiOx-based QLED hole-injection/interface engineering).
- merge driver: workspace merge_physics.py (DOI manifest dedupe; opener-class appends pc>=2;
  gap/linker representative first-sentence rows)
- final rows: opener_distribution 11168, gap_transitions 2577,
  hedge_verbs 133, cross_section_linkers 2190,
  results_discussion_openers 4957; domain_register physics_optoelectronics = 111

### Physics pivot v3.0.0 (2026-09-01)
- Scope: whole-project pivot from multi-domain (bio-dominant) to physics-only (QLED / quantum dots / PeLED / micro-LED / OLED / semiconductors / NiOx HIL), user-confirmed. Skill renamed nature-writing-studio -> physics-writing-studio.
- Deleted 18,863 bio rows (inventory: workspace bio_rows_inventory.tsv; rollback: skill-backups/nature-writing-studio-v2.2.0-pre-physics-pivot/): opener 10430, gap 1668, linkers 1766, rd-openers 4864, R1000-series 25 + R025/R026/R036, P001-P122 + P1000-series, domain_register 45, sentence_stats 23, paper_story 12->5, anti_ai A1000-A1002 + robust_general + state_of_art.
- Added: R3000-R3023 (24 physics rules, 100% paper-backed), P3000-P3039 (40 physics phrases), A2000-A2004 (5 physics adversarial tells), argue chains rebuilt (13), rd-openers re-distilled (769 rows, pc>=2 25.2%), R2000-R2009 / P2000-P2010 backfilled with corpus evidence.
- Prompts: system_writer + style_guide + all section prompts physics-rewritten (Verification Layer / em-dash / hedge-tier methodology unchanged; examples, Tier A/B whitelists, rhythm table swapped to device entities).
- Final rows: writing_rules 91, phrase_bank 51, anti_ai_patterns 136, domain_register 2, paper_story_patterns 5, sentence_stats_by_domain 2, opener_distribution 738, gap_transitions 909, cross_section_linkers 424, hedge_verbs 133, results_discussion_openers 769

### v3.1.0 (2026-09-01) - corpus expansion + original-caliber rebuild + adversarial diff
- Corpus 111 -> 136 papers (+25: QLED colour 6 / perovskite NC 5 / QD physics 8 / NiOx-integration 8 incl. 1 dedup; years widened to 2012-2026; holdout 1 paper reserved in workspace/holdout/).
- gap_transitions +211->1120, cross_section_linkers +97->521, hedge +1->134.
- opener/rd rebuilt to original-project caliber via occ>=2 OR top5-per-paper-section: opener 738->4264 (31.4/paper vs original 25.5), rd 769->1423 (10.5/paper vs original 11.8); pc=1 representative singletons restored (2356/1181 rows).
- anti_ai: adversarial diff methodology (24 AI-generated device-text samples, 204 candidate n-grams, 34 corpus-near-zero, 8 new patterns A2005-A2012, 8 false positives documented); A2000-A2004 upgraded to evidence=adversarial_diff with measured counts. Artifacts: workspace/adversarial_samples/.

### v3.2.0 (2026-09-01) - keyword-directed expansion (user's 15 metric/material keywords)
- Corpus 136 -> 175 papers (+39 over 2 subagent rounds: R1 performance metrics 20 [EQE records / roll-off & lifetime / voltage & mobility / EL spectra & FWHM], R2 materials & fabrication 19 [NiOx solution/sol-gel/blade-coating/ink 4 / Cd-based 6 / InP-based 5 / device architecture 4]; 4 cross-agent dups deduped).
- gap_transitions -> 1422, linkers -> 669, opener rebuilt 5503 (31.4/paper), rd 1836 (10.5/paper), caliber held.
- Known gap: sputtered/ALD NiOx original-title papers are near-absent in Nature-family OA (they live in non-Nature journals); solution-route NiOx fabrication is covered by 4 distinct paradigms.
### v3.3.0 (2026-09-01) - local sputter/ALD seed + gap-fill round (lifetime / CE / NiOx-characterization / CommsPhys)
- Local seed: R3100-R3105 + P3100-P3105 appended (evidence=domain_seed_local) from user's local PDFs ph5c01512 (Co-doped NiOx RF sputter) + el5c01793 (Li-doped NiOx + SAM) - fills the v3.2.0 known gap that sputtered-NiOx originals rarely appear in Nature-family OA. A2000 calibrated in place: "excellent/superb device performance" banned only in bare (no-metric) form; metric-accompanied usage allowed (189-paper audit: 46 papers contain the phrase, 21 occurrences metric-accompanied, 34 bare -> bare form stays banned, metric-accompanied allowed; evidence=adversarial_diff_calibrated).
- Gap-fill subagent round (4 agents, 14 new OA papers, corpus 175 -> 189): lifetime T50/LT95/T80 5 (incl. T95>16,233 h extrapolation benchmark s41467-025-65871-0, T80 Nat. Electron.), current/power efficiency 3 (cd A-1 / lm W-1 / CE-J-EQE curves), NiOx film characterization 4 (XRD+Rietveld, AFM RMS roughness, Kelvin-probe work function, HAXPES band alignment, slot-die vs sol-gel vs sputter HTL comparison), Communications Physics first entries 2 (s42005-021-00742-w oxide mobility, s42005-023-01169-1 QD hole relaxation).
- Merged: gap_transitions 1422 -> 1532, cross_section_linkers 669 -> 725, opener rebuilt 5503 -> 5942 (31.4/paper), rd 1836 -> 2002 (10.6/paper), caliber held (occ>=2 OR top5-per-paper-section). DOI manifest 189, zero cross-agent dups.
- Rows after: writing_rules 97, phrase_bank 57, anti_ai_patterns 144.
