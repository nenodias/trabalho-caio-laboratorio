package br.edu.ite.trabalho.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.Valid;
import javax.validation.constraints.NotNull;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.hibernate.validator.constraints.Length;

@Entity
@Table(name="clientes")
public class Cliente implements Serializable{

	private static final long serialVersionUID = -2034366362085567038L;
	
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Long id;

	@Length(max=150, min=4)
	@Column(length=150, nullable=false)
	private String nome;
	
	@Length(max=200, min=8)
	@Column(length=200)
	private String email;
	
	@NotNull
	@Column(nullable=false)
	private Long rg;
	
	@Length(max=18, min=8)
	@Column(length=18)
	private String telefone;
	
	@Valid
	@NotNull
	@Embedded
	private Endereco endereco;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public Long getRg() {
		return rg;
	}

	public void setRg(Long rg) {
		this.rg = rg;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Cliente){
			Cliente outro = (Cliente)obj;
			return new EqualsBuilder()
					.append(this.id, outro.id)
					.append(this.nome, outro.nome)
					.append(this.email, outro.email)
					.append(this.rg, outro.rg)
					.append(this.telefone, outro.telefone)
					.append(this.endereco, outro.endereco)
					.isEquals();
		}
		return false;
	}
	
	@Override
	public int hashCode() {
		return new HashCodeBuilder()
				.append(id)
				.append(nome)
				.append(email)
				.append(rg)
				.append(telefone)
				.append(endereco)
				.toHashCode();
	}
	
}
