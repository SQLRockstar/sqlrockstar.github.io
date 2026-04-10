---
layout: post
title: Fail Better, Then Finish 21st
date: '2026-04-09 16:35:38 +0000'
categories:
- Data Analytics
---

<link rel="icon" type="image/x-icon" href="/gravatar.png">

<p>Every March, data scientists and sports fans collide on Kaggle. This year, I came out ahead of 3,464 of them. 21st place out of 3,485 entries. Top 1%. I'll take it.</p>

<img src="https://sqlrockstar.github.io/wp-content/uploads/2026/04/kaggle_silver_cert.png" alt="Kaggle 2026 Silver Certificate" style="width:75%; display:block; margin: 0 auto;">

<p>This is how I did it.</p>

<h2>Why Am I Even Doing This?</h2>

<p>I have an MS in Mathematics, way before some hipster decided to rename "statistics" as "data science". I spent the better part of a decade as a database administrator before deciding I wanted to do more with data than store it. About ten years ago I started consuming and <a href="https://thomaslarock.com/2017/07/why-im-learning-data-science/">learning all things data science</a>, and lurking around other data folks at places like <a href="https://www.kaggle.com/">Kaggle</a>. As you read this I am finishing my second MS degree, this one in Data Analytics from Georgia Tech, I graduate in a few weeks.</p>

<p>Now, I am not saying I spent $10,000+ and three-plus years of my life just to get better at Kaggle competitions.</p>

<p>But, I am not not saying that either.</p>

<p>The <a href="https://www.kaggle.com/competitions/march-machine-learning-mania-2026">Kaggle March Machine Learning Mania competition</a> is a good proving ground. It is time-boxed, the data is clean, the scoring is well-defined, and the competition is deep. This year there were 3,485 entries; not a trivial field. There are serious data scientists in that pool. People who do this professionally, people with larger compute budgets, people with more elegant solutions than mine. Finishing in the top 1% means something.</p> 

<p>Well, it does to me, at least.</p>

<p>It also means I have to write this post, now, because when I finish 2000th next year I will want people to forget I ever mentioned it.</p>

<h2>The Approach</h2>

<p>Let me walk you through how I built this, and more importantly, why I made the decisions I did.</p>

<p>The competition asks you to submit a prediction for every possible matchup between two teams in both the Men's and Women's tournaments. With 64 teams in each field, the submission contains 132,133 entries. Each entry has a team identifier and a probability between 0 and 1, representing the likelihood that the lower-seeded team ID wins the game, should these two teams meet. You do not pick teams to advance, you measure their probability of winning any given game. Honestly, this is more fun than a traditional bracket challenge.</p>

<p>The competition is scored using the Brier score. Unlike accuracy, which only cares about right or wrong, the Brier score rewards how confident and calibrated your predictions are. A lower Brier score is better. A perfect model scores 0. A model predicting 50/50 for every game scores 0.25. My final score was 0.1203942, which was the average of the two results for Men (0.1416504) and Women (0.0991382). This is another way of saying I was right on 46 (out of 63) games for the men, and 55 games for the women.</p>

<p>The easiest approach to the competition is to train a model, output some predictions, and call it a day. Some people do exactly that and get decent results. The problem with this method is simple: a model trained carelessly will learn things which are not true, and you only find out after the games are played.</p>

<p>A few deliberate choices made the difference for me.</p>

<h3>Symmetric Training Data</h3>

<p>Every game appears twice in my training data, once with Team A listed first, once with Team B. Without this, the model can quietly learn that “being listed first” correlates with winning, which is obviously nonsense but surprisingly easy for a model to pick up. This doubled the training data and also eliminated perspective bias. Also, I focused exclusively on differentials rather than raw values. For example, instead of using each team's average points scored, I used the scoring gap between the two teams. This gives the model the right context to find meaningful patterns in a head-to-head matchup.</p>

<h3>Walk-Forward Validation</h3>

<p>Standard cross-validation does not work here. If you train on 2024 data and validate on 2022, the model has already seen the future, which is one of the fastest ways to build a model which performs great in testing but fails in reality. Walk-forward validation trains on all data before a given season and validates on that season only, which mirrors exactly what the prediction task requires. I validated across six seasons: 2019, 2021, 2022, 2023, 2024, and 2025, skipping 2020 because the tournament was cancelled that year for reasons I am sure everyone has forgotten by now. Recent seasons were weighted more heavily since the game evolves year to year.</p>

<h3>Feature Engineering</h3>

<p>All features were computed as differentials (Team A minus Team B) to keep the model focused on relative team quality. None of these features are exotic individually, but together they describe three things: how good a team is, how consistent they are, and how they perform against strong opponents:</p>

<ul>
<li>MOV-adjusted ELO, using a FiveThirtyEight-style margin-of-victory correction</li>
<li>Pythagorean win percentage and last-10-game momentum</li>
<li>Strength of schedule, consistency, and volatility</li>
<li>Seed matchup win rates — historical, recent 5-year, and recent 10-year windows</li>
<li>Multi-dimensional performance gap analysis across key seasonal metrics</li>
</ul>

<p>None of these features are secret. What matters is how they work together to describe the relative quality and momentum of two teams heading into a neutral-site elimination game.</p>

<h2>Where the Magic Happened</h2>

<p>Five models. One ensemble. More compute time than a free account would allow.</p>

<p>I trained five models independently: LightGBM, XGBoost, HistGradientBoosting, Logistic Regression, and a Neural Network. Each model saw the same features and the same walk-forward validation scheme. The question was not which model to use but rather how much to trust each one.</p>

<p>Rather than averaging the predictions equally, I used <a href="https://optuna.org/">Optuna</a> to optimize the ensemble weights separately for men and women, minimizing Brier score on the walk-forward predictions. This is important because not all models fail in the same way, and weighting them properly lets you keep their strengths while minimizing their blind spots. Think of this as "smoothing the edges" on the predictions across the models. These are the results:</p>

<table>
<thead>
<tr><th>Model</th><th>Men</th><th>Women</th></tr>
</thead>
<tbody>
<tr><td>LightGBM</td><td>58.4%</td><td>34.0%</td></tr>
<tr><td>Logistic Regression</td><td>21.9%</td><td>8.5%</td></tr>
<tr><td>XGBoost</td><td>18.4%</td><td>10.7%</td></tr>
<tr><td>Neural Network</td><td>0.1%</td><td>43.9%</td></tr>
<tr><td>HistGradientBoosting</td><td>1.3%</td><td>2.8%</td></tr>
</tbody>
</table>

<br></br>

<p>A few things stand out here.</p>

<p>LightGBM dominated the men's side at 58.4%. No surprise, as it was the best individual model throughout tuning. Logistic Regression contributed a meaningful 21.9%, which tells you something about the value of a simple linear model when your features are well constructed.</p>

<p>The Neural Network result is the most interesting story in the table. For men, Optuna effectively ignored it, 0.1% weight is a rounding error. For women, it carried 43.9% of the load. This suggests the women's game has non-linear patterns the tree models simply do not capture. Different datasets reward different modeling assumptions, and assuming one approach works everywhere is an easy way to plateau. Whether this is due to differences in pace, efficiency, or seed dominance, I cannot say with certainty. But the data was clear.</p>

<p>HistGradientBoosting was essentially noise at 1-3% across both genders. Next year I would either force it to find a different signal or drop it entirely in favor of more tuning time on LightGBM.</p>

<p>The ensemble Brier score of 0.1203942 beat every individual model. That is the point of an ensemble, not to find the best single model, but to combine models and build a system which is more reliable than any single model would be on its own.</p>

<h2>The Insight — Or, How I Learned to Stop Being Clever</h2>

<p>I played basketball. I coached basketball. And when I first entered this competition years ago I was certain my domain expertise would give me an edge over the data scientists who had never watched a college game in their lives.</p>

<p>I was wrong. Very, very wrong.</p>

<p>It turns out knowing basketball does not help you predict basketball outcomes any better than someone who has never seen a game, provided they know how to collect, transform, and analyze data properly. The sport has too much variance. The tournament has too much chaos. And the things I thought I knew, which teams were dangerous, which matchups favored underdogs, and when to trust a double-digit seed was just noise dressed up as intuition.</p>

<p>The humbling moment came when I started looking at my predictions for upset-prone matchups. My instinct, informed by years of watching March Madness, was to adjust my model's predictions to account for the possibility of an upset. If my model said a 1-seed had a 93% chance of winning, and I knew from experience upsets happen, why not nudge that number down a bit? Give the 9-seed a fighting chance in the predictions, just like they sometimes get in real life!</p>

<p>Remember the MS in mathematics I have? Yeah, so I did the math on this idea.</p>

<p>It turns out this instinct, however well-intentioned, is mathematically guaranteed to make your Brier score worse. Every time. Without exception. I wrote a short explanation of this on Kaggle which you can read <a href="https://www.kaggle.com/competitions/march-machine-learning-mania-2026/discussion/684446">here</a>, but the short version is this: any manual adjustment makes your score worse on average. It does not matter if you are trying to account for an upset, or injuries, or anything. If you alter the model predictions after they are output, you hurt yourself more often than not. And the penalty grows larger the further you alter your prediction from the true value.</p>

<p>But the lesson was not just about upset predictions. It was bigger than that. Being a subject matter expert is not enough. Sure, it helps you ask better questions and interpret results more intelligently. But it is no substitute for knowing how to build models properly. Once I stopped trying to be clever and started trusting the data, my results improved.</p>

<p>Domain expertise and analytical rigor are not competing advantages. They are complementary ones. It just took me a few years of finishing in the middle of the pack to figure that out.</p>

<h2>A Word on Tools</h2>

<p>I used large language models throughout this project. For coding assistance, debugging, and as a sounding board when I was working through methodology decisions. I am not going to pretend otherwise, and I do not think there is anything to be ashamed of in saying so. Kaggle themselves published a starter notebook this year built around Gemini API calls, so the use of LLMs in this competition was hardly a secret.</p>

<p>The key is knowing enough to have a productive conversation. I shared context about my data, my validation scheme, and my methodology decisions. In return the models offered approaches I had not considered, caught errors I had missed, and helped me think through problems from angles I would not have found on my own. This was not a workflow where the human is in charge and the AI is a servant. It was a genuine collaboration, and knowing when to trust the output versus when to push back is itself a skill. A skill soon to be in more demand than many people realize today.</p>

<p>That skill comes from experience. Graduate-level coursework in statistics, machine learning, and data engineering gave me the foundation to evaluate what the tools were telling me. I knew when the output was good, when it was plausible but wrong, and when to ask again.</p>

<p>LLMs did not finish 21st at Kaggle. I did. The tools helped me get there faster.</p>

<h2>Lessons Learned and What's Next</h2>

<p>A few things I want to do differently next year.</p>

<p>HistGradientBoosting earned 1-3% ensemble weight across both genders. That is not a model contributing signal, that is a model taking up compute time. Next year it gets dropped or rebuilt from scratch with a fundamentally different approach. Five models sounds impressive. Four well-tuned models beat five redundant ones every time.</p>

<p>Massey Ordinals are sitting in the Kaggle data and I never used them. They represent a rich source of cross-season team quality rankings compiled by people who think about this more carefully than I do. That is low-hanging fruit I plan to pick next year.</p>

<p>Multiple seeds per model is something I want to explore. The 10th place solution this year used six random seeds per model and averaged the results. If LightGBM is performing well, how much of that is the model and how much is a fortunate random seed? Running multiple seeds adds diversity without adding new models, and the compute cost is manageable.</p>

<p>I also want to incorporate Polymarket data. Prediction markets aggregate the collective judgment of people with money on the line, which is a different and potentially complementary signal to anything a model trained on box scores can produce. Whether that signal survives feature selection is an open question, but it is worth finding out.</p>

<p>And the upset injection proof is now a permanent part of my toolkit. Not because I needed a mathematical proof to tell me to trust my model, but because having one means I will never second-guess it again in the heat of the tournament. There is something freeing about knowing the math is on your side.</p>

<p>What this competition reinforced for me is that good modeling is less about clever ideas and more about disciplined execution. Validation that matches reality, features that reflect the problem, and systems which combine models intelligently.</p>

<p>21st place is a good result, but not a finished result. I will be back next March with better features, a cleaner ensemble, and if Duke does not choke (again), a better result.</p>