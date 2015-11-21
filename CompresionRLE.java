import java.util.regex.*;

/**
 * @author A.Dominguez
 * */
public class CompresionRLE {
	 
    public static String compresion(String texto) {
        StringBuilder rle = new StringBuilder();
        for (int indice = 0; indice < texto.length(); indice++) {
            int contador = 1;
            while (indice+1 < texto.length() 
            		&& texto.charAt(indice) == texto.charAt(indice+1)) {
                contador++;
                indice++;
            }
            rle.append(contador);
            rle.append(texto.charAt(indice));
        }
        return rle.toString();
    }
	 
    public static String inversa(String texto) {
        StringBuilder invrle = new StringBuilder();
        Pattern patron = Pattern.compile("[0-9]+|\\p{ASCII}");
        //Se utiliza regex de ASCII - ^[\\u0000-\\u007F]*$ -
        Matcher comparador = patron.matcher(texto);
        //primero busca cualquier valor dentro del regex compilado al encontrarlo
        //devuelve un true, el group toma el valor subsecuente de la primera incidencia         
        
        while (comparador.find()) {
            int contador = Integer.parseInt(comparador.group());
            //se vuelve a realizar la busqueda y se itera el contador hacia atras para
            // agregar el Value encontrado
            comparador.find();
            while (contador--!= 0) {
            	invrle.append(comparador.group());
            }
        }
        return invrle.toString();
    }
}
