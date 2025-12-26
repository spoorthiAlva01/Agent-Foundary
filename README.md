# Agent-Foundry 🧠⚙️

A **deterministic, multi-agent analytics system** that demonstrates how to design agentic architectures *without depending on always-on LLMs*.

This project focuses on **architecture, contracts, and agent boundaries** first, with Large Language Models treated as *optional, swappable components*.

---

## 🚀 What Problem Does This Solve?

Most "AI agent" projects tightly couple business logic to an LLM.
This makes systems:

* brittle
* hard to test
* difficult to reason about
* expensive to run

**Agent-Foundry takes a different approach**:

> Design a reliable system that works deterministically — and *enhance* it with LLMs, instead of *depending* on them.

---

## 🧩 High-Level Architecture

```
User Input
   ↓
Planner Agent (what to do)
   ↓
Executor Agent (how to do it)
   ↓
Recommendation Agent (what it means)
   ↓
Critic Agent (is it good?)
```

Each agent has a **single responsibility** and communicates using **explicit schemas**.

---

## 🤖 Agents Overview

### 1️⃣ PlannerAgent

**Responsibility:** Decide *what actions* should be taken.

* Accepts user intent
* Produces a **structured plan**
* Output validated via Pydantic schema
* Deterministic by default (FakeLLM)

**Why this matters:**

* Prevents free-form hallucinated workflows
* Isolates intent parsing from execution

---

### 2️⃣ ExecutorAgent

**Responsibility:** Execute the plan using tools.

* No LLM dependency
* Uses a Tool Registry
* Each tool is isolated and testable

**Why this matters:**

* Failures are contained
* Execution is predictable
* Tools can be swapped or extended

---

### 3️⃣ RecommendationAgent

**Responsibility:** Interpret execution results and generate insights.

* Uses deterministic heuristics
* Produces structured recommendations
* Assigns **confidence scores** based on signal strength and severity

**Confidence is heuristic-based**, not probabilistic:

* Strong signal → higher confidence
* Weak or generic insight → lower confidence

This keeps recommendations explainable and debuggable.

---

### 4️⃣ CriticAgent

**Responsibility:** Evaluate recommendation quality.

The Critic **does not generate ideas**.
It acts as a **quality gate**.

Evaluation criteria:

* Clarity (is it actionable?)
* Confidence threshold
* Minimum specificity

Verdicts:

* `accept`
* `revise`
* `reject`

**Why this matters:**

* Separates generation from evaluation
* Prevents low-quality outputs from propagating

---

## 🧠 Why No Real LLM by Default?

LLMs are powerful — but unreliable dependencies.

This project intentionally:

* isolates LLMs behind an interface
* provides a FakeLLM for deterministic operation
* avoids blocking development on API quotas or rate limits

> In production systems, **architecture outlives models**.

When a real LLM is available:

* it plugs into the same interface
* no agent logic needs to change

---

## 🧪 Deterministic First, Probabilistic Later

| Layer       | Deterministic | LLM-ready |
| ----------- | ------------- | --------- |
| Planner     | ✅             | 🔜        |
| Executor    | ✅             | ❌         |
| Recommender | ✅             | 🔜        |
| Critic      | ✅             | 🔜        |

This mirrors real-world system evolution:

1. Rule-based
2. Hybrid
3. Learned

---

## 📂 Project Structure

```
agents/
 ├─ planner.py
 ├─ executor.py
 ├─ recommender.py
 ├─ critic.py

core/
 ├─ fake_llm.py
 ├─ planner_schema.py
 ├─ recommendation_schema.py
 ├─ critic_schema.py

tools/
 ├─ registry.py
 ├─ fetch_data.py
 ├─ analyze_data.py

main.py
```

---

## ▶️ Running the Project

```bash
python main.py
```

Sample output flow:

```
=== PLAN ===
...

=== EXECUTION RESULT ===
...

=== RECOMMENDATIONS ===
- Improve ad creatives and messaging (0.8)

=== CRITIC REVIEW ===
Verdict: accept
```

---

## 🧠 Design Principles Demonstrated

* Single Responsibility per agent
* Explicit contracts (schemas)
* Deterministic execution
* LLMs as replaceable components
* Explainable decision-making

---

## 🔮 Future Extensions

* Plug-in real LLMs (Gemini / OpenAI / HF)
* Multi-candidate recommendation generation
* Critic-driven revision loops
* Learned confidence scoring
* Policy-based recommendation filters


---

## 📌 Key Takeaway

> **Good agent systems are built on architecture — not prompts.**

Agent-Foundry is designed to prove exactly that.
