CAT_PHOTO_PATH_1 = "cat_funny.jpg"
CAT_PHOTO_PATH_2 = "cat_play.jpg"
CAT_PHOTO_PATH_3 = "cat_sleep.jpg"

class CatStatsDb:
    name = ""
    age = 1
    sleep = False
    satiety = 40
    happy = 40
    avatar = CAT_PHOTO_PATH_1

    @classmethod
    def get_avatar(cls):
        if cls.satiety > 53:
            cls.avatar = CAT_PHOTO_PATH_1
        elif cls.play > 15:
            cls.avatar = CAT_PHOTO_PATH_2


    @classmethod
    def play(cls):
        cls.happy += 15
        cls.satiety += 10
        cls.get_avatar()