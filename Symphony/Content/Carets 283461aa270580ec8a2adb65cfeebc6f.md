# Carets

tantivy = "0.21"         # Full-text search

abi_stable = "0.11"      # ABI-stable interfaces # Why there is abi stable, does this mean Rust’s ABI is not stable?

bumpalo

rlimit = "0.10"          # Resource limit control

slotmap = "1.0"          # Efficient entity storage

twox-hash = "1.6"        # Fast non-crypto hashing # Vs Sha2

multihash = "0.19"       # IPFS-style content addressing

cid = "0.11"             # Content identifiers

ordinal = "0.3"          # Statistical calculations

moka = "0.12"            # High-performance cache
flurry = "0.5"           # Lock-free HashMap

regorus = "0.1"          # Policy evaluation (like OPA)

rust_decimal = "1.33"    # Precise decimal math for costs # Rust does not have support for decimal functions builtin like Python?

opendal = "0.44"         # Unified storage access layer

```
humansize = "2.1"        # Human-readable sizes
du = "0.9"               # Disk usage calculation
```

linfa = "0.7"            # ML for value assessment

flume = "0.11"           # MPMC channels

batch = "0.2"            # Batch processing

load_balancer = "0.1"    # Request distribution

zerocopy = "0.7"         # Zero-copy abstractions

```markdown
glob = "0.3"             # File pattern matching

vs
goblin = "0.7"           # Binary parsing
vs
globset = "0.4"          # Glob pattern matching

```

```markdown
version-compare = "0.1"  # Version comparison

# Isolation
namespaces = "0.1"       # Namespace isolation (Unix)

# Resource Tracking
weakmap = "0.1"          # Weak references for cleanup
```

```markdown
futures-util = "0.3"     # Stream utilities
pin-project = "1.1"      # Pin projection
```

governor = "0.6"         # Rate limiting

backoff = "0.4"          # Exponential backoff

```markdown
http = "1.0"
http-body = "1.0"
```

rhai = "1.16"            # Embedded scripting language

```markdown
download = "0.1"         # Parallel downloads
request-rate-limiter = "0.1" # Rate limiting downloads
```

bubblewrap = "0.1"       # Linux sandboxing
spdx = "0.10"            # SPDX identifiers

askama = "0.12"          # Type-safe templates

```markdown
proc-macro2 = "1.0"      # Procedural macros
quote = "1.0"            # Code generation
syn = { version = "2.0", features = ["full"] }
```

```markdown
deadpool-postgres = "0.12" # Connection pooling
refinery = { version = "0.8", features = ["tokio-postgres"] } # Migrations
```

```markdown
meilisearch-sdk = "0.24" # Alternative search engine
typesense = "0.1"        # Real-time search
```

mobc = "0.8"             # Async connection pooling

fastly = "0.9"           # Edge delivery

psutil = "3.2"           # Process utilities

```
count-min-sketch = "0.1" # Approximate counting
bloom = "0.3"            # Bloom filters for deduplication
```

eventbus = "0.1"         # Internal event bus
hook-registry = "0.1"    # Hook registration system

```markdown
dbus = "0.9"             # D-Bus integration
libnotify = "0.1"        # Linux notifications
```

```markdown
# Auto-update
tauri-plugin-updater = "1.0" # Auto-update support
self_update = "0.39"         # Alternative updater

# Deep Linking
tauri-plugin-deep-link = "0.1" # URL scheme handling

# Single Instance
tauri-plugin-single-instance = "0.1" # Prevent multiple instances

# Store/Settings
tauri-plugin-store = "0.1"  # Persistent storage

# System Integration
tauri-plugin-clipboard = "0.1" # Clipboard access
tauri-plugin-shell = "0.1"     # Shell commands

# Analytics (Optional)
tauri-plugin-posthog = "0.1"   # PostHog analytics
```

multipart = "0.18"       # Multipart form data

apalis = "0.5"           # Job queue