package br.edu.ite.trabalho.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import br.edu.ite.trabalho.model.Cliente;

@RepositoryRestResource(collectionResourceRel = "cliente", path = "cliente")
public interface ClienteRepository extends PagingAndSortingRepository<Cliente, Long> {

}
