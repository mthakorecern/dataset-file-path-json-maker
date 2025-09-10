import os
import subprocess
import json
import argparse

REDIRECTOR = "root://cmsxcache.hep.wisc.edu/"

def determine_year_key(dataset):
    """Infer year from run era (Run2022X, Run2023X, etc.)"""
    if "Run2024" in dataset:
        return "2024"
    elif "Run2023" in dataset:
        return "2023"
    elif "Run2022" in dataset:
        return "2022"
    else:
        return "Other"

def extract_short_name(dataset):
    """
    Extract a short name from the dataset.
    For MC: /WtoENu_4Jets/Run3.../NANOAODSIM → WtoENu_4Jets_vX
    For Data: /JetMET0/Run2024C-MINIv6NANOv15-v1/NANOAOD → JetMET0_Run2024C_MINIv6NANOv15-v1
    """
    parts = dataset.strip("/").split("/")
    
    if "Run20" in parts[1]:  # Likely data
        return f"{parts[0]}_{parts[1]}"
    else:  # MC-like
        version_tag = parts[1].split("_")[-1]
        return "_".join(parts[0].split("-")[:2]) + f"_{version_tag}"


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
