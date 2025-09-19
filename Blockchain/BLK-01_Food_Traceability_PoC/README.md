    # BLK-01 — Food Traceability PoC

    **Why it matters:** End-to-end produce traceability with temperature excursions and chain-of-custody.

    ## Demo Scope
    - Hash events (case_id, gtin, temp) and anchor references.
- Join anchored refs with recall logic; visualize custody path.

    ## KPIs & Outcomes
    - Recall scope reduction time
    - Temperature breach rate
    - Tamper-evidence verification rate

    ## Skill Takeaways
    - Hashing & immutability basics
    - Data modeling for traceability
    - Join on anchored refs
    - Intro to smart contracts

    ## How to Run
    1) Open `Blockchain/common/notebooks/01_hash_and_anchor.ipynb` to learn the local anchoring workflow.

    2) Explore this project's `notebooks/` for domain-specific examples.

    3) (Optional) Deploy `ProofOfProvenance.sol` to a testnet and replace the local registry with on-chain calls.
