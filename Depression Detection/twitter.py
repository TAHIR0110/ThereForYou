from ntscraper import Nitter


def extractweet(given_user, num=10):
    scraper = Nitter(log_level=1, skip_instance_check=False)
    tweets = scraper.get_tweets(given_user, mode="user", number=num)

    tweets.keys()

    data = {
        "date": [],
        "text": [],
    }

    for tweet in tweets["tweets"]:
        data["date"].append(tweet["date"])
        data["text"].append(tweet["text"])

    import pandas as pd

    df = pd.DataFrame(data)
    df.head()
    filename = given_user + ".csv"
    df.to_csv(filename)
    return df


given_user = input("Enter: ")
extractweet(given_user)
