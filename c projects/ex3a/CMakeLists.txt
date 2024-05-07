cmake_minimum_required(VERSION 3.23)
project(ex3a_orin_levi C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(ex3a_orin_levi
        linked_list.c
        linked_list.h
        markov_chain.c
        markov_chain.h
        tweets_generator.c)
