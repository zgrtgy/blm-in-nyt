# blm-in-nyt
- Repo for "Media Portrayals of Racial Minority Protests: An In-depth Analysis of Black Lives Matter Coverage in the New York Times"

    - [nyt_api.ipynb](https://github.com/zgrtgy/blm-in-nyt/blob/main/nyt_api.ipynb) showcases the code used to retrieve article snippets from NYT, can be run on Google Colab with an NYT API key placed in linked GDrive. NYT API Terms of Service (iii) prevents us from sharing the content acquired through the API. [NYT API Terms of Service](https://developer.nytimes.com/terms)

    - "nyt_blm_bertopic_0_16.ipynb" showcases the code used to run BERTopic on the retrieved snippets, can be run on Google Colab with the NYT snippets saved as a csv dataframe placed in linked GDrive.

    - "nyt_ngram_wordfreq_counter.py" showcases the code used to run ngram and word frequency analysis on the retrieved snippets.
