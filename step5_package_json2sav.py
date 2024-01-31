#!/usr/bin/env python3

import argparse
import json
import os

from lib.gvas import GvasFile
from lib.noindent import CustomEncoder
from lib.palsav import compress_gvas_to_sav, decompress_sav_to_gvas
from lib.paltypes import PALWORLD_CUSTOM_PROPERTIES, PALWORLD_TYPE_HINTS


def main():
    parser = argparse.ArgumentParser(
        prog="palworld-save-tools",
        description="Converts Palworld save files to and from JSON",
    )
    parser.add_argument("filename")
    parser.add_argument(
        "--to-json",
        action="store_true",
        help="Override heuristics and convert SAV file to JSON",
    )
    parser.add_argument(
        "--from-json",
        action="store_true",
        help="Override heuristics and convert JSON file to SAV",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file (default: <filename>.json or <filename>.sav)",
    )
    parser.add_argument("--minify-json", action="store_true", help="Minify JSON output")
    args = parser.parse_args()

    if args.to_json and args.from_json:
        print("Cannot specify both --to-json and --from-json")
        exit(1)

    if not os.path.exists(args.filename):
        print(f"{args.filename} does not exist")
        exit(1)
    if not os.path.isfile(args.filename):
        print(f"{args.filename} is not a file")
        exit(1)

    if args.to_json or args.filename.endswith(".sav"):
        if not args.output:
            output_path = args.filename + ".json"
        else:
            output_path = args.output
        convert_sav_to_json(args.filename, output_path, args.minify_json)

    if args.from_json or args.filename.endswith(".json"):
        if not args.output:
            output_path = args.filename.replace(".json", "")
        else:
            output_path = args.output
        convert_json_to_sav(args.filename, output_path)


def convert_sav_to_json(filename, output_path, minify):
    print(f"Converting {filename} to JSON, saving to {output_path}")

    print(f"Decompressing sav file")
    with open(filename, "rb") as f:
        data = f.read()
        raw_gvas, _ = decompress_sav_to_gvas(data)
    print(f"Loading GVAS file")
    gvas_file = GvasFile.read(raw_gvas, PALWORLD_TYPE_HINTS, PALWORLD_CUSTOM_PROPERTIES)
    print(f"Writing JSON to {output_path}")
    with open(output_path, "w", encoding="utf8") as f:
        indent = None if minify else "\t"
        json.dump(gvas_file.dump(), f, indent=indent, cls=CustomEncoder)


def convert_json_to_sav(filename, output_path):
    print(f"Converting {filename} to SAV, saving to {output_path}")

    print(f"Loading JSON from {filename}")
    with open(filename, "r", encoding="utf8") as f:
        data = json.load(f)
    gvas_file = GvasFile.load(data)
    print(f"Compressing SAV file")
    if (
            "Pal.PalWorldSaveGame" in gvas_file.header.save_game_class_name
            or "Pal.PalLocalWorldSaveGame" in gvas_file.header.save_game_class_name
    ):
        save_type = 0x32
    else:
        save_type = 0x31
    sav_file = compress_gvas_to_sav(
        gvas_file.write(PALWORLD_CUSTOM_PROPERTIES), save_type
    )
    print(f"Writing SAV file to {output_path}")
    with open(output_path, "wb") as f:
        f.write(sav_file)


def convert_all_json_to_sav(source_dir, final_dir, convert_func):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".json"):
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                final_file_path = os.path.join(final_dir, relative_path, file.replace(".json", ".sav"))

                if not os.path.exists(os.path.dirname(final_file_path)):
                    os.makedirs(os.path.dirname(final_file_path))

                # 假设 convert_json_to_sav 是已知的函数
                convert_func(source_file, final_file_path)

# 示例使用路径（请根据实际情况替换）
source_json_dir = 'source_json'
final_dir = 'final'

# 假设的 convert_json_to_sav 函数

# 执行转换操作
convert_all_json_to_sav(source_json_dir, final_dir, convert_json_to_sav)
