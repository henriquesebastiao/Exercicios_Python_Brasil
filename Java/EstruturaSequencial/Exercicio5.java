package EstruturaSequencial;

import java.util.Scanner;
public class Exercicio5 {
    public static void main(String[] args) {
        Scanner inputs = new Scanner(System.in);
        System.out.println("Metros:");
        float metros = inputs.nextFloat();
        float centimetros = metros * 100;
        System.out.println("Centímetros: " + centimetros + "cm");
    }
}
