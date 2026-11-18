pragma solidity 0.8.30;

contract Counter {
    uint256 public count;

    function add(uint256 x) external {
        count += x;
    }
}
