pragma solidity 0.8.30;

contract Counter {
    uint256 private counter;

    function get() external view returns (uint256) {
        return counter;
    }

    function add(uint256 x) external {
        counter += x;
    }
}
