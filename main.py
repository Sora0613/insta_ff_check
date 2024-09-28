from instagrapi import Client


def main() :
    username = "USERNAME"
    password = "PASSWORD"

    cl = Client()
    cl.login(username, password)

    user_info_dict = cl.user_info_by_username_v1(username).dict()

    user_id = user_info_dict["pk"]

    # get followers by pk
    followings = cl.user_following_v1(user_id)

    for following in followings :
        following_id = following.pk

        following_followings = cl.user_following_v1(following_id)

        for follow in following_followings :
            if follow.pk == user_id :
                print(following.full_name + "(" + following.username + ")" + " is following you")
                break

            elif follow.pk != user_id :
                print(following.username + " is not following you")
                yes_or_no = input(
                    "Do you want to unfollow " + following.full_name + "(" + following.username + ") ? (y/n): ")
                if yes_or_no == "y" :
                    cl.user_unfollow(following.pk)
                    print(following.username + " is unfollowed")
                else :
                    break
                break


if __name__ == "__main__" :
    main()
