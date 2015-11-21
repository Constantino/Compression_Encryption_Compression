
/**
 * @author A.Dominguez
 * */
public class CompresionRLE_Test {

	public static void main(String[] args) {
		CompresionRLE rle = new CompresionRLE();
		System.out.println(rle.compresion("%%%%&&&&#######"));
		System.out.println(rle.inversa("12(1#12@3{24]1+14="));
		System.out.println(rle.compresion(rle.inversa("12(1#12@3{24]1+14=")));
		System.out.println(rle.inversa(rle.compresion(rle.inversa("12(1#12@3{24]1+14="))));
	}

}