#ifndef DENSE_H
#define DENSE_H

#include "Activation.h"

// Insert Dense class here...
class Dense{
public:
    Dense(Matrix const &weights, Matrix const &bias, activation_func func);

    const Matrix &get_weights() const;
    const Matrix &get_bias() const;
    activation_func get_activation() const;

    Matrix operator()(Matrix const &img) const;

private:
    const Matrix& _weights, _bias;
    activation_func _func;
};


#endif //DENSE_H
