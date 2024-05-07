//
// Created by orin levi on 22/09/2022
//
#include "RSUsersLoader.h"

#include <fstream>
#include <sstream>

#define ERROR_FILE_PATH "invalid path"

#define EMPTY "NA"
#define MAC_EMPTY "NA\r"
#define ZERO 0

#define SPACE ' '
#define DASH '-'

typedef std::vector<sp_movie> movies_vec;
typedef std::vector<double> ratings_vec;

movies_vec get_movies_vec(std::ifstream &file,
                          const up_recommender_system &rs){
    movies_vec movies{};

    std::istringstream line_stream{};
    std::string line{}, name_and_year{}, movie_name{}, movie_year_str{};
    int movie_year = 0;

    std::getline(file, line);
    line_stream = std::istringstream (line);
    while (std::getline(line_stream, name_and_year, SPACE)) {
        std::size_t pos = name_and_year.find(DASH);
        movie_name = name_and_year.substr(0, pos);
        movie_year_str = name_and_year.substr(++pos);
        std::istringstream movie_year_stream(movie_year_str);
        movie_year_stream >> movie_year;

        sp_movie movie = rs->get_movie(movie_name, movie_year);
        movies.push_back(movie);
    }
    return movies;
}

ratings_vec get_rating_vec(std::istringstream &line_stream){
    ratings_vec ratings{};

    std::string movie_rate_str{};
    double movie_rate = 0;

    while(std::getline(line_stream, movie_rate_str, SPACE)) {
        if (movie_rate_str == EMPTY || movie_rate_str == MAC_EMPTY) {
            movie_rate = ZERO;
        } else {
            std::istringstream movie_rate_stream(movie_rate_str);
            movie_rate_stream >> movie_rate;
            if (MIN_RATE > movie_rate || movie_rate > MAX_RATE) {
                throw std::runtime_error(ERROR_MOVIE_RATE);
            }
        }
        ratings.push_back(movie_rate);
    }
    return ratings;
}

rank_map get_user_movies_map(const movies_vec &movies, const ratings_vec
&ratings){
    rank_map user_movies_map(0, sp_movie_hash, sp_movie_equal);
    for(int i = 0; i < (int) movies.size(); i++){
        if(ratings[i] != ZERO){
            user_movies_map[movies[i]] = ratings[i];
        }
    }
    return user_movies_map;
}

std::vector<RSUser>
RSUsersLoader::create_users_from_file(const std::string &users_file_path,
               up_recommender_system rs) noexcept(false){

    std::ifstream file(users_file_path, std::ifstream::in);
    if(!file){ throw std::runtime_error(ERROR_FILE_PATH); }

    std::vector<RSUser> users{};
    movies_vec movies = get_movies_vec(file, rs);

    std::istringstream line_stream{};
    std::string line{}, user_name{};

    sp_recommender_system shared_recommender_sys = std::move(rs);

    while (std::getline(file, line)){
        line_stream = std::istringstream(line);
        std::getline(line_stream, user_name, SPACE);

        ratings_vec ratings = get_rating_vec(line_stream);
        rank_map user_movies_map = get_user_movies_map(movies, ratings);

        users.push_back(RSUser(user_name, user_movies_map,
                               shared_recommender_sys));
    }
    return users;
}

