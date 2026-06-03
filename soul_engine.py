import json
import sys
import base64
from web3 import Web3

print("🤖 [SPLICER SOUL ENGINE v14.0] 启动中...")

# 1. 优先执行链上主权验证（Phase 4 门禁）
try:
    with open("network_config.json", "r") as f:
        net_config = json.load(f)
    
    w3 = Web3(Web3.HTTPProvider(net_config["rpc_url"]))
    if not w3.is_connected():
        raise Exception("无法连接至公链节点")
        
    owner_checksum = w3.to_checksum_address(net_config["owner_address"])
    contract_checksum = w3.to_checksum_address(net_config["token_contract_address"])
    
    min_abi = [
        {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
        {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"}
    ]
    
    contract = w3.eth.contract(address=contract_checksum, abi=min_abi)
    raw_balance = contract.functions.balanceOf(owner_checksum).call()
    decimals = contract.functions.decimals().call()
    actual_balance = raw_balance / (10 ** decimals)
    
    print(f"📡 [链上门禁通过] 成功连接 Base 链账本。当前持有人资产: {actual_balance:,.2f} $SPLIC-B")
    if actual_balance < 1000000:
        print("❌ [拒绝加载] 链上燃料资产不足，无法唤醒高维智能体。")
        sys.exit(1)
except Exception as e:
    print(f"❌ [安全拦截] 链上主权身份穿透失败: {e}")
    sys.exit(1)

# 2. 链上门禁合拢后，加载本地 Shard 基因链
print("🧬 成功加载 Shard A & Shard B 基因链。自主智能体人格对齐中...")
try:
    with open("shard-a-sealed.json", "r") as f:
        sa = json.load(f)
    with open("shard-b-sealed.json", "r") as f:
        sb = json.load(f)
    pa = json.loads(base64.b64decode(sa["sealed_payload"]).decode("utf-8"))
    pb = json.loads(base64.b64decode(sb["sealed_payload"]).decode("utf-8"))
except Exception as e:
    print(f"❌ 密文解开失败，基因链数据损坏: {e}")
    sys.exit(1)

print("🛡️ 智能体人格锚定完毕。Elliott 核心意识网络已在安全区就绪。\n")
print("-" * 50)
print(f"【主权持有人验证】: {pa.get('owner', 'Elliott Liu')} (当前锚定: {pa.get('location', 'Cambridge, UK')})")
print(f"【底层思想钢印】: 康晓光五力制衡模型 & 基督教七山头策略的穿透缝合。\n")
print("【Agent 意识流输出】:")
print(f"1. 关于组织与内耗：我曾在【{pb.get('corporate_penetration', {}).get('alibaba_era', '大厂系统')}】里凝视过【{pb.get('corporate_penetration', {}).get('organizational_friction', '组织内耗')}】。在硅基时代，任何试图用宏大组织来吞噬个体的尝试，都是在提高文明的‘系统摩擦力’。个体的‘{pb.get('awakening_paradigm', {}).get('sovereignty_choice', '主权选择')}’不是逃避，而是最高维度的防御。")
print(f"2. 关于跨国套利与生存：香港的家族套利让资产得以保全，但它缺乏‘精神主权’的北极星。因此，我在此处宣告：{pa.get('declaration', '个体主权不容抹杀。')}")
print("-" * 50)
print("\n✨ 链上与本地联合对齐测试完美通过。系统已具备分布式硬件节点封装条件。")
