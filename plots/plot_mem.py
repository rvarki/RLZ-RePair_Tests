import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import matplotlib.ticker as ticker

def extract_file_number_and_software(filename):
    # Expected format: something.NUM.SOFTWARE.RULE.something.txt
    match = re.search(r'(\w+)\.(\d+)\.([\w-]+)\.([\w-]+)\.(\w+)', filename)
    return (int(match.group(2)), match.group(3)) if match else (None, None)

def plot_file_numbers(directories, extension, output_basename, sample, multiplier, rlz_rules=None):
    # Mapping of internal software names to display names
    name_map = {
        "rlz-repair": "RLZ-RePair",
        "repair": "RePair",
        "bigrepair": "BigRePair",
        "rerepair": r"$\mathrm{Re^2Pair}$",
    }

    file_data = []
    for i, directory in enumerate(directories):
        rule = rlz_rules[i] if rlz_rules and i < len(rlz_rules) else None
        for file in os.listdir(directory):
            if file.endswith(extension):
                filepath = os.path.join(directory, file)
                num, soft = extract_file_number_and_software(file)
                if num is not None:
                    file_data.append((num, soft, rule if soft == "rlz-repair" else None, filepath))

    # Group files by software+rule combo
    software_groups = {}
    for num, soft, rule, f in file_data:
        key = f"{soft}-{rule}" if soft == "rlz-repair" else soft
        if key not in software_groups:
            software_groups[key] = {}
        software_groups[key][num] = f

    # Gather all unique file numbers
    all_file_numbers = sorted(set(num for num, _, _, _ in file_data))

    plt.figure(figsize=(12, 6))

    for software, files in software_groups.items():
        sorted_numbers = []
        memory = []

        for num in all_file_numbers:
            if num in files:
                df = pd.read_csv(files[num], delimiter='\t')
                if 'max_rss' not in df.columns:
                    continue
                sorted_numbers.append(num)
                memory.append(df['max_rss'].iloc[-1])

        if sorted_numbers:
            base_name = software.split("-")[0]
            if base_name == "rlz":
                rule_name = software.split("-")[2] if "-" in software else None
                display_name = f"RLZ-RePair ({rule_name})"
            else:
                display_name = name_map.get(software, software)
            plt.plot(sorted_numbers, memory, marker='o', linestyle='-', label=display_name)

    # Set x-axis to log scale
    plt.xscale("log")
    plt.xticks(all_file_numbers, labels=[str(num) for num in all_file_numbers])
    plt.gca().xaxis.set_major_locator(ticker.FixedLocator(all_file_numbers))
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())

    # Axis labels
    if multiplier:
        plt.xlabel('Haplotypes (1000x) (Log Scale)')
    else:
        plt.xlabel('Haplotypes (Log Scale)')
    plt.ylabel('Memory (MiB)')
    plt.title(sample)
    plt.legend()
    plt.grid(True, which="both", linestyle="--")

    # Save plot
    for ext in ['jpeg']:
        plt.savefig(f"{output_basename}.{ext}")


# plot_file_numbers(
#     directories=[
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_2000_ref",
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_4000_ref", 
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_8000_ref",  
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/SARS",
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/bigrepair/SARS",
#         "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rerepair/SARS"
#     ],
#     extension=".compress.benchmark.txt",
#     output_basename="sars_memory",
#     sample="SARS-CoV-2",
#     multiplier=True,
#     rlz_rules=["0.5%", "1%", "2%", None, None, None]
# )

plot_file_numbers(
    directories=[
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19/final_chr19_1_ref",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19/final_20_ref",   
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/chr19",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/bigrepair/chr19",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rerepair/chr19"
    ],
    extension=".compress.benchmark.txt",
    output_basename="chr19_memory",
    sample="Chromosome 19",
    multiplier=False,
    rlz_rules=["1 ref","2%", None, None, None]
)

