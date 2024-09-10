import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);

        System.out.println("Você deseja acelerar esse carro? ");
        String acelerar = scan.nextLine();

        int velocidade = 0;

        if (acelerar.equalsIgnoreCase("sim")) {

            velocidade = Caracters.Acelerar(0);
        } else {
            System.out.println("Ok");
        }

        System.out.println(velocidade);
        Caracters car = new Caracters("Nissan", "Versa", 2012);
        System.out.println(car);
    }
}
