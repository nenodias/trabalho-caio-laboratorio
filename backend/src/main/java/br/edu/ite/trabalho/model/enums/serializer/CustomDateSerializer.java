package br.edu.ite.trabalho.model.enums.serializer;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;

import br.edu.ite.trabalho.utils.Formatos;

@Component
public class CustomDateSerializer extends StdSerializer<Date>{

	private static final long serialVersionUID = 1L;

	public CustomDateSerializer() {
		super(Date.class);
	}

	@Override
	public void serialize(Date value, JsonGenerator generator, SerializerProvider p) throws IOException {
		final SimpleDateFormat formatador = new SimpleDateFormat(Formatos.FORMATO_DATETIME);
		try{
			generator.writeString(formatador.format(value));
		}catch (Exception e) {
			generator.writeNull();
		}
	}
	
}
