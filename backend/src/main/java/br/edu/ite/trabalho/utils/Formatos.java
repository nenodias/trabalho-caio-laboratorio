package br.edu.ite.trabalho.utils;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Formatos {
	
	public static final String FORMATO_DATETIME = "yyyy-MM-dd HH:mm:ss";
	
	public static String formataData(Date date){
		try{
			final SimpleDateFormat formatador = new SimpleDateFormat(FORMATO_DATETIME);
			return formatador.format(date);
		}catch (Exception e) {
			
		}
		return null;
	}
	
	public static Date parseData(String texto){
		try{
			final SimpleDateFormat formatador = new SimpleDateFormat(FORMATO_DATETIME);
			return formatador.parse(texto);
		}catch (Exception e) {
			
		}
		return null;
	}

}
