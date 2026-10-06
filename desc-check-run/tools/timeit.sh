#!/usr/bin/env bash
# timeit.sh - run a command N times and print wall-clock statistics as JSON.
#
# Usage: tools/timeit.sh N <command...>
#
# The command is executed directly (no shell); use `bash -c '...'` for pipes or
# redirections. Its stdout goes to /dev/null so that this script's stdout is
# only the JSON object; its stderr is passed through. Wall time is measured with
# python's time.perf_counter around each run (monotonic, sub-microsecond).
# Output: {"n","mean","sd","min","max","unit":"s","failures","times":[...],"command":[...]}
#   sd is the sample standard deviation (n-1); 0.0 when n == 1.
# Exit status: 0 if every run exited 0, 1 if any run failed, 2 on usage error.
# The JSON is printed even when runs failed, with "failures" > 0.

if [ "$#" -lt 2 ]; then
  echo "usage: $0 N <command...>" >&2
  exit 2
fi
N="$1"
shift
case "$N" in
  ''|*[!0-9]*|0) echo "error: N must be a positive integer, got '$N'" >&2; exit 2 ;;
esac

exec python3 -c '
import json, statistics, subprocess, sys, time
n = int(sys.argv[1]); cmd = sys.argv[2:]
times, failures = [], 0
for _ in range(n):
    t0 = time.perf_counter()
    try:
        rc = subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode
    except OSError as e:
        print("error: cannot run %r: %s" % (cmd[0], e), file=sys.stderr)
        sys.exit(2)
    t1 = time.perf_counter()
    times.append(t1 - t0)
    failures += rc != 0
out = {"n": n, "mean": statistics.fmean(times),
       "sd": statistics.stdev(times) if n > 1 else 0.0,
       "min": min(times), "max": max(times), "unit": "s",
       "failures": failures, "times": [round(t, 6) for t in times], "command": cmd}
print(json.dumps(out))
sys.exit(1 if failures else 0)
' "$N" "$@"
