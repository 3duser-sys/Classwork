import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

init(autoreset=True)

def load_data(file_path='imbd_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combine_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + "Error: File not found. Please ensure 'imbd_top_1000.csv' is in the correct directory.")
        exit()

movies_df = load_data()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combine_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def list_genres():
    return sorted(set(genre.strip() for sublist in movies_df['Genre'].dropna().str.split(', ') for genre in sublist))
df['Genre'].dropna().str.split(', ') for genre in sublist))

genres = list_genres(movies_df)

def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]

    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity < 0) or polarity >= 0)) or not mood:
            recommendations.append((row['Series_Title'], polarity))
        if len(recommendations) >= top_n:
            break
    
    return recommendations if recommendations else "No suitable movie recommendations found."

def display_recommendations(recs, name):
    print(Fore.Yellow + f"\n Ai Analyzed Movie Recommendation for {name}:\n")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive" if polarity >= 0 else "Negative" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity:.2f}, {sentiment})")

def proccess_animations():
    for _ in range(3):
        print(Fore.YELLOW + ",", end="", flush=True)
        time.sleep(0.5)
    
def handle_ai(name):
    print(Fore.BLUE + "\n???? Let's find the perfect movie for you!\n")
    print(Fore.GREEN + "Available Genres: ", end="")

    for idx, genre in enumerate(genres, 1):

        print(f"{Fore.CYAN}{idx}. {genre}")  

    print()

    while True:
        genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title() in genres:
            

