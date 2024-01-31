import os
import json
def replace_header_in_level_files(source_json_dir, target_json_dir):
    file_names = ["LevelMeta.json", "Level.json"]

    for file_name in file_names:
        src_filepath = os.path.join(source_json_dir, file_name)
        tgt_filepath = os.path.join(target_json_dir, file_name)

        if os.path.exists(src_filepath) and os.path.exists(tgt_filepath):
            # 读取 target 文件的 header 部分
            with open(tgt_filepath, 'r') as tgt_file:
                tgt_data = json.load(tgt_file)
                target_header = tgt_data.get("header", {})

            # 读取 source 文件，替换 header 部分，并保存
            with open(src_filepath, 'r') as src_file:
                src_data = json.load(src_file)
                src_data["header"] = target_header

            with open(src_filepath, 'w') as src_file:
                json.dump(src_data, src_file, indent=4)

# 示例使用路径（请根据实际情况替换）
source_json_dir = 'source_json'
target_json_dir = 'target_json'

# 执行替换操作
replace_header_in_level_files(source_json_dir, target_json_dir)
