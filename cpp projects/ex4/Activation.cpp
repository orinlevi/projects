//
// Created by orin levi on 02/09/2022.
//
#include "Activation.h"
#include <cmath>

Matrix activation:: relu(const Matrix& matrix){
    Matrix new_matrix(matrix.get_rows(), matrix.get_cols());
    for(int i = 0; i < matrix.get_rows() * matrix.get_cols(); i++){
        if(matrix[i] >= 0){
            new_matrix[i] = matrix[i];
        } else{
            new_matrix[i] = 0;
        }
    }
    return new_matrix;
}

Matrix activation:: softmax(const Matrix& matrix){
    Matrix new_matrix(matrix.get_rows(), matrix.get_cols());

    float sum = 0;
    for(int i = 0; i < matrix.get_rows() * matrix.get_cols(); i++){
        new_matrix[i] = std::exp(matrix[i]);
        sum += new_matrix[i];
    }

    float divisor = (1 / sum);
    return (new_matrix * divisor) ;
}
