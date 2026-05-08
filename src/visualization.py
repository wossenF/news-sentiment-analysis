import matplotlib.pyplot as plt



def plot_headline_length_distribution(df):
    plt.figure(figsize=(10, 5))

    plt.hist(df["headline_length"], bins=50)

    plt.title("Headline Length Distribution")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")

    plt.show()



def plot_top_publishers(publisher_counts):
    plt.figure(figsize=(10, 5))

    publisher_counts.plot(kind="bar")

    plt.title("Top Publishers")
    plt.xlabel("Publisher")
    plt.ylabel("Article Count")

    plt.show()



def plot_daily_news_volume(daily_counts):
    plt.figure(figsize=(12, 5))

    daily_counts.plot()

    plt.title("Daily News Volume")
    plt.xlabel("Date")
    plt.ylabel("Articles")

    plt.show()

def plot_hourly_news_volume(hourly_counts):
    plt.figure(figsize=(10, 5))

    hourly_counts.plot(kind="bar")

    plt.title("Hourly News Distribution")
    plt.xlabel("Hour")
    plt.ylabel("Articles")

    plt.show()