import csv

with open("decisions.csv") as f:
    rows = list(csv.DictReader(f))
    print(len(rows))

def count_outcomes(rows):
    tpCount = 0
    fpCount = 0
    fnCount = 0
    tnCount = 0
    for row in rows:
        if ((row["model_flag"] == "yes") and (row["human_flag"] == "yes")):
            tpCount = tpCount + 1
        if ((row["model_flag"] == "yes") and (row["human_flag"] == "no")):
            fpCount = fpCount + 1
        if ((row["model_flag"] == "no") and (row["human_flag"] == "yes")):
            fnCount = fnCount+ 1
        if ((row["model_flag"] == "no") and (row["human_flag"] == "no")):
            tnCount =  tnCount+ 1
    return tpCount, fpCount, fnCount, tnCount

"""
ALTERNATIVE APPROACH: Counter

from collections import Counter

def count_outcomes_counter(rows):
    counts = Counter((row["model_flag"], row["human_flag"]) for row in rows)
    return counts[("yes", "yes")], counts[("yes", "no")], counts[("no", "yes")], counts[("no", "no")]

Why this approach:
- Counts every (model_flag, human_flag) pair in one step instead of
  four separate counters, so there's less room for a copy-paste typo.
- Unexpected values (like "Yes" or a blank) still show up as their own
  pair instead of being silently skipped.
- Counter returns 0 for a missing pair instead of raising a KeyError.
"""

tp, fp, fn, tn = count_outcomes(rows)
print(f"TP: {tp}")
print(f"FP: {fp}")
print(f"FN: {fn}")
print(f"TN: {tn}")

# f before the quotes = formatted string: fills in the {values}
# .1% inside the braces = show as a percent with 1 decimal place
# (Inside the braces, an f like {x:.2f} would mean float, 2 decimal places)

if tp + fp == 0:
    precision = 0
else:
    precision = tp / (tp + fp)
print(f"Precision: {precision:.1%}")


if tp + fn == 0:
    recall = 0
else:
    recall = tp/(tp + fn)
print(f"Recall: {recall:.1%}")


if tp + fp + fn + tn == 0:
    agreement = 0
else:
    agreement = (tp + tn) / (tp + fp + fn + tn)
print(f"Agreement: {agreement:.1%}")

"""
def calculate_metrics(tp, fp, fn, tn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    agreement = (tp + tn) / (tp + fp + fn + tn)
    return precision, recall, agreement

precision, recall, agreement = calculate_metrics(tp, fp, fn, tn)
print(f"Precision: {precision:.1%}")
print(f"Recall: {recall:.1%}")
print(f"Agreement: {agreement:.1%}")
"""

