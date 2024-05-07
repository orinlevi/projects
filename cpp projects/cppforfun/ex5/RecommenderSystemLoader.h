
#ifndef RECOMMENDERSYSTEMLOADER_H
#define RECOMMENDERSYSTEMLOADER_H

#include "RecommenderSystem.h"
#include "RSUser.h"

class RecommenderSystemLoader {

 private:

 public:
  RecommenderSystemLoader () = delete;
  /**
   * loads _movies by the given format for _movies with their feature's score
   * @param movies_file_path a path to the file of the _movies
   * @return smart pointer to a RecommenderSystem which was created with
   * those _movies
   */
  static up_recommender_system create_rs_from_movies_file
	  (const std::string &movies_file_path) noexcept (false);
};

#endif //RECOMMENDERSYSTEMLOADER_H
