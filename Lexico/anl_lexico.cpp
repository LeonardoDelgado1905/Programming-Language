#include <bits/stdc++.h>

using namespace std;

string caracteres[10];

int main(){
    freopen("arreglos.txt", "w", stdout);

    string symbols[] = {
"booleano",
"caracter",
"entero",
"real",
"cadena",
"fin_principal",
"fin_principal",
"leer",
"imprimir",
"si ",
"entonces",
"fin_si",
"si_no",
"mientras ",
"hacer",
"fin_mientras",
"para ",
"fin_para",
"seleccionar ",
"entre",
"caso ",
"romper",
"defecto",
"fin_seleccionar",
"estructura ",
"fin_estructura",
"funcion ",
"retornar ",
"fin_funcion",
"verdadero",
"falso",

};
    cout<< "[";
    for (char i = 'a'; i <= 'z'; ++i){
        cout<<"'"<<i<<"', ";
    }
    cout<<"]"<<endl;


    cout<< "[";
    for (char i = 'A'; i <= 'Z'; ++i){
        cout<<"'"<<i<<"', ";
    }
    cout<<"]"<<endl;


    cout<< "[";
    for (char i = '0'; i <= '9'; ++i){
        cout<<"'"<<i<<"', ";
    }
    cout<<"]"<<endl;

    int len = *(&symbols + 1) - symbols;

    cout<< "[";
    for (int i; i < len; ++i){
        cout<<"'"<<symbols[i]<<"', ";
    }
    cout<<"]"<<endl;
    return 0;
}