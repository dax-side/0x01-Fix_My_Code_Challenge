The module provides just one function, tabulate, which takes a list of lists or another tabular data type as the first argument, and outputs a nicely formatted plain-text table:
* list of lists or another iterable of iterables
* list or another iterable of dicts (keys as columns)
* dict of iterables (keys as columns)
* two-dimensional NumPy array
* NumPy record arrays (names as columns)
* pandas.DataFrame
Examples in this file use Python2. Tabulate supports Python3 too.
The second optional argument named headers defines a list of column headers to be used:
If headers="firstrow", then the first row of data is used:
If headers="keys", then the keys of a dictionary/dataframe, or column indices are used. It also works for NumPy record arrays and lists of dictionaries or named tuples:
By default, only pandas.DataFrame tables have an additional column called row index. To add a similar column to any other type of table, pass showindex="always" or showindex=True argument to tabulate(). To suppress row indices for all types of data, pass showindex="never" or showindex=False.  To add a custom row index column, pass showindex=rowIDs, where rowIDs is some iterable:
There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how the table is formatted.
plain tables do not use any pseudo-graphics to draw lines:
simple is the default format (the default may change in future versions).  It corresponds to simple_tables in `Pandoc Markdown extensions`_:
github follows the conventions of `Github flavored Markdown`.  It corresponds to the pipe format without alignment colons: