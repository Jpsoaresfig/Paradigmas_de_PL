import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int escolha;
        int saldo = 0;  // O saldo inicial é 0
         
        System.out.println("Seja bem-vindo ao sistema do seu banco");

        do {
            System.out.println("1- para Sacar ");
            System.out.println("2- para Depositar");
            System.out.println("3- Consultar saldo em conta");
            System.out.println("4- Sair ");

            escolha = scan.nextInt();

            switch (escolha) {
                case 1:
                    System.out.println("Quanto você quer Sacar? ");
                    int valorSacar = scan.nextInt();
                    
                    // Verifica se o saldo é suficiente para o saque
                    if (saldo >= valorSacar) {
                        saldo = Dados.saque(saldo, valorSacar);  // Atualiza o saldo
                        System.out.println("Saque realizado com sucesso. Seu saldo é de: R$" + saldo);
                    } else {
                        System.out.println("Saldo insuficiente.");
                    }
                    break;

                case 2:
                    System.out.println("Quanto você quer Depositar? ");
                    int valorDepositar = scan.nextInt();
                    saldo = Dados.deposito(saldo, valorDepositar);  // Atualiza o saldo
                    System.out.println("Depósito realizado com sucesso. Seu saldo é de: R$" + saldo);
                    break;

                case 3:
                    System.out.println("Seu saldo é de: R$" + saldo);  // Exibe o saldo atual
                    break;

                case 4:
                    System.out.println("Obrigado por usar o nosso sistema.");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }

        } while (escolha != 4);  // O loop continua até que o usuário escolha a opção de sair

        scan.close();
    }
}
