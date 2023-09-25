import os
import json
from collections import defaultdict

def extract_name(filename):
    parts = filename.split("-")[3:]
    return " ".join(parts)

def main():
    root_folder = r'C:\Users\marv_\Downloads\SVGs'
    json_output = []
    type_counts = defaultdict(int)
    
    for root, _, files in os.walk(root_folder):
        folder_name = os.path.basename(root).replace(" ", "_").replace("+", "plus")
        
        for file in files:
            if file.endswith('.svg'):
                file_name_no_ext = os.path.splitext(file)[0]
                type_value = file_name_no_ext.replace(" ", "_")
                type_counts[type_value] += 1
                
                item = {
                    "type": type_value,
                    "category": folder_name,
                    "backgroundImageUrl": f"assets/diagram_icons/{folder_name}/{file}",
                    "title": extract_name(file_name_no_ext),
                    "defaultWidth": 1.5,
                    "defaultHeight": 1,
                    "minWidth": 1.5,
                    "minHeight": 1,
                    "maxWidth": 3,
                    "maxHeight": 2,
                    "allowEditText": True
                }
                json_output.append(item)

    duplicates = [key for key, value in type_counts.items() if value > 1]
    if duplicates:
        print("Duplicate types found:", duplicates)
    else:
        print("No duplicates found.")
                
    print(json.dumps(json_output, indent=4))

if __name__ == "__main__":
    main()