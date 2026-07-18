import pickle

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):

    if movie not in movies["title"].values:
        return []

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append({
            "title": movies.iloc[i[0]]["title"],
            "rating": movies.iloc[i[0]]["vote_average"],
            "release": movies.iloc[i[0]]["release_date"],
            "overview": movies.iloc[i[0]]["overview"]
        })

    return recommendations