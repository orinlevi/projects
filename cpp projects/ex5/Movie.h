
#ifndef INC_22B_C_C__EX5_MOVIE_H
#define INC_22B_C_C__EX5_MOVIE_H

#include <iostream>
#include <vector>
#include <memory>

#define HASH_START 17



class Movie;

typedef std::shared_ptr<Movie> sp_movie; // define your smart pointer

/**
 * those declartions and typedefs are given to you and should be used in the ex
 */
typedef std::size_t (*hash_func)(const sp_movie& movie);
typedef bool (*equal_func)(const sp_movie& m1,const sp_movie& m2);
std::size_t sp_movie_hash(const sp_movie& movie);
bool sp_movie_equal(const sp_movie& m1,const sp_movie& m2);

class Movie
{
public:
    /**
     * constructor
     * @param name: _name of movie
     * @param year: year it was made
     */
    Movie(const std::string& name, int year): name(name), year(year){}

    /**
     * returns the _name of the movie
     * @return const ref to _name of movie
     */
    std::string get_name() const{ return name; }

    /**
     * returns the year the movie was made
     * @return year movie was made
     */
    int get_year() const { return year; }

	/**
     * operator< for two _movies
     * @param rhs: right hand side
     * @param lhs: left hand side
     * @return returns true if (lhs.year) < rhs.year or (rhs.year == lhs
     * .year & lhs._name < rhs._name) else return false
     */
    friend bool operator<(const Movie &rhs, const Movie &lhs);

    /**
     * operator<< for movie
     * @param os ostream to output info with
     * @param movie movie to output
     */
    friend std::ostream& operator<<(std::ostream& os, const Movie &movie);

private:
    std::string name;
    int year;
};


#endif //INC_22B_C_C__EX5_MOVIE_H
