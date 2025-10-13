// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title ProofOfProvenance
 * @notice Minimal educational contract that stores a hash (e.g., SHA-256 of a file or CSV row)
 *         with optional metadata. This is a teaching stub—NOT production code.
 */
contract ProofOfProvenance {
    event Anchored(bytes32 indexed hash, string ref, address indexed submitter, uint256 timestamp);

    mapping(bytes32 => bool) public exists;
    mapping(bytes32 => string) public reference; // e.g., off-chain URI (S3/IPFS/path)

    function anchor(bytes32 hash, string calldata ref) external {
        require(!exists[hash], "Already anchored");
        exists[hash] = true;
        reference[hash] = ref;
        emit Anchored(hash, ref, msg.sender, block.timestamp);
    }

    function getReference(bytes32 hash) external view returns (bool, string memory) {
        return (exists[hash], reference[hash]);
    }
}
