package br.edu.ite.trabalho.model.enums;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

import br.edu.ite.trabalho.model.enums.serializer.TipoRegistroDeserializer;
import br.edu.ite.trabalho.model.enums.serializer.TipoRegistroSerializer;

@JsonFormat(shape = JsonFormat.Shape.STRING)
@JsonSerialize(using = TipoRegistroSerializer.class)
@JsonDeserialize(using = TipoRegistroDeserializer.class)
public enum TipoRegistro {
	
	ENTRADA("ENTRADA", "Entrada"),
	SAIDA("SAIDA", "Saída");
	
	private String codigo;
	private String descricao;
	
	private TipoRegistro(String codigo, String descricao) {
		this.codigo = codigo;
		this.descricao = descricao;
	}

	@JsonValue
	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	
}
