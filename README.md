# eval-metrics

A Python script that measures how well an AI's decisions match a human's. Give it a CSV of AI decisions next to human decisions, and it reports how often the AI was right and how it was wrong.

## About this version

This is intentionally simple. I built it as a hands-on project alongside the Coursera course [Audit Your AI Decisions](https://www.coursera.org/learn/audit-your-ai-decisions), and it's the starting point for a project I'm growing step by step. Each improvement will be its own commit, so the history shows how it develops.

Right now it:

- uses only Python's standard library, with no packages to install
- handles one kind of decision: a plain yes or no
- runs on a small 20-item sample file
- prints results to the screen, with no tests yet

The [next steps](#next-steps) list is where it's headed.

## Example output

```
20
TP: 8
FP: 2
FN: 4
TN: 6
Precision: 80.0%
Recall: 66.7%
Agreement: 70.0%
```

## What the metrics mean

The human's decision is treated as the correct answer.

- **Precision:** when the AI flags something, how often is it right?
- **Recall:** of everything that should be flagged, how much did the AI catch?
- **Agreement:** how often did the AI and the human give the same answer?

## Input format

A CSV with one row per item:

```
item,model_flag,human_flag
1,yes,yes
2,no,no
3,yes,no
```

`model_flag` is the AI's decision and `human_flag` is the human's. Both are `yes` or `no`.

## Run it

Requires Python 3.

```
python3 eval_metrics.py
```

## Next steps

- [ ] Break metrics down by category
- [ ] List every false positive and false negative for review
- [ ] Add a confidence score and compare thresholds
- [ ] Add confidence intervals for each metric
- [ ] Measure agreement between two human labelers
- [ ] Use an LLM to make the decisions, then score it