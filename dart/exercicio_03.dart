//  3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 

// caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e

//  imprimir seu valor na tela.
import 'dart:io';

void main(){
  print("Digite o valor de A: ");
  String? input_A = stdin.readLineSync();
  print("Digite o valor de B: ");
  String? input_B = stdin.readLineSync();

  if (input_A != null && input_B != null){
    int A = int.parse(input_A);
    int B = int.parse(input_B);

    if ( A == B ){
      int C = A + B;
      print("A soma dos valores A e B = ($C)");
    }else{
      int C = A * B;
      print("A multiplicação dos valores A e B = ($C)");

    }
  }

}