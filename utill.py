import pandas as pd

PATH = "/Users/junyuwu/Amazon/components/apple_iphone_11_reviews.csv"
df = pd.read_csv(PATH)
df.dropna(inplace = True)
df.reset_index(drop=True, inplace=True)
df.drop(columns = "index", inplace=True)

def get_comments():
    bycomments = df["total_comments"].value_counts().to_frame()
    bycomments.reset_index(inplace=True)
    return bycomments

def get_rate():
    byrate = df["review_rating"].value_counts().to_frame()
    byrate.reset_index(inplace=True)
    return byrate

def get_text(): 
    bytext = df["review_text"].value_counts()[:10].to_frame()
    bytext.reset_index(inplace=True)
    return bytext

def get_title():
    bytitle = df["review_title"].value_counts()[:10].to_frame()
    bytitle.reset_index(inplace=True)
    return bytitle