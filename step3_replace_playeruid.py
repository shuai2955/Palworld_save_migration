import os
import json

def replace_playeruids_and_timestamp_in_source(source_json_dir, target_json_dir, source_lines, target_lines):
    for src_filename, tgt_filename in zip(source_lines, target_lines):
        src_filepath = os.path.join(source_json_dir, src_filename + '.json')
        tgt_filepath = os.path.join(target_json_dir, tgt_filename + '.json')

        if os.path.exists(src_filepath) and os.path.exists(tgt_filepath):
            # 读取 target 文件的 PlayerUID 和 Timestamp
            with open(tgt_filepath, 'r') as tgt_file:
                tgt_data = json.load(tgt_file)
                target_uid = tgt_data.get("properties", {}).get("SaveData", {}).get("value", {}).get("PlayerUID", {}).get("value", "")
                target_timestamp = tgt_data.get("Timestamp", None)

            # 读取 source 文件并替换所有的 PlayerUID 和 Timestamp
            if target_uid:
                with open(src_filepath, 'r') as src_file:
                    src_data = json.load(src_file)
                    src_data["properties"]["SaveData"]["value"]["PlayerUID"]["value"] = target_uid
                    if target_timestamp is not None:
                        src_data["Timestamp"] = target_timestamp

                with open(src_filepath, 'w') as src_file:
                    json.dump(src_data, src_file, indent=4)

# 示例使用路径（请根据实际情况替换）
source_json_dir = 'source_json/Players'
target_json_dir = 'target_json/Players'
source_txt_path = 'source.txt'
target_txt_path = 'target.txt'

# 读取 source.txt 和 target.txt 中的文件名
source_lines = []
target_lines = []

with open(source_txt_path, 'r') as src_file:
    source_lines = [line.strip() for line in src_file.readlines()]

with open(target_txt_path, 'r') as tgt_file:
    target_lines = [line.strip() for line in tgt_file.readlines()]

# 确保两个列表的长度相同
if len(source_lines) != len(target_lines):
    raise ValueError("source.txt 和 target.txt 的行数不匹配")

# 执行替换操作
replace_playeruids_and_timestamp_in_source(source_json_dir, target_json_dir, source_lines, target_lines)
