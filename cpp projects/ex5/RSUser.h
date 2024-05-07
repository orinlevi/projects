//
// Created on 2/20/2022.
//

#ifndef GIT_USER_H
#define GIT_USER_H
#include <unordered_map>
#include <utility>
#include <vector>
#include <string>
#include <memory>
#include "Movie.h"

#define MIN_RATE 1
#define MAX_RATE 10
#define ERROR_MOVIE_RATE "invalid movie rate"

class RecommenderSystem;
typedef std::shared_ptr<RecommenderSystem> sp_recommender_system;
typedef std::unique_ptr<RecommenderSystem> up_recommender_system;

typedef std::unordered_map<sp_movie, double, hash_func,equal_func> rank_map;

class RSUser
{
public:
	/**
	 * Constructor for the class
	 */
	// TODO RSUser() this constructor can be implemented however you want
    RSUser(std::string name, rank_map movies, sp_recommender_system
    recommender_sys_sptr): _name(std::move(name)), _movies(std::move(movies)),
    _recommender_sys_sptr(std::move(recommender_sys_sptr)){}

	/**
	 * a getter for the user's _name
	 * @return the username
	 */
    std::string get_name() const{return _name;}

	/**
	 * function for adding a movie to the DB
	 * @param name _name of movie
     * @param year year it was made
	 * @param features a vector of the movie's features
	 * @param rate the user rate for this movie
	 */
	void add_movie_to_rs(const std::string &name, int year,
                         const std::vector<double> &features,
                         double rate);


    /**
     * a getter for the ranks map
     * @return
     */
    rank_map get_ranks() const {return _movies;}

	/**
	 * returns a recommendation according to the movie's content
	 * @return recommendation
	 */
	sp_movie get_recommendation_by_content() const;

	/**
	 * returns a recommendation according to the similarity recommendation
	 * method
	 * @param k the number of the most similar _movies to calculate by
	 * @return recommendation
	 */
	sp_movie get_recommendation_by_cf(int k) const;

	/**
	 * predicts the score for a given movie
	 * @param name the _name of the movie
	 * @param year the year the movie was created
	 * @param k the parameter which represents the number of the most
	 * similar _movies to predict the score by
	 * @return predicted score for the given movie
	 */
	double get_prediction_score_for_movie(const std::string& name, int year,
                                          int k) const;

	/**
	 * output stream operator
	 * @param os the output stream
	 * @param user the user
	 * @return output stream
	 */
	// TODO &operator<<
    friend std::ostream& operator<<(std::ostream &os, const RSUser &user);

private:
    std::string _name;
    rank_map _movies;
    sp_recommender_system _recommender_sys_sptr;

};



#endif //GIT_USER_H
