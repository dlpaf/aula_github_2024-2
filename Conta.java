public class Conta {
    private double saldo;

    public Conta() {
        this.saldo = 0;
    }

    public double getSaldo() {
        return saldo;
    }

    public boolean transferir(Conta destino, double valor) {
        if (valor > 0 && valor <= saldo) {
            this.sacar(valor);
            destino.depositar(valor);
            System.out.println("Transferência de R$ " + valor + " realizada com sucesso.");
            return true;
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
            return false;
        }
    }
}
