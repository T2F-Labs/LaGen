# Chapter6-new — Against-Document
# Every section of the current chapter mapped to what must change

**Legend:**
- `[REMOVE]` — delete entirely, content is wrong or fabricated
- `[MODIFY]` — keep the section but rewrite the content
- `[ADD]` — new section/subsection that does not exist yet
- `[MOVE]` — relocate to a different position in the chapter

---

## CHAPTER STRUCTURE — TOP LEVEL

### [MODIFY] Overall chapter organization

The current chapter has 6 top-level sections:
- 4.1 FQT/FQG
- 4.2 Multi-Agent Architecture
- 4.3 Database and Storage
- 4.4 UI
- 4.5 Testing and Deployment
- 4.6 Evaluation

The new chapter must be reorganized as follows:
- 4.1 System Architecture and Boundaries  ← NEW
- 4.2 The Conductor — RL Agent Design     ← replaces old 4.1 + parts of 4.2
- 4.3 Function Quest Generator (FQG)      ← replaces old 4.1
- 4.4 Storage and Artifact Management     ← replaces old 4.3 (stripped down)
- 4.5 User Interface                      ← old 4.4 (modified)
- 4.6 Testing Strategy                    ← old 4.5 (stripped to what was actually done)
- 4.7 Evaluation                          ← old 4.6 (rewritten with real data)

Rationale: The current structure buries the most novel contribution (the RL agent,
the training environment, the model family) inside a generic "FQT" section and
a vague "multi-agent" section. The new structure leads with the architecture,
then the Conductor, then FQG as its training environment.

---

---

## SECTION 4.1 — "Function Quest Training Architecture" (current)

### [REMOVE] 4.1.1 "Core Implementation Principles" — Functional Abstraction / Progressive Complexity / Transfer Learning Design

These three bullets describe generic RL training principles with no specificity.
"Functional Abstraction", "Progressive Complexity", "Transfer Learning Design" are
marketing language, not implementation description. The actual principles are:
the FQG challenge YAML schema, the three-tier curriculum (Farid/Darwish/Baleegh),
and the sim-to-real bridge via adapter parity. None of those appear here.
Delete and replace with the real architecture description in the new 4.3.

### [REMOVE] Table 4.1 — "Quest Difficulty Progression"

The table (Beginner/Intermediate/Advanced/Expert with "2-3 functions", "4-6 functions"
etc.) is fabricated. The real FQG uses named difficulty levels tied to the
`ComplexityType` enum: `easy`, `medium`, `hard`, mapped to FQG levels (level1,
level2, ...). The success rate targets in the table are also wrong — the real
targets come from the curriculum progression thresholds in the training loop spec.
Delete entirely.

### [REMOVE] 4.1.2 "Reinforcement Learning Integration" — entire subsection

This subsection describes a reward table with made-up values:
"Task Completion +100", "Efficiency Bonus +10 to +50", "Error Penalty -20",
"Exploration Reward +5", "Resource Efficiency +15 to +30".
None of these match the actual 8-term reward function. The real reward has:
production reward (±1.0), artifact quality × credibility, VOID chain signal,
cardinality compliance, optional exploration, required retry penalty, step penalty
(−0.01), and timeout modifier. The completion bonus is 7.0–10.0, not "+100".
The entire subsection must be deleted and replaced in the new 4.2 (Conductor section).

### [REMOVE] Table 4.2 — "Reward Function Components"

Fabricated. See above. Delete.

### [MODIFY] 4.1.2 "State Representation" bullet list

The five bullets (Available Functions, Current Artifacts, Resource State,
Goal Conditions, Execution History) are directionally correct but vague and
incomplete. The real state has exactly five named components with precise tensor
shapes:
- query: (batch, 64) — enriched by DeepSeek, immutable during episode
- fqt: (batch, 25, 64) — per-extension embeddings, unordered set
- artifact_pool: (batch, 50, 70) — 4-dim one-hot type + melody_score + overall_score + 64-dim produced_by embedding
- call_history: (batch, 50, 66) — GRU-encoded sequence of (ext_id_emb, success, step_norm)
- step_count: (batch,) — normalized to [0,1]

Rewrite as a proper state space description in the new 4.2.2.
"Resource State" and "Goal Conditions" do not exist as state components — remove them.

### [REMOVE] 4.1.3 "Automated Quest Generation System" — "Three-Stage Generation Pipeline" heading

The heading exists but the content is missing (the PDF has a gap here).
The real FQG generation pipeline is: challenge YAML authoring with the schema
(meta, query, extensions, paths blocks), the `FQGGenerator` for automated
generation, and `ChallengeValidator` for validation. Replace with real description.

### [REMOVE] Table 4.3 — "Adaptive Generation Parameters"

Fabricated metrics (Success Rate 70-85%, Completion Time 2-5 minutes, etc.).
FQG does not have a real-time adaptive difficulty scaler of this kind.
The real adaptation mechanism is curriculum progression: the training loop
unlocks the next level when `eval_results[level].success_rate > progression_threshold`.
Delete the table. Describe curriculum progression correctly in 4.2.

### [REMOVE] 4.1.4 "Artifact Store Integration" — entire subsection

This subsection describes SHA-256 content-addressable storage and Tantivy search
as part of FQG. This is wrong on two counts:
1. The Artifact Store is a Rust component (The Pit), not part of FQG.
2. FQG does not use SHA-256 CAS or Tantivy. FQG stores challenges as YAML files
   in `.fqg/game/<tier>/levels/` and embeddings in an EmbeddingStore.
Delete entirely. The Artifact Store gets its own correct description in new 4.4.

### [REMOVE] Table 4.4 — "FQT Performance Comparison"

"Traditional Training 67% → FQT 89%", "Learning Speed 450 → 180 episodes" etc.
These numbers are fabricated. No such comparison was run.
Delete. The evaluation section (4.7) will contain only real or design-target numbers.

### [REMOVE] 4.1.5 "Scalability and Performance" metrics

"1,200+ quests per hour", "0.3-0.8ms retrieval latency", "50+ concurrent training
sessions", "34% storage reduction" — all fabricated. Delete.

### [REMOVE] 4.1.6 "Research Contributions and Implications" — entire subsection

"First application of puzzle-game mechanics", "60% faster learning", "84% skill
transfer quality" — fabricated claims with no backing data.
The real research contributions of FQG are: the challenge YAML schema as a
declarative training environment specification, the `ScorerProtocol` injection
pattern (custom reward without FQG changes), the adapter parity invariant
(FQGAdapter and ProductionAdapter produce bit-identical tensors), and the
`preferred_usage` soft logit bias mechanism. None of these appear in the current text.
Delete and replace with accurate contributions in the new 4.3.

---

---

## SECTION 4.2 — "Multi-Agent Architecture Implementation" (current)

### [REMOVE] 4.2 opening paragraph — "compared to single-model approaches"

The opening sentence fragment ("compared to single-model approaches, while providing
better fault tolerance and scalability") is a dangling sentence with no context.
The entire framing of this section as a "multi-agent system" is misleading.
Symphony is not a peer-to-peer multi-agent system. It is a hierarchical system:
DeepSeek (LLM) → Conductor (RL agent) → Extensions (tools). The Conductor is
not one of six equal agents. It is the orchestrator. Delete the framing.

### [REMOVE] 4.2.1 "Architectural Design Principles" — Specialization / Coordination / Resilience

These three principles are generic software engineering platitudes.
The real architectural principles are the language responsibility split:
Python owns RL policy, embeddings, reward computation, DeepSeek integration.
Rust owns filesystem, process lifecycle, resource management, IPC routing.
The boundary is PyO3 FFI (~50ns) for in-process Rust (The Pit) and Unix sockets
(~0.3ms) for out-of-process extensions. None of this appears in the current text.
Delete and replace with the system boundaries description in new 4.1.

### [REMOVE] Table 4.5 — "Agent Specialization Domains"

The six agents (Enhancer-Prompt, Feature, Planner, Coordinator, Code-Visualizer,
Code-Editor) are described as equal peers. This is wrong. The real system has:
- DeepSeek: query enrichment, FQT selection, classification, post-execution summary
- Conductor: RL policy, orchestration decisions, artifact pool management
- Extensions: atomic tools called by the Conductor (prompt_enhancer, code_implementer,
  test_generator, git_committer, documentation_writer for Farid v1)
The "Coordinator" and "Planner" agents do not exist as separate components.
Delete the table entirely.

### [REMOVE] 4.2.2 "Enhancer-Prompt Agent Implementation" — NLP Pipeline, Context Enrichment, etc.

This describes a standalone NLP agent. In reality, prompt enhancement is one
extension (`prompt_enhancer`) that the Conductor may or may not call depending
on the FQT. It is not a separate architectural component with its own NLP pipeline.
Delete. The extension concept is described correctly in new 4.2 (Conductor section)
under the action space description.

### [REMOVE] Table 4.6 — "Enhancer-Prompt Agent Performance"

Fabricated metrics. Delete.

### [REMOVE] 4.2.2 "Feature Agent", "Planner Agent", "Code-Editor Agent" subsections

Same reason as above. These are extensions, not architectural agents.
The Code-Editor description ("Multi-Language Support", "Framework Integration") is
a description of what an extension does, not how the Conductor orchestrates it.
Delete all three.

### [REMOVE] 4.2.3 "Inter-Agent Communication Implementation" — entire subsection

The "layered protocol architecture" (Application/Session/Transport/Network layers)
and the six message types (Task Request, Status Update, etc.) describe a generic
distributed system. The real communication architecture is:
- DeepSeek → Conductor: direct Python function call (same process, no IPC)
- Conductor → The Pit (Rust): PyO3 FFI, direct in-process call, ~50ns
- Conductor → out-of-process extensions: IPC Bus via Unix sockets, ~0.3ms
- Extension Runner → Extension: sandboxed subprocess
There is no "Session layer" or "Transport layer". Delete entirely.

### [REMOVE] Table 4.7 — "Communication Protocol Stack"

Fabricated. Delete.

### [REMOVE] 4.2.4 "Collaboration Pattern Implementation" — Sequential/Parallel/Hierarchical/Peer-to-Peer

These four patterns (pipeline, fork-join, manager-worker, consensus) describe
generic distributed computing patterns. The Conductor does not implement these
as explicit patterns. The Conductor selects one extension per step based on its
policy — the "collaboration pattern" emerges from the learned policy, not from
a hardcoded pattern selector. Delete entirely.

### [REMOVE] Table 4.8 — "Consensus Decision Making"

Fabricated. The Conductor does not use consensus voting. Delete.

### [REMOVE] 4.2.5 "Fault Tolerance Implementation" — Heartbeat Monitoring, Timeout Management, etc.

The fault tolerance described here (heartbeat monitoring, warm/cold standby) is
for a distributed microservices system. The real fault tolerance in the Conductor is:
- Required extension failure → retry up to MAX_RETRIES=3, then mark exhausted
- Repetition loop detection → force-break with −3.0 penalty (Farid)
- Step cap hit → bootstrap GAE with V(s), not 0
- Extension timeout → apply −0.3 modifier to melody_score, episode continues
- Cancellation flag → checked at start of each step
Delete the current content. The real fault handling belongs in the reward function
description (new 4.2.4) and the termination semantics description (new 4.2.5).

### [REMOVE] Table 4.9 — "Agent Redundancy and Recovery"

"Conductor: Hot standby <1 second", "Planner: Cold standby <30 seconds" — fabricated.
The Conductor is a single RL model, not a redundant service. Delete.

### [REMOVE] Tables 4.10, 4.11 — "Individual Agent Performance", "Collaboration Pattern Performance"

All numbers fabricated. "Enhancer-Prompt: 92% accuracy, 450 specs/hour" etc.
Delete both tables.

### [REMOVE] 4.2.7 "Research Contributions" — "25% performance improvement through specialization" etc.

All percentage claims are fabricated. Delete.

---

---

## SECTION 4.3 — "Hybrid Database Architecture" (current)

### [REMOVE] 4.3.1 "Hybrid Database Architecture" — SQLite + Sled / DuckDB + redb

The entire hybrid database framing is wrong. The system does not use SQLite,
DuckDB, Sled, or redb. The actual storage architecture is:
- The Pit (Rust, in-process via PyO3): Pool Manager, DAG Tracker, Artifact Store,
  Arbitration Engine, Stale Manager
- Artifact Store writes to `.symphony/pool/cache/<session_id>/` on the filesystem
- Melody memory stored as plain JSON (~1-2KB per melody)
- Polyphony server for melody sharing (HTTP, handled by Rust Artifact Store)
Delete the entire hybrid database framing.

### [REMOVE] Table 4.12 — "Hybrid Architecture Workload Distribution"

Fabricated. Delete.

### [REMOVE] Table 4.13 — "Hybrid Configuration Performance Comparison"

"SQLite + Sled: 78ms avg", "DuckDB + redb: 45ms avg" — fabricated, wrong technology.
Delete.

### [MODIFY] 4.3.2 "Content-Addressable Artifact Store" — keep concept, rewrite content

The concept of a content-addressable artifact store is correct — the Artifact Store
does persist artifacts with unique IDs. However:
- It is NOT SHA-256 based in the current design. Artifacts are identified by
  session-scoped integer IDs (artifact_0, artifact_1, etc.)
- It is a Rust component (The Pit), not a Python component
- Python must never touch the filesystem directly — all storage goes through
  PyO3 FFI calls to the Rust Artifact Store
- The metadata.json schema is defined: id, type, produced_by, melody_score,
  overall_score, timestamp, path, size_bytes
- Cleanup schedule: session ends → 1 month → cloud archive → 6 months → deleted

Rewrite to describe the actual Rust Artifact Store, its FFI interface, and the
real filesystem layout. Remove SHA-256 claims.

### [REMOVE] Table 4.14 — "Content Deduplication Analysis"

"Training Quests 85% duplication rate, 80-90% storage reduction" — fabricated.
The Artifact Store does not deduplicate by content hash. Delete.

### [REMOVE] 4.3.3 "Quality Scoring and Metadata Management" — Static Code Analysis, Test Coverage, etc.

The quality scoring described here (static analysis, test coverage, performance
profiling, documentation quality) is not how melody_score and overall_score work.
The real quality scores are:
- melody_score: computed inside the extension after artifact production, measuring
  relevance to the current workflow (type match, semantic similarity, field coverage,
  format validity). Range [0,1].
- overall_score: historical aggregate of melody_score across all past workflows,
  exponentially weighted toward recent runs (decay=0.95). New extensions start at 0.7.
- credibility: cross-melody necessity measure. In-house extensions start at 70%,
  marketplace at 50%. Multiplies melody_score in the reward formula.
Delete the current content. Replace with real score definitions in new 4.4.

### [REMOVE] Table 4.15 — "Quality Assessment Framework"

"Functional Correctness 40%, Technical Quality 30%" etc. — fabricated weighting
scheme unrelated to melody_score. Delete.

### [REMOVE] 4.3.4 "Resource Optimization Implementation" — ML-driven predictive allocation

"Usage Pattern Learning", "Context-Aware Prediction", "Confidence-Based Decisions"
describe a hypothetical ML resource allocator. The real Pool Manager is a Rust
component that manages extension process lifecycle. The 50-100ns allocation time
mentioned is for PyO3 FFI calls, not ML prediction. The "Player Extension State
Management" paragraph mixes up terminology (Instruments, Operators, Motifs are
extension categories, not Pool Manager internals).
Delete the ML prediction framing. Keep a brief accurate description of the Pool
Manager's role in new 4.4.

### [REMOVE] Table 4.16 — "Predictive Allocation Performance"

"5 minutes horizon: 92% accuracy, 65% latency reduction" — fabricated. Delete.

### [REMOVE] 4.3.5 "Search and Discovery Implementation" — Tantivy integration

Tantivy is mentioned as part of the Artifact Store. This is not confirmed in the
current implementation. The Conductor does not search artifacts by text query —
it reasons from artifact metadata (type, melody_score, overall_score, produced_by)
encoded as tensors. Melody memory lookup uses cosine similarity on query embeddings,
not Tantivy. Delete or defer to a future work note.

### [REMOVE] Table 4.17 — "Search Performance Metrics"

Fabricated. Delete.

### [REMOVE] 4.3.6 "Cache Consistency and Data Management" — TTL, read-through cache, etc.

This describes a generic caching layer. The real caching in the system is:
- Python-side in-memory encoding cache in MelodyMemory (_encoding_cache), cleared
  on restart
- The Rust Artifact Store handles persistence; Python never caches to disk
Delete the generic cache consistency description.

### [REMOVE] Table 4.18 — "Cache Invalidation Strategies"

Fabricated. Delete.

### [REMOVE] 4.3.7 "Performance Evaluation" — 1000+ concurrent workflows, 500+ queries/second

All throughput numbers are fabricated. Delete.

### [REMOVE] 4.3.8 "Research Contributions" — "2.3x throughput improvement", "34% storage reduction"

Fabricated claims. Delete.

---

---

## SECTION 4.4 — "UI Implementation" (current)

### [MODIFY] 4.4.1 "AI-First Interaction Paradigm" — keep framing, update content

The three principles (Intent-Driven, Transparent Orchestration, Progressive Disclosure)
are reasonable and can stay. Table 4.20 (Traditional IDE vs Symphony) is acceptable
in concept but needs to reflect the real modes: Maestro/Virtuoso/Solo, not generic
"Natural language prompt vs Code editor". Update the table to use real mode names
and real interaction differences.

### [MODIFY] 4.4.2 "Triple-Mode Architecture" — keep structure, fix descriptions

Maestro/Virtuoso/Solo mode names are correct. The descriptions need updating:
- Maestro Mode: full Conductor orchestration, DeepSeek conversation, Harmony Board
  access, ConductorReport review after episode
- Virtuoso Mode: traditional editor + inline AI assistance, direct extension calls
- Solo Mode: lightweight, quick queries, no full orchestration
The current descriptions are directionally correct but too generic. Update.

### [MODIFY] 4.4.3 "Harmony Board Implementation" — keep concept, fix architecture

The Harmony Board as a visual workflow composition interface is correct.
However the implementation detail needs updating:
- It is an out-of-process Rust extension, not a React-only component
- It communicates with the Python layer via the IPC Bus (Unix sockets)
- The React frontend renders a Virtual DOM from the Rust extension's output
- Node-based visual programming with React Flow is correct
Table 4.21 component architecture is acceptable but must note the Rust/React split.

### [MODIFY] 4.4.4 "Visualization and Feedback Systems" — keep concept, add ConductorReport detail

The orchestration visualization concept is correct. Add:
- The ConductorReport is the primary data source for post-episode visualization
- Per-step StepOutput fields: selected_extension, action_confidence (softmax score,
  NOT a calibrated probability), artifact_quality, is_fallback flag
- EpisodeDebugRecord (~2KB) persisted alongside artifacts for replay
- The behavioral fingerprint (required_coverage, noise_call_rate, path_diversity)
  is the primary explainability mechanism for ML engineers
- action_confidence must be labeled "softmax score" everywhere in the UI —
  never "probability"

### [REMOVE] 4.4.5 "Performance Optimization" — Virtual Scrolling, Web Workers, etc.

These are generic React performance techniques. Table 4.23 ("Keystroke Response
8-12ms", "AI Suggestion Display 150-180ms") is fabricated. Delete the fabricated
numbers. Keep a brief mention of standard React optimization techniques without
specific unverified metrics.

### [REMOVE] 4.4.6 "User Experience Evaluation" — "50 developers over 4 weeks"

No such user study was conducted. Delete the study claims. The interaction pattern
table (Table 4.24) is fabricated. Delete.

### [MODIFY] 4.4.7 "Research Contributions" — rewrite

Remove fabricated HCI contribution claims. The real UI contribution is the
ConductorReport visualization layer and the three-audience explainability design:
ML engineer (TensorBoard), domain expert (call_history + artifact quality),
end user (DeepSeek summary — Conductor is invisible to the user).

---

## SECTION 4.5 — "Testing and Deployment" (current)

### [MODIFY] 4.5.1 "AI-First Testing Methodology" — keep framing, fix test counts

The five-layer testing pyramid concept is correct and matches the real test
structure (unit/rl/integration/acceptance). However:
- Table 4.25 test counts are fabricated ("2,100 foundation tests", "150 emergent")
- The real test suite has 7 invariant tests that are the primary quality gates:
  1. Adapter parity (FQGAdapter == ProductionAdapter, torch.equal not allclose)
  2. Masking correctness (softmax(apply_mask(logits, mask))[invalid] == 0.0 exactly)
  3. GAE ordering (good episode advantages > bad episode advantages)
  4. Set encoder empty pool (returns learned empty_token, not zeros)
  5. Sequence encoder packing (padded history == unpadded history for same lengths)
  6. Normalizer round-trip (save/load produces identical normalization)
  7. Checkpoint parity (loaded model produces bit-identical outputs)
Replace fabricated counts with the real 7-invariant structure.

### [REMOVE] "Probabilistic Quality Validation" — Statistical Quality Bounds, Confidence Correlation

These describe a hypothetical probabilistic testing framework. The real approach
uses Hypothesis (property-based testing) for GAE mathematical properties:
- advantages are finite for any valid input
- GAE is linear in rewards (scaling rewards scales advantages proportionally)
Replace with accurate description of Hypothesis-based property testing.

### [REMOVE] 4.5.2 "Multi-Agent Orchestration Testing" — Coordination Pattern Testing, etc.

The "emergent behavior validation" and Table 4.26 test results are fabricated.
The real integration tests are:
- test_adapter_parity.py — the architectural invariant test
- test_checkpoint_parity.py — loaded model produces bit-identical outputs
- test_reward_tracker_integration.py — reward component breakdown visible from step 1
- test_supervised_pretraining_integration.py — >80% accuracy gate
- test_full_episode.py (acceptance) — ConductorAgent.run() returns a valid report
Delete the fabricated multi-agent testing content.

### [REMOVE] 4.5.3 "Performance and Quality Metrics" — 45 functional metrics, 35 performance metrics, etc.

These metric counts are fabricated. Delete. Replace with the real monitoring
components: RewardTracker (completion bonus fraction alert), GradientMonitorCallback
(NaN detection, per-step norm logging), KLMonitor (log-only for Farid), BiasAuditor
(pre-training data quality checks).

### [REMOVE] Table 4.27 — "Quality Monitoring Automation"

Fabricated. Delete.

### [REMOVE] 4.5.4 "Deployment Architecture" — Tiered AI Model Distribution

"Core Model Tier: 35MB", "Community Tier: decentralized networks" — fabricated
deployment architecture. The real deployment is the phased rollout plan:
Phase 0 (staging, 10 dummy extensions), Phase 1 (internal dogfooding, 5 in-house
extensions), Phase 2 (limited beta, 50 users), Phase 3 (public launch).
Replace with the real phased deployment description.

### [REMOVE] Table 4.28 — "Cross-Platform Deployment Performance"

"Windows x64: 142MB, 94% AI Performance" — fabricated. Delete.

### [REMOVE] 4.5.5 "Intelligent Update Orchestration" — entire subsection

Fabricated. The system does not have a custom update orchestration protocol.
Delete.

### [REMOVE] 4.5.6 "Distribution Strategies" — Multi-Channel Distribution, Tables 4.29, 4.30

All fabricated. "Direct Download 45% adoption", "Security Incident Rate 0.01%"
etc. Delete entirely.

### [MODIFY] 4.5.7 "CI/CD Pipeline" — keep concept, remove fabricated numbers

"All 4,390 tests run on every commit" is fabricated. The real CI gate is:
adapter parity test runs on every commit (the architectural invariant).
Keep the concept of automated testing gates. Remove the specific fabricated count.

### [REMOVE] 4.5.8 "Research Contributions" — Probabilistic Testing Framework, Tiered AI Distribution

All fabricated contribution claims. Delete.

---

---

## SECTION 4.6 — "Evaluation" (current)

### [REMOVE] Table 4.31 — "Evaluation Methodology Overview"

"10,000+ test runs", "50 developers", "5 competing IDEs" — fabricated.
Delete the table. Replace with honest description of what was actually evaluated:
the 7 invariant tests, the training loop smoke tests (CPU, 5-step verification),
and the design-target metrics from the steering specs.

### [REMOVE] 4.6.2 "System Performance Benchmarks" — Table 4.32

"Startup Time 1.2s (40% better than target)", "IPC Latency 0.3ms (70% better)"
etc. — fabricated benchmark results. The 0.3ms IPC latency is from the system
design spec, not a measured result. Delete the "Measured" column or clearly
label these as design targets, not measurements.

### [REMOVE] 4.6.2 "AI Orchestration Performance" — "8.2s average for 7-model workflow"

Fabricated. No such measurement was taken. Delete.

### [REMOVE] 4.6.3 "Comparative Analysis" — Table 4.33 IDE comparison

"Symphony 1.2s startup vs VSCode 2.8s vs Cursor 3.2s" — fabricated comparison.
No benchmarking against other IDEs was conducted. Delete entirely.

### [REMOVE] 4.6.4 "User Experience Evaluation" — "50 developers over 4 weeks", Tables 4.34

No user study was conducted. All productivity numbers (33% faster feature
development, 50% faster documentation) are fabricated. Delete entirely.

### [REMOVE] 4.6.5 "Scalability Evaluation" — Table 4.35

"1000 concurrent users: 2.8s avg response, 0.3% error rate" — fabricated load
test results. Delete.

### [MODIFY] 4.6.6 "Training System Evaluation" — rewrite with real targets

The current content (Table 4.36: "FQT 89% success rate vs Traditional 67%") is
fabricated. Replace with the real production-ready criteria from the training spec:
- Success rate > 60% on final level eval_set
- Efficiency > 0.70 (total_score / max_achievable)
- Stable for 500+ updates (moving avg change < 0.03 over 100 updates)
- Dead extension rate < 20%
- Completion bonus < 60% of total reward (proxy gaming detection)
- No NaN gradients at any point
- Checkpoint save/load produces bit-identical outputs
Label these clearly as design targets / success criteria, not measured results.

### [REMOVE] 4.6.7 "Database Implementation Evaluation" — Table 4.37

Fabricated database performance numbers. Delete.

### [MODIFY] 4.6.8 "Limitations and Future Work" — rewrite with real limitations

The current limitations (AI Model Diversity, Learning Curve, Offline Capabilities,
Language Support) are generic and not specific to this system.
The real known limitations and deferred items are:
- Tier 3 extension confidence threshold enforcement deferred to Darwish
- Artifact consumption tracking (Term 3 of reward) deferred to Darwish
- Per-step OOD detection deferred to Darwish
- Softmax → calibrated probability (temperature scaling) deferred to Darwish
- DeepSeek post-execution feedback loop into training deferred to Darwish
- Counterfactual explanation deferred to Darwish
- Full StateVector replay surface deferred to Darwish
- Baleegh: DeepSeek hidden state integration, multilingual manifest encoding
- Permission-based exclusion classification criteria (TBD in production spec)
- DeepSeek strictness dial (strict vs flexible FQT) — mechanism TBD

Future work directions:
- Darwish tier: trainable encoder, auto KL adjustment, larger architecture
- Baleegh tier: DeepSeek hidden state gating, enterprise workflows
- Melody memory: Polyphony marketplace, lineage tracking
- Temporal decay and retraining protocol (6-month floor, PSI > 0.2 trigger)
- Champion/challenger deployment (10% traffic for 48h before full promotion)

### [REMOVE] 4.6.9 "Research Contributions Summary" — empty section

The section heading exists but content is missing in the PDF. Delete the empty
heading. Contributions are listed in each subsection.

### [MODIFY] 4.6.10 "Conclusion" — rewrite

Remove fabricated achievement bullets ("40% faster startup", "70% lower IPC
latency", "4.2/5.0 satisfaction", "99.1% reliability"). Replace with honest
summary of what was designed and implemented: the Conductor RL agent (Farid v1,
210K parameters), the FQG training environment, the adapter parity invariant,
the 8-term reward function, the three-tier model family design, and the
production deployment plan.

---

---

## NEW SECTIONS TO ADD (do not exist in current chapter)

### [ADD] New 4.1 — "System Architecture and Boundaries"

This section does not exist at all in the current chapter. It must be added first
because everything else depends on understanding the architecture.

Must cover:
- The four-layer architecture diagram: React UI → out-of-process Rust extensions
  → IPC Bus → Python process (DeepSeek + Conductor + The Pit via PyO3)
- Language responsibility table: Python owns RL policy / embeddings / reward /
  DeepSeek integration. Rust owns filesystem / process lifecycle / resource
  management / IPC routing.
- The two boundaries: PyO3 FFI (~50ns, in-process) for The Pit; Unix sockets
  (~0.3ms) via IPC Bus for user-facing extensions
- The hard boundary rules: Python never touches filesystem. Rust never computes
  embeddings. IPC Bus never makes orchestration decisions.
- The DeepSeek → Conductor handoff: direct Python function call (same process),
  async tool call pattern, "Conductor is working..." status, callback on completion
- Data flow for a single orchestration step (the 5-step sequence: build state →
  policy forward pass → execute action via IPC → store artifact via FFI →
  compute reward in Python)

### [ADD] New 4.2 — "The Conductor: RL Agent Design and Implementation"

This is the core contribution section. Must cover:

**4.2.1 — The Model Family (Farid / Darwish / Baleegh)**
- Three tiers named after musical tempos: Farid (lively/fast), Darwish (walking
  pace), Baleegh (majestic/grand)
- Farid: embedding_size=64, GRU hidden=128, FFN=[256,128], frozen all-MiniLM-L6-v2
  encoder, targets simple-to-medium workflows, 210K parameters
- Darwish: embedding_size=128, GRU hidden=256, FFN=[512,256], trainable encoder
  (encoder LR=1e-5, Conductor LR=3e-4)
- Baleegh: embedding_size=256, GRU hidden=512, FFN=[1024,512,256], DeepSeek hidden
  state (4096-dim) + trainable encoder via learned gating
- Three types of change: architecture change → major version + retrain from scratch;
  size change → different tier, retrain; improvement → minor version, fine-tune
- Versioning rule: version number must communicate exactly what kind of change happened

**4.2.2 — State Space**
- Five components with exact tensor shapes (Farid v1):
  query (batch,64), fqt (batch,25,64), artifact_pool (batch,50,70),
  call_history (batch,50,66), step_count (batch,) normalized [0,1]
- Query: immutable during episode, enriched by DeepSeek, inserted into artifact
  pool at step 0
- FQT: unordered set, max 25 extensions, static during episode
- Artifact pool: each artifact encoded as [type_one_hot(4) | melody_score(1) |
  overall_score(1) | produced_by_embedding(64)] = 70-dim
- Call history: GRU-encoded, each step = [ext_id_emb(64) | success(1) | step_norm(1)] = 66-dim
- Step count: normalized to [0,1] by dividing by episode_cap (50)

**4.2.3 — Neural Network Architecture**
- Multi-input architecture: each state component has its own processing head
- Query head: Linear(128→64)
- FQT head: SetEncoder with masked mean pooling, produces summary (batch,64) +
  individual embeddings (batch,25,64)
- Artifact head: SetEncoder with learned empty_token for step 0
- History head: GRU with pack_padded_sequence, learned h0, orthogonal_ init for
  hidden-hidden weights, forget gate bias=1.0
- Step head: Linear(1→1) after normalization
- Combine: concat all heads → (batch,327) → LayerNorm → FFN [256,128] with GELU
- Shared trunk output: (batch,128) → actor head + critic head
- Actor: dot product state_repr @ FQT_individual.T → softmax (extension selector)
  + sigmoid (artifact selector, independent per artifact)
- Critic: Linear(128→64) → GELU → Linear(64→1), no softmax
- Action masking: invalid logits set to -inf before softmax, never 0
- Temperature schedule: 2.0 early → 1.0 mid → 0.5 late → argmax at eval

**4.2.4 — Reward Function**
- 8-term reward: production reward, artifact quality × credibility, VOID chain
  signal, cardinality compliance, optional exploration, required retry penalty,
  step penalty (−0.01), timeout modifier
- Terminal reward: completion bonus 7.0–10.0 (efficiency-scaled), or −1.0/−5.0
  for cap-hit cases
- Proxy declaration: reward is a proxy for orchestration quality, not quality
  itself. The behavioral fingerprint detects proxy gaming.
- Farid vs Baleegh differences: credibility formula, loop handling (force-break
  vs escalating penalty), exploration bias
- Reward normalization: RunningMeanStd (Welford's algorithm), state saved with
  checkpoint, loaded identically in production
- Dead extension exploration bonus: continuous decay formula, disabled at eval

**4.2.5 — Training Algorithm (PPO)**
- Three nested cycles: outer (curriculum), middle (evaluation every K updates),
  inner (episode collection + PPO update)
- PPO loss: actor (clipped ratio), critic (MSE, coeff=0.5), entropy bonus
  (coeff=0.01→0.001)
- GAE: per-batch normalization only, never per-episode
- Hyperparameters table: LR=3e-4, gamma=0.97 (Farid), GAE lambda=0.95,
  clip epsilon=0.2, batch=16 episodes, PPO epochs=4, parallel workers=16,
  eval every 10 updates
- Gradient safety: unscale_ before clip_grad_norm_, NaN detection stops training
- KL monitoring: log-only for Farid, thresholds (frozen<0.01, healthy 0.01-0.1,
  warning 0.1-0.5, critical>2.0)
- Linear LR schedule: start_factor=1.0, end_factor=0.1

**4.2.6 — Supervised Pre-training (Cold Start)**
- Run before PPO, must not be skipped
- Source: optimal paths from FQG challenge YAMLs (3-5 paths per challenge)
- Cross-entropy loss for extension selection, BCE for artifact selection
- Gate: >80% accuracy on training set before proceeding to PPO
- If <40% after pre-training: stop, fix data or loss function
- Data augmentation: shuffle optional extension order, add/remove optionals,
  vary artifact selection → 100 trajectories → 500-1000

**4.2.7 — Curriculum Progression**
- Start with Level 1 only
- Unlock Level 2 when success_rate > threshold for stability_window updates
- Keep Level 1 active at 50/50 mix when Level 2 unlocks (catastrophic forgetting
  prevention)
- Production-ready criteria: success_rate > 60%, efficiency > 0.70, stable 500+
  updates, dead extension rate < 20%

**4.2.8 — Action Space and Masking**
- Action = (extension_id, artifact_subset)
- Extension masking: invalid if depends_on not satisfied OR usage_limit exceeded
- Artifact selection: sigmoid, independent per artifact, threshold 0.5
- is_fallback field: populated when top-1 action was masked
- FQT classification: required/optional (query-relative, not extension-intrinsic),
  cardinality ("1", "1..n", "0..n"), preferred_usage (soft logit bias for optionals)
- Extension reversibility tiers: Tier 1 (read/analyze), Tier 2 (write/transform),
  Tier 3 (irreversible/broadcast) — declared in manifest, Tier 3 confidence gating
  deferred to Darwish

### [ADD] New 4.3 — "Function Quest Generator (FQG)"

Must cover:

**4.3.1 — Purpose and Design Philosophy**
- FQG is the training environment, not a production component
- Sim-to-real parity is the primary design constraint: FQGAdapter and
  ProductionAdapter must produce bit-identical tensors for equivalent logical states
- FQG owns encoding: the Conductor never encodes raw text, receives pre-computed
  embeddings via fqg.generate_embeddings()
- FQG mock extensions run inside the FQG Python process — never through IPC Bus

**4.3.2 — Challenge YAML Schema**
- Four blocks: meta (name, family, complexity, domain, tags), query (base, enhanced),
  extensions (id, description, required, score, returns, depends_on, cardinality,
  tool_calls, extra), paths (id, type, label, sequence, score)
- extensions[].extra: credibility, timeout_probability — FQG passes through without
  interpreting, Conductor owns the semantics
- paths block: optimal/known/unknown/failed path types, used for supervised
  pre-training and evaluation scoring
- preferred_usage on optional extensions: soft logit bias, not enforcement
- UnsafeFQTSizeError: raised if preferred_usage hints declared on <5 extensions

**4.3.3 — TorchRL Integration**
- Challenge implements TorchRL EnvBase interface
- Observation: TensorDict with typed specs (Bounded, Composite, UnboundedContinuous)
- Action: TensorDict with extension_id + optional artifact_indices
- step_info_extra: raw artifact list, termination_reason
- apply_mask: imported from fqg in training, own implementation in production
  (both parity-tested)
- ScorerProtocol: FaridReward injected via Challenge(config, scorer=FaridReward())

**4.3.4 — Adapter Parity Invariant**
- FQGAdapter (training) and ProductionAdapter (inference) are the only two callers
  of the vectorization layer
- Parity test uses torch.equal, not torch.allclose — no legitimate source of float
  drift between two Python functions on the same hardware
- This test runs on every commit as the CI gate
- AdapterBase: shared __init__ + _build_state_vector() extracted to eliminate
  duplication

**4.3.5 — Evaluation and Metrics**
- Held-out eval_set: fixed challenges, never trained on, noise-free
- EpisodeScore fields: success, efficiency, path_quality (optimal/known/unknown/failed),
  noise_avoidance, optional_precision, terminated_early, terminated_late
- Unknown paths: valid sequences not in ground truth — log and review for FQG addition
- Behavioral fingerprint: required_coverage > 0.95, noise_call_rate < 0.02,
  dependency_violation_rate == 0.0, path_diversity > 0.2

### [ADD] New 4.4 — "Storage and Artifact Management" (replaces old 4.3, stripped)

Must cover (briefly — this is not the primary contribution):
- The Pit: Rust in-process components (Pool Manager, DAG Tracker, Artifact Store,
  Arbitration Engine, Stale Manager), accessed via PyO3 FFI
- Artifact Store filesystem layout: .symphony/pool/cache/<session_id>/
- Artifact metadata schema (the real one from the production spec)
- melody_score and overall_score definitions (real formulas)
- Melody memory: JSON storage format (~1-2KB), symbolic not embedding-based,
  version-compatible via extension ID aliasing
- Polyphony: melody sharing via HTTP, handled by Rust Artifact Store
- EpisodeDebugRecord: ~2KB per episode, persisted for replay

---

---

## CROSS-CUTTING ISSUES (apply to the entire chapter)

### [MODIFY] All fabricated performance numbers

Every specific metric in the current chapter that is not sourced from an actual
measurement must be either:
a) Deleted
b) Replaced with the design target from the steering spec, clearly labeled as
   "design target" not "measured result"
c) Replaced with the actual measured value if one exists

Known actual measured values (from Phase 9 verification):
- Farid v1 model parameters: 210,389 trainable
- Training step verification: non-zero losses (0.28 → 0.047 over 5 steps)
- PyO3 FFI overhead: ~50ns (from system design spec, not measured)
- IPC Bus latency: ~0.3ms (from system design spec, not measured)
- Episode cap: 50 steps (hard cap, from ENV constants)
- Supervised pre-training gate: >80% accuracy (design target)
- PPO success rate target: >60% on final level eval_set (design target)

### [MODIFY] All references to "agents" as peers

Every place the current chapter says "agents collaborate", "agents communicate",
"agent consensus" must be rewritten. The system has one RL agent (the Conductor).
Extensions are tools, not agents. DeepSeek is an LLM layer, not an agent peer.
The word "agent" in this chapter should refer only to the Conductor.

### [REMOVE] All references to "Tantivy", "SQLite", "DuckDB", "Sled", "redb"

These technologies are not part of the implemented system. Remove all mentions.

### [REMOVE] All references to "SHA-256 content-addressable storage" as a Conductor feature

SHA-256 CAS is not how the Artifact Store works in the current design.
Remove all mentions.

### [ADD] Consistent use of real terminology throughout

The following terms must be used consistently and correctly:
- FQG (Function Quest Generator) — the training environment
- FQT (Function Quest Table) — the per-episode action space provided by DeepSeek
- Conductor — the RL agent (not "orchestrator agent" or "coordinator")
- Extension — an atomic tool (not "agent", not "model", not "function")
- Artifact — the output of an extension call
- melody_score — per-artifact relevance score for current workflow
- overall_score — historical quality aggregate for an extension
- credibility — cross-melody necessity measure
- The Pit — the Rust in-process components
- IPC Bus — the Unix socket message router for out-of-process extensions
- Farid/Darwish/Baleegh — the three model tiers (not "v1/v2/v3")
- ConductorReport — the output returned to DeepSeek after an episode
- Behavioral fingerprint — the proxy-gaming detection mechanism

### [ADD] Proxy declaration in reward section

The reward function section must include an explicit acknowledgment that the
reward is a proxy for orchestration quality, not quality itself. The gap between
the proxy and the goal must be stated. This is a research honesty requirement.

### [ADD] Autonomy budget statement

The chapter must state the autonomy level of the Conductor:
Level 2 — model acts, human reviews at episode end. Scope bounded by the FQT.
Magnitude bounded by the FQT. Horizon: 50 steps maximum. This is a research
contribution (explicit autonomy budgeting for RL agents in production).

---

## SUMMARY TABLE

| Current Section | Action | Reason |
|---|---|---|
| 4.1.1 Core Implementation Principles | REMOVE | Generic, not specific to this system |
| Table 4.1 Quest Difficulty | REMOVE | Fabricated, wrong schema |
| 4.1.2 RL Integration (reward table) | REMOVE | Wrong reward function entirely |
| 4.1.2 State Representation bullets | MODIFY | Correct direction, wrong detail |
| 4.1.3 Three-Stage Generation | REMOVE | Content missing, replace with real FQG |
| Table 4.3 Adaptive Generation | REMOVE | Fabricated |
| 4.1.4 Artifact Store Integration | REMOVE | Wrong system, wrong technology |
| Table 4.4 FQT Performance | REMOVE | Fabricated |
| 4.1.5 Scalability metrics | REMOVE | Fabricated |
| 4.1.6 Research Contributions | REMOVE | Fabricated claims |
| 4.2 Multi-Agent framing | REMOVE | Wrong architecture model |
| Table 4.5 Agent Specialization | REMOVE | Wrong component model |
| 4.2.2 Individual agent subsections | REMOVE | Extensions ≠ agents |
| 4.2.3 Communication Protocol Stack | REMOVE | Wrong, fabricated |
| Table 4.7 Protocol Stack | REMOVE | Fabricated |
| 4.2.4 Collaboration Patterns | REMOVE | Not how Conductor works |
| Table 4.8 Consensus Decision Making | REMOVE | Fabricated |
| 4.2.5 Fault Tolerance | REMOVE | Wrong fault model |
| Tables 4.9, 4.10, 4.11 | REMOVE | Fabricated |
| 4.2.7 Research Contributions | REMOVE | Fabricated |
| 4.3.1 Hybrid Database | REMOVE | Wrong technology entirely |
| Tables 4.12, 4.13 | REMOVE | Fabricated, wrong tech |
| 4.3.2 CAS description | MODIFY | Concept ok, details wrong |
| Table 4.14 Deduplication | REMOVE | Fabricated |
| 4.3.3 Quality Scoring | REMOVE | Wrong scoring model |
| Table 4.15 Quality Framework | REMOVE | Fabricated |
| 4.3.4 Predictive Resource Allocation | REMOVE | Fabricated ML allocator |
| Table 4.16 Predictive Allocation | REMOVE | Fabricated |
| 4.3.5 Tantivy Search | REMOVE | Not confirmed in implementation |
| Table 4.17 Search Performance | REMOVE | Fabricated |
| 4.3.6 Cache Consistency | REMOVE | Wrong caching model |
| Table 4.18 Cache Invalidation | REMOVE | Fabricated |
| 4.3.7 Performance Evaluation | REMOVE | Fabricated numbers |
| 4.3.8 Research Contributions | REMOVE | Fabricated |
| 4.4.1 AI-First Paradigm | MODIFY | Keep framing, update table |
| 4.4.2 Triple-Mode Architecture | MODIFY | Names correct, details need update |
| 4.4.3 Harmony Board | MODIFY | Add Rust/IPC detail |
| 4.4.4 Visualization | MODIFY | Add ConductorReport, softmax score label |
| 4.4.5 Performance Optimization | REMOVE fabricated numbers | Keep generic techniques |
| 4.4.6 User Experience Evaluation | REMOVE | No study was conducted |
| 4.4.7 Research Contributions | MODIFY | Replace with real contributions |
| 4.5.1 Testing Methodology | MODIFY | Replace counts with 7 invariants |
| 4.5.2 Multi-Agent Testing | REMOVE | Replace with real integration tests |
| 4.5.3 Quality Metrics | REMOVE | Replace with real monitoring components |
| 4.5.4 Deployment Architecture | REMOVE | Replace with real phased rollout |
| 4.5.5 Update Orchestration | REMOVE | Fabricated |
| 4.5.6 Distribution Strategies | REMOVE | Fabricated |
| 4.5.7 CI/CD | MODIFY | Remove fabricated test count |
| 4.5.8 Research Contributions | REMOVE | Fabricated |
| 4.6.1 Evaluation Methodology | REMOVE fabricated numbers | Keep framework |
| 4.6.2 Performance Benchmarks | REMOVE measured column | Label as design targets |
| 4.6.3 Comparative Analysis | REMOVE | No comparison was done |
| 4.6.4 User Experience | REMOVE | No study was done |
| 4.6.5 Scalability | REMOVE | No load test was done |
| 4.6.6 Training Evaluation | MODIFY | Replace with real success criteria |
| 4.6.7 Database Evaluation | REMOVE | Wrong technology |
| 4.6.8 Limitations | MODIFY | Replace with real deferred items |
| 4.6.9 Contributions Summary | REMOVE | Empty section |
| 4.6.10 Conclusion | MODIFY | Remove fabricated bullets |
| New 4.1 System Architecture | ADD | Does not exist |
| New 4.2 Conductor RL Agent | ADD | Scattered/missing across chapter |
| New 4.3 FQG | ADD | Partially in old 4.1, needs full rewrite |
| New 4.4 Storage (stripped) | ADD | Replaces old 4.3 |


---

## ADDENDUM — Three Gaps Found After Deeper Review

### [ADD] Melody Memory — full subsection missing from new 4.4

The current chapter has zero mention of melody memory. The against-document's ADD
section for new 4.4 mentioned it only in passing. It needs its own subsection.

Must cover:
- What a melody is: a stored workflow — a sequence of extension calls that achieved
  a score for a given query, stored per user, shareable, version-agnostic
- Storage format: pure JSON, symbolic (extension IDs + artifact references), no
  embeddings, no binary data, ~1-2KB per melody
- The two types of Conductor knowledge: global knowledge (NN weights, learned from
  FQG training) vs instance memory (melody store, specific workflows that worked
  for this user/domain). Instance memory is not weights — it is a structured lookup.
- Runtime: Rust Artifact Store owns the files on disk via PyO3 FFI. Python holds
  an in-memory encoding cache (_encoding_cache), cleared on restart. Python
  re-encodes symbolic sequences into the current embedding space at load time.
- How it is used: cosine similarity on query embeddings to find the best matching
  melody (threshold 0.85), then used as a prior — bias the action distribution
  toward the known-good sequence, but allow the policy to deviate based on current
  state. The Conductor must not blindly follow the suggested path.
- Version compatibility: symbolic storage makes melodies architecture-agnostic.
  Minor version change → no migration. Major version change → extension ID aliasing.
  Extension removed from marketplace → graceful degradation with user notification.
- Melody lineage: parent_melody_id, version, changes — track evolution over time.
- Polyphony marketplace: export/import as plain JSON, upload/download via HTTP
  handled by Rust Artifact Store. Shared melodies work across users, machines,
  and Conductor versions.

### [ADD] FQT Strictness Dimension and Permission Footprint — missing from new 4.2.8

The against-document's ADD section for new 4.2.8 covered required/optional,
cardinality, and preferred_usage but missed two important points from the
FQT classification spec.

**Strictness dimension** must be added:
- DeepSeek operates on a spectrum from strict to flexible when building the FQT
- Strict: only clearly required extensions, small FQT, focused action space, faster
  and more deterministic episodes. Risk: local optimal — better path existed but
  the extensions enabling it were never included.
- Flexible: required + optional extensions, larger FQT, more room to explore
  quality improvements. Risk: more noise for the Conductor to filter.
- This is a user-facing quality dial, not just a training parameter
- The Conductor must be trained on both modes. Training only on strict FQTs means
  the model will not know what to do with optionals in production. Training only
  on flexible FQTs means it will not learn to execute efficiently on tight FQTs.
- Curriculum design: early levels use strict FQTs (learn required chains), middle
  levels introduce optionals (learn cost/benefit), later levels use flexible FQTs
  (learn to discriminate and adapt to FQT shape)

**Permission footprint as classification signal** must be added:
- Every extension manifest declares `tool_calls` — the system permissions it needs
  at runtime (fs:read, fs:write, network:outbound, process:exec, git:write, etc.)
- DeepSeek uses this as a primary classification signal: if an extension's permission
  footprint is inconsistent with what the query needs, it is excluded or down-ranked
- The Extension Runner uses the same field as a hard sandbox enforcement boundary
- These two uses are independent: classification signal is a soft heuristic,
  sandbox enforcement is a hard constraint
- The Conductor does not enforce permissions — it learns the correlation between
  permission footprint and required/optional classification through training

### [ADD] Production Monitoring, Rollback, and Retraining Protocol — missing from new 4.7

The against-document's new 4.7 (Evaluation) only covered training success criteria.
The production monitoring architecture is a complete design that belongs in the chapter.

Must cover:

**Real-time monitoring metrics:**
- Episode-level: rolling success rate (window=100), avg melody_score per workflow,
  avg steps per workflow, completion bonus frequency, termination penalty frequency
- Extension-level: usage distribution, credibility scores, timeout rate, failure rate
- User-level: success rate per user, avg workflow complexity, melody reuse rate

**Alert tiers:**
- Critical (page on-call): success rate < 40% for 50 consecutive workflows, any
  extension credibility drops to 0.0, Conductor crashes or infinite loops, action
  mask violations
- Warning (Slack): success rate < 55% for 100 workflows, credibility < 0.3 for
  24 hours, timeout rate > 20% for any extension
- Info (daily digest): unknown paths discovered, extension usage distribution shifts,
  new failure patterns

**Rollback:**
- Automatic triggers: success rate < 30% for 100 consecutive workflows, extension
  credibility drops to 0.0, infinite loop detected 10 times in 1 hour
- Rollback SLA: < 5 minutes from decision to traffic switched
- Blue-green deployment, preserve all production data, no user data loss

**Temporal decay and retraining protocol:**
- Decay triggers (any one sufficient): extension catalog drift > 20% unknown to
  model, success rate drop > 10% on any workflow category over 30 days, PSI > 0.2
  on melody_score or overall_score distributions, 6-month time floor
- Retraining data window: rolling 90 days, minimum 10,000 episodes
- Evaluation gate: new model must beat current on held-out eval set, efficiency
  not regressed > 2%, behavioral fingerprint healthy, all 7 invariant tests pass
- Champion/challenger: new model runs on 10% of traffic for 48h before full promotion

**Unknown path discovery as continuous improvement loop:**
- Unknown paths (valid sequences not in FQG ground truth) are logged in production
- Weekly review: add valid unknown paths to FQG as new challenges
- This is the feedback loop from production back into the training environment

**Score computation validation in production:**
- melody_score honesty: spot-check 10 random artifacts per day in Phase 1-2
- Phase 3 (marketplace): external evaluator spot-checks 10% of artifacts, divergence
  > 0.2 from self-reported score flags the extension
- overall_score staleness: monitor for cases where overall_score = 0.8 but recent
  melody_scores average 0.4 — the aggregate is lagging behind quality drops
