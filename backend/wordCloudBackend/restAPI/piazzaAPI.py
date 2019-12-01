from piazza_api import Piazza
from html.parser import HTMLParser

# using this library to parse html tags in the content string
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def login(email, password):
    piazza = Piazza()
    piazza.user_login(email, password)
    class_dictionary = piazza.get_user_classes()
    return class_dictionary

    courseToHash = {}
    #print(len(class_dictionary))
    for i in range(len(class_dictionary)):
        courseToHash.update({class_dictionary[i]['num']: class_dictionary[i]['nid']})


def piazza_reader(email, password, coursecode):
    # User credentials
    piazza = Piazza()
    # Login
    piazza.user_login(email, password)
    # classHash from get_user_class, get classroom to read posts and questions

    class_dictionary = piazza.get_user_classes()

    courseToHash = {}
    #print(len(class_dictionary))
    for i in range(len(class_dictionary)):
        courseToHash.update({class_dictionary[i]['num']: class_dictionary[i]['nid']})

    print(courseToHash)

    classroom = piazza.network(courseToHash[coursecode])

    print(coursecode)
    print(courseToHash[coursecode])

    # go through all the posts, aggregate them in a data-structure
    postquestions = []
    postanswers = []

    # board_posts type is generator: cannot access memory in the lazy list
    board_posts = classroom.iter_all_posts(limit=30)

    for post in board_posts:
        # get rid of html tags
        question_string = strip_tags(post["history"][0]["content"])

        # append to questions array
        postquestions.append(question_string)

        # checks if there's an answer associated to the question
        if "children" in post.keys() and post["children"] and "history" in post["children"][0]:
            # for all answers in a single post (iterate)
            for answer_index in range(len(post["children"][0]["history"])):
                # get rid of html tags and check if the entry is a string
                if type(post["children"][0]["history"][answer_index]["content"]) == str:
                    answer_string = strip_tags(post["children"][0]["history"][answer_index]["content"])
                    # append to answers array
                    postanswers.append(answer_string)

    # print(postQuestions + postAnswers)

    return " ".join(postquestions + postanswers)

