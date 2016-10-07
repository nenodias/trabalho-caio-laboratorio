package br.edu.ite.trabalho.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import br.edu.ite.trabalho.model.Registro;

@RepositoryRestResource(collectionResourceRel = "registro", path = "registro")
public interface RegistroRepository extends PagingAndSortingRepository<Registro, Long> {

}
