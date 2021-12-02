import random

import praw
reddit = praw.Reddit(
    client_id="eaeEIxHT_w_FMXK7r1ewiw",
    client_secret="YM7rHWvyO__Q3Pf55YHrkige_vXYDg",
    password="svpassword",
    username="pretentious_emo_name",
    user_agent = "amirite"
)
subreddit = reddit.subreddit('rareinsults')
while True:
    for post in subreddit.stream.submissions:
        replies = ["Oof that really was a violation","How do they come up with this LMAO","Ouch apply water to the burn man sheesh","Excuse me i am here to report a murder","Bit too far theyve been actually murdered"]
        reply = random.choice(replies)
        post.reply(reply)
