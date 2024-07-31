// 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

import 'dart:io';

void main(){
  print("Digite o valor de A: ");
  String? input_A = stdin.readLineSync();

  print("Digite o valor de B: ");
  String? input_B = stdin.readLineSync();

  print("Digite o valor de B: ");
  String? input_C = stdin.readLineSync();
  
  if (input_A != null &&  input_B != null  && input_C != null){
    int A = int.parse(input_A);
    int B = int.parse(input_B);
    int C = int.parse(input_C);
    int soma =  A + B;

    print("O valor da soma de A + B = $soma");

    if (soma < C){
      print("O valor é menor que o valor de C = $C");
    }
    else if (soma > C){
      print("O valor é maior que o valor de C = $C");
    }
    else{
      print("O valor é iqual ao valor de C = $C");
    }
  }
}