# IMDB Selenium Python Crawler
This project can extract all movie and series information from imdb.

## Output example
```json
[
    {
        "Title": "Edge of Tomorrow", 
        "Poster": "https://m.media-amazon.com/images/...", 
        "Year": "2014", 
        "Ages": "PG-13", 
        "Duration": "1h 53m", 
        "Images": ["https://m.media-amazon.com/images/...", "..."], 
        "IMDB Rate": "7.9", 
        "Meta Score": "71", 
        "Popularity": "733", 
        "Genre": ["Action", "Adventure", "Sci-Fi"], 
        "Directors": ["Doug Liman"], 
        "Writers": ["Christopher McQuarrie", "Jez Butterworth", "John-Henry Butterworth"], 
        "Stars": ["Tom Cruise", "Emily Blunt", "Bill Paxton"], 
        "Story Line": "An alien race has hit ...", 
        "Country": ["United States", "Canada"], 
        "language": ["English"], 
        "Budget": "$178,000,000", 
        "Gross worldwide": "$370,541,256",
        "IMDB Id": "tt1631867"
    }
]
```

## Installation
First of all make sure you install Firefox in your system before.

Install these packages :
```bash
sudo apt install python3-pip python3-venv
```
After download source code, navigate to folder project and :
```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r req.txt
```
Finally run it : 
```bash
python3 main.py
```

## How to use
- You can get information with two methods.

1. 
```python
 get_id('tt1631867')
```
You must pass imdb id as method input. 

2. 
With this method you can get information of all media list in url.
```python
get_list('https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')
```
You must pass url as method input.

- You can get results with two methods.

1. 
```python
print_json()
```
2. 
```python
print_dict()
```