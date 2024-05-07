//
// Created by orin levi on 22/09/2022.
//
#include "RecommenderSystem.h"
#include <cmath>

sp_movie RecommenderSystem::add_movie(const std::string &name, int year,
                                      const features &movie_features) {
    sp_movie movie_sptr = std::make_shared<Movie>(name, year);
    movies[movie_sptr] = movie_features;
    return movie_sptr;
}

sp_movie
RecommenderSystem::get_movie(const std::string &name, int year) const {
    sp_movie temp_movie_sptr = std::make_shared<Movie>(name, year);
    auto it = movies.find(temp_movie_sptr);
    if(it != movies.end()){return it->first;}
    else{return nullptr;}
}

std::ostream& operator<<(std::ostream &os, const RecommenderSystem &system) {
    for(const auto &map_pair: system.movies){
        os << *(map_pair.first);
    }
    return os;
}

double get_ratings_avg(const rank_map &ratings_map){
    double ratings_sum = 0;
    int num_of_rate_movies = 0;
    for(const auto &pair: ratings_map){
        ratings_sum += pair.second;
        num_of_rate_movies++;
    }
    return (ratings_sum / num_of_rate_movies);
}

double get_the_cos_ang_between_vectors(const features &rhs, const features
&lhs){
    double mult_vectors = 0;
    double rhs_size = 0;
    double lhs_size = 0;
    for(int i = 0; i < (int) rhs.size(); i++) {
        mult_vectors += rhs[i] * lhs[i];
        rhs_size += pow(rhs[i], 2);
        lhs_size += pow(lhs[i], 2);
    }
    rhs_size = sqrt(rhs_size);
    lhs_size = sqrt(lhs_size);

    return mult_vectors / (rhs_size * lhs_size);

}

sp_movie RecommenderSystem::recommend_by_content(const RSUser &user) {
    //makes normalized vec
    rank_map ratings_map = user.get_ranks();
    double avg = get_ratings_avg(ratings_map);
    features predict_vector(movies.begin()->second.size(), 0);

    for(const auto &user_pair: ratings_map){
        double normalize_rate = user_pair.second - avg;
        for(int i = 0; i < (int) predict_vector.size(); i++){
            predict_vector[i] += normalize_rate * movies[user_pair
                                                            .first][i];
        }
    }

    sp_movie recommended_movie = std::make_shared<Movie>("", 0);
    double max_cos_angle = 0;

    for(const auto &recommender_sys_pair: movies){
        if(ratings_map.count(recommender_sys_pair.first) == 0){
            double cos_ang = get_the_cos_ang_between_vectors
                    (predict_vector, recommender_sys_pair.second);
            if(cos_ang > max_cos_angle){
                max_cos_angle = cos_ang;
                recommended_movie = recommender_sys_pair.first;
            }
        }
    }
    return recommended_movie;
}

double RecommenderSystem::predict_movie_score(const RSUser &user,
                                              const sp_movie &movie, int k) {
    rank_map ratings_map = user.get_ranks();
    double_sp_vec_map cos_ang_map{};
    features movie_features = movies[movie];
    for(const auto &user_pair: ratings_map){
        double cos_ang = get_the_cos_ang_between_vectors(movie_features,
                         movies[user_pair.first]);
        cos_ang_map.insert({cos_ang, user_pair.first});
    }

    double mult_of_cos_angles = 0, sum_of_cos_angles = 0;
    auto iter = cos_ang_map.begin();
    for(int i = 0; i < k; i++){
        mult_of_cos_angles += ratings_map[iter->second] * iter->first;
        sum_of_cos_angles += iter->first;
        iter++;
    }
    double rate = (mult_of_cos_angles / sum_of_cos_angles);
    return rate;
}

sp_movie RecommenderSystem::recommend_by_cf(const RSUser &user, int k) {
    double_sp_vec_map cos_ang_map{};
    for(const auto &recommender_sys_pair: movies){
        if(user.get_ranks().count(recommender_sys_pair.first) == 0){
            double predict_score = predict_movie_score(user,
                                   recommender_sys_pair.first, k);
            cos_ang_map.insert({predict_score, recommender_sys_pair.first});
        }
    }
    return cos_ang_map.begin()->second;
}

