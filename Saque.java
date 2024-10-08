import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Menu mainMenu = new Menu("Menu Principal", Arrays.asList("Conta", "Cliente", "Operacoes", "Realizar Saque"));
        int selectedOption = mainMenu.getSelection();

        switch (selectedOption) {
            case 1:
                System.out.println("Opção Conta selecionada");
                break;
            case 2:
                System.out.println("Opção Cliente selecionada");
                break;
            case 3:
                System.out.println("Opção Operações selecionada");
                break;
            case 4:
                realizarSaque();
                break;
            default:
                System.out.println("Opção inválida");
        }
        
        System.out.println("Fim");
    }

    private static void realizarSaque() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Informe o valor a ser sacado: ");
        double valor = scanner.nextDouble();

        // Lógica de validação de saque
        if (valor <= 0) {
            System.out.println("Valor inválido para saque.");
        } else {
            System.out.println("Saque de R$ " + valor + " realizado com sucesso!");
            // Aqui você pode adicionar lógica para atualizar o saldo ou o que for necessário
        }
    }
}
