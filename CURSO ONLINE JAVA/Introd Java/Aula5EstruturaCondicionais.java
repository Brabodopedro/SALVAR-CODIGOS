public class Aula5EstruturaCondicionais{

    public static void main(String[] args) {
        //escrever o codigo

        int nota = 50;
        String Graduacao;

        //A 80 B 70 C 60 D 
        //if-else 

        if (nota >= 80){
            Graduacao = "A";
        }else if (nota < 80 && nota >= 70){
            Graduacao = "B";
        }else if (nota < 70 && nota >= 60){
            Graduacao = "C";
        }else if (nota < 60 && nota >= 0){
            Graduacao = "D";
        }else{
            Graduacao = " ";
        }

        switch (Graduacao){
            case "A":
            case "B":
                System.out.println("Aluno Aprovado");
                break;
            case "C":
            case "D":
                System.out.println("Aluno Reporvado");
                break;
            default:
                System.out.println("Graduação Inválida");
                break;

        }


    }
}