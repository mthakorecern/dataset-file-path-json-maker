import os
import subprocess
import json
import argparse

REDIRECTOR = "root://xrootd-cms.infn.it/"

def determine_year_key(dataset):
    """Determine year key for output grouping."""
    if "2024" in dataset:
        return "2024"
    elif "2022" in dataset:
        return "2022"
    else:
        return "Other"

def extract_short_name(dataset):
    """
    Extract short name from dataset:
    - Base name: WtoENu_4Jets
    - Version tag: v2-v2 → extracted from second component
    Result: WtoENu_4Jets_v2-v2
    """
    parts = dataset.strip("/").split("/")
    base = parts[0]
    version_tag = parts[1].split("-")[-1]  # e.g., 'v2' from "...realistic_v2-v2"
    version_suffix = parts[1].split("_")[-1]  # e.g., 'v2-v2'
    short_name = "_".join(base.split("-")[:2]) + f"_{version_suffix}"
    return short_name

def main():
    parser = argparse.ArgumentParser(description="Generate filelist JSON for datasets.")
    parser.add_argument("input_file", help="Text file with one dataset per line")
    parser.add_argument("process_label", help="Physics process label (e.g., WJets, ZJets)")
    parser.add_argument("output_file", help="Output JSON filename (e.g., output.json)")

    args = parser.parse_args()

    output_json = {}

    with open(args.input_file) as f:
        for line in f:
            dataset = line.strip()
            if not dataset:
                continue

            try:
                print(f"[DAS] Querying files for: {dataset}")
                result = subprocess.check_output(
                    ["dasgoclient", "--query", f"file dataset={dataset} status=VALID", "--limit=0"],
                    text=True
                )
                rootfiles = result.strip().split("\n")
                full_paths = [f"{REDIRECTOR}{f.strip()}" for f in rootfiles if f.strip()]
            except subprocess.CalledProcessError:
                print(f"DAS query failed: {dataset}")
                continue

            short_name = extract_short_name(dataset)
            year_key = determine_year_key(dataset)

            output_json[dataset] = {
                "short_name": short_name,
                "year": year_key,
                "process": args.process_label,
                "xsec": None,  
                "files": full_paths
            }

    with open(args.output_file, "w") as fout:
        json.dump(output_json, fout, indent=2)
    print(f"Saved: {args.output_file}")

if __name__ == "__main__":
    main()
