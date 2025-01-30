#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h> // Para inet_pton y otras funciones

#pragma comment(lib, "Ws2_32.lib") // Vincula la biblioteca de WinSock automáticamente

using namespace std;

int main() {
    WSADATA wsaData;
    SOCKET serverSocket, clientSocket;
    sockaddr_in serverAddr, clientAddr;
    int clientAddrSize = sizeof(clientAddr);

    // Inicializar WinSock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        cerr << "Error al inicializar WinSock" << endl;
        return 1;
    }

    // Crear socket
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET) {
        cerr << "Error al crear socket" << endl;
        WSACleanup();
        return 1;
    }

    // Configurar dirección del servidor
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY; // Acepta conexiones desde cualquier dirección
    serverAddr.sin_port = htons(9999);

    // Asociar el socket al puerto
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        cerr << "Error al asociar socket: " << WSAGetLastError() << endl;
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    // Escuchar conexiones
    if (listen(serverSocket, 5) == SOCKET_ERROR) {
        cerr << "Error al escuchar en el puerto: " << WSAGetLastError() << endl;
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    cout << "Servidor en espera de conexiones..." << endl;

    while (true) {
        clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrSize);
        if (clientSocket == INVALID_SOCKET) {
            cerr << "Error al aceptar conexión: " << WSAGetLastError() << endl;
            continue;
        }

        char clientIP[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &(clientAddr.sin_addr), clientIP, INET_ADDRSTRLEN);
        cout << "Conectado con " << clientIP << ":" << ntohs(clientAddr.sin_port) << endl;

        // Enviar hora actual al cliente
        time_t now = time(0);
        string currentTime = ctime(&now);
        send(clientSocket, currentTime.c_str(), currentTime.length(), 0);

        // Cerrar conexión con el cliente
        closesocket(clientSocket);
    }

    // Cerrar socket del servidor y limpiar WinSock
    closesocket(serverSocket);
    WSACleanup();

    return 0;
}
