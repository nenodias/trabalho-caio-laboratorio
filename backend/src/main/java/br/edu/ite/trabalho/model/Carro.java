package br.edu.ite.trabalho.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.hibernate.validator.constraints.Length;

@Entity
@Table(name="carros")
public class Carro implements Serializable{

	private static final long serialVersionUID = 4461962521681833984L;
	
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Long id;
	
	@Length(max=10, min=8)
	@Column(length=10, nullable=false)
	private String placa;
	
	@Length(min=3,max=30)
	@Column(length=30, nullable=false)
	private String marca;
	
	@Length(min=3,max=30)
	@Column(length=30, nullable=false)
	private String modelo;
	
	@NotNull
	@Column(nullable=false)
	private Integer ano;
	
	@Length(min=3,max=20)
	@Column(length = 20)
	private String cor;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getPlaca() {
		return placa;
	}

	public void setPlaca(String placa) {
		this.placa = placa;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public Integer getAno() {
		return ano;
	}

	public void setAno(Integer ano) {
		this.ano = ano;
	}

	public String getCor() {
		return cor;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Carro){
			Carro outro = (Carro)obj;
			return new EqualsBuilder()
					.append(id, outro.id)
					.append(placa, outro.placa)
					.append(marca, outro.marca)
					.append(modelo, outro.modelo)
					.append(ano, outro.ano)
					.append(cor, outro.cor)
					.isEquals();
		}
		return false;
	}
	
	@Override
	public int hashCode() {
		return new HashCodeBuilder()
				.append(id)
				.append(placa)
				.append(marca)
				.append(modelo)
				.append(ano)
				.append(cor)
				.toHashCode();
	}
	
}
