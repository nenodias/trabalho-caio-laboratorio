package br.edu.ite.trabalho.model.enums.serializer;

import java.io.IOException;

import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;

import br.edu.ite.trabalho.model.enums.TipoRegistro;

@Component
public class TipoRegistroSerializer extends StdSerializer<TipoRegistro>{

	private static final long serialVersionUID = -5296815071537321741L;
	
	public TipoRegistroSerializer() {
		super(TipoRegistro.class);
	}

	@Override
	public void serialize(TipoRegistro value, JsonGenerator generator, SerializerProvider p) throws IOException {
        generator.writeString(value.getCodigo());
	}
	
}
