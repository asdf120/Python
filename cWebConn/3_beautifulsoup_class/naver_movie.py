from urllib.request import *
from bs4 import BeautifulSoup

html = urlopen(
    "https://movie.naver.com/movie/bi/mi/basic.nhn?code=184517&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false")

soup = BeautifulSoup(html, 'html.parser')

scores = soup.select('div.score_result li>div.star_score>em')
reviews = soup.select('div.score_result li>div.score_reple>p')
for score, review in zip(scores, reviews):
    review = review.text.split()
    review = " ".join(review)
    print('평점 : {}점, 리뷰 : {}'.format(score.text, review))
