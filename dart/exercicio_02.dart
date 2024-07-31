// 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

import 'dart:io';

void main(){
  print("Digite um número: ");
  String? input = stdin.readLineSync();

  if(input != null){
    int numero = int.parse(input);

    if ( numero < 0 ){
      if (numero % 2 == 0){
        print("O numero ($numero) é par e negativo");
      }else{
        print("O numero ($numero) é ímpar e negativo");
      }
    }else{
      if (numero % 2 == 0){
        print("O numero ($numero) é par e positivo");
      }else{
        print("O numero ($numero) é ímpar e positivo");
      }
    }

  }


}