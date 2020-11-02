## About The Project
This is aparat downloader. It use selenium to crawl sites and get links.
It use downloader to download the links.

## Getting Started
Before using this downloader should flow the steps:

### Prerequisites
0. Make sure you have python 3 installed
1. Clone the repository
2. Get the selenium driver from this [link](https://github.com/mozilla/geckodriver/releases)  
3. Extract the file
3. Change `<your-path-to-selenium-driver>` to  your path to selenium driver
4. Create virtualenv using `python3 -m virtualenv --python python3 env` or any commands you use to create env
5. Activate virtualenv using `. env/bin/activate` or any commands you use to activate your env
6. Install requirements using `pip install -r requirements.txt`

## Usage
While your env is activate run the flowing command to get all links from an aparat channel.
````
python get_all_links_from_aparat_channel.py -n <channel-name>
````
And to download all the links we discover and store in `links.json`, use the flowing command. 
````
python downloader.py -f <filename>
````
## Example 
Get all links from aparat channel
````
python get_all_links_from_aparat_channel.py -n hellodigi
````
Downloading all links
````
python downloader.py -f links.json
````

## To Do
- [ ] Add Download All videos from playlist
- [ ] Show downloading process
- [ ] Add farsi readme
- [ ] Add multiprocessing for downloading
