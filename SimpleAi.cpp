#include <iostream>
#include <vector>
#include <cmath>


// Фукнция активации (сигмоида) и ее производная (activation function (sigmoid) and its derivative)
double sigmoid(double x) {return 1.0 / (1.0 + exp(-x)); }
double sigmoidDerivative(double x) { return x * (1.0 - x);}

int main()
{
    // Обучающая выборка для операции ИИ (Training dataset for an AI operation)
    std::vector<std::vector<double>> inputs = {{0,0}, {0,1}, {1,0}, {1,1}};
    std::vector<double> outputs = {0, 1, 1, 1};

    // Инициализация весов и смещения случайными числами (Weight and bias initialization with random numbers)
    double w1 = 0.5, w2 = 0.5, bias = -0.2;
    double lr = 0.1;  // Скорость обучения (Learning rate)

    // Обучение сети (10000 эпох) (Network training (10,000 epochs))
    for (int epoch = 0; epoch < 10000; epoch++)
    {
        for (size_t i = 0; i < inputs.size(); i++)
        {
            // Прямой подход (Direct approach)
            double sum = inputs[i][0] * w1 + inputs[i][1] * w2 + bias;
            double pred = sigmoid(sum);

            // Расчет ошибки (Error calculation)
            double error = outputs[i] - pred;
            double gradient = error * sigmoidDerivative(pred);

            // Корректировка весов и смещения (Adjustment of weights and bias)
            w1 += lr * gradient * inputs[i][0];
            w2 += lr * gradient * inputs[i][1];
            bias += lr * gradient;
        }
    }

    // Проверка результатов (Verification of results)
    std::cout << "Test results:\n" << std::endl;
    for (size_t i = 0; i < inputs.size(); i++)
    {
        double sum = inputs[i][0] * w1 + inputs[i][1] * w2 + bias;
        std::cout << inputs[i][0] << "OR" << inputs[i][1]
                  << " = " <<  sigmoid(sum) << "\n" << std::endl;
    }

    return 0;
}