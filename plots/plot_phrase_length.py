import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import matplotlib.ticker as ticker

###########  SARS ########### 
avg_lengths_0_5 = [517.011, 1960.458, 2118.688, 2344.270, 2308.461, 2346.422]  
avg_lengths_1 = [545.611, 2181.873, 2365.697, 2609.676, 2568.146, 2613.410]  
avg_lengths_2 = [600.016, 2425.336, 2639.597, 2910.687, 2862.744, 2914.757]

# Standard deviations for each sequence
std_dev_0_5 = [1095.982, 3558.317, 3826.538, 4234.769, 4178.048, 4219.380]  
std_dev_1 = [1146.196, 3893.736, 4209.440, 4635.012, 4563.463, 4612.021]
std_dev_2 = [1215.679, 4301.732, 4662.223, 5115.183, 5031.623, 5086.630] 

# Sequence numbers (x-axis)
sequence_numbers = [10, 25, 50, 100, 200, 400]

# Plotting with error bars
plt.figure(figsize=(6.4, 4))
plt.errorbar(sequence_numbers, avg_lengths_0_5, yerr=std_dev_0_5, fmt='-o', color='blue', label='RLZ-RePair (0.5%)', capsize=5)
plt.errorbar(sequence_numbers, avg_lengths_1, yerr=std_dev_1, fmt='-o', color='orange', label='RLZ-RePair (1%)', capsize=5)
plt.errorbar(sequence_numbers, avg_lengths_2, yerr=std_dev_1, fmt='-o', color='green', label='RLZ-RePair (2%)', capsize=5)

# Labels and title
plt.xscale("log")
plt.xticks(sequence_numbers, labels=[str(num) for num in sequence_numbers])
plt.gca().xaxis.set_major_locator(ticker.FixedLocator(sequence_numbers))
plt.gca().xaxis.set_minor_locator(ticker.NullLocator())
plt.tick_params(axis='both', which='major', labelsize=12)  # for major ticks
plt.tick_params(axis='both', which='minor', labelsize=10)  # optional, for minor ticks
plt.xlabel('Number of Sequences (1000x) (Log Scale)', fontsize = 16)
plt.ylabel('Average RLZ Phrase Length', fontsize = 16)
plt.legend()
plt.legend(fontsize=12)
plt.grid(True, which="both", linestyle="--")

# Save plot
for ext in ['jpeg','pdf','svg','eps']:
    plt.savefig("sars_phrase_stats" + "." + ext, bbox_inches='tight', dpi=300)


######### Chr 19 ########

avg_lengths_0_5 = [2993.873, 3092.526, 3029.630, 3031.092, 3104.322, 3110.121, 3235.973, 3246.648, 3408.368, 3208.598, 2896.723]  
avg_lengths_1 = [4478.451, 4800.289, 5006.564, 5199.627, 5381.108, 5418.084, 5703.696, 5685.689, 5971.818, 5344.815, 4429.407]  
avg_lengths_2 = [6810.526, 6950.459, 7293.686, 7265.709, 7395.064, 7363.259, 7751.080, 7695.370, 7988.366, 7177.118, 6009.618]

# Standard deviations for each sequence
std_dev_0_5 = [23074.179, 23589.332, 23329.454, 23349.490, 23664.690, 23699.737, 59785.871, 59939.780, 46866.794, 41178.068, 43146.238]  
std_dev_1 = [28448.775, 29667.909, 30365.965, 30960.315, 31578.723, 31694.924, 107681.444, 94573.034, 96917.239, 77018.728, 68206.478]
std_dev_2 = [35136.763, 35783.512, 36774.359, 36755.625, 37140.909, 37082.402, 125566.028, 110065.310, 134628.969, 102316.264, 97148.807] 

# Sequence numbers (x-axis)
sequence_numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# Plotting with error bars
plt.figure(figsize=(6.4, 4))
plt.errorbar(sequence_numbers, avg_lengths_0_5, yerr=std_dev_0_5, fmt='-o', color='blue', label='RLZ-RePair (0.5%)', capsize=5)
plt.errorbar(sequence_numbers, avg_lengths_1, yerr=std_dev_1, fmt='-o', color='orange', label='RLZ-RePair (1%)', capsize=5)
plt.errorbar(sequence_numbers, avg_lengths_2, yerr=std_dev_1, fmt='-o', color='green', label='RLZ-RePair (2%)', capsize=5)

# Labels and title
plt.xscale("log")
plt.xticks(sequence_numbers, labels=[str(num) for num in sequence_numbers])
plt.gca().xaxis.set_major_locator(ticker.FixedLocator(sequence_numbers))
plt.gca().xaxis.set_minor_locator(ticker.NullLocator())
plt.tick_params(axis='both', which='major', labelsize=12)  # for major ticks
plt.tick_params(axis='both', which='minor', labelsize=10)  # optional, for minor ticks
plt.xlabel('Number of Sequences (Log Scale)', fontsize = 16)
plt.ylabel('Average RLZ Phrase Length', fontsize = 16)
plt.legend()
plt.legend(fontsize=12)
plt.grid(True, which="both", linestyle="--")

# Save plot
for ext in ['jpeg','pdf','svg','eps']:
    plt.savefig("chr19_phrase_stats" + "." + ext, bbox_inches='tight', dpi=300)


