package br.edu.ite.trabalho.model.enums;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

import br.edu.ite.trabalho.model.enums.serializer.TipoRegistroDeserializer;
import br.edu.ite.trabalho.model.enums.serializer.TipoRegistroSerializer;

@JsonSerialize(using=TipoRegistroSerializer.class)
@JsonDeserialize(using=TipoRegistroDeserializer.class)
public enum TipoRegistro {
	
	ENTRADA("ENTRADA", "Entrada"),	
	SAIDA("SAIDA", "Saída");
	
	private String codigo;
	private String descricao;
	
	private TipoRegistro(String codigo, String descricao) {
		this.codigo = codigo;
		this.descricao = descricao;
	}

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
	
	public static TipoRegistro buscarPorCodigo(String codigo){
		for(TipoRegistro tipo: TipoRegistro.values()){
			if(tipo.getCodigo().equals(codigo)){
				return tipo;
			}
		}
		return null;
	}
	
}
