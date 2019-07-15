{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "nltk.download('punkt')\n",
    "from nltk.corpus import stopwords\n",
    "import nltk\n",
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import bs4 as bs  \n",
    "import urllib.request  \n",
    "import re\n",
    "\n",
    "scraped_data = urllib.request.urlopen('https://www.crictracker.com/icc-announces-the-odi-rankings-after-the-2019-world-cup/')  \n",
    "article = scraped_data.read()\n",
    "\n",
    "parsed_article = bs.BeautifulSoup(article,'lxml')\n",
    "paragraphs = parsed_article.find_all('p')\n",
    "art= \"\"\n",
    "for p in paragraphs:  \n",
    "    a+= p.text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>In the script above we first import the important libraries required for scraping the data from the web. We then use the urlopen function from the urllib.request utility to scrape the data. Next, we need to call read function on the object returned by urlopen function in order to read the data. To parse the data, we use BeautifulSoup object and pass it the scraped data object i.e. article and the lxml parser. To retrieve the text we need to call find_all function on the object returned by the BeautifulSoup. The tag name is passed as a parameter to the function. The find_all function returns all the paragraphs in the art in the form of a list. All the paragraphs have been combined to recreate the article.<p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Preprocessing<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.tokenize import sent_tokenize,word_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "article_text=re.sub(r'\\[[0-9]*\\]', ' ',a)  \n",
    "article_text = re.sub(r'\\s+', ' ', article_text)  \n",
    "formatted_text=re.sub('[^a-zA-Z]', ' ', article_text )    \n",
    "formatted_text = re.sub(r'\\s+', ' ', formatted_text)\n",
    "#article_text\n",
    "\n",
    "#formatted_text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following script removes the square brackets and replaces the resulting multiple spaces by a single space.The article_text object contains text without brackets. However, we do not want to remove anything else from the article since this is the original article. We will not remove other numbers, punctuation marks and special characters from this text since we will use this text to create summaries and weighted word frequencies will be replaced in this article.\n",
    "To clean the text and calculate weighted frequences, we will create another object named as formatted_text.Now we have two objects article_text, which contains the original article and formatted_text which contains the formatted article. We will use formatted_text to create weighted frequency histograms for the words and will replace these weighted frequencies with the words in the article_text object.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Converting Text To Sentences<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "sentences=sent_tokenize(article_text)\n",
    "#sentences"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Here,we tokenize article_text into sentences.<p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "article_words=word_tokenize(article_text)\n",
    "#article_words\n",
    "formatted_words=word_tokenize(formatted_text)\n",
    "#formatted_words"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We tokenize article_text and formatted_text into words for calculating words frequency. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Find Weighted Frequency of Occurrence"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To find the frequency of occurrence of each word, we use the formatted_text variable. We used this variable to find the frequency of occurrence since it doesn't contain punctuation, digits, or other special characters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "stop_words = stopwords.words('english')\n",
    "word_frequencies = {}  \n",
    "for word in formatted_words:  \n",
    "    if word not in stop_words:\n",
    "        if word not in word_frequencies.keys():\n",
    "            word_frequencies[word] = 1\n",
    "        else:\n",
    "            word_frequencies[word] += 1\n",
    "#word_frequencies            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the script above, we first store all the English stop words from the nltk library into a stopwords variable. Next, we loop through all the sentences and then corresponding words to first check if they are stop words. If not, we proceed to check whether the words exist in word_frequencies dictionary or not. If the word is encountered for the first time, it is added to the dictionary as a key and its value is set to 1. Otherwise, if the word previously exists in the dictionary, its value is simply updated by 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_freq=max(word_frequencies.values())\n",
    "for i in word_frequencies:\n",
    "    word_frequencies[i]=word_frequencies[i]/max_freq\n",
    "#word_frequencies    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, to find the weighted frequency, we can simply divide the number of occurances of all the words by the frequency of the most occurring word."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Calculating Sentence Scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "sent_score={}\n",
    "for sent in sentences:\n",
    "    for word in(word_tokenize(sent.lower())):\n",
    "        if(word in word_frequencies):\n",
    "            if len(sent.split(' ')) < 50:\n",
    "                if sent not in sent_score:\n",
    "                    sent_score[sent] = word_frequencies[word]\n",
    "                else:\n",
    "                    sent_score[sent] += word_frequencies[word]\n",
    "#sent_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the script above, we first create an empty sent_score dictionary. The keys of this dictionary will be the sentences themselves and the values will be the corresponding scores of the sentences. Next, we loop through each sentence in the sentence_list and tokenize the sentence into words.\n",
    "\n",
    "We then check if the word exists in the word_frequencies dictionary. This check is performed since we created the sentence list from the article_text object; on the other hand, the word frequencies were calculated using the formatted_text object, which doesn't contain any stop words, numbers, etc.\n",
    "We then count the weight of each sentence.If sentence is present in dictionary sent_score then we increments its value by the word_frequencies else we simply create a new key using sentence in dictionary sent_score."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Getting the Summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jason Roy’s 85 from 65 balls in the semi-final win over Australia has helped him into the top 10 for the first time.Another notable gainer in the rankings for batsmen is Ravindra Jadeja, whose valiant knock of 77 against New Zealand has lifted him 24 places to 108th position. His previous best was fourth position in 2016.Bangladesh’s Shakib Al Hasan continues to lead the list of all-rounders, but second-placed Stokes has reached a career-best 319 points. New Zealand seam bowler Matt Henry’s consistency has taken him back into the world’s top 10 as he took three wickets in the semifinals and one in the final. Advertisementby Press AuthorPublished - Jul 15, 2019 8:30 pm | Updated - Jul 15, 2019 8:30 pmEngland and New Zealand players have moved up in the MRF Tyres ICC Men’s ODI Player Rankings after featuring in an exhilarating ICC Men’s Cricket World Cup 2019 final at Lord’s on Sunday.\n"
     ]
    }
   ],
   "source": [
    "import heapq  \n",
    "summary_sentences = heapq.nlargest(7, sent_score,key=sent_score.get)\n",
    "summary = ' '.join(summary_sentences)  \n",
    "print(summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
