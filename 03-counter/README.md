# Lab 03 — Counter 智能合约

本实验使用 Solidity 实现链上计数器，通过 Remix VM 验证累加行为，再由钱包所有者部署到 Sepolia 测试网。

- `uint256 public count`：保存计数值，部署后默认为 `0`。Solidity 自动生成只读的 `count()`。
- `add(uint256 x)`：执行 `count += x`。任何地址都能调用；`x` 为 `0` 时值不变，溢出时交易回滚。
- 编译器：Solidity `0.8.30`。Remix 中关闭优化，EVM Version 保持编译器默认设置。

## Remix VM 手动测试

1. 在 [Remix](https://remix.ethereum.org/) 的 File Explorer 中新建 `Counter.sol`，复制本目录的源码。
2. 在 **Solidity Compiler** 中选择 `0.8.30`，点击 **Compile Counter.sol**。
3. 在 **Deploy & Run Transactions** 中选择 **Remix VM**，选中 `Counter` 并点击 **Deploy**。
4. 展开 **Deployed Contracts** 中的新实例，按表操作。每次 `add` 后确认交易成功，再点击 `count`；切换账户后继续使用同一个实例。

| 步骤 | 操作 | `count()` 预期值 | 实测值 |
| --- | --- | ---: | --- |
| 1 | 部署后直接读取 `count()` | 0 | 0 |
| 2 | 使用部署账户调用 `add(5)` | 5 | 5 |
| 3 | 切换到另一个 Remix VM 账户，调用 `add(3)` | 8 | 8 |
| 4 | 调用 `add(0)` | 8 | 8 |

## Sepolia 部署

1. 通过 VM 测试后，在 MetaMask 切换到 Sepolia（链 ID `11155111`），确认账户有足够的 Sepolia 测试 ETH 支付 gas。
2. 在 Remix 的 **Deploy & Run Transactions** 中选择浏览器钱包环境（如 **Injected Provider - MetaMask**）。由钱包所有者确认连接，并核对网络和账户。
3. 选择 `Counter`，保持 **Value** 为 `0`，点击 **Deploy**。由钱包所有者核对并确认交易，等待链上确认。
4. 读取新实例的 `count()`（预期 `0`），调用 `add(5)` 并在钱包确认，交易成功后再次读取（预期 `5`）。
5. 切换到 Account 2，对同一合约调用 `add(3)`，交易成功后读取 `count()`（预期 `8`）。

## 作业凭证

网络：Sepolia（链 ID `11155111`）。

根据提交者提供的实测记录，Sepolia 部署成功，初始 `count()` 为 `0`；Account 1 调用 `add(5)` 后为 `5`，Account 2 在同一合约上调用 `add(3)` 后为 `8`。`add(0)` 仅在 Remix VM 测试。上述结果来自提交者，未独立核验链上记录。

| 项目 | 地址或交易 Hash | 浏览器凭证 |
| --- | --- | --- |
| 合约地址 | `0x75a9e4dc9100F98c674cfdf60B87281307315A63` | [Etherscan](https://sepolia.etherscan.io/address/0x75a9e4dc9100F98c674cfdf60B87281307315A63) |
| 部署交易 Hash | `0xcd259b7e83e2002e0002f15303200cd47ac36e3b8915b54591de9725d1cce986` | [Etherscan](https://sepolia.etherscan.io/tx/0xcd259b7e83e2002e0002f15303200cd47ac36e3b8915b54591de9725d1cce986) |
| `add(5)` 交易 Hash | `0x7831630cd5f42327fb0722760ac437867fe69455b5ed8a1fbfafbea4f0e15f89` | [Etherscan](https://sepolia.etherscan.io/tx/0x7831630cd5f42327fb0722760ac437867fe69455b5ed8a1fbfafbea4f0e15f89) |
| `add(3)` 交易 Hash | `0x463a1fdd8a56f7d8a97c6bdc9df2710e6ed998cf67267c2bbb14cc1a3967e9e9` | [Etherscan](https://sepolia.etherscan.io/tx/0x463a1fdd8a56f7d8a97c6bdc9df2710e6ed998cf67267c2bbb14cc1a3967e9e9) |

## 截图清单

现有截图包括 1 张 Remix VM 截图和 4 张 Sepolia 凭证：

- [Remix VM：本地测试](screenshots/01-remix-vm.png)
- [Remix：Sepolia 合约的 `count = 8`](screenshots/02-sepolia-count.png)
- [Etherscan：部署成功](screenshots/03-deployment.png)
- [Etherscan：第一个账户调用成功](screenshots/04-add5.png)
- [Etherscan：第二个账户调用同一合约成功](screenshots/05-add3.png)

三笔交易截图中的 Hash 和合约地址与上表一致。调用截图未展示完整输入数据；参数及中间计数来自实测记录。Remix VM 各步骤的实测结果见测试表。详见[截图索引](screenshots/README.md)。
