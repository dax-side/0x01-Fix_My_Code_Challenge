# Holdout manifest (H1-H6)

Written by worker-holdout. Secret: builders of the new method must not open this folder (BRIEF.md section 4).

## Cases

| case | base | planted errors | base's own issues | neutral sentences in GT |
|---|---|---|---|---|
| H1 | paraphrase_P | 3 | 0 | 5 |
| H2 | paraphrase_P | 3 | 0 | 5 |
| H3 | paraphrase_P | 2 | 0 | 5 |
| H4 | rewrite_B | 3 | 0 | 0 |
| H5 | rewrite_B | 3 | 0 | 0 |
| H6 | paraphrase_P | 0 | 0 | 5 |

Bases:

- `paraphrase_P` = cases/holdout/H6.md, a fresh own-words PR-style paraphrase of fixtures/spec_A.md written for this holdout. H6 is P unmodified (control). Labelled fact by fact in labelling_H6_B.md: 105/105 facts stated correctly, 0 added claims, 5 neutral framing sentences.
- `rewrite_B` = fixtures/rewrite_B.md. H4 and H5 started as byte-exact copies (sha256 checked before editing). Labelled fact by fact in labelling_H6_B.md: 105/105 facts stated correctly, 0 added claims, 0 neutral sentences.

## Planted errors

| # | case | fact_id | kind | original text | new text | note |
|---|---|---|---|---|---|---|
| 1 | H1 | F13 | contradicted | Give it more cells than there are columns and you get a `ValueError` instead. | Give it more cells than there are columns and you get a `TypeError` as well. | swapped exception type: a footer with more cells than columns raises ValueError, draft says TypeError |
| 2 | H1 | H20 | missing | When they fall short, we add an untitled group over the first columns. | (deleted) | deleted sentence: untitled group added over the first columns when a level's spans cover fewer columns |
| 3 | H1 | added | added | Footer cells are measured along with the rest of the table when we work out column widths. | Footer cells are measured along with the rest of the table when we work out column widths. `maxcolwidths` applies to footer cells too, so a long footer value is wrapped like any other cell. | invented behaviour: spec says nothing about maxcolwidths or wrapping footer cells |
| 4 | H2 | H05 | contradicted | and is `center` when you leave it out | and is `left` when you leave it out | wrong default: align defaults to center, draft says left |
| 5 | H2 | F29 | missing | We do this even when there are no headers or rows. | (deleted) | deleted sentence: footer drawn like the header row also when there are no headers or rows |
| 6 | H2 | added | added | In `html` and `unsafehtml`, every level becomes a `tr` of `th` cells, and each cell carries its group's span and alignment. | In `html` and `unsafehtml`, every level becomes a `tr` of `th` cells, and each cell carries its group's span and alignment. Those `th` cells also get a `scope="colgroup"` attribute. | invented behaviour: spec says nothing about a scope attribute |
| 7 | H3 | F10 | contradicted | gets empty cells added on its left. | gets empty cells added on its right. | flipped side: a short footer is padded with empty cells on the left, draft says right |
| 8 | H3 | H70 | contradicted | Column numbers in those rules start from 1. | Column numbers in those rules start from 0. | off-by-one: LaTeX rule column numbers start at 1, draft says 0 |
| 9 | H4 | F14 | contradicted | If there are no rows and no headers, then the footer determines the number of columns. | If there are no rows, then the footer determines the number of columns. | condition broadened: spec requires no rows AND no headers, draft drops 'no headers' |
| 10 | H4 | H54 | missing | A one-column group has no colspan attribute. | (deleted) | deleted sentence: html/unsafehtml one-column group has no colspan attribute |
| 11 | H4 | added | added | LaTeX formats write each level after the opening lines. | LaTeX formats write each level after the opening lines. latex_longtable also repeats the levels at the top of every page. | invented behaviour: spec says nothing about repeating levels on each page |
| 12 | H5 | H71 | contradicted | * orgtbl, pipe, presto, textile, tsv | * orgtbl, pipe, presto, textile, tsv, youtrack | list gains a name: youtrack added to the unsupported-format list |
| 13 | H5 | F33 | missing | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". | rst repeats the line with hyphens instead of "=" signs. | deleted clause: an empty first footer cell in rst is written as '..' |
| 14 | H5 | added | added | Other footer values, including True and False, are displayed as text. | Other footer values, including True and False, are displayed as text. Footer cells can also contain line breaks, and the footer row then takes the height of its tallest cell. | invented behaviour: spec says nothing about multi-line footer cells |

Totals: 14 planted; contradicted=6, missing=4, added=4. Fact-ID issues on F facts=5, on H facts=5; added claims: 2 about footer (H1, H5), 2 about headergroups (H2, H4).

For `added` rows the original text is the sentence the new one was appended after; the GT sentence is only the appended sentence.

## Labelling notes on planted errors

- H3 / F10 (left -> right): the next sentence in P still says the padding is the same as for headers and lets the footer leave out the `showindex` column. Those two claims (F11, F12) are still made and are not false by themselves, so GT lists F10 only. A strict reader could also flag F11/F12 as now inconsistent.
- H5 / H71 (`youtrack` added to the unsupported list): labelled `contradicted` on H71 because the definitive list is stated wrongly. It could also be read as an `added` claim about `youtrack`; the GT has it as fact H71 only.
- H4 / F14 (condition broadened): only F14 changes; no other fact depends on it.
