import json
import argparse
import glob
import os

def merge_trace_files(input_files, output_file):
    # Read the first file as the base
    with open(input_files[0], 'r') as f:
        merged_data = json.load(f)
    
    # Merge traceEvents from the remaining files
    for file_path in input_files[1:]:
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Assume traceEvents are under the root key or "traceEvents" key
            trace_events = data.get("traceEvents", data)
            merged_data["traceEvents"].extend(trace_events)
    
    # Write the merged data to the output file
    with open(output_file, 'w') as f:
        json.dump(merged_data, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge multiple Chrome JSON trace files')
    parser.add_argument('input_patterns', nargs='+', help='Input JSON trace file paths or glob patterns')
    parser.add_argument('-o', '--output', default='merged.json', help='Output file path (default: merged.json)')
    args = parser.parse_args()
    
    # Expand glob patterns to get all matching files
    input_files = []
    for pattern in args.input_patterns:
        matched_files = glob.glob(pattern)
        if not matched_files:
            print(f"Warning: No files matched pattern '{pattern}'")
        input_files.extend(matched_files)
    
    # Check if any files were found
    if not input_files:
        print("Error: No input files found")
        exit(1)
    
    # Sort files by modification time (optional)
    input_files.sort(key=os.path.getmtime)
    
    merge_trace_files(input_files, args.output)
    print(f"Successfully merged {len(input_files)} files into {args.output}")
    print("List of merged files:")
    for file in input_files:
        print(f"  - {file}")