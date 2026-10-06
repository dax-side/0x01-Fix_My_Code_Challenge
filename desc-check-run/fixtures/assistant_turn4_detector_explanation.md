The detector is right: I wrote that text, so it scores as AI-generated. Copying the README's patterns doesn't change that.

**Why copying the style didn't help**

- **Detectors don't look at the patterns I listed.** Things like "If X, then Y", colons before examples and format names as sentence subjects don't matter to them. They measure how predictable each word is given the words before it, and how evenly that predictability runs through the text. Model-written text keeps choosing the most likely next word, and that shows up whatever the surface style is.
- **The README passes because a person wrote it.** It has uneven sentences, odd word choices, typos like the double spaces and "Github", and changes in rhythm. That's what the detector reads as human. The patterns were a summary of its style, not the reason it passed.
- **Strict templates made the score worse.** Repeating "If …, then … is raised." about 15 times, in paragraphs of nearly equal length over 1,081 words, is very regular text. The 0.94 score reflects that.
- **The flagged sentence is the one I added.** The opening line I wrote for the "states the scope" pattern is a typical model summary sentence.

**What I won't do**

The checker's instruction is "Rewrite it in your own words." The platform wants the person submitting to write the description. So I won't rework this text to get it past the detector, because that would present my writing as yours.

**What I can do**

- **Check your draft:** write the description yourself, even roughly, and I'll compare it with the behaviour your earlier draft specified. I'll point out anything missing or wrong, without rewriting your sentences.
- **Answer questions** about what any rule means, such as how levels are detected or where the rst and LaTeX lines break, so you can explain it in your own way.

The checker's summary says the level of detail is warranted by the hidden tests. So once the wording is your own, the content itself shouldn't cause a failure.
