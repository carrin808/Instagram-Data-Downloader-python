import instaloader

insta = instaloader.Instaloader()

acc = 'nairobi_electronics.ke'

insta.download_profile(acc, profile_pic_only=False)