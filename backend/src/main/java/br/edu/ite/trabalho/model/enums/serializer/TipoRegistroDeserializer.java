package br.edu.ite.trabalho.model.enums.serializer;

import java.io.IOException;

import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import br.edu.ite.trabalho.model.enums.TipoRegistro;

@Component
public class TipoRegistroDeserializer extends StdDeserializer<TipoRegistro> {

	private static final long serialVersionUID = -249126285690833652L;

	public TipoRegistroDeserializer() {
		super(TipoRegistro.class);
	}

	@Override
	public TipoRegistro deserialize(JsonParser p, DeserializationContext ctxt)
			throws IOException, JsonProcessingException {
		return TipoRegistro.buscarPorCodigo(p.getValueAsString());
	}


}
