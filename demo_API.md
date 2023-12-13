# Demo APIs

## 1. Search API with Multiple Parameters

### Endpoint
- [https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic)

### Method
- GET

### Parameters
- `search_author` (optional): Author name to search for.
- `at_from` and `at_to` (optional): Date range for comments.
- `like_from` and `like_to` (optional): Range for like counts.
- `reply_from` and `reply_to` (optional): Range for reply counts.
- `search_text` (optional): Search string in the text field.

### Response

```json
[
  {
    "at": "Thu, 19 Jan 2023 09:59:46 GMT",
    "author": "Fredrick Carlos",
    "like": 1,
    "reply": 1,
    "text": "*Because of the economic crisis that always comes up the best thing to be on every wise individual’s mind or list is to invest in different streams of income that’s not depending on the government to generate funds.*"
  },
  {
    "at": "Thu, 19 Jan 2023 09:59:49 GMT",
    "author": "Fredrick Carlos",
    "like": 4,
    "reply": 3,
    "text": "*I think every investor goes broke during a bear market and other major crashes but wrong!some make millions,i also thought everybody went out of business during the great depression but they didn't.Some went into Businesses, there's always depression/recession for some people and there's always profit to be made for others, It's all about perspective and right trading plan*"
  }
]
```

## 2. Search by Author

### Endpoint
- [https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick)

### Method
- GET

### Parameters
- `search_author`: Author name to search for.

### Response

```json
[
  {
    "at": "Thu, 19 Jan 2023 09:59:46 GMT",
    "author": "Fredrick Carlos",
    "like": 1,
    "reply": 1,
    "text": "*Because of the economic crisis that always comes up the best thing to be on every wise individual’s mind or list is to invest in different streams of income that’s not depending on the government to generate funds.*"
  },
  {
    "at": "Thu, 19 Jan 2023 09:59:49 GMT",
    "author": "Fredrick Carlos",
    "like": 4,
    "reply": 3,
    "text": "*I think every investor goes broke during a bear market and other major crashes but wrong!some make millions,i also thought everybody went out of business during the great depression but they didn't.Some went into Businesses, there's always depression/recession for some people and there's always profit to be made for others, It's all about perspective and right trading plan*"
  }
]
```
## 3. Search by Date Range

### Endpoint
- [https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?at_from=24-01-2023&at_to=27-01-2023](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?at_from=24-01-2023&at_to=27-01-2023)

### Method
- GET

### Parameters
- `at_from` and `at_to`: Date range for comments.

### Response
```json
[
  {
    "at": "Wed, 25 Jan 2023 23:59:38 GMT",
    "author": "Did you know?",
    "like": 0,
    "reply": 0,
    "text": "Thank you for this info , hoping to be monetized soon ! hopefully"
  },
  {
    "at": "Tue, 24 Jan 2023 13:17:41 GMT",
    "author": "Easy Groophz",
    "like": 0,
    "reply": 0,
    "text": "Good point. When you have a look at the history of chatbots ChatGPT is a bit smarter, but still too generic and has all the problems in it that the internet has (hate, bias, etc) because its database is the internet. There has to be invested a lot more time to get a tool that is really useful. If you are not firm in a certain niche it can give worth hints but if you are an expert in a niche or topic it is useless. And the problem with „intelligence“ in A.I., btw a marketing term, is that the technology behind is the simplest form of a brain simulation. It is not able to be creative and create something new to a certain problem. It is more of an intelligent pattern recognizer in a big amount of data. Helpful and faster than a human but not intelligent in the end. No system that can we trust in critical situations at the moment. The question is if we can develop an artifical intelligence without understanding how the human brain creates intelligence. Or when will we understand the human brain to start with a corresponding simulation ;-)."
  },
  {
    "at": "Tue, 24 Jan 2023 00:57:32 GMT",
    "author": "2nerdsonacouch",
    "like": 0,
    "reply": 0,
    "text": "We aren't entirely sure when but supposedly youtube is rolling out something that even if we have copyrighted music in our videos that we can license/share revenue on those videos? Any idea if that would be retroactive for videos that have already been posted?  Thank you :)"
  },
  {
    "at": "Tue, 24 Jan 2023 17:55:36 GMT",
    "author": "Louizon",
    "like": 1,
    "reply": 0,
    "text": "This that I don't understand you, you said that Ride at motion Channel have more that 300 subscribe! And you say that he still grows is income monthly. \n\nSo i'am so confused youtube monatize term say to get monatize you have to proof 1000 subscribe and 4000 watch hours! Right!\n\nHow he do that? youtube just privileges him? I'am confused now I don't understand any more 😕"
  },
  {
    "at": "Tue, 24 Jan 2023 13:31:51 GMT",
    "author": "Styling with Deon",
    "like": 0,
    "reply": 0,
    "text": "How to make 5000 monthly from my channel?"
  }
]
```

## 4. Search by Like and Reply Count Range

### Endpoint
- [https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?like_from=1&like_to=2&reply_from=0&reply_to=2](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?like_from=1&like_to=2&reply_from=0&reply_to=2)

### Method
- GET

### Parameters
- `like_from` and `like_to`: Range for like counts.
- `reply_from` and `reply_to`: Range for reply counts.

### Response
```json
[
  {
    "at": "Thu, 19 Jan 2023 09:59:46 GMT",
    "author": "Fredrick Carlos",
    "like": 1,
    "reply": 1,
    "text": "*Because of the economic crisis that always comes up the best thing to be on every wise individual’s mind or list is to invest in different streams of income that’s not depending on the government to generate funds.*"
  },
  {
    "at": "Wed, 18 Jan 2023 09:07:34 GMT",
    "author": "Nikita Maree",
    "like": 1,
    "reply": 1,
    "text": "The first one  👍\nI would love to know more about how much money different types of creators are making with how many views/  watchhours/ subscribers they have. Wether that's from add revenue or sponsored vids."
  },
  {
    "at": "Sat, 21 Jan 2023 02:01:36 GMT",
    "author": "KissMe",
    "like": 1,
    "reply": 1,
    "text": "Who uses patron????? Curious how it’s working out for you."
  },
  {
    "at": "Thu, 19 Jan 2023 04:47:35 GMT",
    "author": "HGNext ",
    "like": 1,
    "reply": 1,
    "text": "Whats up Nate! Your channel has been so helpful. I recently started my YT channel and it’s going well so far. Only thing is that I’m not getting the views I’d hope for. I feel like my content is too well crafted to not be seen by more people. Wondering if you can give me some advice?"
  },
  {
    "at": "Wed, 18 Jan 2023 04:03:44 GMT",
    "author": "KeSetoKaiba",
    "like": 1,
    "reply": 1,
    "text": "Howdy :D Nice video timing as my channel just got accepted for YPP and monetization about yesterday. Also, 10:28 I like both video ideas, but the 1st option piques my interest more right now. :)"
  },
  {
    "at": "Tue, 17 Jan 2023 22:06:43 GMT",
    "author": "CarsonRocks35",
    "like": 1,
    "reply": 1,
    "text": "The 5k a month would be definitely be an interesting one, but I tend to watch anything you put up. I also am curious about easier ways to study or be able to tell your channels quality with a much more popular video still effecting the direct statistics for the month. See I running a Minecraft/pokemon gaming channel where I grew up watching the two and always found lots of people liked both content types, but with no channels mixing them. Changing that was my hopes and it's really run well but I have a video from about a year ago and it's blown up. It pushed to the final stretch to monetization, but it's still going sorta which yes I'm happy about, but with all the views and revenue it's getting I haven't had a month of monetization without it, so it's hard to judge my revenue, monthly views and things since it still has effects on it currently. So I don't know my channels average monthlys are. Hope that made since sorry for the ramble as well.😆"
  },
  {
    "at": "Mon, 23 Jan 2023 23:44:12 GMT",
    "author": "OutThereSomeWhere",
    "like": 1,
    "reply": 0,
    "text": "Hey Nate, great video as always😃. Ive just started Project24. Im really enjoying the system structure, simply brilliant! I've been struggling to clearly define which approach I should take to monitise my channel. So would be keen on understanding \"How YouTubers are making money (with  real data)\". I've been working on my channel for over 12 months 650 subs, 3200 Watch Hrs. Hoping to start gaining Ad Revenue before the end of the year. But I know the real earning is outside of Ad Revenue."
  },
  {
    "at": "Wed, 18 Jan 2023 00:06:17 GMT",
    "author": "Tea Formula",
    "like": 1,
    "reply": 0,
    "text": "Is there an independent company that do merchandise on a no purchase, no fee basic like Patreon?"
  },
  {
    "at": "Tue, 24 Jan 2023 17:55:36 GMT",
    "author": "Louizon",
    "like": 1,
    "reply": 0,
    "text": "This that I don't understand you, you said that Ride at motion Channel have more that 300 subscribe! And you say that he still grows is income monthly. \n\nSo i'am so confused youtube monatize term say to get monatize you have to proof 1000 subscribe and 4000 watch hours! Right!\n\nHow he do that? youtube just privileges him? I'am confused now I don't understand any more 😕"
  },
  {
    "at": "Thu, 19 Jan 2023 09:09:14 GMT",
    "author": "Five Star",
    "like": 1,
    "reply": 0,
    "text": "Geology dude is a rock star\n\nYes I said it"
  },
  {
    "at": "Tue, 17 Jan 2023 22:46:55 GMT",
    "author": "Chris Reed Beats",
    "like": 1,
    "reply": 1,
    "text": "I always pre-boop the like button before watching 😂"
  },
  {
    "at": "Tue, 17 Jan 2023 22:43:46 GMT",
    "author": "scribbledjoy",
    "like": 1,
    "reply": 1,
    "text": "I’m sure option B could have a great, attention-getting title, but I also doubt every style of channel can get that kind of revenue. \n\nI’d much rather see content that combines what you did here (vlog channel = sponsorship focus) with real data from real channels."
  }
]
```

