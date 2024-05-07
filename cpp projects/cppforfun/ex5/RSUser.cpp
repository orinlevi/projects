//
// Created on 2/20/2022.
//

// don't change this includes
#include "RSUser.h"
#include "RecommenderSystem.h"


// implement your cpp code here
void RSUser::add_movie_to_rs(const std::string &name, int year,
                             const std::vector<double> &features,
                             double rate) {
    if (MIN_RATE > rate || rate > MAX_RATE) {
        throw std::runtime_error(ERROR_MOVIE_RATE);
    }
    sp_movie movie = (*_recommender_sys_sptr).add_movie(name, year, features);
    _movies[movie] = rate;

}

std::ostream& operator<<(std::ostream &os, const RSUser &user) {
    os << "_name:" << user._name << std::endl;
    os << *(user._recommender_sys_sptr);
    return os;
}

sp_movie RSUser::get_recommendation_by_content() const{
    return(*_recommender_sys_sptr).recommend_by_content(*this);
}

sp_movie RSUser::get_recommendation_by_cf(int k) const {
    return(*_recommender_sys_sptr).recommend_by_cf(*this, k);
}

double
RSUser::get_prediction_score_for_movie(const std::string &name, int year,
                                       int k) const {
    sp_movie movie = _recommender_sys_sptr->get_movie(name, year);
    return(*_recommender_sys_sptr).predict_movie_score(*this, movie, k);
}
