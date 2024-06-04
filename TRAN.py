import pandas as pd
import json

# 读取CSV文件
def process_csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    # 确保所有列都被视为字符串，尤其是处理缺失数据时
    df.fillna('', inplace=True)  # 将NaN值替换为空字符串
    df['Dialogue'] = df['Dialogue'].astype(str)
    df['Speaker'] = df['Speaker'].astype(str)
    # 创建一个列表来存储所有的记录
    records = []

    for index, row in df.iterrows():
        # 添加指定的描述文本
        intro_text = """######CONTEXT###### MBTI personality analyzes people from four perspectives by understanding their preferences in doing things, obtaining information, and making decisions. Each dimension has two directions, totaling eight aspects. It includes (E)Extrovert and (I)Introvert, (S)Sensing and (N)iNtuitive, (T)Thinking and (F)Feeling, (J)Judging and (P)Perceptive. You are a psychoanalyst skilled at analyzing user texts to infer user personalities. We have a collection that includes text posted by users on social media. ######OBJECT####### We hope you can analyze the MBTI types of users based on their text. Please follow the steps below to 1. Determine E/I 2. Determine S/N 3. Determine T/F 4. Determine J/P ######Output Format##### Only output MBTI prediction results separated by ',' EXAMPLE-------->YOU OUTPUT-------->[E,N,T,P] ############INPUT#################"""
        
        # 将描述文本和对话内容合并
        full_text = intro_text + "\n" + row['Dialogue']
        
        # 创建一个字典来存储每个记录
        record = {
            'instruction':"",
            'input': full_text,
            'output': row['Speaker']
        }
        records.append(record)
    
    # 将所有记录保存到JSON文件
    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(records, outfile, indent=4, ensure_ascii=False)

# 调用函数
csv_file_path = '/root/autodl-tmp/dialogues.csv'
json_file_path = '/root/autodl-tmp/dialogues.json'
process_csv_to_json(csv_file_path, json_file_path)
