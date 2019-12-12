from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
POSTS = {
    "0": {
      "details":"This is a detail",
      "timestamp":"2019-11-24 15:27:45.741138",
      "user_id":9,
      "username":"Paul"
    },
    "1": {
      "details":"Down Vote: <Post id 103 - Jimmy>",
      "timestamp":"2019-11-22 04:23:16.517407",
      "user_id":26,
      "username":"larry"
    },
    "2": {
      "details":"Down Vote: <Post id 21 - A python script to run another python script>",
      "timestamp":"2019-11-22 04:22:36.511905",
      "user_id":26,
      "username":"larry"
    },
    "3": {
      "details":"Login <User id 26 - larry>",
      "timestamp":"2019-11-22 04:22:25.282066",
      "user_id":26,
      "username":"larry"
    },
    "4": {
      "details":"Logout <User id 25 - lebron_james>",
      "timestamp":"2019-11-21 23:03:29.236250",
      "user_id":25,
      "username":"lebron_james"
    },
    "5": {
      "details":"Up Vote: <Post id 27 - get list of users' latest tweet dates?>",
      "timestamp":"2019-11-21 23:02:43.876970",
      "user_id":25,
      "username":"lebron_james"
    },
    "6": {
      "details":"Login <User id 25 - lebron_james>",
      "timestamp":"2019-11-21 23:01:09.597690",
      "user_id":25,
      "username":"lebron_james"
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/posts
    with the complete lists of posts

    :return:        sorted list of posts
    """
    # Create the list of people from our data
    return [POSTS[key] for key in sorted(POSTS.keys())]
