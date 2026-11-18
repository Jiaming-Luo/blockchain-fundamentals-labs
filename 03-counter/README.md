# Lab 03 — Counter Smart Contract

This lab implements an on-chain counter in Solidity, tests its accumulation behavior in Remix VM, and documents deployment to the Sepolia testnet by the wallet owner.

- `uint256 private counter`: Stores the counter value, which starts at `0`.
- `get()`: Returns the current value without modifying state.
- `add(uint256 x)`: Executes `counter += x`. Any address can call it. Adding `0` leaves the count unchanged; overflow reverts the transaction.
- Compiler: Solidity `0.8.30`. In Remix, disable optimization and leave the EVM version at the compiler default.

## Manual Testing in Remix VM

1. In the [Remix](https://remix.ethereum.org/) File Explorer, create `Counter.sol` and paste the source from this directory.
2. In **Solidity Compiler**, select `0.8.30` and click **Compile Counter.sol**.
3. In **Deploy & Run Transactions**, select **Remix VM** as the environment, select `Counter`, and click **Deploy**.
4. Expand the new instance under **Deployed Contracts** and follow the steps below. After each `add` call, confirm that the transaction succeeds, then call `get()`. Keep using the same instance when switching accounts.

| Step | Action | Expected `get()` | Observed `get()` |
| --- | --- | ---: | --- |
| 1 | Read `get()` immediately after deployment | 0 | 0 |
| 2 | Call `add(5)` from Account 1 | 5 | 5 |
| 3 | Switch to Account 2 and call `add(3)` | 8 | 8 |
| 4 | Call `add(0)` | 8 | 8 |

## Sepolia Deployment

1. After the VM tests pass, switch MetaMask to Sepolia (chain ID `11155111`) and ensure the account has enough Sepolia test ETH to pay for gas.
2. In Remix's **Deploy & Run Transactions** panel, select a browser wallet environment (for example, **Injected Provider - MetaMask**). Have the wallet owner approve the connection and verify the network and account.
3. Select `Counter`, leave **Value** at `0`, and click **Deploy**. Have the wallet owner review and approve the transaction, then wait for on-chain confirmation.
4. Read `get()` on the new instance (expected: `0`), call `add(5)`, and confirm it in the wallet. Once the transaction succeeds, read `get()` again (expected: `5`).
5. Switch to Account 2, call `add(3)` on the same contract, and read `get()` after the transaction succeeds (expected: `8`).

## Deployment Evidence

Network: Sepolia (chain ID `11155111`).

In the lab author's manual test, deployment succeeded and `get()` started at `0`. Account 1 called `add(5)`, bringing the count to `5`; Account 2 called `add(3)` on the same contract, bringing it to `8`. `add(0)` was tested only in Remix VM. The Sepolia records were not independently verified on-chain.

| Item | Address or Transaction Hash | Explorer Link |
| --- | --- | --- |
| Contract address | `0xc1E2ee40d8EF17eE21fe5517A71dE88069F2F55F` | [Etherscan](https://sepolia.etherscan.io/address/0xc1E2ee40d8EF17eE21fe5517A71dE88069F2F55F) |
| Deployment transaction hash | `0xc62231c6c6cca4f5536bab5bce665e52fe562873c2808d368d0291ec7a813ebf` | [Etherscan](https://sepolia.etherscan.io/tx/0xc62231c6c6cca4f5536bab5bce665e52fe562873c2808d368d0291ec7a813ebf) |
| `add(5)` transaction hash | `0x78b26aedf7a35016b23534470ea3a526e7940a49589fd5393970c6b21150ed09` | [Etherscan](https://sepolia.etherscan.io/tx/0x78b26aedf7a35016b23534470ea3a526e7940a49589fd5393970c6b21150ed09) |
| `add(3)` transaction hash | `0x5204e4034545592ed498cdd25525bcb1474fafebd1c045f73c1520ff1e011cbf` | [Etherscan](https://sepolia.etherscan.io/tx/0x5204e4034545592ed498cdd25525bcb1474fafebd1c045f73c1520ff1e011cbf) |

## Screenshots

The evidence includes one Remix VM screenshot and four Sepolia screenshots:

- [Remix VM: Local test](screenshots/01-remix-vm.png)
- [Remix: Sepolia contract with `get() = 8`](screenshots/02-sepolia-count.png)
- [Etherscan: Successful deployment](screenshots/03-deployment.png)
- [Etherscan: Successful call from the first account](screenshots/04-add5.png)
- [Etherscan: Successful call to the same contract from the second account](screenshots/05-add3.png)

The transaction hashes and contract address shown in the screenshots match the table above. The call screenshots do not show the full transaction input; the arguments and intermediate counts are from the manual test record. The Remix VM table lists the observed result for each step. See the [screenshot index](screenshots/README.md) for details.
