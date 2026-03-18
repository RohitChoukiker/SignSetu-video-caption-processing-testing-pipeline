# Video Caption Processing API - Automated Test Suite

This project implements a robust end-to-end automated test suite for a Video Caption Processing Pipeline API using Pytest.
It validates the complete lifecycle of video processing while actively uncovering backend inconsistencies related to asynchronous execution, state management, and system reliability.

---

##  Tech Stack

* Python
* Pytest
* Requests
* Pytest-xdist (parallel execution)
* Pytest-rerunfailures (flaky test detection)

---

##  Testing Strategy

### 1. End-to-End Workflow Validation

The suite automates the full API lifecycle:

1. Authenticate user
2. Create video resource
3. Trigger caption processing
4. Poll for completion (async handling)
5. Validate caption output
6. Cleanup resources

---

### 2. Asynchronous Handling

1. Implemented polling mechanism (`processing`)
2. Timeout-based validation to prevent infinite waits
3. Designed to detect unstable or non-deterministic async behavior

---

### 3. Negative Testing & Vulnerability Hunting

The suite actively attempts to break the system using adversarial scenarios:

1. Missing authentication headers
2. Invalid video IDs
3. Duplicate processing triggers
4. Deletion during processing
5. Fetching captions before processing
6. Repeated execution to detect instability

---

## Bugs & Vulnerabilities Identified

The following critical issues were discovered:

1. **Premature Data Exposure**

    Captions API returns `200 OK` even before processing is triggered

2. **Async Processing Instability**

    Caption processing frequently remains stuck in "processing" state
    Jobs do not complete reliably within expected time

3. **Non-Deterministic Behavior**

    Same test produces different results across runs

4. **End-to-End Pipeline Failure**

    Full workflow is not consistently reliable

5. **Weak State Validation**

    Processing can be triggered for non-existent videos

6. **Inconsistent API Responses**

   Mixed status codes (400, 401, 403) for similar scenarios

7. **Improper Resource Handling**

    Duplicate delete operations are not consistently rejected

---

## Repeatability & Stability

1. Tests are designed to be independent
2. Cleanup ensures no residual data
3. Failures observed are due to backend inconsistencies, not test defects
4. Rerun results confirm system flakiness rather than transient errors

---

## How to Run

```bash
pip install -r requirements.txt
pytest -n auto --reruns 2
```

---

##  Key Highlights

1. Strong focus on **system reliability over happy-path validation**
2. Designed to expose **real-world failure scenarios**
3. Clear separation between functional, negative, and destructive testing
4.  Demonstrates **deep validation of async workflows and data integrity**

---

##  Final Note

> The observed test failures highlight critical backend inconsistencies rather than issues in the test implementation.
> The system exhibits instability in async processing, weak state validation, and non-deterministic behavior under repeated execution.
