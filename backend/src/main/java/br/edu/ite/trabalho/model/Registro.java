package br.edu.ite.trabalho.model;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import com.fasterxml.jackson.annotation.JsonFormat;

import br.edu.ite.trabalho.model.enums.TipoRegistro;

@Entity
@Table(name="registros")
public class Registro implements Serializable{

	private static final long serialVersionUID = -1603241993797435631L;
	
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Long id;

	@ManyToOne
	@JoinColumn(name="id_carro",nullable = false)
	private Carro carro;
	
	@ManyToOne
	@JoinColumn(name="id_cliente",nullable = false)
	private Cliente cliente;
	
	@NotNull
	@Column(nullable=false)
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd HH:mm:ss")
	private Date data;
	
	@Column(length=10, nullable=false)
	@Enumerated(EnumType.STRING)
	private TipoRegistro tipo;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Carro getCarro() {
		return carro;
	}

	public void setCarro(Carro carro) {
		this.carro = carro;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public Date getData() {
		return data;
	}

	public void setData(Date data) {
		this.data = data;
	}

	public TipoRegistro getTipo() {
		return tipo;
	}

	public void setTipo(TipoRegistro tipo) {
		this.tipo = tipo;
	}

	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Registro){
			Registro outro = (Registro)obj;
			return new EqualsBuilder()
					.append(id, outro.id)
					.append(carro, outro.carro)
					.append(cliente, outro.cliente)
					.append(data, outro.data)
					.append(tipo, outro.tipo)
					.isEquals();
		}
		return false;
	}
	
	@Override
	public int hashCode() {
		return new HashCodeBuilder()
				.append(id)
				.append(carro)
				.append(cliente)
				.append(data)
				.append(tipo)
				.toHashCode();
	}
	
}
