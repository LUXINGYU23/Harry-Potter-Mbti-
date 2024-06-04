import json
import pandas as pd

def parse_json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    dialogues = {}

    # 遍历JSON文件中的每个会话
    for session_key, session in data.items():
        if 'dialogue' in session:
            for line in session['dialogue']:
                # 分割对话行，获取发言人和对话内容
                parts = line.split(':', 1)
                if len(parts) == 2:
                    speaker = parts[0].strip()
                    content = parts[1].strip()
                    # 累积每个发言人的对话内容
                    if speaker in dialogues:
                        dialogues[speaker] += " " + content
                    else:
                        dialogues[speaker] = content
    
    # 转换字典到列表的格式，用于创建DataFrame
    dialogue_list = [{'Speaker': speaker, 'Dialogue': dialogue} for speaker, dialogue in dialogues.items()]
    df = pd.DataFrame(dialogue_list)

    # 保存DataFrame到CSV
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

# 调用函数
json_file_path = '/root/autodl-tmp/en_train_set.json'
csv_file_path = '/root/autodl-tmp/dialogues.csv'
parse_json_to_csv(json_file_path, csv_file_path)
