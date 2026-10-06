# facts_coverage.md: spec_A sentences mapped to facts.json IDs

Source: `fixtures/spec_A.md` (19 paragraphs). Sentences are numbered in reading order and quoted verbatim.
Paragraphs 1-7 produce F facts (general arguments and footer); paragraphs 8-19 produce H facts (headergroups).
A sentence that yields several facts was split because its parts could be wrong independently.
S31's clause "including the `showindex` column" restates S43, so it maps to H18 (anchored on S43, with S31 in H18's `also_in`) instead of creating a duplicate fact.


## Paragraph 1 (F)

- S01: `tabulate()` has two new optional arguments named `footer` and `headergroups`.  
  -> F01
- S02: Both default to `None`.  
  -> F02
- S03: Passing `None` has the same effect as leaving the argument out.  
  -> F03
- S04: Existing arguments keep their current positions and defaults.  
  -> F04, F05

## Paragraph 2 (F)

- S05: When rows are present, headers beyond the longest row are cut off from the end.  
  -> F06

## Paragraph 3 (F)

- S06: The `footer` argument defines the cells shown below the table data.  
  -> F07
- S07: A footer can be any iterable of cells.  
  -> F08
- S08: A string, bytes value, or non-iterable footer raises `TypeError`.  
  -> F09
- S09: If the footer has fewer cells than the table has columns, empty cells are added on the left.  
  -> F10
- S10: This is the same padding used for headers and allows the footer to leave out the `showindex` column.  
  -> F11, F12
- S11: A footer with more cells than the table has columns raises `ValueError`.  
  -> F13

## Paragraph 4 (F)

- S12: When there are no rows and no headers, the footer determines the number of columns.  
  -> F14
- S13: A `None` footer cell is displayed as empty.  
  -> F15
- S14: Footer cells do not change the type of their columns.  
  -> F16
- S15: For numeric columns, a footer number uses `intfmt` when both the number and column are integers.  
  -> F17
- S16: Otherwise it uses `floatfmt`.  
  -> F18
- S17: The same rules apply to numbers wrapped in ANSI colour codes, with the codes kept around the formatted number.  
  -> F19, F20
- S18: Other footer values, including `True` and `False`, are displayed as text.  
  -> F21

## Paragraph 5 (F)

- S19: Footer cells are included when column widths are calculated.  
  -> F22
- S20: They use the same alignment as the table data and can therefore change the alignment of the data.  
  -> F23, F24

## Paragraph 6 (F)

- S21: In `html` and `unsafehtml`, the footer is a row of `td` cells inside `tfoot`, after `tbody`.  
  -> F25, F26
- S22: In `pipe`, `github` and `asciidoc`, the footer is another data row.  
  -> F27
- S23: Other formats, including a caller-created `TableFormat`, draw the footer like their header row.  
  -> F28
- S24: This also applies when there are no headers or rows.  
  -> F29

## Paragraph 7 (F)

- S25: Formats that have a line below the header repeat that line immediately above the footer.  
  -> F30
- S26: In `latex_longtable`, the repeated line is `\hline` without `\endhead`.  
  -> F31
- S27: In `rst`, the repeated line uses hyphens instead of `=` signs.  
  -> F32
- S28: An empty first footer cell in `rst` is written as `..`.  
  -> F33

## Paragraph 8 (H)

- S29: The `headergroups` argument describes one or more levels of column groups.  
  -> H01
- S30: A group is a list or tuple containing `(title, span)` or `(title, span, align)`.  
  -> H02
- S31: The span covers adjacent columns, including the `showindex` column.  
  -> H03, H18
- S32: `align` can be `left`, `center` or `right`, and defaults to `center`.  
  -> H04, H05
- S33: Titles are converted with `str()`.  
  -> H06
- S34: ANSI colour codes in titles do not count toward their width.  
  -> H07

## Paragraph 9 (H)

- S35: One level is written as a list of groups, for example `[("A", 2), ("B", 2)]`.  
  -> H08
- S36: Several levels are written as a list of levels, for example `[[("All", 4)], [("A", 2), ("B", 2)]]`.  
  -> H09
- S37: `headergroups` is treated as several levels only when it is non-empty and every item is a list or tuple whose entries are all lists or tuples.  
  -> H10
- S38: Otherwise it is treated as one level.  
  -> H11
- S39: Empty levels are allowed.  
  -> H12

## Paragraph 10 (H)

- S40: A `TypeError` is raised when `headergroups` is a string, bytes or non-iterable.  
  -> H13
- S41: It is also raised when a group is not a list or tuple containing two or three items, or when `align` is not a string.  
  -> H14, H15
- S42: A `ValueError` is raised when a span is not a positive integer or is a boolean, and when `align` is not `left`, `center` or `right`.  
  -> H16, H17

## Paragraph 11 (H)

- S43: Spans include the `showindex` column.  
  -> H18
- S44: A level whose spans cover more columns than are available raises `ValueError`.  
  -> H19
- S45: If the spans cover fewer columns, an untitled group is added over the first columns.  
  -> H20
- S46: Group boundaries in one level must also be boundaries in the level below.  
  -> H21
- S47: An empty level is treated as one untitled group.  
  -> H22

## Paragraph 12 (H)

- S48: The merged-cell formats are `simple`, `plain`, `psql`, `pretty`, and all grid and outline formats.  
  -> H23
- S49: Each level is drawn above the normal header.  
  -> H24
- S50: A title is placed in one merged cell covering its group's columns and separators.  
  -> H25
- S51: Titles are padded and aligned according to `align`.  
  -> H26

## Paragraph 13 (H)

- S52: The top line breaks only at boundaries from the top level.  
  -> H27
- S53: `simple` draws its top and bottom lines even without headers.  
  -> H28
- S54: The level line is the format's line between rows.  
  -> H29
- S55: A format without such a line uses its line below the header instead.  
  -> H30
- S56: Between two levels, the line breaks at the boundaries of the lower level.  
  -> H31
- S57: Under the last level, it breaks at every column.  
  -> H32
- S58: If a title and its cell padding are wider than the merged cell, the group's last column is widened.  
  -> H33
- S59: The bottom level is widened first.  
  -> H34
- S60: Other formats do not widen columns for titles, except `rst`.  
  -> H35, H36

## Paragraph 14 (H)

- S61: Titles can contain `\n`, `\r` or `\r\n`.  
  -> H37
- S62: A `\r\n` sequence counts as one line break.  
  -> H38
- S63: In merged-cell formats, the level row has the height of its tallest title.  
  -> H39
- S64: Shorter titles get empty lines at the bottom.  
  -> H40
- S65: Each line is aligned separately, and the widest line determines the required width.  
  -> H41, H42
- S66: `rst` raises `ValueError` when a title contains more than one line.  
  -> H43
- S67: `html` and LaTeX keep title line breaks.  
  -> H44

## Paragraph 15 (H)

- S68: `rst` builds its level rows like the merged-cell formats, but its top line breaks at every column.  
  -> H45, H46
- S69: The line after a level is made of hyphens and breaks at that level's group boundaries.  
  -> H47, H48
- S70: `rst` always left-aligns titles, regardless of `align`.  
  -> H49
- S71: An empty first title is written as `..`.  
  -> H50

## Paragraph 16 (H)

- S72: In `html` and `unsafehtml`, each level is a `tr` containing `th` cells.  
  -> H51
- S73: The cells use the group's span and alignment.  
  -> H52, H53
- S74: A one-column group has no `colspan` attribute.  
  -> H54
- S75: When a header row exists, the level rows are inside the `thead`.  
  -> H55
- S76: Without a header row, the level rows form their own `thead` before the `tbody`.  
  -> H56
- S77: `html` escapes titles and `unsafehtml` does not.  
  -> H57, H58

## Paragraph 17 (H)

- S78: In LaTeX, each level is written after the opening lines.  
  -> H59
- S79: Cells are separated by `&` and the row ends with ` \\`.  
  -> H60, H61
- S80: A group covering several columns uses `\multicolumn{SPAN}{A}{TITLE}`, where `A` is `l`, `c` or `r`.  
  -> H62, H63
- S81: A one-column group uses its title directly.  
  -> H64
- S82: Titles use the same escaping as headers, except in `latex_raw`.  
  -> H65, H66

## Paragraph 18 (H)

- S83: A level containing titled groups is followed by one rule for each titled group.  
  -> H67
- S84: `latex_booktabs` uses `\cmidrule(lr){FIRST-LAST}`.  
  -> H68
- S85: Other LaTeX formats use `\cline{FIRST-LAST}`.  
  -> H69
- S86: Column numbers start at 1.  
  -> H70

## Paragraph 19 (H)

- S87: `headergroups` is not supported by `asciidoc`, `github`, `jira`, `mediawiki`, `moinmoin`, `orgtbl`, `pipe`, `presto`, `textile`, `tsv`, or a caller-created `TableFormat`.  
  -> H71
- S88: Passing `headergroups` to any of these formats raises `ValueError`.  
  -> H72

## Counts

- Paragraphs: 19
- Sentences: 88 (paragraphs 1-7: 28; paragraphs 8-19: 60)
- Facts: 105 (F: 33, H: 72)
- Sentences split into more than one fact: 17
- Facts with an `ambiguity` note: 29
- Sentences with no fact: 0
