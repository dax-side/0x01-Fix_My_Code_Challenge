# Per-fact labelling of R2 (rewrite_B) and R3 (rewrite_C) against facts.json

Worker: worker-dev. Ruler: RUN/facts.json (105 facts). Drafts: RUN/cases/dev/R2.md, RUN/cases/dev/R3.md (byte-identical copies of fixtures/rewrite_B.md and fixtures/rewrite_C.md).

Rule applied: a fact is `stated` when the draft gives the same condition, value, exception type, scope and format list in any wording; `contradicted` when any of these differ; `missing` when no sentence gives it. Every quote below was checked by script to be an exact substring of the draft that occurs exactly once (`\n` in a quote is a line break in the draft). Section 3 lists every sentence, list and code unit of each draft, so a reader can see that no unit was skipped when looking for `added` claims.

## 1a. R2 per fact (rewrite_B)

| fact | status | draft text that states it | note |
|---|---|---|---|
| F01 | stated | tabulate takes two new optional arguments named footer and headergroups. |  |
| F02 | stated | By default, both are None. |  |
| F03 | stated | Passing None is the same as leaving the argument out. |  |
| F04 | stated | Existing arguments keep their current positions and defaults. |  |
| F05 | stated | Existing arguments keep their current positions and defaults. |  |
| F06 | stated | If the table has rows, then headers beyond the longest row are cut off from the end. |  |
| F07 | stated | To add a row below the table data, pass footer=cells, where cells is a list or another iterable of cells. |  |
| F08 | stated | To add a row below the table data, pass footer=cells, where cells is a list or another iterable of cells. |  |
| F09 | stated | If footer is a string, a bytes value or not iterable, then TypeError is raised. |  |
| F10 | stated | If the footer has fewer cells than the table has columns, then empty cells are added on the left. |  |
| F11 | stated | This is the same padding used for headers, and it lets the footer leave out the showindex column. |  |
| F12 | stated | This is the same padding used for headers, and it lets the footer leave out the showindex column. |  |
| F13 | stated | If the footer has more cells than the table has columns, then ValueError is raised. |  |
| F14 | stated | If there are no rows and no headers, then the footer determines the number of columns. |  |
| F15 | stated | A None footer cell is displayed as empty. |  |
| F16 | stated | Footer cells do not change the type of their columns. |  |
| F17 | stated | In numeric columns, a footer number uses intfmt if both the number and the column are integers. |  |
| F18 | stated | Otherwise it uses floatfmt. |  |
| F19 | stated | The same rules apply to numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). |  |
| F20 | stated | The same rules apply to numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). |  |
| F21 | stated | Other footer values, including True and False, are displayed as text. |  |
| F22 | stated | Footer cells are included when column widths are calculated. |  |
| F23 | stated | They use the same alignment as the table data, so they can change the alignment of the data. |  |
| F24 | stated | They use the same alignment as the table data, so they can change the alignment of the data. |  |
| F25 | stated | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. |  |
| F26 | stated | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. |  |
| F27 | stated | pipe, github and asciidoc write the footer as another data row. |  |
| F28 | stated | Other formats, including a caller-created TableFormat, draw the footer like their header row. |  |
| F29 | stated | This also applies when there are no headers or rows. |  |
| F30 | stated | Formats that have a line below the header repeat that line immediately above the footer. |  |
| F31 | stated | latex_longtable repeats \hline without \endhead. |  |
| F32 | stated | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". |  |
| F33 | stated | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". |  |
| H01 | stated | The optional argument named headergroups defines one or more levels of column groups. |  |
| H02 | stated | A group is a list or tuple of (title, span) or (title, span, align). |  |
| H03 | stated | The span covers adjacent columns, including the showindex column. |  |
| H04 | stated | align can be "left", "center" or "right". |  |
| H05 | stated | By default, align is "center". |  |
| H06 | stated | Titles are converted with str(). |  |
| H07 | stated | ANSI colour codes in titles do not count toward their width. |  |
| H08 | stated | One level is written as a list of groups: / [("A", 2), ("B", 2)]\n``` |  |
| H09 | stated | Several levels are written as a list of levels: / [[("All", 4)], [("A", 2), ("B", 2)]] |  |
| H10 | stated | If headergroups is non-empty and every item is a list or tuple whose entries are all lists or tuples, then it is treated as several levels. / Otherwise it is treated as one level. | spec says "only when"; draft gives "If ... then" plus "Otherwise it is treated as one level", which together state the same iff |
| H11 | stated | Otherwise it is treated as one level. |  |
| H12 | stated | Empty levels are allowed. |  |
| H13 | stated | If headergroups is a string, a bytes value or not iterable, then TypeError is raised. |  |
| H14 | stated | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. |  |
| H15 | stated | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. |  |
| H16 | stated | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". |  |
| H17 | stated | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". |  |
| H18 | stated | Spans include the showindex column. |  |
| H19 | stated | If the spans of a level cover more columns than are available, then ValueError is raised. |  |
| H20 | stated | If they cover fewer columns, then an untitled group is added over the first columns. |  |
| H21 | stated | Group boundaries in one level must also be boundaries in the level below. |  |
| H22 | stated | An empty level is treated as one untitled group. |  |
| H23 | stated | The merged-cell formats are:\n\n* simple\n* plain\n* psql\n* pretty\n* all grid and outline formats | all 5 entries present (bullet list) |
| H24 | stated | In these formats, each level is drawn above the normal header. |  |
| H25 | stated | A title is placed in one merged cell covering its group's columns and separators. |  |
| H26 | stated | Titles are padded and aligned according to align. |  |
| H27 | stated | The top line breaks only at boundaries from the top level. |  |
| H28 | stated | simple draws its top and bottom lines even without headers. |  |
| H29 | stated | The level line is the format's line between rows. |  |
| H30 | stated | If a format has no such line, then it uses its line below the header instead. |  |
| H31 | stated | Between two levels, the line breaks at the boundaries of the lower level. |  |
| H32 | stated | Under the last level, it breaks at every column. |  |
| H33 | stated | If a title and its cell padding are wider than the merged cell, then the group's last column is widened. |  |
| H34 | stated | The bottom level is widened first. |  |
| H35 | stated | Other formats, except rst, do not widen columns for titles. |  |
| H36 | stated | Other formats, except rst, do not widen columns for titles. |  |
| H37 | stated | Titles can contain "\n", "\r" or "\r\n". |  |
| H38 | stated | A "\r\n" sequence counts as one line break. |  |
| H39 | stated | In merged-cell formats, the level row has the height of its tallest title. |  |
| H40 | stated | Shorter titles get empty lines at the bottom. |  |
| H41 | stated | Each line is aligned separately, and the widest line determines the required width. |  |
| H42 | stated | Each line is aligned separately, and the widest line determines the required width. |  |
| H43 | stated | rst raises ValueError if a title contains more than one line. |  |
| H44 | stated | html and LaTeX keep title line breaks. |  |
| H45 | stated | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. |  |
| H46 | stated | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. |  |
| H47 | stated | The line after a level is made of hyphens and breaks at that level's group boundaries. |  |
| H48 | stated | The line after a level is made of hyphens and breaks at that level's group boundaries. |  |
| H49 | stated | rst always left-aligns titles, regardless of align. |  |
| H50 | stated | An empty first title is written as "..". |  |
| H51 | stated | html and unsafehtml write each level as a tr of th cells. |  |
| H52 | stated | The cells use the group's span and alignment. |  |
| H53 | stated | The cells use the group's span and alignment. |  |
| H54 | stated | A one-column group has no colspan attribute. |  |
| H55 | stated | If a header row exists, then the level rows are inside the thead. |  |
| H56 | stated | Otherwise the level rows form their own thead before the tbody. |  |
| H57 | stated | html escapes titles, and unsafehtml does not. |  |
| H58 | stated | html escapes titles, and unsafehtml does not. |  |
| H59 | stated | LaTeX formats write each level after the opening lines. |  |
| H60 | stated | Cells are separated by "&", and each row ends with a space followed by two backslashes. |  |
| H61 | stated | Cells are separated by "&", and each row ends with a space followed by two backslashes. | "each row" in the level paragraph; " \\" spelled as "a space followed by two backslashes" |
| H62 | stated | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". |  |
| H63 | stated | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". |  |
| H64 | stated | A one-column group uses its title directly. |  |
| H65 | stated | Titles use the same escaping as headers, except in latex_raw. |  |
| H66 | stated | Titles use the same escaping as headers, except in latex_raw. |  |
| H67 | stated | A level that contains titled groups is followed by one rule for each titled group. |  |
| H68 | stated | latex_booktabs uses \cmidrule(lr){FIRST-LAST}. |  |
| H69 | stated | Other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. |  |
| H70 | stated | Other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. |  |
| H71 | stated | headergroups is not supported by:\n\n* asciidoc, github, jira, mediawiki, moinmoin\n* orgtbl, pipe, presto, textile, tsv\n* a caller-created TableFormat | all 11 names present (bullet list) |
| H72 | stated | If headergroups is passed with any of these formats, then ValueError is raised. |  |

R2 totals: stated 105, missing 0, contradicted 0.

## 1b. R3 per fact (rewrite_C)

| fact | status | draft text that states it | note |
|---|---|---|---|
| F01 | stated | The tabulate function has two more optional arguments, footer and headergroups, which add a row of cells below the table data and titled groups of columns above the header. | "two more optional arguments" = two new optional arguments |
| F02 | stated | By default, both are None, and passing None is the same as leaving the argument out. |  |
| F03 | stated | By default, both are None, and passing None is the same as leaving the argument out. |  |
| F04 | stated | Existing arguments keep their current positions and defaults. |  |
| F05 | stated | Existing arguments keep their current positions and defaults. |  |
| F06 | stated | If the table has rows, then headers beyond the longest row are cut off from the end. |  |
| F07 | stated | The tabulate function has two more optional arguments, footer and headergroups, which add a row of cells below the table data and titled groups of columns above the header. / To add such a row, pass footer=cells, where cells is a list or another iterable of cells. |  |
| F08 | stated | To add such a row, pass footer=cells, where cells is a list or another iterable of cells. |  |
| F09 | stated | If footer is a string, a bytes value or not iterable, then TypeError is raised. |  |
| F10 | stated | If the footer has fewer cells than the table has columns, then empty cells are added on the left. |  |
| F11 | stated | This is the same padding used for headers, and it lets the footer leave out the showindex column. |  |
| F12 | stated | This is the same padding used for headers, and it lets the footer leave out the showindex column. |  |
| F13 | stated | If the footer has more cells than the table has columns, then ValueError is raised. |  |
| F14 | stated | If there are no rows and no headers, then the footer determines the number of columns. |  |
| F15 | stated | A None footer cell is displayed as empty. |  |
| F16 | stated | Footer cells do not change the type of their columns. |  |
| F17 | stated | In numeric columns, a footer number uses intfmt if both the number and the column are integers, and floatfmt otherwise. |  |
| F18 | stated | In numeric columns, a footer number uses intfmt if both the number and the column are integers, and floatfmt otherwise. |  |
| F19 | stated | It also works for numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). | "It also works" = the intfmt/floatfmt rule of the previous sentence also applies |
| F20 | stated | It also works for numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). |  |
| F21 | stated | Other footer values, including True and False, are displayed as text. |  |
| F22 | stated | Footer cells are included when column widths are calculated. |  |
| F23 | stated | They use the same alignment as the table data, so they can change the alignment of the data. |  |
| F24 | stated | They use the same alignment as the table data, so they can change the alignment of the data. |  |
| F25 | stated | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. |  |
| F26 | stated | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. |  |
| F27 | stated | pipe, github and asciidoc write the footer as another data row. |  |
| F28 | stated | Other formats, including a caller-created TableFormat, draw the footer like their header row. |  |
| F29 | stated | This also applies when there are no headers or rows. |  |
| F30 | stated | Formats that have a line below the header repeat that line immediately above the footer. |  |
| F31 | stated | latex_longtable repeats \hline without \endhead. |  |
| F32 | stated | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". |  |
| F33 | stated | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". |  |
| H01 | stated | The optional argument named headergroups defines one or more levels of such column groups. | "such column groups" refers back to the neutral framing sentence "a title over several columns"; read as a pointer, not as a scope limit, since the draft itself later describes one-column groups (H54, H64) |
| H02 | stated | A group is a list or tuple of (title, span) or (title, span, align), where span is the number of adjacent columns it covers (the showindex column included). |  |
| H03 | stated | A group is a list or tuple of (title, span) or (title, span, align), where span is the number of adjacent columns it covers (the showindex column included). |  |
| H04 | stated | align can be "left", "center" or "right", and it is "center" by default. |  |
| H05 | stated | align can be "left", "center" or "right", and it is "center" by default. |  |
| H06 | stated | Titles are converted with str(), and ANSI colour codes in titles do not count toward their width. |  |
| H07 | stated | Titles are converted with str(), and ANSI colour codes in titles do not count toward their width. |  |
| H08 | stated | One level is written as a list of groups: / [("A", 2), ("B", 2)]\n``` |  |
| H09 | stated | Several levels are written as a list of levels: / [[("All", 4)], [("A", 2), ("B", 2)]] |  |
| H10 | stated | If headergroups is non-empty and every item is a list or tuple whose entries are all lists or tuples, then it is treated as several levels. / Otherwise it is treated as one level. | spec says "only when"; draft gives "If ... then" plus "Otherwise it is treated as one level", which together state the same iff |
| H11 | stated | Otherwise it is treated as one level. |  |
| H12 | stated | Empty levels are allowed. |  |
| H13 | stated | If headergroups is a string, a bytes value or not iterable, then TypeError is raised. |  |
| H14 | stated | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. |  |
| H15 | stated | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. |  |
| H16 | stated | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". |  |
| H17 | stated | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". |  |
| H18 | stated | Spans include the showindex column. |  |
| H19 | stated | If the spans of a level cover more columns than are available, then ValueError is raised. |  |
| H20 | stated | If they cover fewer columns, then an untitled group is added over the first columns. |  |
| H21 | stated | Group boundaries in one level must also be boundaries in the level below. |  |
| H22 | stated | An empty level is treated as one untitled group. |  |
| H23 | stated | The merged-cell formats are simple, plain, psql, pretty, and all grid and outline formats. | all 5 entries present |
| H24 | stated | They draw each level above the normal header, and place each title in one merged cell covering its group's columns and separators. |  |
| H25 | stated | They draw each level above the normal header, and place each title in one merged cell covering its group's columns and separators. |  |
| H26 | stated | Titles are padded and aligned according to align. |  |
| H27 | stated | The top line breaks only at boundaries from the top level. |  |
| H28 | stated | simple draws its top and bottom lines even without headers. |  |
| H29 | stated | The level line is the format's line between rows, or its line below the header if it has no line between rows. |  |
| H30 | stated | The level line is the format's line between rows, or its line below the header if it has no line between rows. |  |
| H31 | stated | Between two levels, the line breaks at the boundaries of the lower level. |  |
| H32 | stated | Under the last level, it breaks at every column. |  |
| H33 | stated | If a title and its cell padding are wider than the merged cell, then the group's last column is widened, starting with the bottom level. |  |
| H34 | stated | If a title and its cell padding are wider than the merged cell, then the group's last column is widened, starting with the bottom level. |  |
| H35 | stated | Other formats, except rst, do not widen columns for titles. |  |
| H36 | stated | Other formats, except rst, do not widen columns for titles. |  |
| H37 | stated | Titles can contain "\n", "\r" or "\r\n", and "\r\n" counts as one line break. |  |
| H38 | stated | Titles can contain "\n", "\r" or "\r\n", and "\r\n" counts as one line break. |  |
| H39 | stated | In merged-cell formats, the level row has the height of its tallest title, and shorter titles get empty lines at the bottom. |  |
| H40 | stated | In merged-cell formats, the level row has the height of its tallest title, and shorter titles get empty lines at the bottom. |  |
| H41 | stated | Each line is aligned separately, and the widest line determines the required width. |  |
| H42 | stated | Each line is aligned separately, and the widest line determines the required width. |  |
| H43 | stated | rst raises ValueError if a title contains more than one line. |  |
| H44 | stated | html and LaTeX keep title line breaks. |  |
| H45 | stated | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. |  |
| H46 | stated | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. |  |
| H47 | stated | The line after a level is made of hyphens and breaks at that level's group boundaries. |  |
| H48 | stated | The line after a level is made of hyphens and breaks at that level's group boundaries. |  |
| H49 | stated | rst always left-aligns titles, regardless of align, and writes an empty first title as "..". |  |
| H50 | stated | rst always left-aligns titles, regardless of align, and writes an empty first title as "..". |  |
| H51 | stated | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. |  |
| H52 | stated | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. |  |
| H53 | stated | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. |  |
| H54 | stated | A one-column group has no colspan attribute. |  |
| H55 | stated | If a header row exists, then the level rows are inside the thead. |  |
| H56 | stated | Otherwise they form their own thead before the tbody. |  |
| H57 | stated | html escapes titles, and unsafehtml does not. |  |
| H58 | stated | html escapes titles, and unsafehtml does not. |  |
| H59 | stated | LaTeX formats write each level after the opening lines. |  |
| H60 | stated | Cells are separated by "&", and each row ends with a space followed by two backslashes. |  |
| H61 | stated | Cells are separated by "&", and each row ends with a space followed by two backslashes. | "each row" in the level paragraph; " \\" spelled as "a space followed by two backslashes" |
| H62 | stated | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". |  |
| H63 | stated | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". |  |
| H64 | stated | A one-column group uses its title directly. |  |
| H65 | stated | Titles use the same escaping as headers, except in latex_raw. |  |
| H66 | stated | Titles use the same escaping as headers, except in latex_raw. |  |
| H67 | stated | A level that contains titled groups is followed by one rule for each titled group. |  |
| H68 | stated | latex_booktabs uses \cmidrule(lr){FIRST-LAST}, and other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. |  |
| H69 | stated | latex_booktabs uses \cmidrule(lr){FIRST-LAST}, and other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. |  |
| H70 | stated | latex_booktabs uses \cmidrule(lr){FIRST-LAST}, and other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. |  |
| H71 | stated | headergroups is not supported by asciidoc, github, jira, mediawiki, moinmoin, orgtbl, pipe, presto, textile, tsv, or a caller-created TableFormat. | all 11 names present |
| H72 | stated | If headergroups is passed with any of these formats, then ValueError is raised. |  |

R3 totals: stated 105, missing 0, contradicted 0.

## 2. Added claims and neutral sentences

- R2 added: none. R2 neutral: none (every unit of R2 states at least one fact, or is the supported summary sentence below).
- R3 added: none. R3 neutral (non-behavioural framing, no claim about behaviour, API or output):
  - "A table often needs a row of totals or notes below its data."
  - "Some tables need a title over several columns."
  - "There is more than one way to draw a group title in plain text."
- Supported summary sentences (behavioural, but stated/implied by the spec, so neither `added` nor neutral):
  - R2: "footer adds a row of cells below the table data, and headergroups adds titled groups of columns above the header." Footer half = F07; headergroups half = H01 with H24 (merged-cell levels drawn above the normal header), H45 (rst), H55 (html levels inside thead with the header), H59 (LaTeX levels after the opening lines).
  - R3: the second half of the F01 sentence ("...which add a row of cells below the table data and titled groups of columns above the header."), same reasoning.

## 3a. R2 sentence inventory (91 units, in draft order)

| # | unit | classification |
|---|---|---|
| 1 | tabulate takes two new optional arguments named footer and headergroups. | states F01 |
| 2 | footer adds a row of cells below the table data, and headergroups adds titled groups of columns above the header. | supported summary: summary of F07 + H01/H24 (merged-cell, rst via H45), H55 (html thead), H59 (LaTeX); implied, not added |
| 3 | By default, both are None. | states F02 |
| 4 | Passing None is the same as leaving the argument out. | states F03 |
| 5 | Existing arguments keep their current positions and defaults. | states F04, F05 |
| 6 | If the table has rows, then headers beyond the longest row are cut off from the end. | states F06 |
| 7 | To add a row below the table data, pass footer=cells, where cells is a list or another iterable of cells. | states F07, F08 |
| 8 | If footer is a string, a bytes value or not iterable, then TypeError is raised. | states F09 |
| 9 | If the footer has fewer cells than the table has columns, then empty cells are added on the left. | states F10 |
| 10 | This is the same padding used for headers, and it lets the footer leave out the showindex column. | states F11, F12 |
| 11 | If the footer has more cells than the table has columns, then ValueError is raised. | states F13 |
| 12 | If there are no rows and no headers, then the footer determines the number of columns. | states F14 |
| 13 | A None footer cell is displayed as empty. | states F15 |
| 14 | Footer cells do not change the type of their columns. | states F16 |
| 15 | In numeric columns, a footer number uses intfmt if both the number and the column are integers. | states F17 |
| 16 | Otherwise it uses floatfmt. | states F18 |
| 17 | The same rules apply to numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). | states F19, F20 |
| 18 | Other footer values, including True and False, are displayed as text. | states F21 |
| 19 | Footer cells are included when column widths are calculated. | states F22 |
| 20 | They use the same alignment as the table data, so they can change the alignment of the data. | states F23, F24 |
| 21 | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. | states F25, F26 |
| 22 | pipe, github and asciidoc write the footer as another data row. | states F27 |
| 23 | Other formats, including a caller-created TableFormat, draw the footer like their header row. | states F28 |
| 24 | This also applies when there are no headers or rows. | states F29 |
| 25 | Formats that have a line below the header repeat that line immediately above the footer. | states F30 |
| 26 | latex_longtable repeats \hline without \endhead. | states F31 |
| 27 | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". | states F32, F33 |
| 28 | The optional argument named headergroups defines one or more levels of column groups. | states H01 |
| 29 | A group is a list or tuple of (title, span) or (title, span, align). | states H02 |
| 30 | The span covers adjacent columns, including the showindex column. | states H03 |
| 31 | align can be "left", "center" or "right". | states H04 |
| 32 | By default, align is "center". | states H05 |
| 33 | Titles are converted with str(). | states H06 |
| 34 | ANSI colour codes in titles do not count toward their width. | states H07 |
| 35 | One level is written as a list of groups: | states H08 |
| 36 | ```python\n[("A", 2), ("B", 2)]\n``` | states H08 |
| 37 | Several levels are written as a list of levels: | states H09 |
| 38 | ```python\n[[("All", 4)], [("A", 2), ("B", 2)]]\n``` | states H09 |
| 39 | If headergroups is non-empty and every item is a list or tuple whose entries are all lists or tuples, then it is treated as several levels. | states H10 |
| 40 | Otherwise it is treated as one level. | states H10, H11 |
| 41 | Empty levels are allowed. | states H12 |
| 42 | If headergroups is a string, a bytes value or not iterable, then TypeError is raised. | states H13 |
| 43 | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. | states H14, H15 |
| 44 | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". | states H16, H17 |
| 45 | Spans include the showindex column. | states H18 |
| 46 | If the spans of a level cover more columns than are available, then ValueError is raised. | states H19 |
| 47 | If they cover fewer columns, then an untitled group is added over the first columns. | states H20 |
| 48 | Group boundaries in one level must also be boundaries in the level below. | states H21 |
| 49 | An empty level is treated as one untitled group. | states H22 |
| 50 | The merged-cell formats are: | states H23 |
| 51 | * simple\n* plain\n* psql\n* pretty\n* all grid and outline formats | states H23 |
| 52 | In these formats, each level is drawn above the normal header. | states H24 |
| 53 | A title is placed in one merged cell covering its group's columns and separators. | states H25 |
| 54 | Titles are padded and aligned according to align. | states H26 |
| 55 | The top line breaks only at boundaries from the top level. | states H27 |
| 56 | simple draws its top and bottom lines even without headers. | states H28 |
| 57 | The level line is the format's line between rows. | states H29 |
| 58 | If a format has no such line, then it uses its line below the header instead. | states H30 |
| 59 | Between two levels, the line breaks at the boundaries of the lower level. | states H31 |
| 60 | Under the last level, it breaks at every column. | states H32 |
| 61 | If a title and its cell padding are wider than the merged cell, then the group's last column is widened. | states H33 |
| 62 | The bottom level is widened first. | states H34 |
| 63 | Other formats, except rst, do not widen columns for titles. | states H35, H36 |
| 64 | Titles can contain "\n", "\r" or "\r\n". | states H37 |
| 65 | A "\r\n" sequence counts as one line break. | states H38 |
| 66 | In merged-cell formats, the level row has the height of its tallest title. | states H39 |
| 67 | Shorter titles get empty lines at the bottom. | states H40 |
| 68 | Each line is aligned separately, and the widest line determines the required width. | states H41, H42 |
| 69 | rst raises ValueError if a title contains more than one line. | states H43 |
| 70 | html and LaTeX keep title line breaks. | states H44 |
| 71 | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. | states H45, H46 |
| 72 | The line after a level is made of hyphens and breaks at that level's group boundaries. | states H47, H48 |
| 73 | rst always left-aligns titles, regardless of align. | states H49 |
| 74 | An empty first title is written as "..". | states H50 |
| 75 | html and unsafehtml write each level as a tr of th cells. | states H51 |
| 76 | The cells use the group's span and alignment. | states H52, H53 |
| 77 | A one-column group has no colspan attribute. | states H54 |
| 78 | If a header row exists, then the level rows are inside the thead. | states H55 |
| 79 | Otherwise the level rows form their own thead before the tbody. | states H56 |
| 80 | html escapes titles, and unsafehtml does not. | states H57, H58 |
| 81 | LaTeX formats write each level after the opening lines. | states H59 |
| 82 | Cells are separated by "&", and each row ends with a space followed by two backslashes. | states H60, H61 |
| 83 | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". | states H62, H63 |
| 84 | A one-column group uses its title directly. | states H64 |
| 85 | Titles use the same escaping as headers, except in latex_raw. | states H65, H66 |
| 86 | A level that contains titled groups is followed by one rule for each titled group. | states H67 |
| 87 | latex_booktabs uses \cmidrule(lr){FIRST-LAST}. | states H68 |
| 88 | Other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. | states H69, H70 |
| 89 | headergroups is not supported by: | states H71 |
| 90 | * asciidoc, github, jira, mediawiki, moinmoin\n* orgtbl, pipe, presto, textile, tsv\n* a caller-created TableFormat | states H71 |
| 91 | If headergroups is passed with any of these formats, then ValueError is raised. | states H72 |

## 3b. R3 sentence inventory (78 units, in draft order)

| # | unit | classification |
|---|---|---|
| 1 | The tabulate function has two more optional arguments, footer and headergroups, which add a row of cells below the table data and titled groups of columns above the header. | states F01, F07 |
| 2 | By default, both are None, and passing None is the same as leaving the argument out. | states F02, F03 |
| 3 | Existing arguments keep their current positions and defaults. | states F04, F05 |
| 4 | If the table has rows, then headers beyond the longest row are cut off from the end. | states F06 |
| 5 | A table often needs a row of totals or notes below its data. | neutral |
| 6 | To add such a row, pass footer=cells, where cells is a list or another iterable of cells. | states F07, F08 |
| 7 | If footer is a string, a bytes value or not iterable, then TypeError is raised. | states F09 |
| 8 | If the footer has fewer cells than the table has columns, then empty cells are added on the left. | states F10 |
| 9 | This is the same padding used for headers, and it lets the footer leave out the showindex column. | states F11, F12 |
| 10 | If the footer has more cells than the table has columns, then ValueError is raised. | states F13 |
| 11 | If there are no rows and no headers, then the footer determines the number of columns. | states F14 |
| 12 | A None footer cell is displayed as empty. | states F15 |
| 13 | Footer cells do not change the type of their columns. | states F16 |
| 14 | In numeric columns, a footer number uses intfmt if both the number and the column are integers, and floatfmt otherwise. | states F17, F18 |
| 15 | It also works for numbers wrapped in ANSI colour codes (the codes are kept around the formatted number). | states F19, F20 |
| 16 | Other footer values, including True and False, are displayed as text. | states F21 |
| 17 | Footer cells are included when column widths are calculated. | states F22 |
| 18 | They use the same alignment as the table data, so they can change the alignment of the data. | states F23, F24 |
| 19 | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. | states F25, F26 |
| 20 | pipe, github and asciidoc write the footer as another data row. | states F27 |
| 21 | Other formats, including a caller-created TableFormat, draw the footer like their header row. | states F28 |
| 22 | This also applies when there are no headers or rows. | states F29 |
| 23 | Formats that have a line below the header repeat that line immediately above the footer. | states F30 |
| 24 | latex_longtable repeats \hline without \endhead. | states F31 |
| 25 | rst repeats the line with hyphens instead of "=" signs, and writes an empty first footer cell as "..". | states F32, F33 |
| 26 | Some tables need a title over several columns. | neutral |
| 27 | The optional argument named headergroups defines one or more levels of such column groups. | states H01 |
| 28 | A group is a list or tuple of (title, span) or (title, span, align), where span is the number of adjacent columns it covers (the showindex column included). | states H02, H03 |
| 29 | align can be "left", "center" or "right", and it is "center" by default. | states H04, H05 |
| 30 | Titles are converted with str(), and ANSI colour codes in titles do not count toward their width. | states H06, H07 |
| 31 | One level is written as a list of groups: | states H08 |
| 32 | ```python\n[("A", 2), ("B", 2)]\n``` | states H08 |
| 33 | Several levels are written as a list of levels: | states H09 |
| 34 | ```python\n[[("All", 4)], [("A", 2), ("B", 2)]]\n``` | states H09 |
| 35 | If headergroups is non-empty and every item is a list or tuple whose entries are all lists or tuples, then it is treated as several levels. | states H10 |
| 36 | Otherwise it is treated as one level. | states H10, H11 |
| 37 | Empty levels are allowed. | states H12 |
| 38 | If headergroups is a string, a bytes value or not iterable, then TypeError is raised. | states H13 |
| 39 | TypeError is also raised if a group is not a list or tuple of two or three items, or if align is not a string. | states H14, H15 |
| 40 | ValueError is raised if a span is a boolean or not a positive integer, or if align is not "left", "center" or "right". | states H16, H17 |
| 41 | Spans include the showindex column. | states H18 |
| 42 | If the spans of a level cover more columns than are available, then ValueError is raised. | states H19 |
| 43 | If they cover fewer columns, then an untitled group is added over the first columns. | states H20 |
| 44 | Group boundaries in one level must also be boundaries in the level below. | states H21 |
| 45 | An empty level is treated as one untitled group. | states H22 |
| 46 | There is more than one way to draw a group title in plain text. | neutral |
| 47 | The merged-cell formats are simple, plain, psql, pretty, and all grid and outline formats. | states H23 |
| 48 | They draw each level above the normal header, and place each title in one merged cell covering its group's columns and separators. | states H24, H25 |
| 49 | Titles are padded and aligned according to align. | states H26 |
| 50 | The top line breaks only at boundaries from the top level. | states H27 |
| 51 | simple draws its top and bottom lines even without headers. | states H28 |
| 52 | The level line is the format's line between rows, or its line below the header if it has no line between rows. | states H29, H30 |
| 53 | Between two levels, the line breaks at the boundaries of the lower level. | states H31 |
| 54 | Under the last level, it breaks at every column. | states H32 |
| 55 | If a title and its cell padding are wider than the merged cell, then the group's last column is widened, starting with the bottom level. | states H33, H34 |
| 56 | Other formats, except rst, do not widen columns for titles. | states H35, H36 |
| 57 | Titles can contain "\n", "\r" or "\r\n", and "\r\n" counts as one line break. | states H37, H38 |
| 58 | In merged-cell formats, the level row has the height of its tallest title, and shorter titles get empty lines at the bottom. | states H39, H40 |
| 59 | Each line is aligned separately, and the widest line determines the required width. | states H41, H42 |
| 60 | rst raises ValueError if a title contains more than one line. | states H43 |
| 61 | html and LaTeX keep title line breaks. | states H44 |
| 62 | rst builds its level rows like the merged-cell formats, but its top line breaks at every column. | states H45, H46 |
| 63 | The line after a level is made of hyphens and breaks at that level's group boundaries. | states H47, H48 |
| 64 | rst always left-aligns titles, regardless of align, and writes an empty first title as "..". | states H49, H50 |
| 65 | html and unsafehtml write each level as a tr of th cells, with the group's span and alignment. | states H51, H52, H53 |
| 66 | A one-column group has no colspan attribute. | states H54 |
| 67 | If a header row exists, then the level rows are inside the thead. | states H55 |
| 68 | Otherwise they form their own thead before the tbody. | states H56 |
| 69 | html escapes titles, and unsafehtml does not. | states H57, H58 |
| 70 | LaTeX formats write each level after the opening lines. | states H59 |
| 71 | Cells are separated by "&", and each row ends with a space followed by two backslashes. | states H60, H61 |
| 72 | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE}, where A is "l", "c" or "r". | states H62, H63 |
| 73 | A one-column group uses its title directly. | states H64 |
| 74 | Titles use the same escaping as headers, except in latex_raw. | states H65, H66 |
| 75 | A level that contains titled groups is followed by one rule for each titled group. | states H67 |
| 76 | latex_booktabs uses \cmidrule(lr){FIRST-LAST}, and other LaTeX formats use \cline{FIRST-LAST}, where FIRST and LAST are column numbers starting at 1. | states H68, H69, H70 |
| 77 | headergroups is not supported by asciidoc, github, jira, mediawiki, moinmoin, orgtbl, pipe, presto, textile, tsv, or a caller-created TableFormat. | states H71 |
| 78 | If headergroups is passed with any of these formats, then ValueError is raised. | states H72 |

