import os
import json
from flask import Flask, jsonify, render_template, send_file, abort, request
import argparse

app = Flask(__name__)

# 渲染 index.html 模板
@app.route('/')
def index():
    return render_template('index.html')

# 返回第一个 JSON 文件的数据
@app.route('/vqa-data1')
def vqa_data1():
    with open('/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/agentlego/annotators/generated_data/demo/final_demo_2_ch.json', 'r') as f:
        vqa_items = json.load(f)
        # spilt vqa_items into NUM parts
    return jsonify(vqa_items)

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()
    try:
        with open(f'human_annotation/vqa_results_demo.json', 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'Data saved successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

# 动态提供图片服务
@app.route('/serve-image/<path:filename>')
def serve_image(filename):
    # 检查图片文件是否存在
    filename = '/' + filename
    if os.path.exists(filename):
        return send_file(filename)  # 发送图片文件
    else:
        abort(404)  # 如果文件不存在，返回404错误

app.run(debug=True, host='0.0.0.0', port=5000)