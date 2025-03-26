import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import matplotlib.ticker as ticker

# Uncomment if using SARS
# sorted_phrases = [323494, 1229369, 2437668, 4545892, 9033275, 18035783]

# Uncommennt if using Chr 19
sorted_phrases = [104251, 313186, 729688, 1559103, 3234363, 6555312] # Remove 1 and 128

def extract_file_number_and_software(filename):
    match = re.search(r'(\w+)\.(\d+)\.([\w-]+)\.([\w-]+)\.(\w+)', filename)
    return (int(match.group(2)), match.group(3)) if match else (None, None) 

def get_files_from_directories(directories, extension):
    filenames = []
    for directory in directories:
        for file in os.listdir(directory):
            if file.endswith(extension):
                filenames.append(os.path.join(directory, file))
    return filenames

def plot_file_numbers(directories, extension, output_basename, sample, multiplier):
    filenames = get_files_from_directories(directories, extension)
    file_data = [extract_file_number_and_software(os.path.basename(f)) + (f,) for f in filenames]
    file_data = [(num, soft, f) for num, soft, f in file_data if num is not None]
    
    # Group by software name and store files with file numbers
    software_groups = {}
    for num, soft, f in file_data:
        if soft not in software_groups:
            software_groups[soft] = {}
        software_groups[soft][num] = f
    
    # Find unique file numbers that are present across any software
    all_file_numbers = sorted(set(num for num, soft, _ in file_data))  # Collect only file numbers present in the files
    
    plt.figure(figsize=(12, 6))
    
    # Process each software group
    for software, files in software_groups.items():
        memory = []
        
        # Collect the memory for only the file numbers that are available for this software
        for num in all_file_numbers:
            if num in files:  # Check if the file number is available for this software
                df = pd.read_csv(files[num], delimiter='\t')
                if (num != 128 and num != 1): #TODO: Temp remove later
                    memory.append(df['max_rss'].iloc[-1])
        
        # Plot the data for this software
        if sorted_phrases:  # Only plot if there are valid numbers
            plt.plot(sorted_phrases, memory, marker='o', linestyle='-', label=software)
    
    # Set x-axis to logarithmic scale
    plt.xscale("log")  # Use logarithmic scale
    plt.xticks(sorted_phrases, labels=[str(num) for num in sorted_phrases])  # Set exact tick values
    plt.gca().xaxis.set_major_locator(ticker.FixedLocator(sorted_phrases))  # Force only your numbers
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())  # Remove extra minor ticks
    
    # Formatting
    if multiplier:
        plt.xlabel('Phrases (1000x) (Log Scale)')
    else:
        plt.xlabel('Phrases (Log Scale)')
    plt.ylabel('Memory (MiB)')
    plt.title(sample)
    plt.legend()
    plt.grid(True, which="both", linestyle="--")  # Show grid for better readability
    
    # Save plot in multiple formats
    for ext in ['jpeg', 'svg', 'eps', 'pdf']:
        plt.savefig(f"{output_basename}.{ext}")

# Example usage
plot_file_numbers(["/blue/boucher/rvarki/rlz-repair_analysis/benchmarks/rlz-repair/chr19"], 
                    ".compress.benchmark.txt",
                    "chr19_memory_rlz_phrases",
                    "Chromosome 19",
                    False)

