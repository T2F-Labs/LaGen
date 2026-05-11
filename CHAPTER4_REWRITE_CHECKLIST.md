# Chapter 4 — Rewrite Checklist

Work through this top to bottom. Each item is a discrete writing task.
Check it off when the text is written and reviewed.

---

## PHASE 1 — Structural Setup

- [ ] Create the new chapter skeleton with 7 top-level sections:
  - 4.1 System Architecture and Boundaries
  - 4.2 The Conductor — RL Agent Design and Implementation
  - 4.3 Function Quest Generator (FQG)
  - 4.4 Storage and Artifact Management
  - 4.5 User Interface
  - 4.6 Testing Strategy
  - 4.7 Evaluation

---

## PHASE 2 — Write New Sections (do not exist in current chapter)

### 4.1 — System Architecture and Boundaries
- [ ] Write the four-layer architecture description (React UI → out-of-process Rust → IPC Bus → Python process)
- [ ] Write the language responsibility table (Python owns / Rust owns)
- [ ] Write the two boundary descriptions (PyO3 FFI ~50ns / Unix sockets ~0.3ms)
- [ ] Write the hard boundary rules (Python never touches filesystem, Rust never computes embeddings, IPC Bus never makes orchestration decisions)
- [ ] Write the DeepSeek → Conductor handoff description (same process, async tool call, callback pattern)
- [ ] Write the per-step data flow sequence (5 steps: build state → policy forward → execute via IPC → store via FFI → compute reward)

### 4.2 — The Conductor: RL Agent Design and Implementation

#### 4.2.1 — Model Family
- [ ] Write the three-tier overview (Farid/Darwish/Baleegh, musical tempo naming rationale)
- [ ] Write Farid architecture targets (embedding=64, GRU=128, FFN=[256,128], frozen encoder, 210K params)
- [ ] Write Darwish architecture targets (embedding=128, GRU=256, FFN=[512,256], trainable encoder, dual LR)
- [ ] Write Baleegh architecture targets (embedding=256, GRU=512, FFN=[1024,512,256], DeepSeek hidden state gating)
- [ ] Write the three-types-of-change rule (architecture → major + retrain, size → new tier, improvement → minor + fine-tune)
- [ ] Write the versioning rule (version number communicates change type)

#### 4.2.2 — State Space
- [ ] Write the five-component state description with exact tensor shapes
- [ ] Write the query component (immutable, enriched by DeepSeek, inserted at step 0)
- [ ] Write the FQT component (unordered set, max 25, static during episode)
- [ ] Write the artifact pool component (70-dim encoding breakdown: 4+1+1+64)
- [ ] Write the call history component (66-dim per step: 64+1+1, GRU-encoded)
- [ ] Write the step count component (normalized to [0,1] by episode_cap=50)

#### 4.2.3 — Neural Network Architecture
- [ ] Write the multi-input architecture overview (each component has its own head)
- [ ] Write the query head (Linear 128→64)
- [ ] Write the FQT head (SetEncoder, masked mean pooling, summary + individual embeddings)
- [ ] Write the artifact head (SetEncoder, learned empty_token for step 0)
- [ ] Write the history head (GRU, pack_padded_sequence, learned h0, orthogonal_ init, forget gate bias=1.0)
- [ ] Write the combine step (concat → 327-dim → LayerNorm → FFN [256,128] with GELU)
- [ ] Write the shared trunk (output 128-dim → actor + critic)
- [ ] Write the actor head (dot product scoring, softmax for extension, sigmoid for artifacts)
- [ ] Write the critic head (Linear 128→64 → GELU → Linear 64→1, no softmax)
- [ ] Write the action masking rule (-inf not 0, applied before softmax)
- [ ] Write the temperature schedule (2.0 → 1.0 → 0.5 → argmax at eval)

#### 4.2.4 — Reward Function
- [ ] Write the proxy declaration (reward is a proxy, not quality itself; behavioral fingerprint detects gaming)
- [ ] Write all 8 per-step reward terms
- [ ] Write the terminal reward (completion bonus 7.0–10.0 efficiency-scaled, cap-hit penalties)
- [ ] Write the Farid vs Baleegh differences (credibility formula, loop handling, exploration bias)
- [ ] Write the reward normalization description (RunningMeanStd, Welford's, saved with checkpoint)
- [ ] Write the dead extension exploration bonus (continuous decay, disabled at eval)

#### 4.2.5 — Training Algorithm (PPO)
- [ ] Write the three nested cycles (outer: curriculum, middle: eval every K, inner: episode + update)
- [ ] Write the PPO loss formula (actor clipped ratio + critic MSE + entropy bonus)
- [ ] Write the GAE description (per-batch normalization only, never per-episode, bootstrap with V(s) at cap)
- [ ] Write the hyperparameters table (LR, gamma by tier, GAE lambda, clip epsilon, batch, epochs, workers, eval frequency)
- [ ] Write the gradient safety description (unscale_ before clip_grad_norm_, NaN detection)
- [ ] Write the KL monitoring description (log-only for Farid, four threshold levels)
- [ ] Write the linear LR schedule

#### 4.2.6 — Supervised Pre-training
- [ ] Write the cold start rationale (must run before PPO, not optional)
- [ ] Write the data source (optimal paths from FQG YAMLs, 3-5 paths per challenge)
- [ ] Write the loss functions (cross-entropy for extension selection, BCE for artifact selection)
- [ ] Write the gate rule (>80% accuracy to proceed, <40% stop and fix)
- [ ] Write the data augmentation description (100 → 500-1000 trajectories)

#### 4.2.7 — Curriculum Progression
- [ ] Write the level unlock mechanism (success_rate > threshold for stability_window updates)
- [ ] Write the 50/50 mix rule when Level 2 unlocks (catastrophic forgetting prevention)
- [ ] Write the production-ready criteria (success_rate >60%, efficiency >0.70, stable 500+ updates, dead extension rate <20%)

#### 4.2.8 — Action Space and Masking
- [ ] Write the action definition (extension_id, artifact_subset)
- [ ] Write the masking rules (depends_on not satisfied OR usage_limit exceeded → -inf)
- [ ] Write the artifact selection description (sigmoid, independent, threshold 0.5)
- [ ] Write the is_fallback field description
- [ ] Write the FQT classification description (required/optional query-relative, cardinality, preferred_usage as soft bias)
- [ ] Write the FQT strictness dimension (strict vs flexible, user-facing dial, both needed in training)
- [ ] Write the permission footprint description (tool_calls as DeepSeek classification signal AND Extension Runner sandbox boundary — two independent uses)
- [ ] Write the extension reversibility tiers (Tier 1/2/3, Tier 3 confidence gating deferred to Darwish)

### 4.3 — Function Quest Generator (FQG)

#### 4.3.1 — Purpose and Design Philosophy
- [ ] Write the sim-to-real parity statement (FQG is training only, not production)
- [ ] Write the encoding ownership rule (FQG owns encoding, Conductor receives pre-computed embeddings)
- [ ] Write the mock extension isolation rule (FQG extensions never go through IPC Bus)

#### 4.3.2 — Challenge YAML Schema
- [ ] Write the four-block schema description (meta, query, extensions, paths)
- [ ] Write the extensions[].extra passthrough description (credibility, timeout_probability)
- [ ] Write the paths block description (optimal/known/unknown/failed types)
- [ ] Write the preferred_usage description (soft logit bias, not enforcement, UnsafeFQTSizeError at <5 extensions)

#### 4.3.3 — TorchRL Integration
- [ ] Write the EnvBase interface description (TensorDict, typed specs)
- [ ] Write the step_info_extra description (raw artifact list, termination_reason)
- [ ] Write the ScorerProtocol injection description (FaridReward injected via Challenge constructor)
- [ ] Write the apply_mask parity description (imported from fqg in training, own impl in production, both tested)

#### 4.3.4 — Adapter Parity Invariant
- [ ] Write the invariant statement (FQGAdapter and ProductionAdapter produce bit-identical tensors)
- [ ] Write the torch.equal vs torch.allclose distinction and why it matters
- [ ] Write the CI gate description (runs on every commit)

#### 4.3.5 — Evaluation and Metrics
- [ ] Write the eval_set description (held-out, fixed, noise-free, never trained on)
- [ ] Write the EpisodeScore fields (success, efficiency, path_quality, noise_avoidance, optional_precision, terminated_early/late)
- [ ] Write the unknown path discovery description (log, review, add to FQG)
- [ ] Write the behavioral fingerprint thresholds (required_coverage, noise_call_rate, dependency_violation_rate, path_diversity)

### 4.4 — Storage and Artifact Management

#### 4.4.1 — The Pit
- [ ] Write the five Rust in-process components (Pool Manager, DAG Tracker, Artifact Store, Arbitration Engine, Stale Manager)
- [ ] Write the PyO3 FFI access pattern

#### 4.4.2 — Artifact Store
- [ ] Write the filesystem layout (.symphony/pool/cache/<session_id>/)
- [ ] Write the metadata.json schema (id, type, produced_by, melody_score, overall_score, timestamp, path, size_bytes)
- [ ] Write the cleanup schedule (session ends → 1 month → cloud archive → 6 months → deleted)
- [ ] Write the EpisodeDebugRecord description (~2KB, per-step fields, persisted for replay)

#### 4.4.3 — Quality Scores
- [ ] Write the melody_score definition (computed inside extension, 4-component formula, range [0,1])
- [ ] Write the overall_score definition (exponentially weighted historical aggregate, decay=0.95, new extensions start at 0.7)
- [ ] Write the credibility definition (cross-melody necessity, in-house=70%, marketplace=50%)

#### 4.4.4 — Melody Memory
- [ ] Write the melody definition (stored workflow, per-user, shareable, version-agnostic)
- [ ] Write the JSON storage format (symbolic, no embeddings, ~1-2KB)
- [ ] Write the two-type knowledge distinction (global weights vs instance memory)
- [ ] Write the runtime description (Rust owns disk, Python holds in-memory encoding cache)
- [ ] Write the usage description (cosine similarity lookup, threshold 0.85, used as prior not hard path)
- [ ] Write the version compatibility description (minor: no migration, major: extension ID aliasing, removed extension: graceful degradation)
- [ ] Write the melody lineage description (parent_melody_id, version, changes)
- [ ] Write the Polyphony marketplace description (export/import JSON, HTTP via Rust Artifact Store)

---

## PHASE 3 — Rewrite Existing Sections (keep structure, replace content)

### 4.5 — User Interface (from old 4.4)
- [ ] Rewrite 4.5.1 AI-First Interaction Paradigm (keep three principles, update Table 4.20 with real mode names)
- [ ] Rewrite 4.5.2 Triple-Mode Architecture (Maestro/Virtuoso/Solo with correct descriptions)
- [ ] Rewrite 4.5.3 Harmony Board (add Rust/IPC detail, keep React Flow, note Rust/React split in table)
- [ ] Rewrite 4.5.4 Visualization (add ConductorReport as data source, StepOutput fields, softmax score label, behavioral fingerprint for ML engineers)
- [ ] Rewrite 4.5.5 Performance Optimization (remove fabricated numbers, keep generic React techniques only)
- [ ] Rewrite 4.5.6 Research Contributions (three-audience explainability design: ML engineer / domain expert / end user)

### 4.6 — Testing Strategy (from old 4.5)
- [ ] Rewrite 4.6.1 Testing Methodology (keep five-layer pyramid, replace fabricated counts with 7 invariants)
- [ ] Rewrite 4.6.2 Property-Based Testing (replace "probabilistic framework" with Hypothesis, two GAE properties)
- [ ] Rewrite 4.6.3 Integration Tests (replace multi-agent testing with real integration test list)
- [ ] Rewrite 4.6.4 Training Monitoring (replace fabricated metrics with RewardTracker, GradientMonitorCallback, KLMonitor, BiasAuditor)
- [ ] Rewrite 4.6.5 CI Gate (adapter parity test on every commit, remove fabricated test count)
- [ ] Rewrite 4.6.6 Phased Deployment (Phase 0/1/2/3 with real success criteria)

### 4.7 — Evaluation (from old 4.6)
- [ ] Rewrite 4.7.1 Evaluation Methodology (remove fabricated table, describe what was actually evaluated)
- [ ] Rewrite 4.7.2 Training Success Criteria (7 criteria, clearly labeled as design targets)
- [ ] Rewrite 4.7.3 Production Monitoring (episode/extension/user-level metrics, three alert tiers)
- [ ] Rewrite 4.7.4 Rollback and Retraining Protocol (automatic triggers, SLA, temporal decay triggers, champion/challenger)
- [ ] Rewrite 4.7.5 Limitations and Deferred Items (all Darwish-deferred items, TBD items, known gaps)
- [ ] Rewrite 4.7.6 Future Work (Darwish, Baleegh, Polyphony, retraining protocol)
- [ ] Rewrite 4.7.7 Conclusion (remove fabricated bullets, honest summary of what was built)

---

## PHASE 4 — Cross-Cutting Cleanup (do after all sections are written)

- [ ] Find and replace every instance of "agent" used for extensions or DeepSeek — change to correct term
- [ ] Find and replace every instance of "function" used for extensions — change to "extension"
- [ ] Find and replace "probability" next to action_confidence — change to "softmax score"
- [ ] Remove all mentions of: SQLite, DuckDB, Sled, redb, Tantivy, SHA-256 CAS
- [ ] Audit every number in the chapter — label as "design target", "measured", or remove
- [ ] Verify the terminology glossary is applied consistently throughout:
  - FQG, FQT, Conductor, Extension, Artifact, melody_score, overall_score, credibility,
    The Pit, IPC Bus, Farid/Darwish/Baleegh, ConductorReport, behavioral fingerprint
- [ ] Confirm proxy declaration appears in the reward section
- [ ] Confirm autonomy budget statement appears (Level 2, scope bounded by FQT, 50-step horizon)
- [ ] Confirm unknown path discovery loop is mentioned (production → FQG feedback)
- [ ] Confirm score computation validation is mentioned (spot-checking, marketplace evaluator)

---

## PHASE 5 — Final Review

- [ ] Read the full chapter against the against-document — verify every REMOVE is gone
- [ ] Read the full chapter against the against-document — verify every MODIFY was updated
- [ ] Read the full chapter against the against-document — verify every ADD exists
- [ ] Check that no section makes a claim that isn't either measured, a design target, or clearly labeled as future work
- [ ] Check that the chapter tells a coherent story: architecture → Conductor → FQG → storage → UI → testing → evaluation
