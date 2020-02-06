import pandas as pd
import numpy as np

### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    return {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'std': round(np.std(items, ddof=1), 2),
            'var': round(np.var(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}

### END FUNCTION

def five_num_summary(items):
    # your code here
    return {'max': round(np.max(items), 2),
            'median':  round(np.median(items), 2),
            'min': round(np.min(items), 2),
            'q1': np.percentile(items, 25, interpolation="midpoint"),
            'q3':np.percentile(items, 75, interpolation="midpoint")}

### END FUNCTION

### START FUNCTION
def date_parser(dates):
    # your code here
    return  [str(i.date()) for i in [pd.to_datetime(i) for i in dates]]

### END FUNCTION

### START FUNCTION
def extract_municipality_hashtags(df):
    # your code here
    emails = []
    hashtags = []
    for x in df["Tweets"]:
        emails.append([mun_dict[i] for i in x.lower().split(" ")  if i in mun_dict.keys()])  
        hashtags.append([i[i.find("#"):] for i in x.lower().split(" ")  if "#" in i])  
    formatted_emails = [i if i else np.nan for i in emails]
    formatted_hashtags = [i if i else np.nan for i in hashtags] 
    df["municipality"] = formatted_emails
    df["hashtags"] = formatted_hashtags
    # print(df.info())
    return df

### END FUNCTION

### START FUNCTION
def number_of_tweets_per_day(df):
    parsed = date_parser(df["Date"])
    unique_parsed = sorted(list(set(parsed)))
    counts = [parsed.count(i) for i in unique_parsed]
    
    tweets_per_day_df = pd.DataFrame({"Date": unique_parsed, "Tweets": counts})
    tweets_per_day_df.set_index('Date', inplace=True)

    return tweets_per_day_df

### END FUNCTION

### START FUNCTION
def word_splitter(df):
    # your code here
    df["Split Tweets"] = [i.lower().split(" ") for i in df["Tweets"]]
    return df

### END FUNCTION

### START FUNCTION
def stop_words_remover(df):
    # your code here
    without_stop_words = [[w for w in i if w.lower() not in stop_words_dict["stopwords"]] for i in [i.lower().split(" ") for i in df["Tweets"]]]
    # print(lis)
    without_links = [[x for x in i if "http" not in x] for i in without_stop_words]
    df["Without Stop Words"] = without_links
    return df

### END FUNCTION