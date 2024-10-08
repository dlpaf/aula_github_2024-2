import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        List<String> menuOptions = Arrays.asList("Conta", "Cliente", "Operacoes", "Sair");
        Menu mainMenu = new Menu("Menu Principal", menuOptions);
        
        int opcaoSelecionada = mainMenu.getSelection();
        
        while (opcaoSelecionada != menuOptions.size()) {
            switch (opcaoSelecionada) {
                case 1:
                    System.out.println("Opção Conta foi selecionada");
                    break;
                case 2:
                    cadastrarCliente();
                    break;
                case 3:
                    System.out.println("Opção Operacoes foi selecionada");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
            
            opcaoSelecionada = mainMenu.getSelection();
        }
        
        System.out.println("Fim do programa.");
    }

    public static void cadastrarCliente() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Cadastro de Cliente");
        System.out.print("Nome do cliente: ");
        String nome = scanner.nextLine();
        System.out.print("CPF do cliente: ");
        String cpf = scanner.nextLine();

        Cliente cliente = new Cliente(nome, cpf);
        System.out.println("Cliente cadastrado com sucesso: " + cliente.getNome() + " - " + cliente.getCpf());
    }
}
