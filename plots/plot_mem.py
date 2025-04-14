import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import matplotlib.ticker as ticker

def extract_file_number_and_software(filename):
    # Match a number followed by software name, optionally a rule, ending in compress.benchmark.txt
    match = re.search(r'\b(\d+)\.([\w-]+)(?:\.[\w-]+)?\.compress\.benchmark\.txt$', filename)
    if match:
        num = int(match.group(1))
        software = match.group(2)
        return (num, software)
    return (None, None)


def plot_file_numbers(directories, extension, output_basename, sample, multiplier, rlz_rules=None):
    # Mapping of internal software names to pretty display names
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
                    file_data.append((num, soft, rule, filepath))

    # Group files by (software + rule)
    software_groups = {}
    for num, soft, rule, f in file_data:
        key = f"{soft}__{rule}" if rule else soft
        if key not in software_groups:
            software_groups[key] = {}
        software_groups[key][num] = f

    # Get all unique file numbers
    all_file_numbers = sorted(set(num for num, _, _, _ in file_data))

    plt.figure(figsize=(6.4, 4))

    for key, files in software_groups.items():
        sorted_numbers = []
        times = []

        for num in all_file_numbers:
            if num in files:
                df = pd.read_csv(files[num], delimiter='\t')
                if 'max_rss' not in df.columns:
                    continue
                sorted_numbers.append(num)
                times.append(df['max_rss'].iloc[-1])

        if sorted_numbers:
            if '__' in key:
                soft, rule = key.split('__')
            else:
                soft, rule = key, None
            display_name = name_map.get(soft, soft.capitalize())
            if rule:
                display_name += f" ({rule})"
  
            plt.plot(sorted_numbers, times, marker='o', linestyle='-', label=display_name)

    # X-axis formatting
    plt.xscale("log")
    plt.xticks(all_file_numbers, labels=[str(num) for num in all_file_numbers])
    plt.gca().xaxis.set_major_locator(ticker.FixedLocator(all_file_numbers))
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())
    plt.tick_params(axis='both', which='major', labelsize=12)  # for major ticks
    plt.tick_params(axis='both', which='minor', labelsize=10)  # optional, for minor ticks


    # Axis labels
    plt.xlabel('Number of Sequences (1000x) (Log Scale)' if multiplier else 'Number of Sequences (Log Scale)', fontsize = 16)
    plt.ylabel('Memory (MB)', fontsize = 16)
    plt.title(sample)
    plt.legend()
    plt.legend(fontsize=12)  # Adjust the font size of the legend
    plt.grid(True, which="both", linestyle="--")

    # Save plot
    for ext in ['jpeg','pdf','svg','eps']:
        plt.savefig(f"{output_basename}.{ext}", bbox_inches='tight', dpi=300)


plot_file_numbers(
    directories=[
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_2000_ref",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_4000_ref", 
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/SARS/final_8000_ref",  
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/SARS/normal",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/SARS/large",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/bigrepair/SARS",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rerepair/SARS"
    ],
    extension=".compress.benchmark.txt",
    output_basename="sars_memory",
    sample="",
    multiplier=True,
    rlz_rules=["0.5%", "1%", "2%", "default", "large", None, None]
)

plot_file_numbers(
    directories=[
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19/final_5_ref",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19/final_10_ref",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19/final_20_ref",   
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/chr19/normal",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/repair/chr19/large",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/bigrepair/chr19",
        "/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rerepair/chr19"
    ],
    extension=".compress.benchmark.txt",
    output_basename="chr19_memory",
    sample="",
    multiplier=False,
    rlz_rules=["0.5%","1%","2%", "default", "large", None, None]
)

