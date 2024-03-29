from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1
    plt.cla()
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set_xlabel('Die Value') 
    axes.set_ylabel('Frequency') 
    axes.set_ylim(top=max(frequencies) * 1.10)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,} \n {frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

sns.set_style('whitegrid')
figure = plt.figure('Rolling a Six-Sided Die')
values = list(range(1, 7))
frequencies = [0] * 6
number_of_frames = int(sys.argv[1]) if len(sys.argv) > 1 else 100
rolls_per_frame = int(sys.argv[2]) if len(sys.argv) > 2 else 10
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=200, fargs=(rolls_per_frame, values, frequencies)
)
plt.tight_layout()
plt.show()

# python dices_dinamic.py 50 5 3