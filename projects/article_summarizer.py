
import requests
from bs4 import BeautifulSoup
import urllib.request as url
import re

import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk import word_tokenize

import heapq
import string
import pandas as pd 
from datetime import datetime, timedelta

nltk.download('punkt')
nltk.download('stopwords')
stop_word = stopwords.words('english')

def get_soup(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_headline(soup):
    try:
        title = soup.find("meta", property="og:title")
        title = title["content"] if title else "No meta title given"
    except:
        title = soup.find('h1').get_text()
    return title

def get_url(soup):
    url = soup.find("meta", property="og:url")
    url = url["content"] if url else "No meta url given"
    return url 

def get_text_from_url(soup):
    text = [c.get_text() for c in soup.find_all('p')]
    body = ' '.join(text)

    return body


def get_read_time(article,wpm= 200):
    words = article.split(' ')
    est = len(words) / wpm
    return f"Est. {round(est)} minutes"

def format_article(sentence_score, name = '', headline = 'headline', url = 'url', date_of_article = 'd MMM YYYY',read_time = 'N/A'):
    summary = heapq.nlargest(4,sentence_score,key = sentence_score.get)
    summary = ' '.join(summary)
    headers = f"""
    Headline: {headline}
    URL: {url}
    Date of Article: {format_date(date_of_article)} 
    Read Time: {read_time}
    Summary: """
    final = headers +summary

    return final

def process_text(article):
    processed = article.replace(r'^\s+|\s+?$','')
    processed = processed.replace('\n',' ')
    processed = processed.replace("\\",'')
    processed = processed.replace(",",'')
    processed = processed.replace('"','')
    processed = re.sub(r'\[[0-9]*\]','',processed)
    return processed

def rank_sentences(processed):
    sentences = sent_tokenize(processed)

    frequency = {}
    processed1 = processed.lower()
    for word in word_tokenize(processed1):
        if word not in stop_word and word not in string.punctuation:
            if word not in frequency.keys():
                frequency[word]=1
            else:
                frequency[word]+=1

    max_fre = max(frequency.values())
    for word in frequency.keys():
        frequency[word]=(frequency[word]/max_fre)

    sentence_score = {}
    for sent in sentences:
        for word in word_tokenize(sent):
            if word in frequency.keys():
                if len(sent.split(' '))<30:
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = frequency[word]
                    else:
                        sentence_score[sent]+=frequency[word]
    return sentence_score


def format_date(date_string):
    if date_string != 'd MMM YYYY':
        fmt_date = pd.to_datetime(date_string)
    else: 
        fmt_date = datetime.now()
    return fmt_date.strftime("%d %b %Y")
    

def summarize_article(article = None, url = None, headline = 'headline', date_of_article = 'd MMM YYYY'):
    if url is not None:
        soup = get_soup(url)
        article = get_text_from_url(soup)
        headline = get_headline(soup)

    processed = process_text(article)
    read_time = get_read_time(article,wpm = 200)
    sentence_score = rank_sentences(processed)
    final = format_article(sentence_score, headline= headline, url = url, read_time = read_time)
    return final

test = """
Information extraction (IE) is the task of automatically extracting structured information from unstructured and/or semi-structured machine-readable documents and other electronically represented sources. In most of the cases this activity concerns processing human language texts by means of natural language processing (NLP). Recent activities in multimedia document processing like automatic annotation and content extraction out of images/audio/video/documents could be seen as information extraction

Due to the difficulty of the problem, current approaches to IE focus on narrowly restricted domains.
"""
try:
    summarize_article(test)
    print("[article_summarizer] Test Successful, Article Summarizer Ready!")
except Exception as e:
    print(f"[article_summarizer] {e}")

if __name__ == "__main__":
    URL = "https://www.reuters.com/business/finance/regulators-urged-find-silicon-valley-bank-buyer-industry-frets-about-fallout-2023-03-12/"

    print(summarize_article(url = URL))
    

