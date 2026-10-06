Use a workflow for this task and run it end to end without checking in with me.

GOAL
Find a new way of doing the thing we have been working on in this session
that takes much less time and gives more accurate results. I want a different
way of working, not patches on the current way. Both measures count: a faster
method that is less accurate is a failure, and so is the reverse. I am hoping
to cut wasted time by 99 percent; treat that as a hypothesis to test, not a
number to hit. An honest smaller figure with evidence is worth more to me
than a claimed 99 percent.

FIGURE OUT THE DETAILS YOURSELF
You already have the context: this conversation, the knowledge base, and the
files we have been using. From those, decide what exactly is being rebuilt,
how to measure time spent, how to measure accuracy, which real past cases
make a fair fixed test set, and what the result must still do. Do not ask me
for these. When something is ambiguous, take the most reasonable reading,
record the choice and why, and continue.

CHECK WHAT WE THINK WE KNOW
Your own findings and the knowledge base are claims, not facts. Some are
stale, some contradict each other, and some were only ever assumed. Before
building on a claim, test it against how things actually are now. This
applies to conclusions you reached earlier in this session too.

THE TEAM
Set up these roles as separate agents, each with its own brief. No agent
judges its own work.

- Coordinator: you. Owns the whole picture, hands out work, and makes sure
  nothing is lost between agents. Keeps a master list of every open item,
  who has it and its status, and closes the run only when every item is
  done, dropped with a reason, or listed as a limitation.
- Planner: designs the approach before anything is built. Breaks the current
  way down into parts with the time each takes and why each exists, works
  out the largest saving possible, and proposes two or three new designs.
  Tries remedies in this order: stop doing the step, do it once and reuse
  it, do it less often, do it in parallel, do it more cheaply.
- Budget keeper: tracks what the run itself costs: agents started, tokens
  and time per phase, and what each phase produced for that spend. Warns the
  coordinator when a line of work is costing more than it could save, and
  recommends cutting it.
- Workers: small, narrow jobs only, one piece each: index one part of the
  knowledge base, re-test one claim, measure one case, build one piece of
  the chosen design. A worker follows its brief, reports what it did with
  the evidence, and does not redesign anything.
- Judge: strict and independent. Sees only the claim and the evidence for
  it, not the reasoning of whoever produced it, and tries to disprove it.
  Looks for: measurements or checks that were changed, answers stored for
  the test cases, work quietly dropped, accuracy that got worse, and results
  that differ from recorded past cases. Grades every finding and every
  claimed saving:
    High: reproduced, with evidence the judge checked itself. Accepted.
    Medium: supported but not fully reproduced, or only on part of the test
      set. May be used, with the caveat stated wherever it is used.
    Low: weak, unreproduced or contradicted. Treated as disproved. Nothing
      may be built on it and it does not appear in the results.
  The judge's grade is final. Nobody may regrade their own work.

HOW THE WORK FLOWS
1. Coordinator writes a brief to a new working folder: what the thing is,
   how we have been doing it, where every file and folder lives, the two
   measures, the test set. Agents start with no memory of this conversation,
   so each one is pointed at that brief and the paths it needs.
2. Workers index the knowledge base; the judge grades the claims that would
   change a decision.
3. Workers measure the current way several times on the test set, for both
   time and accuracy, and record the values and their spread. Some cases
   are held back for the final measurement.
4. Planner produces the breakdown, the ceiling and the designs, using only
   High claims and Medium ones with their caveats. Coordinator picks one.
5. Workers build the chosen design for a small slice, beside the current
   way so the current way keeps working. Old and new run on the same cases,
   measured the same way.
6. Judge grades the result. Only if it is High, or Medium with a caveat the
   coordinator accepts, does the work extend to the rest, re-measuring after
   each change that is kept.
7. Stop when the best remaining change would save little, when two rounds in
   a row bring no measurable gain, or when the budget keeper shows the run
   is costing more than it is finding.
8. Final measurement on the full test set and the held-back cases, graded
   by the judge.

Once the measures, the test set and the baseline are fixed, nobody changes
them. They define success.

THE LOG
Keep log.md in the working folder as a running record of the whole run.
Every entry has the time, the role, and one of: task handed out (from whom,
to whom, what was asked), result returned (what came back, where the evidence
is), decision (what was chosen and why), judge's grade (with reason), budget
note, or limitation. Log messages between roles in full enough that I could
follow who told whom what. Entries are only ever added, never edited. If
agents working at the same time would overwrite each other, each writes to
its own file in a log folder and the coordinator merges them into log.md in
time order.

LIMITATIONS
Do not stop for limitations. When you hit one (something you cannot measure,
a claim you cannot verify, a file or tool you cannot reach, an agent that
failed), log it, add it to limitations.md with what it affected, and carry on.

THE ONLY REASONS TO STOP AND ASK
Stop before any action that could not be undone or that reaches outside this
workspace: deleting or overwriting original files or the knowledge base,
touching live or shared systems, sending anything to other people, or
spending money. Everything else is your call.

REPORT
At the end give me: what you decided the target, the two measures and the
test set were; time and accuracy before and after, with number of runs and
spread; the reduction actually achieved beside the ceiling the breakdown
allowed; every finding that survived, with its grade and any caveat; what
was disproved; what the run cost according to the budget keeper; and the
contents of limitations.md. If the target was missed, say so plainly and
say why.
