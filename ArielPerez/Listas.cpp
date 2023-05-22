#include <iostream>

using namespace std;

// Definición de la estructura del nodo de la lista enlazada
struct Node {
    int data;
    Node* next;
};

// Clase ListaEnlazada que contiene las operaciones básicas
class ListaEnlazada {
private:
    Node* head;

public:
    ListaEnlazada() {
        head = NULL;
    }

    // Función para agregar un elemento al final de la lista
    void agregarElemento(int valor) {
        Node* newNode = new Node;
        newNode->data = valor;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }
        cout << "Elemento agregado: " << valor << endl;
    }

    // Función para eliminar un elemento de la lista
    void eliminarElemento(int valor) {
        if (head == NULL) {
            cout << "La lista está vacía." << endl;
            return;
        }

        Node* current = head;
        Node* previous = NULL;
        bool encontrado = false;

        while (current != NULL) {
            if (current->data == valor) {
                encontrado = true;
                break;
            }
            previous = current;
            current = current->next;
        }

        if (!encontrado) {
            cout << "Elemento no encontrado en la lista." << endl;
            return;
        }

        if (previous == NULL) {
            head = current->next;
        } else {
            previous->next = current->next;
        }

        delete current;
        cout << "Elemento eliminado: " << valor << endl;
    }

    // Función para mostrar los elementos de la lista
    void mostrarLista() {
        if (head == NULL) {
            cout << "La lista está vacía." << endl;
            return;
        }

        Node* current = head;
        cout << "Elementos de la lista: ";
        while (current != NULL) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    ListaEnlazada lista;

    lista.agregarElemento(10);
    lista.agregarElemento(20);
    lista.agregarElemento(30);
    lista.mostrarLista();

    lista.eliminarElemento(20);
    lista.mostrarLista();

    return 0;
}