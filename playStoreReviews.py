from google_play_scraper import Sort, reviews
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

result, continuation_token = reviews(
    'co.pariksha.mpgov',
    lang='en',  # defaults to 'en'
    country='in',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    count=500,  # defaults to 100
    filter_score_with=5  # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'co.pariksha.mpgov',
    # defaults to None(load from the beginning)
    continuation_token=continuation_token
)

word_count = Counter()
for i in result:
    clean_str = i['content'].lower()
    words = clean_str.split(' ')
    for word in words:
        if word in stop_words:
            continue
        else:
            word_count[word] += 1
    # print(i['content'], i['at'])

print(word_count.most_common(50))
