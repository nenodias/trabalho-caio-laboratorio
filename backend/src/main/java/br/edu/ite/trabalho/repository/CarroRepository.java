package br.edu.ite.trabalho.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import br.edu.ite.trabalho.model.Carro;

@RepositoryRestResource(collectionResourceRel = "carro", path = "carro")
public interface CarroRepository extends PagingAndSortingRepository<Carro, Long> {

}
