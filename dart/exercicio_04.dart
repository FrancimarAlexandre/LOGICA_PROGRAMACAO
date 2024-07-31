// 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor

import 'dart:io';

void main(){
  print("Digite um valor: ");
  String? input = stdin.readLineSync();

  if (input != null){
    int num = int.parse(input);
    int ant = num -1;
    int suc = num + 1;
    print("O antecessor de $num é $ant e o sucessor é $suc");
  }

}