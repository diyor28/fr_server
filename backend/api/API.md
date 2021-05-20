#API

###GET requests

GET `http://127.0.0.1:8000/api/users/` will yield all users in following format:

##### Sample Response:
```json
[
  {
    "id": 28535,
    "gender": "Male",
    "vectors": [
      50725,
      50726
    ]
  },
  {
    "id": 28537,
    "gender": "Female",
    "vectors": [
      50727,
      49284
    ]
  },
  {
    "id": 28538,
    "gender": null,
    "vectors": [
      50728
    ]
  },
  {
    "id": 28539,
    "gender": null,
    "vectors": [
      50729
    ]
  }
]
```

GET `http://127.0.0.1:8000/api/users/?gender=Male` will yield only users with `gender=Male` in following format:

##### Sample Response:
```json
[
  {
    "id": 28535,
    "gender": "Male",
    "vectors": [
      50725,
      50726
    ]
  }
]
```

GET `http://127.0.0.1:8000/api/users/28535/` will yield a single user in following format:

The same works for all API queries

```json
    {
        "id": 28535,
        "visits": 0,
        "gender": null
    }
```

GET `http://127.0.0.1:8000/api/vectors/` will yield all vectors in following format:

```json
[
  {
    "id": 56461,
    "image": "http://127.0.0.1:8000/media/users/9179bc56eb2242d8983196fa80aa6fc0.jpg",
    "vector": [
      0.0674706399440765,
      0.33631956577301,
      0.0312996059656143,
      0.619466125965118,
      1.15994572639465,
      -0.82746100425720
    ],
    "confidence": 0.999988436698914,
    "user": 34270
  },
  {
    "id": 56460,
    "image": "http://127.0.0.1:8000/media/users/038c1c8938a742d791fac1d96cf0076e.jpg",
    "vector": [
      0.00205361843109131,
      2.09113502502441,
      -0.586905658245087,
      0.3498615026474,
      -1.40612971782684,
      0.993250727653503,
      0.409193426370621
    ],
    "confidence": 0.999609887599945,
    "user": 34269
  }
]
```

GET `http://127.0.0.1:8000/api/vectors?user_id=34720` will yield a single vector with `user_id=34720` in following format:

```json
  {
    "id": 56461,
    "image": "http://127.0.0.1:8000/api/media/users/9179bc56eb2242d8983196fa80aa6fc0.jpg",
    "vector": [
      0.0674706399440765,
      0.33631956577301,
      0.0312996059656143,
      0.619466125965118,
      1.15994572639465,
      0.154980704188347,
      -0.184786051511765,
      -0.82746100425720
    ],
    "confidence": 0.999988436698914,
    "user": 34270
  }
```



GET `http://127.0.0.1:8000/api/tasks/` will yield all pending tasks in following format:

```json
[
    {
        "id": 2672,
        "vector": [
            -0.388358294963837,
            2.83241367340088,
            -0.335491836071014,
            -0.449235498905182,
            -0.636573731899261,
            1.09059345722198,
            -0.161360621452332
        ],
        "camera_id": 1,
        "date": "2019-08-05T20:06:15.890331Z",
        "active": true,
        "image": "http://127.0.0.1:8000/media/temp/image_WcCYo4H.jpg"
    },
    {
        "id": 2673,
        "vector": [
            -0.187223076820374,
            2.83814835548401,
            -0.157589167356491,
            -0.818372130393982,
            -0.717805683612823,
            0.87730747461319,
            -0.740335047245026,
        ],
        "camera_id": 1,
        "date": "2019-08-05T20:35:01.301940Z",
        "active": false,
        "image": "http://127.0.0.1:8000/media/temp/image_NEkyOOe.jpg"
    },
    {
        "id": 2674,
        "vector": [
            -0.0423222705721855,
            2.34185481071472,
            0.11867905408144,
            -0.251777142286301,
            -0.969533622264862,
            0.852595686912537,
            -0.328652143478394
        ],
        "camera_id": 2,
        "date": "2019-08-05T20:35:21.420037Z",
        "active": false,
        "image": "base-url/media/temp/image_gUl2kD9.jpg"
    }
]
```

GET `http://127.0.0.1:8000/api/workers/` will yield all workers in following format:

```json
[
    {
        "id": 10,
        "active": false
    },
    {
        "id": 1,
        "active": true
    },
    {
        "id": 6,
        "active": true
    }
]
```


###POST requests

POST `http://127.0.0.1:8000/api/users/`

Request body:
```json
{
"gender": "Male"
}
```

```json
{
    "id": 34280,
    "gender": "Male"
}
```


