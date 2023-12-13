# Demo APIs

## 1. Search API with Multiple Parameters

### Endpoint
[https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic)

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


## 3. Search by Date Range

### Endpoint
- [https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search](https://v2a30s3qi5.execute-api.ap-south-1.amazonaws.com/dev/search)

### Method
- GET

### Parameters
- `at_from` and `at_to`: Date range for comments.

### Response
- Returns comments posted within the specified date range.

**Example:**

