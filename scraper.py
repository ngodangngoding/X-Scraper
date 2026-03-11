import asyncio, json, os
import pandas as pd
from twikit import Client

KEYWORD = "saham indonesia"
TARGET = 1000
PRODUCT = "Top"
SLEEP_DURATION = 5
COOKIES_PATH = "auth/cookies.json"

os.makedirs('data', exist_ok=True)

def load_and_clean_cookies(client, filepath='auth/cookies.json'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)

            if isinstance(raw_data, list):
                cookies_dict = {c['name']: c['value'] for c in raw_data}
                client.set_cookies(cookies_dict)
            else:
                client.set_cookies(raw_data)

    except FileNotFoundError:
        print(f"{filepath} not found")
        exit()

async def scrape_tweets(client, query):
    data = []
    
    try:
        tweets = await client.search_tweet(query, product=PRODUCT)

        while len(data) < TARGET:   
            if not tweets:
                break

            for tweet in tweets:
                data.append({
                    'Username': tweet.user.screen_name,
                    'Isi Tweet': tweet.text,
                    'Tanggal': tweet.created_at,
                    'Likes': tweet.favorite_count,
                    'Retweets': tweet.retweet_count
                })

                if len(data) >= TARGET:
                    break

            print(f"amount data: {len(data)} / {TARGET} data")

            if len(data) < TARGET:
                await asyncio.sleep(SLEEP_DURATION)
                tweets = await tweets.next()

    except Exception as e:
        print(f"error: {e}") 

    return data

def save_to_excel(data, keyword):
    df = pd.DataFrame(data)
    filename = f"data/scrape_{keyword.replace(' ','_')}.xlsx"
    df.to_excel(filename, index=False)
    print(f"Save as {filename}")

async def main():
    client = Client('en-US')
    load_and_clean_cookies(client, COOKIES_PATH)

    query = f"{KEYWORD} -filter:links -filter:replies -filter:retweets -judi -slot -gacor -promo lang:id"
    print(f"\n Start search: {query}")
    print("-" * 40)

    data = await scrape_tweets(client, query)
    print(f"get data: {len(data)}")

    if data:
        save_to_excel(data, KEYWORD)
        

if __name__ == '__main__':
    asyncio.run(main())