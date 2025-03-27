import matplotlib.pyplot as plt


def create_pie_chart(easy_count, medium_count, hard_count, last_updated):
  
    labels, counts, colors, legend_labels = [], [], [], []

    if easy_count > 0:
        labels.append('Easy')
        counts.append(easy_count)
        colors.append('lightgreen')
        legend_labels.append(f'Easy ({easy_count})')

    if medium_count > 0:
        labels.append('Medium')
        counts.append(medium_count)
        colors.append('gold')
        legend_labels.append(f'Medium ({medium_count})')

    if hard_count > 0:
        labels.append('Hard')
        counts.append(hard_count)
        colors.append('salmon')
        legend_labels.append(f'Hard ({hard_count})')

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        counts,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        labels=None
    )

    ax.set_title(f'Task Difficulty Distribution\n(Last Updated: {last_updated})')
    ax.axis('equal')

    # Separate legend with counts
    ax.legend(wedges, legend_labels, title="Difficulty", loc="center left", bbox_to_anchor=(1, 0.5))

    # Save and show
    output_file = 'task_distribution.png'
    plt.savefig(output_file, bbox_inches='tight')

easy_count = 1
medium_count = 0
hard_count = 0
last_updated = '27-Mar-2025'

create_pie_chart(easy_count, medium_count, hard_count, last_updated)