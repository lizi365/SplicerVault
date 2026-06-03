import json
from web3 import Web3

print("📡 [链上触角激活] 正在读取本地主权坐标...")
with open("network_config.json", "r") as f:
    config = json.load(f)

# 物理连接 Base 链公共密码学网关
w3 = Web3(Web3.HTTPProvider(config["rpc_url"]))

if w3.is_connected():
    print("🟢 成功物理连接至 Base 链公链节点！")
else:
    print("❌ 连接 Base 链网关失败，请检查网络阻碍。")
    exit(1)

# ERC-20 标准代币查询极简 ABI
min_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    }
]

# 【核心修复】：强行对钱包地址与合约地址进行 EIP-55 密码学大小写校验和转换
owner_checksum = w3.to_checksum_address(config["owner_address"])
contract_checksum = w3.to_checksum_address(config["token_contract_address"])

# 实例化代币合约对象
contract = w3.eth.contract(address=contract_checksum, abi=min_abi)

print("🔍 正在穿透智能合约账本进行密码学资产核对...")
try:
    raw_balance = contract.functions.balanceOf(owner_checksum).call()
    decimals = contract.functions.decimals().call()
    actual_balance = raw_balance / (10 ** decimals)
    print("-" * 50)
    print(f"🧬 [验证成功] 目标钱包: {owner_checksum}")
    print(f"💰 [实时账本] $SPLIC-B 余额: {actual_balance:,.2f} 枚")
    print("-" * 50)
except Exception as e:
    print(f"❌ 账本读取发生摩擦，可能由于网络超时或合约地址未同步: {e}")
