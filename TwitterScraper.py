import twint
import pandas as pd

def searchTweets():
    c = twint.Config()

    c.Limit = 3200
    c.Search = "#bitcoin"
    c.Min_likes = 20
    c.Since = "2021-08-14 00:00:00"
    c.Until = "2021-08-14 02:00:00"
    c.Custom["tweet"] = ["likes_count",
                         "hashtags",
                         "cashtags",
                         "photos",
                         "video",
                         "time",
                         "date",
                         "username"]
    c.Output = "tweets.csv"
    c.Store_csv = True

    tweets = twint.run.Search(c)

def addFollowersPerTweet():
    df = pd.read_csv("tweets.csv")

    followers = []
    for index, row in df.iterrows():
        c = twint.Config()
        c.Username = row["username"]
        c.Format = "{username},{followers}"
        c.Custom["user"] = ["followers"]
        c.Output = "tempFollowerColumn.csv"

        try:
            twint.run.Lookup(c)
        except:
            with open('tempFollowerColumn.csv', 'a') as fd:
                fd.write(row["username"] + ", null\n")

def combineFollowersAndTweets():
    followerColumn = pd.read_csv("tempFollowerColumn.csv", sep=',')['followers']
    tweets = pd.read_csv("tweets.csv", sep=',')
    tweets['followers'] = followerColumn

    tweets.to_csv("combined_csv.csv", index=False)



