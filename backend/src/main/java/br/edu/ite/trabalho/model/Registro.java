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
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonSetter;

import br.edu.ite.trabalho.model.enums.TipoRegistro;

@Entity
@Table(name="registros")
public class Registro implements Serializable{

	private static final long serialVersionUID = -1603241993797435631L;
	
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Long id;

	@JsonIgnore
	@ManyToOne
	@JoinColumn(name="id_carro",nullable = false)
	private Carro carro;
	
	@JsonIgnore
	@ManyToOne
	@JoinColumn(name="id_cliente",nullable = false)
	private Cliente cliente;
	
	@Column(nullable=false)
	@Temporal(TemporalType.TIMESTAMP)
	@JsonFormat(pattern="yyyy-MM-dd HH:mm:ss")
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
	
	@JsonGetter
	public Long getIdCliente(){
		if(cliente != null){
			return cliente.getId();
		}
		return null;
	}
	
	@JsonSetter
	public void setIdCliente(Long id){
		if(cliente == null){
			cliente = new Cliente();
		}
		cliente.setId(id);
	}
	
	@JsonGetter
	public Long getIdCarro(){
		if(carro != null){
			return carro.getId();
		}
		return null;
	}
	
	@JsonSetter
	public void setIdCarro(Long id){
		if(carro == null){
			carro = new Carro();
		}
		carro.setId(id);
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
