package br.edu.ite.trabalho.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.hibernate.validator.constraints.Length;

@Embeddable
public class Endereco  implements Serializable{

	private static final long serialVersionUID = 2547388888211552327L;
	
	@Length(max=80, min=3)
	@Column(length = 80, nullable=false)
	private String rua;
	
	@Length(max=80, min=1)
	@Column(length = 10, nullable=false)
	private String numero;
	
	@Length(max=30, min=3)
	@Column(length = 30, nullable=false)
	private String bairro;
	
	@Length(max=50, min=3)
	@Column(length = 50, nullable=false)
	private String cidade;

	public String getRua() {
		return rua;
	}

	public void setRua(String rua) {
		this.rua = rua;
	}

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public String getBairro() {
		return bairro;
	}

	public void setBairro(String bairro) {
		this.bairro = bairro;
	}

	public String getCidade() {
		return cidade;
	}

	public void setCidade(String cidade) {
		this.cidade = cidade;
	}

	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Endereco){
			Endereco outro = (Endereco)obj;
			return new EqualsBuilder()
					.append(this.numero, outro.numero)
					.append(this.rua, outro.rua)
					.append(this.bairro, outro.bairro)
					.append(this.cidade, outro.cidade)
					.isEquals();
		}
		return false;
	}
	
	@Override
	public int hashCode() {
		return new HashCodeBuilder()
				.append(numero)
				.append(rua)
				.append(bairro)
				.append(cidade)
				.toHashCode();
	}
	
}
