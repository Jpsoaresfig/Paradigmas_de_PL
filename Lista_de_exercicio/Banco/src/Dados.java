public class Dados {
    
    private int saldo;
    private String titular;
    public int getSaldo() {
        return saldo;
    }
    public Dados(int saldo, String titular) {
        this.saldo = saldo;
        this.titular = titular;
    }

    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }
    public String getTitular() {
        return titular;
    }
    public void setTitular(String titular) {
        this.titular = titular;
    } 

    //funções

    public static Integer deposito(int saldo, int valorDepositar){
        int deposito = saldo + valorDepositar ;
        return deposito;
    }

    public static Integer saque(int saldo, int valorSacar){
        int saque = saldo - valorSacar;
        return saque;
    }
}
