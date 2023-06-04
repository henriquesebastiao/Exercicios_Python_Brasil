package EstruturaSequencial;

import java.util.Scanner;
public class Exercicio3 {
    public static void main(String[] args) {
        Scanner inputs = new Scanner(System.in);
        System.out.println("Informe um número: ");
        int numero1 = inputs.nextInt();
        System.out.println("Informe outro número: ");
        int numero2 = inputs.nextInt();
        System.out.println(numero1 + " + " + numero2 + " = " + (numero1 + numero2));
    }
}
