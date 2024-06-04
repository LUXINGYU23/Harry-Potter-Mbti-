import json

def process_files(dialogue_file, predictions_file, output_file):
    # 读取对话数据
    with open(dialogue_file, 'r', encoding='utf-8') as file:
        dialogues = json.load(file)
    
    # 读取预测数据
    predictions = []
    with open(predictions_file, 'r', encoding='utf-8') as file:
        for line in file:
            pred_data = json.loads(line)
            # 只取前四个大写字符作为MBTI类型
            mbti = ''.join([char for char in pred_data["predict"] if char.isupper()][:4])
            predictions.append(mbti)
    
    # 根据索引合并数据
    results = []
    for index, dialogue in enumerate(dialogues):
        speaker = dialogue['output']
        mbti_type = predictions[index]
        result = {
            "Speaker": speaker,
            "MBTI": mbti_type
        }
        results.append(result)

    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

# 调用函数处理文件
dialogue_file = '/root/autodl-tmp/dialogues.json'
predictions_file = '/root/autodl-tmp/generated_predictions.jsonl'
output_file = '/root/autodl-tmp/results.json'
process_files(dialogue_file, predictions_file, output_file)
