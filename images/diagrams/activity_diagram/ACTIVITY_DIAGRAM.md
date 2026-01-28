# Symphony IDE - Comprehensive Activity Diagrams

This document contains detailed activity diagrams covering all major workflows in Symphony IDE, showing the step-by-step logic, decision points, and parallel execution paths for key system processes.

---

## 1. System Bootstrap (Phased Initialization)

**Overview**: Visualizes the five-phase initialization process of Symphony IDE (Foundation, IPC, Pit, Conductor, UI) including parallel component loading, health checks, and automatic rollback on failure.

<iframe src="./activity_diagram_system_bootstrap.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./activity_diagram_system_bootstrap.html)

---

## 2. Melody Execution Workflow

**Overview**: Illustrates the end-to-end flow of executing a Melody, from user prompt to artifact generation. It details the interaction between the Developer, Conductor (AI), and The Pit (Execution Engine), showcasing both Maestro (AI) and Manual modes.

<iframe src="./activity_diagram_melody_execution.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./activity_diagram_melody_execution.html)

---

## 3. Extension Lifecycle (Chambering)

**Overview**: Shows the complete lifecycle of a Symphony extension within the "Chambering" state machine. It covers discovery, verification, dependency resolution, installation, security validation, and runtime execution.

<iframe src="./activity_diagram_extension_lifecycle.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./activity_diagram_extension_lifecycle.html)

---

## 4. Extension Development Workflow (Carets CLI)

**Overview**: Depicts the developer journey for creating, testing, and publishing extensions using the Carets CLI toolchain. It shows the flow from `carets new` to `carets publish`, including template generation, testing, signing, and marketplace upload.

<iframe src="./activity_diagram_extension_development.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./activity_diagram_extension_development.html)

---

## 5. Harmony Board Melody Creation

**Overview**: Demonstrates the visual workflow composition process in the Harmony Board using drag-and-drop actions. It covers node selection, connection validation, real-time error checking, and saving/publishing to the Polyphony Store.

<iframe src="./activity_diagram_harmony_board_creation.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./activity_diagram_harmony_board_creation.html)

---

## 6. Symphony Use Case Diagram

**Overview**: A high-level view of all system actors (Developer, Extension Creator, User) and their interactions with the core system components (Conductor, Orchestra Kit), showing inheritance relationships and key use cases.

<iframe src="./symphony_usecase_diagram.html" width="100%" height="800px" style="border:none;"></iframe>

[View Full Diagram](./symphony_usecase_diagram.html)
