//Ordenamiento de un Array: Escribir un programa que ordene un array de enteros

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int arr[] = {10, 50, 45, 35, 25, 55, 60};
    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr + n);
    cout << "Array ordenado: \n";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
