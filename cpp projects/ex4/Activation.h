#include "Matrix.h"

#ifndef ACTIVATION_H
#define ACTIVATION_H

typedef Matrix (*activation_func) (const Matrix& matrix);

// Insert Activation class here...
namespace activation{
    Matrix relu(const Matrix& matrix);
    Matrix softmax(const Matrix& matrix);
}

#endif //ACTIVATION_H