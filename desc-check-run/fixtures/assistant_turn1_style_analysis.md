This is the reference-manual style of the `tabulate` README. Every sentence either says what something does or tells you how to change it. Here are the patterns I found.

## 1. Structure

| Pattern | Example from the text |
|---|---|
| **The opening sentence covers the whole scope**: what the module is, what goes in and what comes out | "The module provides just one function, tabulate, which takes … as the first argument, and outputs a nicely formatted plain-text table" |
| **Arguments are introduced in positional order** | "the first argument" → "The second optional argument…" → "The third optional argument…" |
| **Simple cases come before advanced ones** | `headers` list → `"firstrow"` → `"keys"`; default index → always/never → custom index |
| **Each paragraph is one idea plus an example.** Paragraphs are 1–3 sentences, then a code block. | Every paragraph |
| **A general statement comes before the feature that addresses it** | "There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how…" |

## 2. Recurring sentence templates

1. **"The [ordinal] optional argument named X defines Y."** An argument is introduced by its position, whether it's optional, its name and its job.
   - "The second optional argument named headers defines a list of column headers to be used"
2. **"If X="value", then Y is used."** Behaviour is keyed to a literal value.
   - "If headers="firstrow", then the first row of data is used"
   - "If headers="keys", then the keys of … are used"
3. **"By default, … To [goal], pass [value]."** The default is stated first, then short recipes that start with the goal.
   - "To add a similar column…, pass showindex="always"…"
   - "To suppress row indices…, pass showindex="never"…"
   - "To add a custom row index column, pass showindex=rowIDs…"
4. **"[name] [verb]s …"** Each option starts its own sentence and stays lowercase even there.
   - "plain tables do not use…", "simple is the default format…", "github follows the conventions of…"
5. **"It corresponds to [external standard]."** A second sentence links the option to an existing convention.
   - "It corresponds to simple_tables in Pandoc…", "It corresponds to the pipe format without alignment colons"
6. **"It also works for …"** Scope is widened after the main rule.
7. **"where X is some Y"** defines a placeholder inline: "showindex=rowIDs, where rowIDs is some iterable"

## 3. Punctuation and formatting habits

- **Colons lead into examples.** Almost every paragraph ends with ":" so the code example finishes the sentence.
- **Literal values stay in quotes, not code formatting:** headers="firstrow", showindex=True.
- **Equivalent values are paired with "or":** `"always"` or `True`, `"never"` or `False`.
- **Caveats go in parentheses:** "(the default may change in future versions)", "(keys as columns)", "(names as columns)".
- **Slashes join alternatives:** "dictionary/dataframe".
- **There are two spaces after some full stops** ("showindex=False.  To add…"). This comes from the reStructuredText source.
- **Links use reStructuredText syntax**, `` `Pandoc Markdown extensions`_ ``. The GitHub link is missing the trailing `_`, which looks like a small error in the original.

## 4. Lists

- **Bullets are noun phrases with no verbs:** "two-dimensional NumPy array", "pandas.DataFrame".
- **"X or another Y" names a concrete case and then the general one:** "list of lists or another iterable of iterables", "list or another iterable of dicts".
- **Short parentheses show how items map to columns:** "(keys as columns)", "(names as columns)". This mapping is repeated later ("keys … are used"), so the terms stay consistent.
- **Items run from most common to most specialised:** Python built-ins first, then NumPy, then pandas.

## 5. Voice and tone

- **Present tense throughout:** "provides", "defines", "is used", "follows".
- **Third person for the software, imperative for the reader:** "tabulate … outputs" vs. "pass showindex=…". It never uses "you".
- **Passive voice is used when the data is the subject:** "the first row of data is used", "column indices are used".
- **Modest, plain words:** "just one function", "nicely formatted", "some iterable", "pseudo-graphics". There is no marketing language.
- **Admits uncertainty:** "the default may change in future versions".
- **Very short standalone notes:** "Examples in this file use Python2. Tabulate supports Python3 too." These are two short, flat statements with no transition.
- **Names are spelled the way their projects spell them:** NumPy, pandas (lowercase), Pandoc. "Github" and "Python2" (no space) are period quirks.

## 6. A reusable template

To write in this style, fill in these slots:

```
The module provides [N] function(s), [name], which takes [input] as the first
argument, and outputs [result]:

* [concrete type] or another [general type]
* [type] ([how it maps])

The [ordinal] optional argument named [param] defines [purpose]:

If [param]="[value]", then [behaviour]:

By default, [default behaviour]. To [goal], pass [param]=[value] or [param]=[alt].
To [other goal], pass [param]=[value], where [value] is some [type]:

[option] [does something]. It corresponds to [known standard]:
```

In short: say what it does, give its position, state the default, give the recipe, point to an existing standard, then show the example after the colon.
