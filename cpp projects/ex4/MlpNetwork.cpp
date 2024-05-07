//
// Created by orin levi on 02/09/2022.
//
#include "MlpNetwork.h"
#define NUM_OF_NUMBERS 10

MlpNetwork::MlpNetwork(const Matrix *weight, const Matrix *biases): layer_1
(weight[0], biases[0], activation::relu), layer_2(weight[1], biases[1],
        activation::relu), layer_3(weight[2], biases[2], activation::relu),
        layer_4(weight[3], biases[3], activation::softmax){}

digit MlpNetwork::operator()(const Matrix &img) const {
    Matrix v1 = layer_1(img);
    Matrix v2 = layer_2(v1);
    Matrix v3 = layer_3(v2);
    Matrix v4 = layer_4(v3);


    unsigned int value = 0;
    float probability = v4[0];

    for(int i = 1; i < NUM_OF_NUMBERS; i++){
        if(v4[i] > probability){
            value = i;
            probability = v4[i];
        }
    }
    return digit{value, probability};
}
