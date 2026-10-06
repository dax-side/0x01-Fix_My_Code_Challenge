`tabulate()` has two new optional arguments named `footer` and `headergroups`. Both default to `None`. Passing `None` has the same effect as leaving the argument out. Existing arguments keep their current positions and defaults.

When rows are present, headers beyond the longest row are cut off from the end.

The `footer` argument defines the cells shown below the table data. A footer can be any iterable of cells. A string, bytes value, or non-iterable footer raises `TypeError`. If the footer has fewer cells than the table has columns, empty cells are added on the left. This is the same padding used for headers and allows the footer to leave out the `showindex` column. A footer with more cells than the table has columns raises `ValueError`.

When there are no rows and no headers, the footer determines the number of columns. A `None` footer cell is displayed as empty. Footer cells do not change the type of their columns. For numeric columns, a footer number uses `intfmt` when both the number and column are integers. Otherwise it uses `floatfmt`. The same rules apply to numbers wrapped in ANSI colour codes, with the codes kept around the formatted number. Other footer values, including `True` and `False`, are displayed as text.

Footer cells are included when column widths are calculated. They use the same alignment as the table data and can therefore change the alignment of the data.

In `html` and `unsafehtml`, the footer is a row of `td` cells inside `tfoot`, after `tbody`. In `pipe`, `github` and `asciidoc`, the footer is another data row. Other formats, including a caller-created `TableFormat`, draw the footer like their header row. This also applies when there are no headers or rows.

Formats that have a line below the header repeat that line immediately above the footer. In `latex_longtable`, the repeated line is `\hline` without `\endhead`. In `rst`, the repeated line uses hyphens instead of `=` signs. An empty first footer cell in `rst` is written as `..`.

The `headergroups` argument describes one or more levels of column groups. A group is a list or tuple containing `(title, span)` or `(title, span, align)`. The span covers adjacent columns, including the `showindex` column. `align` can be `left`, `center` or `right`, and defaults to `center`. Titles are converted with `str()`. ANSI colour codes in titles do not count toward their width.

One level is written as a list of groups, for example `[("A", 2), ("B", 2)]`. Several levels are written as a list of levels, for example `[[("All", 4)], [("A", 2), ("B", 2)]]`. `headergroups` is treated as several levels only when it is non-empty and every item is a list or tuple whose entries are all lists or tuples. Otherwise it is treated as one level. Empty levels are allowed.

A `TypeError` is raised when `headergroups` is a string, bytes or non-iterable. It is also raised when a group is not a list or tuple containing two or three items, or when `align` is not a string. A `ValueError` is raised when a span is not a positive integer or is a boolean, and when `align` is not `left`, `center` or `right`.

Spans include the `showindex` column. A level whose spans cover more columns than are available raises `ValueError`. If the spans cover fewer columns, an untitled group is added over the first columns. Group boundaries in one level must also be boundaries in the level below. An empty level is treated as one untitled group.

The merged-cell formats are `simple`, `plain`, `psql`, `pretty`, and all grid and outline formats. Each level is drawn above the normal header. A title is placed in one merged cell covering its group's columns and separators. Titles are padded and aligned according to `align`.

The top line breaks only at boundaries from the top level. `simple` draws its top and bottom lines even without headers. The level line is the format's line between rows. A format without such a line uses its line below the header instead. Between two levels, the line breaks at the boundaries of the lower level. Under the last level, it breaks at every column. If a title and its cell padding are wider than the merged cell, the group's last column is widened. The bottom level is widened first. Other formats do not widen columns for titles, except `rst`.

Titles can contain `\n`, `\r` or `\r\n`. A `\r\n` sequence counts as one line break. In merged-cell formats, the level row has the height of its tallest title. Shorter titles get empty lines at the bottom. Each line is aligned separately, and the widest line determines the required width. `rst` raises `ValueError` when a title contains more than one line. `html` and LaTeX keep title line breaks.

`rst` builds its level rows like the merged-cell formats, but its top line breaks at every column. The line after a level is made of hyphens and breaks at that level's group boundaries. `rst` always left-aligns titles, regardless of `align`. An empty first title is written as `..`.

In `html` and `unsafehtml`, each level is a `tr` containing `th` cells. The cells use the group's span and alignment. A one-column group has no `colspan` attribute. When a header row exists, the level rows are inside the `thead`. Without a header row, the level rows form their own `thead` before the `tbody`. `html` escapes titles and `unsafehtml` does not.

In LaTeX, each level is written after the opening lines. Cells are separated by `&` and the row ends with ` \\`. A group covering several columns uses `\multicolumn{SPAN}{A}{TITLE}`, where `A` is `l`, `c` or `r`. A one-column group uses its title directly. Titles use the same escaping as headers, except in `latex_raw`.

A level containing titled groups is followed by one rule for each titled group. `latex_booktabs` uses `\cmidrule(lr){FIRST-LAST}`. Other LaTeX formats use `\cline{FIRST-LAST}`. Column numbers start at 1.

`headergroups` is not supported by `asciidoc`, `github`, `jira`, `mediawiki`, `moinmoin`, `orgtbl`, `pipe`, `presto`, `textile`, `tsv`, or a caller-created `TableFormat`. Passing `headergroups` to any of these formats raises `ValueError`.
