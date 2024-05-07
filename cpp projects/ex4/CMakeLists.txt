cmake_minimum_required(VERSION 3.23)
project(ex4_orin_levi)

set(CMAKE_CXX_STANDARD 11)

add_executable(ex4_orin_levi
        Activation.h
        Activation.cpp
        Dense.h
        Dense.cpp
        main.cpp
        Matrix.h
        Matrix.cpp
        MlpNetwork.h
        MlpNetwork.cpp)

add_executable(presubmit
        prusbmit.cpp
        Activation.h
        Activation.cpp
        Dense.h
        Dense.cpp
        Matrix.h
        Matrix.cpp
        MlpNetwork.h
        MlpNetwork.cpp)
