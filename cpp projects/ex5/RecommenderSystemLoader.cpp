//
// Created by orin levi on 22/09/2022.
//
#include "RecommenderSystemLoader.h"
#include <fstream>
#include <sstream>

#define ERROR_FILE_PATH "invalid path"
#define ERROR_SCORE_RANG "invalid feature score"

#define MIN_FEATURE_SCORE 1
#define MAX_FEATURE_SCORE 10

#define SPACE ' '
#define DASH '-'

up_recommender_system RecommenderSystemLoader::create_rs_from_movies_file(
        const std::string &movies_file_path) noexcept(false) {

    std::ifstream file(movies_file_path, std::ifstream::in);
    if(!file){ throw std::runtime_error(ERROR_FILE_PATH); }

    up_recommender_system recommended_sys_uptr =
            std::make_unique<RecommenderSystem>();

    std::istringstream line_stream{};
    std::string line{}, name_and_year{}, movie_name{}, movie_year_str{},
    cur_feature_score_str{};
    int movie_year = 0;
    double cur_feature_score = 0;

    while (std::getline(file, line)){
        line_stream = std::istringstream(line);
        std::getline(line_stream, name_and_year, SPACE);
        std::size_t pos = name_and_year.find(DASH);
        movie_name = name_and_year.substr(0,pos);
        movie_year_str = name_and_year.substr(++pos);
        std::istringstream movie_year_stream (movie_year_str);
        movie_year_stream >> movie_year;

        features movie_features{};
        while (std::getline(line_stream, cur_feature_score_str, SPACE)){
            std::istringstream cur_feature_score_stream(cur_feature_score_str);
            cur_feature_score_stream >> cur_feature_score;
            if(MIN_FEATURE_SCORE <= cur_feature_score && cur_feature_score <=
            MAX_FEATURE_SCORE){
                movie_features.push_back(cur_feature_score);
            }
            else{ throw std::runtime_error(ERROR_SCORE_RANG); }
        }
        recommended_sys_uptr->add_movie(movie_name, movie_year,
                                        movie_features);
    }
    return recommended_sys_uptr;
}

