public class Caracters {

    private String marca;
    private String modelo;
    private int ano;

    
    public Caracters(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    public String getMarca() {
        return marca;
    }


    public void setMarca(String marca) {
        this.marca = marca;
    }


    public String getModelo() {
        return modelo;
    }


    public void setModelo(String modelo) {
        this.modelo = modelo;
    }


    public int getAno() {
        return ano;
    }


    public void setAno(int ano) {
        this.ano = ano;
    }
    //funções---------------------------
    public String toString(){
        return marca + " " + modelo + " " + ano;
    }
    public static Integer Acelerar(int acelerar){
        int velocidade = acelerar += 1; 
        return velocidade;
    
    }
    
}

