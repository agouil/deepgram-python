# deepgram-python
A Python wrapper for the Deepgrap API https://www.deepgram.com/.

## Requirements
The wrapper is currently written for Python 2.7.xx

## Installation
Install this package with `pip`:
```
pip install git+https://github.com/agouil/deepgram-python
```

Or you can clone / download the repository and run:
```
python setup.py install
```

## Usage
```python
from deepgram import Deepgram

dg = Deepgram("API-KEY")

print dg.check_balance()  # => { "balance":  12.99, "userID":  "API-KEY" }
```

## Documentation

### check_balance()
*Returns the available balance for the user.*

Return value:
```json
{
    "balance":  12.99,
    "userID":  "API-KEY"
}
```

### check_status(obj)
*Returns the status of an audio object on the server.*

Params:

 - obj (*string*): The content ID of the object

Return value:
```json
{
    "status": "done"
}
```

### upload(media_url, tags=*None*)
*Uploads a remote audio file to the API.*

Params:

- media_url (*string*): The URL of the remote audio file
- tags (*list*) -- optional: Tags to describe the audio file

Return value:
```json
{
    "contentID":  "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx"
}
```

### upload_list(media_list)
*Uploads a list of remote audio files to the API.*

Params:

- media_list (*list*): A list of remote audio file URLs

Return value:
```json
{
    "contentID": [
        "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx",
        "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx"
    ]
}
```

### query(obj, query, **kwargs)
*Searches the specified object for the given term and returns the parts of it that contain any matches to the search term.*

Params:

- obj (*string*): The content ID fo the object
- query (*string*): The query term
- kwargs (*dict*): Extra arguments to pass to the function. Include:
    - Nmax (*int*): The maximum number of matches to return. **Default**: 10
    - Pmin (*float*): The minimum probability that qualifies a match. **Default**: 0.55
    - snippet (*bool*): Whether to return the transcript of a match. **Default**: True
    - sort (*string*): The term to sort by. **Default**: "time"

Return value:
```json
{
    "snippet": [
        "hello world"
    ],
    "P": [
        1.0
    ],
    "startTime": [
        1.11
    ],
    "endTime": [
        1.23
    ],
    "N": [
        0
    ]
}
```

### group_search(query, tag=*""*)
*Searches in all the uploaded audio objects with a given "tag" and "query term" and returns the contentIDs of any matches.*

Params:

- query (*string*):  The query term
- tag   (*string*) -- optional: The tag to use for the search. Narrows down the objects to be searched.

Return value:
```json
{
    "contentID": [
        "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx"
    ],
    "P": [
        1.0
    ],
    "N": [
        0
    ]
}
```

### parallel_search(query, **kwargs)
*Searched in all the uploaded audio objects with the given "tag" and "query term" and returns the parts of it that contain any matches to the search term.*

Params:

- query (*string*): The query term
- kwargs (*dict*):   Extra arguments to pass to the function. Include:
    - tag (*string*): The tag to use for the search. Narrows down the objects to be searched.
    - snippet (*bool*): Whether to return the transcript of a match. **Default**: True
    - group_Nmax (*int*): The maximum number of objects to return. **Default**: 10
    - object_Nmax (*int*): The maximum number of matches to return within the same object. **Default**: 10
    - object_Pmin (*float*): The minimum probability that qualifies a match. **Default**: 0.55
    - sort  (*string*): The term to sort by. **Default**: "time"

Return value:
```json
{
    "object_result": [
        {
            "contentID": "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx",
            "N": [
                0,
                1
            ],
            "snippet": [
                "hello world",
                "hello world again"
            ],
            "P": [
                1.0,
                0.4827729100918347
            ],
            "startTime": [
                1.11,
                10.82
            ],
            "endTime": [
                1.23,
                11.086666666666666
            ]
        }
    ]
}
```

### tag(obj, tag)
*Tags an audio object in the server with the specified tag.*

Params:

- obj (*string*): The content ID of the object
- tag (*string*): The tag of the object

Return Value:
```json
{
    "result": "success"
}
```

### get_tags(obj)
*Returns the tags that are associated with a specific audio object on the server.*

Params:

- obj (*string*): The content ID of the object

Return value:
```json
{
    "contentID": "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx",
    "tags": [
        "sample",
        "mp3"
    ]
}
```

### transcript(obj)
*Returns the transcript of a specific audio object.*

Params:

- obj (*string*): The content ID of the object

Return value:
```json
{
    "contentID": "14xxxxx-xxxxx-xxxx-xxxx-xxxxxx",
    "paragraphs": [
        "this is a simple hello world transcript."
    ],
    "paragraphStartTimes": [
        0.67
    ]
}
```

## Contributing
Fork the repository, make necessary changes, run tests and submit a pull request. :muscle:

### Testing
Before running tests, install the necessary requirements with:
```
pip install -r requirements_tests.txt
```

Run tests with `nosetests` command.


## Issues
To submit any issues, raise an issue through the [Issues Page](https://github.com/agouil/deepgram-python/issues)

## License
[MIT](LICENSE)
