from twitter import Twitter
import time

tw = Twitter()
botid = '1214915482702114816'

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    if "tweetindong" in message:
                        message = message.replace("tweetindong", "its/")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media!")
                                tw.post_tweet_with_media(message, dms[i]['media'])
                                tw.delete_dm(id)

                        else:
                            print("DM deleted because it's an empty message")
                            #tw.read_dm() 
                            tw.delete_dm(id)


                    else:
                        print("DM will be deleted, no keyword detected!")
                        #tw.read_dm()
                        tw.delete_dm(id)

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(30)

if __name__ == "__main__":
    start()
