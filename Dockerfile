# 1. 采用官方极其精简的 Python 轻量级基础镜像
FROM python:3.10-slim

# 2. 设置容器内部的工作目录
WORKDIR /app

# 3. 复制本地的核心主权资产、验证配置以及引擎到容器中
COPY shard-a-sealed.json .
COPY shard-b-sealed.json .
COPY network_config.json .
COPY soul_engine.py .

# 4. 在容器内部安全安装 Web3 核心通讯组件
RUN pip install --no-cache-dir web3

# 5. 设定容器启动时的默认物理命令：直接激活 Elliott 灵魂引擎
CMD ["python", "soul_engine.py"]
