cmake_minimum_required(VERSION 3.23)
project(ex1_orin_levi C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(ex1_orin_levi
        cipher.c
        cipher.h
        main.c
        tests.c
        tests.h)
