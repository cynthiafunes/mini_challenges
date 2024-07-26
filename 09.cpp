// Escribir un programa que pida al usuario dos números y los sume.

#include <iostream>

int main() {
    int num1, num2, suma;

    std::cout << "Ingrese el primer numero: ";
    std::cin >> num1;

    std::cout << "Ingrese el segundo numero: ";
    std::cin >> num2;

    suma = num1 + num2;

    std::cout << "La suma de " << num1 << " + " << num2 << " es: " << suma << std::endl;

    return 0;
}
