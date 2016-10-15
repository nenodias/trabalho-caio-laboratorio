package br.edu.ite.trabalho.model.enums.serializer;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import br.edu.ite.trabalho.utils.Formatos;

@Component
public class CustomDateDeserializer extends StdDeserializer<Date>{

	private static final long serialVersionUID = -3627093089819979395L;
	
	public CustomDateDeserializer() {
		super(Date.class);
	}

	@Override
	public Date deserialize(JsonParser p, DeserializationContext ctxt) throws IOException, JsonProcessingException {
		String valor = p.getValueAsString();
		final SimpleDateFormat formatador = new SimpleDateFormat(Formatos.FORMATO_DATETIME);
		try{

			return formatador.parse(valor);
		}catch (Exception e) {
			
		}
		return null;
	}
	
	

}
