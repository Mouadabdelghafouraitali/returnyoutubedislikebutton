import sys
import threading
import requests
import json

video_url = sys.argv[1]
# e.g. https://youtu.be/kxOuG8jMIgI
main_api = "https://returnyoutubedislikeapi.com/votes?videoId="


def get_video_id(video_url):
    _video_ID = video_url.replace("https://youtu.be/", "")
    _video_ID = _video_ID.replace("https://youtube.com/watch?v=", "")
    _video_ID = _video_ID.replace("https://www.youtu.be/", "")
    _video_ID = _video_ID.replace("https://www.youtube.com/watch?v=", "")
    _video_ID = _video_ID.replace("&feature=share", "")
    return _video_ID


video_id = get_video_id(video_url)


def get_data(video_id):
    res = requests.get(main_api + video_id)
    response = json.loads(res.text)
    likes = response["likes"]
    dislikes = response["dislikes"]
    rating = response["rating"]
    view_count = response["viewCount"]
    print("Likes: {:,} \nDislike {:,} \nRating: {}/5 \nViews:  {:,}".format(likes,
                                                                            dislikes,
                                                                            round(rating, 2),
                                                                            view_count))


thread = threading.Thread(name='process', target=get_data(video_id))
thread.start()
