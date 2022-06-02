# Taxam Grouper

- [en](../../readme.md)

Taxam Grouper é um módulo de ferramentas do projeto [TaxAM](https://github.com/TaxAM/taxam) criado para agrupar amostras por matrizes geradas pelo TaxAM. No módulo, temos as seguintes ferramentas:

- [Grouper](https://github.com/TaxAM/taxam_grouper)   
    Usado para agrupar amostras por matrizes geradas pelo TaxAM.

- [Taxam Grouper GUI](https://github.com/TaxAM/taxam_grouper/tree/main/groups_viewer)
    Usado para visualizar as grupos gerados pelo TaxAM Grouper.

## Grouper
Usa alguns algoritmos para agrupar amostras. O primeiro é o [K-means](https://en.wikipedia.org/wiki/K-means_clustering) algoritmo. O segundo é o [Hierarchical Clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) algoritmo.

### Como usar o Grouper

1. Instalar todas as dependências no arquivo [requirements.txt](../../requirements.txt).
```
pip install -r requirements.txt
```
2. Executar script grouper:

```sh
python grouper <nome_do_algoritmo> <flag_1> <valor_1> <flag_2> <valor_2> ...
```

- Flags globais:
    - `-fp` or `--file_path`: Matriz a ser agrupada.
    - `-on` or `--output_name`: Nome para o arquivo de saída do TaxAM Grouper. Padrão "TaxAM_grouper".
    - `-h` or `--help`: Mostra a mensagem de ajuda e sai.

- Flags do K-means:
    - `-n` or `--number_of_clusters`: Define o número de clusters que o Kmeans vai usar para agrupar amostras. Padrão 2.
    - `-ni` or `n_init`: Número de vezes que o Kmeans vai rodar com centroides diferentes. O resultado final será o melhor de n_init rodadas consecutivas em termos de inércia. Padrão 10.
    - `-mi` or `max_iter`: Número máximo de iterações do algoritmo Kmeans para uma única rodada. Padrão 300.

#### Exemplo de uso
```sh
python grouper kmeans -fp "matrix.txt" -on "TaxAM_grouper" -n 3
```

## Taxam Grouper GUI
É uma interface gráfica que permite visualizar os grupos gerados pelo TaxAM Grouper.

- Abra o [index.html](../../groups_viewer/index.html) no navegador.
- Selecione a matriz que você deseja visualizar.

    ![Escolher arquivo](../src/images/choose_file.png)
- Clique no botão "Visualizar".

    ![Visualize](../src/images/view_btn.png)
- Então é possível visualizar os dados de cada grupo.

    ![Groups](../src/images/groups.png)
