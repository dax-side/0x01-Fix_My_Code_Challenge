# Labelling of H6 (paraphrase P) and rewrite_B against facts.json

Written by worker-holdout. Each draft was labelled independently, fact by fact, before any mutant was made. No other agent's labels were consulted; cases/dev and cases/dev_answers were not opened.

## H6 (paraphrase P, unmodified control)

Draft: `cases/holdout/H6.md`. Labelled against `facts.json` (105 facts), one row per fact. Status is `stated` (stated correctly), `missing` or `contradicted`. Evidence is an exact substring of the draft (checked by script).

| fact | status | evidence in draft | note |
|---|---|---|---|
| F01 | stated | This PR gives `tabulate()` two new optional arguments, `footer` and `headergroups`. |  |
| F02 | stated | Each one defaults to `None` |  |
| F03 | stated | passing `None` yourself does exactly what leaving the argument out does |  |
| F04 | stated | The existing arguments are where they were, in the same positions |  |
| F05 | stated | with the same defaults |  |
| F06 | stated | When the table has rows, any headers beyond the longest row are dropped from the end. | moved to the end of the text |
| F07 | stated | `footer` supplies the cells for a row that appears underneath the table data. |  |
| F08 | stated | the footer can be any iterable of cells |  |
| F09 | stated | Strings and bytes are rejected with a `TypeError`, and so is anything that isn't iterable. |  |
| F10 | stated | A footer that's shorter than the number of columns gets empty cells added on its left. |  |
| F11 | stated | That's the same padding headers already get |  |
| F12 | stated | it's what lets you leave the `showindex` column out of the footer |  |
| F13 | stated | Give it more cells than there are columns and you get a `ValueError` instead. | 'instead' = instead of padding; exception type correct |
| F14 | stated | With no rows and no headers, the footer alone decides how many columns there are. |  |
| F15 | stated | A `None` in the footer shows up as an empty cell. |  |
| F16 | stated | Footer cells never change what type a column is. |  |
| F17 | stated | In a numeric column, a footer number is formatted with `intfmt` when it is an integer and the column is an integer column as well |  |
| F18 | stated | any other number in a numeric column goes through `floatfmt` |  |
| F19 | stated | Numbers wrapped in ANSI colour codes follow the same two rules |  |
| F20 | stated | the colour codes are kept around the formatted value |  |
| F21 | stated | Everything else, `True` and `False` included, is shown as text. |  |
| F22 | stated | Footer cells are measured along with the rest of the table when we work out column widths. |  |
| F23 | stated | They are aligned the same way as the data |  |
| F24 | stated | which means a footer can change how the data itself is aligned |  |
| F25 | stated | The `html` and `unsafehtml` output puts it in a `tfoot` that comes after the `tbody`, as a single row of `td` cells. |  |
| F26 | stated | a `tfoot` that comes after the `tbody` |  |
| F27 | stated | For `pipe`, `github` and `asciidoc` it is simply one more data row. |  |
| F28 | stated | Every other format draws it the way it draws its header row, and that includes a `TableFormat` you construct yourself. | 'you' = the caller |
| F29 | stated | We do this even when there are no headers or rows. | keeps the spec's own ambiguity ('this', 'no headers or rows') |
| F30 | stated | When a format has a line under its header, that same line is drawn a second time directly above the footer. |  |
| F31 | stated | `latex_longtable` repeats a bare `\hline` there, with no `\endhead`. |  |
| F32 | stated | In `rst` the repeated line is made of hyphens instead of `=` signs |  |
| F33 | stated | an empty first footer cell comes out as `..` | same sentence opens 'In `rst`' |
| H01 | stated | The other new argument, `headergroups`, describes column groups, either one level of them or several levels. |  |
| H02 | stated | Each group is written as `(title, span)` or `(title, span, align)`, using either a list or a tuple. |  |
| H03 | stated | Its span covers neighbouring columns | neighbouring = adjacent |
| H04 | stated | `align` takes `left`, `center` or `right` |  |
| H05 | stated | and is `center` when you leave it out |  |
| H06 | stated | Titles are passed through `str()` |  |
| H07 | stated | ANSI colour codes inside a title don't count toward its width |  |
| H08 | stated | To give one level, pass a list of groups such as `[("A", 2), ("B", 2)]`. |  |
| H09 | stated | To give several, pass a list of levels such as `[[("All", 4)], [("A", 2), ("B", 2)]]`. |  |
| H10 | stated | We only read the value as several levels when it is non-empty and every one of its items is itself a list or tuple made up only of lists or tuples. |  |
| H11 | stated | Anything else is read as a single level. |  |
| H12 | stated | A level is allowed to be empty |  |
| H13 | stated | `headergroups` itself must be iterable and must not be a string or bytes; otherwise it raises `TypeError`. |  |
| H14 | stated | Each group has to be a list or tuple with two or three items | with 'Breaking either rule is a `TypeError` too.' |
| H15 | stated | `align` has to be a string. Breaking either rule is a `TypeError` too. |  |
| H16 | stated | A span must be a positive integer and must not be a boolean | with 'Breaking either of these is a `ValueError`.' |
| H17 | stated | `align` must be one of `left`, `center` or `right`. Breaking either of these is a `ValueError`. |  |
| H18 | stated | the `showindex` column is counted among them | stated once, inside the span sentence (spec states it twice) |
| H19 | stated | Spans in a level that add up to more columns than are available give a `ValueError`. |  |
| H20 | stated | When they fall short, we add an untitled group over the first columns. |  |
| H21 | stated | every boundary in one level must also be a boundary in the level below it |  |
| H22 | stated | an empty level behaves like one untitled group |  |
| H23 | stated | By merged-cell formats I mean `simple`, `plain`, `psql`, `pretty`, and all of the grid and outline formats. |  |
| H24 | stated | In these, every level is drawn above the normal header. |  |
| H25 | stated | Each title sits in a single merged cell that stretches across its group's columns and the separators between them |  |
| H26 | stated | padded and aligned according to the group's `align` |  |
| H27 | stated | The top border breaks only at the top level's group boundaries. |  |
| H28 | stated | Even without headers, `simple` still draws a top line and a bottom line. |  |
| H29 | stated | Under a level we draw the format's between-rows line |  |
| H30 | stated | or its below-the-header line for formats that have no between-rows line |  |
| H31 | stated | Between two levels that line breaks at the lower level's boundaries |  |
| H32 | stated | under the last level it breaks at every column |  |
| H33 | stated | When a title plus its cell padding is wider than its merged cell, we widen the last column of that group. |  |
| H34 | stated | We widen the bottom level first. |  |
| H35 | stated | Apart from `rst`, no other format widens columns to fit titles. | 'other' = outside the merged-cell formats, from context |
| H36 | stated | Apart from `rst` |  |
| H37 | stated | Titles may include line breaks written as `\n`, `\r` or `\r\n` |  |
| H38 | stated | with `\r\n` treated as one break |  |
| H39 | stated | In the merged-cell formats, a level row is as tall as its tallest title |  |
| H40 | stated | shorter titles are filled out with blank lines at the bottom |  |
| H41 | stated | Each line is aligned on its own |  |
| H42 | stated | the widest line sets the width the title needs |  |
| H43 | stated | `rst` doesn't allow this: a title with more than one line raises `ValueError` there. |  |
| H44 | stated | `html` and the LaTeX formats keep the line breaks. |  |
| H45 | stated | `rst` follows the merged-cell layout for its level rows. |  |
| H46 | stated | Its top line is different, though: in `rst` it breaks at every column. |  |
| H47 | stated | Each level is followed by a line of hyphens |  |
| H48 | stated | that breaks at that level's own group boundaries |  |
| H49 | stated | Titles in `rst` are always left-aligned, whatever `align` says |  |
| H50 | stated | an empty first title is written as `..` |  |
| H51 | stated | In `html` and `unsafehtml`, every level becomes a `tr` of `th` cells |  |
| H52 | stated | each cell carries its group's span and alignment |  |
| H53 | stated | each cell carries its group's span and alignment |  |
| H54 | stated | A group that covers only one column gets no `colspan` attribute. |  |
| H55 | stated | When there is a header row, the level rows go inside the `thead`. |  |
| H56 | stated | When there isn't, they get a `thead` of their own, placed before the `tbody`. |  |
| H57 | stated | `html` escapes titles |  |
| H58 | stated | `unsafehtml` leaves them as they are |  |
| H59 | stated | For LaTeX, the level rows follow the opening lines. |  |
| H60 | stated | Cells are separated with `&` |  |
| H61 | stated | each level row ends in ` \\` |  |
| H62 | stated | A group spanning more than one column is written as `\multicolumn{SPAN}{A}{TITLE}` |  |
| H63 | stated | with `A` being `l`, `c` or `r` |  |
| H64 | stated | while a one-column group just gets its title |  |
| H65 | stated | Escaping of titles matches the escaping of headers |  |
| H66 | stated | with `latex_raw` as the exception |  |
| H67 | stated | After any level that has titled groups we emit one rule per titled group |  |
| H68 | stated | `\cmidrule(lr){FIRST-LAST}` in `latex_booktabs` |  |
| H69 | stated | `\cline{FIRST-LAST}` in the other LaTeX formats |  |
| H70 | stated | Column numbers in those rules start from 1. |  |
| H71 | stated | `headergroups` is rejected with `ValueError` by the formats that don't support it: `asciidoc`, `github`, `jira`, `mediawiki`, `moinmoin`, `orgtbl`, `pipe`, `presto`, `textile`, `tsv`, and any `TableFormat` the caller builds. | same 10 names + caller-built TableFormat |
| H72 | stated | `headergroups` is rejected with `ValueError` by the formats that don't support it |  |

Counts: stated=105; added=0; neutral sentences=5.

Added claims (exact draft sentences): none.

Neutral sentences (pure framing, no behavioural claim): 
- I'll go through `footer` first and then `headergroups`.
- For reference, these are the error cases.
- The rest of this description goes through rendering, one family of formats at a time.
- One last note on headers.
- Happy to split this into two PRs if that is easier to review.

Sentences reviewed for `added` and judged supported (not issues):
- "How that row is drawn depends on the output format." : summary of F25-F28; supported
- "On the input side, the footer can be any iterable of cells." : 'On the input side' is framing; claim = F08
- "Group boundaries also have to nest" : label for H21, same content

## rewrite_B (fixtures/rewrite_B.md; base of H4, H5)

Draft: `fixtures/rewrite_B.md`. Labelled against `facts.json` (105 facts), one row per fact. Status is `stated` (stated correctly), `missing` or `contradicted`. Evidence is an exact substring of the draft (checked by script).

| fact | status | evidence in draft | note |
|---|---|---|---|
| F01 | stated | tabulate takes two new optional arguments named footer and headergroups. |  |
| F02 | stated | By default, both are None. |  |
| F03 | stated | Passing None is the same as leaving the argument out. |  |
| F04 | stated | Existing arguments keep their current positions and defaults. |  |
| F05 | stated | Existing arguments keep their current positions and defaults. |  |
| F06 | stated | If the table has rows, then headers beyond the longest row are cut off from the end. |  |
| F07 | stated | footer adds a row of cells below the table data | also 'To add a row below the table data, pass footer=cells' |
| F08 | stated | where cells is a list or another iterable of cells |  |
| F09 | stated | If footer is a string, a bytes value or not iterable, then TypeError is raised. |  |
| F10 | stated | If the footer has fewer cells than the table has columns, then empty cells are added on the left. |  |
| F11 | stated | This is the same padding used for headers |  |
| F12 | stated | it lets the footer leave out the showindex column |  |
| F13 | stated | If the footer has more cells than the table has columns, then ValueError is raised. |  |
| F14 | stated | If there are no rows and no headers, then the footer determines the number of columns. |  |
| F15 | stated | A None footer cell is displayed as empty. |  |
| F16 | stated | Footer cells do not change the type of their columns. |  |
| F17 | stated | In numeric columns, a footer number uses intfmt if both the number and the column are integers. |  |
| F18 | stated | Otherwise it uses floatfmt. |  |
| F19 | stated | The same rules apply to numbers wrapped in ANSI colour codes |  |
| F20 | stated | (the codes are kept around the formatted number) |  |
| F21 | stated | Other footer values, including True and False, are displayed as text. |  |
| F22 | stated | Footer cells are included when column widths are calculated. |  |
| F23 | stated | They use the same alignment as the table data |  |
| F24 | stated | so they can change the alignment of the data |  |
| F25 | stated | html and unsafehtml write the footer as a row of td cells inside tfoot, after tbody. |  |
| F26 | stated | inside tfoot, after tbody |  |
| F27 | stated | pipe, github and asciidoc write the footer as another data row. |  |
| F28 | stated | Other formats, including a caller-created TableFormat, draw the footer like their header row. |  |
| F29 | stated | This also applies when there are no headers or rows. |  |
| F30 | stated | Formats that have a line below the header repeat that line immediately above the footer. |  |
| F31 | stated | latex_longtable repeats \hline without \endhead. |  |
| F32 | stated | rst repeats the line with hyphens instead of "=" signs |  |
| F33 | stated | writes an empty first footer cell as ".." |  |
| H01 | stated | The optional argument named headergroups defines one or more levels of column groups. | also previewed in paragraph 1 |
| H02 | stated | A group is a list or tuple of (title, span) or (title, span, align). |  |
| H03 | stated | The span covers adjacent columns, including the showindex column. |  |
| H04 | stated | align can be "left", "center" or "right". |  |
| H05 | stated | By default, align is "center". |  |
| H06 | stated | Titles are converted with str(). |  |
| H07 | stated | ANSI colour codes in titles do not count toward their width. |  |
| H08 | stated | [("A", 2), ("B", 2)] | code block after 'One level is written as a list of groups:' |
| H09 | stated | [[("All", 4)], [("A", 2), ("B", 2)]] | code block after 'Several levels are written as a list of levels:' |
| H10 | stated | If headergroups is non-empty and every item is a list or tuple whose entries are all lists or tuples, then it is treated as several levels. | 'If ... then' plus the 'Otherwise' sentence gives the spec's 'only when' |
| H11 | stated | Otherwise it is treated as one level. |  |
| H12 | stated | Empty levels are allowed. |  |
| H13 | stated | If headergroups is a string, a bytes value or not iterable, then TypeError is raised. |  |
| H14 | stated | TypeError is also raised if a group is not a list or tuple of two or three items |  |
| H15 | stated | or if align is not a string |  |
| H16 | stated | ValueError is raised if a span is a boolean or not a positive integer |  |
| H17 | stated | or if align is not "left", "center" or "right" |  |
| H18 | stated | Spans include the showindex column. |  |
| H19 | stated | If the spans of a level cover more columns than are available, then ValueError is raised. |  |
| H20 | stated | If they cover fewer columns, then an untitled group is added over the first columns. |  |
| H21 | stated | Group boundaries in one level must also be boundaries in the level below. |  |
| H22 | stated | An empty level is treated as one untitled group. |  |
| H23 | stated | * simple / * plain / * psql / * pretty / * all grid and outline formats | bullet list after 'The merged-cell formats are:' |
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
| H36 | stated | except rst |  |
| H37 | stated | Titles can contain "\n", "\r" or "\r\n". |  |
| H38 | stated | A "\r\n" sequence counts as one line break. |  |
| H39 | stated | In merged-cell formats, the level row has the height of its tallest title. |  |
| H40 | stated | Shorter titles get empty lines at the bottom. |  |
| H41 | stated | Each line is aligned separately |  |
| H42 | stated | the widest line determines the required width |  |
| H43 | stated | rst raises ValueError if a title contains more than one line. |  |
| H44 | stated | html and LaTeX keep title line breaks. |  |
| H45 | stated | rst builds its level rows like the merged-cell formats |  |
| H46 | stated | but its top line breaks at every column |  |
| H47 | stated | The line after a level is made of hyphens |  |
| H48 | stated | breaks at that level's group boundaries |  |
| H49 | stated | rst always left-aligns titles, regardless of align. |  |
| H50 | stated | An empty first title is written as "..". |  |
| H51 | stated | html and unsafehtml write each level as a tr of th cells. |  |
| H52 | stated | The cells use the group's span and alignment. |  |
| H53 | stated | The cells use the group's span and alignment. |  |
| H54 | stated | A one-column group has no colspan attribute. |  |
| H55 | stated | If a header row exists, then the level rows are inside the thead. |  |
| H56 | stated | Otherwise the level rows form their own thead before the tbody. |  |
| H57 | stated | html escapes titles |  |
| H58 | stated | unsafehtml does not |  |
| H59 | stated | LaTeX formats write each level after the opening lines. |  |
| H60 | stated | Cells are separated by "&" |  |
| H61 | stated | each row ends with a space followed by two backslashes | spelled out instead of ` \\`; 'each row' read as each level row from context |
| H62 | stated | A group covering several columns uses \multicolumn{SPAN}{A}{TITLE} |  |
| H63 | stated | where A is "l", "c" or "r" |  |
| H64 | stated | A one-column group uses its title directly. |  |
| H65 | stated | Titles use the same escaping as headers |  |
| H66 | stated | except in latex_raw |  |
| H67 | stated | A level that contains titled groups is followed by one rule for each titled group. |  |
| H68 | stated | latex_booktabs uses \cmidrule(lr){FIRST-LAST}. |  |
| H69 | stated | Other LaTeX formats use \cline{FIRST-LAST} |  |
| H70 | stated | where FIRST and LAST are column numbers starting at 1 | attached to the \cline sentence; FIRST/LAST are the placeholders of both rules, so read as covering both |
| H71 | stated | * asciidoc, github, jira, mediawiki, moinmoin / * orgtbl, pipe, presto, textile, tsv / * a caller-created TableFormat | bullet list after 'headergroups is not supported by:'; same 10 names + TableFormat |
| H72 | stated | If headergroups is passed with any of these formats, then ValueError is raised. |  |

Counts: stated=105; added=0; neutral sentences=0.

Added claims (exact draft sentences): none.

Neutral sentences (pure framing, no behavioural claim): none.

Sentences reviewed for `added` and judged supported (not issues):
- "footer adds a row of cells below the table data, and headergroups adds titled groups of columns above the header." : UNSURE. Overview sentence. 'below the table data' = F07. 'titled groups of columns above the header' generalises H01 + H24 (merged-cell formats; rst like merged-cell; html level rows inside thead). The spec never states the position relative to the header for LaTeX (only 'after the opening lines') and allows untitled groups (H20, H22). Labelled as supported summary, not `added`.
- "To add a row below the table data, pass footer=cells, where cells is a list or another iterable of cells." : F07 + F08; supported
- "One level is written as a list of groups:" : H08 lead-in
- "Several levels are written as a list of levels:" : H09 lead-in
- "The merged-cell formats are:" : H23 lead-in
- "headergroups is not supported by:" : H71 lead-in
