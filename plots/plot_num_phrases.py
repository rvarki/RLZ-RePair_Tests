import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import matplotlib.ticker as ticker

###########  SARS ########### 
phrases_0_5 = [576461, 379881, 703391, 1272508, 2584077, 5084916]  
phrases_1 = [546244, 341331, 629948, 1143093, 2322781, 4565438]  
phrases_2 = [496715, 307067, 564581, 1024879, 2083750, 4093433]

# Sequence numbers (x-axis)
sequence_numbers = [10, 25, 50, 100, 200, 400]

# Plotting with error bars
plt.figure(figsize=(6.4, 4))
plt.plot(sequence_numbers, phrases_0_5, marker='o', linestyle='-', color='blue', label='RLZ-RePair (0.5%)')
plt.plot(sequence_numbers, phrases_1, marker='o', linestyle='-', color='orange', label='RLZ-RePair (1%)')
plt.plot(sequence_numbers, phrases_2, marker='o', linestyle='-', color='green', label='RLZ-RePair (2%)')

# Labels and title
plt.xscale("log")
plt.yscale("log")
plt.xticks(sequence_numbers, labels=[str(num) for num in sequence_numbers])
plt.gca().xaxis.set_major_locator(ticker.FixedLocator(sequence_numbers))
plt.gca().xaxis.set_minor_locator(ticker.NullLocator())
plt.gca().yaxis.set_minor_locator(ticker.NullLocator())
plt.tick_params(axis='both', which='major', labelsize=12)  # for major ticks
plt.tick_params(axis='both', which='minor', labelsize=10)  # optional, for minor ticks
plt.xlabel('Number of Sequences (1000x) (Log)', fontsize = 16)
plt.ylabel('Number of RLZ Phrases (Log)', fontsize = 16)
plt.legend()
plt.legend(fontsize=12)
plt.grid(True, which="both", linestyle="--")

# Save plot
for ext in ['jpeg','pdf','svg','eps']:
    plt.savefig("sars_num_phrases" + "." + ext, bbox_inches='tight', dpi=300)


######### Chr 19 ########

phrases_0_5 = [19750, 38239, 78064, 156051, 304736, 608333, 1169345, 2330995, 4440792, 9434558, 20900644]  
phrases_1 = [13203, 24635, 47239, 90969, 175800, 349199, 663424, 1331047, 2534547, 5663752, 13668505]  
phrases_2 = [8682, 17014, 32426, 65101, 127923, 256950, 488186, 983438, 1894737, 4217808, 10074413]
 
# Sequence numbers (x-axis)
sequence_numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# Plotting with error bars
plt.figure(figsize=(6.4, 4))
plt.plot(sequence_numbers, phrases_0_5, marker='o', linestyle='-', color='blue', label='RLZ-RePair (0.5%)')
plt.plot(sequence_numbers, phrases_1, marker='o', linestyle='-', color='orange', label='RLZ-RePair (1%)')
plt.plot(sequence_numbers, phrases_2, marker='o', linestyle='-', color='green', label='RLZ-RePair (2%)')

# Labels and title
plt.xscale("log")
plt.yscale("log")
plt.xticks(sequence_numbers, labels=[str(num) for num in sequence_numbers])
plt.gca().xaxis.set_major_locator(ticker.FixedLocator(sequence_numbers))
plt.gca().xaxis.set_minor_locator(ticker.NullLocator())
plt.gca().yaxis.set_minor_locator(ticker.NullLocator())
plt.tick_params(axis='both', which='major', labelsize=12)  # for major ticks
plt.tick_params(axis='both', which='minor', labelsize=10)  # optional, for minor ticks
plt.xlabel('Number of Sequences (Log)', fontsize = 16)
plt.ylabel('Number of RLZ Phrases (Log)', fontsize = 16)
plt.legend()
plt.legend(fontsize=12)
plt.grid(True, which="both", linestyle="--")

# Save plot
for ext in ['jpeg','pdf','svg','eps']:
    plt.savefig("chr19_num_phrases" + "." + ext, bbox_inches='tight', dpi=300)


