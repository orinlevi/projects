
#include "Dense.h"

//
// Created by orin levi on 02/09/2022.
//

Dense::Dense(const Matrix &weights, const Matrix &bias, activation_func
func):_weights(weights), _bias(bias), _func(func){}

const Matrix &Dense::get_weights() const {
    return _weights;
}

const Matrix &Dense::get_bias() const {
    return _bias;
}

activation_func Dense::get_activation() const {
    return _func;
}

Matrix Dense::operator()(const Matrix &img) const {
    Matrix partial_v = ((_weights * img) + _bias);
    return _func(partial_v);
}
