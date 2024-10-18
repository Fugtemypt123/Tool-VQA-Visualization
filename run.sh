#!/bin/bash

# 启动 Flask 实例
for ((i=0; i<80; i++)); do
    echo "Starting server with index $i..."
    
    # 启动 Flask 应用，每个应用根据 idx 计算端口和数据范围
    nohup python app.py --idx $i &
done

echo "All servers started."