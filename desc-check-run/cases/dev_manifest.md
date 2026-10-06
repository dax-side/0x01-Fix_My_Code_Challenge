# Dev mutation manifest (M1-M5)

Worker: worker-dev. Each mutant started as a byte-exact `cp` of fixtures/rewrite_C.md (sha256 e52d795a67dd5cc08678f96f4c5fe2d200510bc52224f63bd4e4f3d6b61f1526); the edits below were then applied as exact one-occurrence string replacements. R3 (= rewrite_C) has no issues, so each mutant's GT = the planted issues below + R3's three neutral sentences (none of which was edited).

## M1 (3 planted)

| # | fact_id / added | kind | original text (rewrite_C) | new text (mutant) | note |
|---|---|---|---|---|---|
| 1 | F13 | contradicted | If the footer has more cells than the table has columns, then ValueError is raised. | If the footer has more cells than the table has columns, then TypeError is raised. | exception type swapped: a footer longer than the column count raises ValueError, draft says TypeError |
| 2 | H20 | contradicted | If they cover fewer columns, then an untitled group is added over the first columns. | If they cover fewer columns, then an untitled group is added over the last columns. | side flipped: the untitled group goes over the first columns, draft says the last columns |
| 3 | added | added | Titles are converted with str(), and ANSI colour codes in titles do not count toward their width. | Titles are converted with str(), and ANSI colour codes in titles do not count toward their width. Leading and trailing spaces in titles are removed. | spec says titles are converted with str(); it says nothing about stripping spaces |

## M2 (2 planted)

| # | fact_id / added | kind | original text (rewrite_C) | new text (mutant) | note |
|---|---|---|---|---|---|
| 1 | F14 | contradicted | If there are no rows and no headers, then the footer determines the number of columns. | If there are no rows, then the footer determines the number of columns. | condition broadened: spec needs no rows AND no headers; draft says no rows is enough |
| 2 | H54 | missing | with the group's span and alignment. A one-column group has no colspan attribute. If a header row exists | with the group's span and alignment. If a header row exists | sentence deleted: html/unsafehtml one-column group has no colspan attribute |

## M3 (4 planted)

| # | fact_id / added | kind | original text (rewrite_C) | new text (mutant) | note |
|---|---|---|---|---|---|
| 1 | H05 | contradicted | align can be "left", "center" or "right", and it is "center" by default. | align can be "left", "center" or "right", and it is "left" by default. | wrong default: align defaults to "center", draft says "left"; still stated in the edited sentence: H04 |
| 2 | H70 | contradicted | where FIRST and LAST are column numbers starting at 1. | where FIRST and LAST are column numbers starting at 0. | off by one: column numbers in \cmidrule/\cline start at 1, draft says 0; still stated in the edited sentence: H68, H69 |
| 3 | F33 | missing | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". | rst repeats the line with hyphens instead of "=" signs. | clause deleted: an empty first footer cell in rst is written as ".."; still stated in the edited sentence: F32 |
| 4 | added | added | latex_longtable repeats \hline without \endhead. | latex_longtable repeats \hline without \endhead. In latex_longtable, the footer is also repeated at the bottom of every page. | spec only says the repeated line is \hline without \endhead; nothing about repeating the footer on every page |

## M4 (3 planted)

| # | fact_id / added | kind | original text (rewrite_C) | new text (mutant) | note |
|---|---|---|---|---|---|
| 1 | F26 | contradicted | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. | html and unsafehtml write the footer as a row of td cells inside tfoot, before tbody. | placement moved: tfoot comes after tbody, draft says before; still stated in the edited sentence: F25 |
| 2 | H38 | missing | Titles can contain "\n", "\r" or "\r\n", and "\r\n" counts as one line break. | Titles can contain "\n", "\r" or "\r\n". | clause deleted: a "\r\n" sequence counts as one line break; still stated in the edited sentence: H37 |
| 3 | added | added | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. The alignment is written as a style attribute on each th cell. | spec says the cells use the group's alignment but not how it is written in HTML |

## M5 (3 planted)

| # | fact_id / added | kind | original text (rewrite_C) | new text (mutant) | note |
|---|---|---|---|---|---|
| 1 | H23 | contradicted | The merged-cell formats are simple, plain, psql, pretty, and all grid and outline formats. | The merged-cell formats are simple, plain, pretty, and all grid and outline formats. | format dropped from list: psql is a merged-cell format, the draft's list leaves it out |
| 2 | F05 | missing | Existing arguments keep their current positions and defaults. | Existing arguments keep their current positions. | clause deleted: existing arguments keep their current defaults; still stated in the edited sentence: F04 |
| 3 | added | added | They use the same alignment as the table data, so they can change the alignment of the data. | They use the same alignment as the table data, so they can change the alignment of the data. Footer cells are never wrapped, even when maxcolwidths is set. | spec says nothing about wrapping footer cells or about maxcolwidths |

Totals: 15 planted = 7 contradicted, 4 missing, 4 added. Footer-side (F / footer added): F13, F14, F26, F05, F33, 2 added (M3 latex_longtable, M5 maxcolwidths). Headergroups-side (H / title added): H20, H05, H70, H23, H54, H38, 2 added (M1 title spaces, M4 html style).

Co-located facts: where an edited sentence also states other facts, those facts are still stated after the edit and are not issues: M3 H04, H68, H69, F32; M4 F25, H37; M5 F04. Checked by script: in each mutant the only facts whose R3 evidence quote no longer appears are the planted facts plus these co-located ones, and each co-located fact has a new exact quote in the mutant.
