import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in); // Substituindo console por Scanner

        System.out.println("Digite um animal que você queira saber o som (passaro, cachorro, gato):");
        String animal = scan.nextLine(); // Lendo a entrada do usuário

        switch (animal.toLowerCase()) { // Comparação com letras minúsculas para maior flexibilidade
            case "passaro":
                System.out.println(Sons.Passaro());
                break;
            case "cachorro":
                System.out.println(Sons.Cachorro());
                break;
            case "gato":
                System.out.println(Sons.Gato());
                break;
            default:
                System.out.println("Animal desconhecido.");
                break;
        }

        scan.close(); // Fechando o Scanner
    }
}
