package EstruturaSequencial;

import java.util.Scanner;

public class Exercicio4 {
    public static void main(String[] args) {
        Scanner entradas = new Scanner(System.in);
        float media = 0;
        for (int x=1; x <= 4; x++) {
            System.out.println("Nota " + x + ":");
            float nota = entradas.nextFloat();
            media = media + nota;
        }
        media = media / 4;
        System.out.println("Média: " + media);
    }
}
