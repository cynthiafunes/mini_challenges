// Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo
#include <iostream> 
#include <string>    
#include <algorithm>

bool esPalindromo(std::string str) {
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);

    int n = str.length();
    for (int i = 0; i < n / 2; i++) {
        if (str[i] != str[n - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    std::string palabra;
    std::cout << "Ingresa una palabra: ";
    std::cin >> palabra;

    if (esPalindromo(palabra)) {
        std::cout << "La palabra es un palindromo." << std::endl;
    } else {
        std::cout << "La palabra no es un palindromo." << std::endl;
    }

    return 0;
}

