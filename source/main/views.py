from django.views.generic import TemplateView, CreateView
import pandas as pd
import numpy as np
###importing surprise library to implement the recommending systems needed
from surprise import NMF, SVD, SVDpp, KNNBasic, KNNWithMeans, KNNWithZScore, CoClustering
from surprise.model_selection import cross_validate
from surprise import Reader, Dataset
from django.shortcuts import render
import requests
from accounts.models import City

class MovieRatingsView(TemplateView):
    template_name = 'main/ratings.html'

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class MovieReccomdationView(TemplateView):
    template_name = 'main/recomend.html'

def reccomendation_system(request):
    current_user = request.user
    user_id = request.user.id
    print("User ID:", user_id)

    columns = ['user_id', 'item_id', 'rating', 'timestamp']

    df = pd.read_csv('main/ml-100k/u.data', sep='\t', names=columns)

    columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    movies = pd.read_csv('main/ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
    movie_names = movies[['item_id', 'movie title']]
    combined_movies_data = pd.merge(df, movie_names, on='item_id')
    combined_movies_data = combined_movies_data[['user_id', 'movie title', 'rating']]
### Current user's rating
    my_ratings = pd.read_csv('main/ml-100k/my_movies_rating.csv')
#print(my_ratings)

### combining the dataset rating with the user rating to produre
### later on bespoke recommendations for the user that asks them

    combined_movies_data = combined_movies_data.append(my_ratings)
#print(combined_movies_data.columns)
# rename the columns to userID, itemID and rating
    combined_movies_data.columns = ['userID', 'itemID', 'rating']

# use the transform method group by userID and count to keep the movies with more than 25 reviews
    combined_movies_data['reviews'] = combined_movies_data.groupby(['itemID'])['rating'].transform('count')
    combined_movies_data = combined_movies_data[combined_movies_data.reviews > 25][['userID', 'itemID', 'rating']]

###setting the rating scale from 1 to 5
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(combined_movies_data, reader)

    def personalise_movie_list_for_user(user_id):
    ###removing from the list the movies rated by the current user
    # get the list of the movie ids
        unique_ids = combined_movies_data['itemID'].unique()
    # get the list of the ids that the userid 1001 has rated
        iids1001 = combined_movies_data.loc[combined_movies_data['userID'] == id, 'itemID']
    # remove the rated movies for the recommendations
        movies_to_predict = np.setdiff1d(unique_ids, iids1001)
        return movies_to_predict

#Recommender Systems using SDV
    def SDV_algo(user_id):
        movies_to_predict = personalise_movie_list_for_user(id)
        algo1 = SVD()
        algo1.fit(data.build_full_trainset())
        my_recs = []
        for iid in movies_to_predict:
            my_recs.append((iid, algo1.predict(uid=1001, iid=iid).est))

        print(pd.DataFrame(my_recs, columns=['iid', 'predictions']).sort_values('predictions', ascending=False).head(10))

    def inserting_row(user_id, rating):
        movie_title = selecting_movie(movie_names)
        fields = [user_id, movie_title, rating]
        with open(r'main/ml-100k/my_movies_rating.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

    SDV_algo(1000)
    
    return render(request,'main/recomend.html')

def results(request):
    data = Students.objects.all()

    stu = {
        "student_number": data
    }
    return render("login/profile.html", stu)

def showlist(request):
    city_istance = City.objects.create(name='Aladdin (1992)')
    city_istance2 = City.objects.create(name='Braveheart (1995)')
    results=City.objects.all
    return render(request, "home.html",{"showcity":results})