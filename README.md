# Métodos Potenciais
Disciplina ministrada ao Programa de Pós-Graduação em Geociências da Faculdade de Geologia da Universidade do Estado do Rio de Janeiro (FGEL/UERJ).

**Professor**: [André Luis A. Reis](https://www.pinga-lab.org/people/andre.html)

**E-mails:** reisandreluis@gmail.com / andre.reis@uerj.br

>**Aviso:** O material disponibilizado neste repositório está em constante desenvolvimento e, portanto, a universidade e a coordenação de graduação não possuem qualquer responsabilidade sobre o seu conteúdo. As aulas não serão gravadas.

## Ementa

Método  Gravimétrico:  Potencial  Gravitacional,  equações  dos  campos  potenciais,  gravidade terrestre,  instrumentação,  correções  gravimétricas,  anomalias  gravimétricas,  densidade  das rochas   e   minerais.   Processamento   de   Dados   Gravimétricos.   Interpretação   de   dados gravimétricos. Prática: Prática de Campo-Treinamento na aquisição de dados gravimétricos. Prática  de  Processamento-uso  de  programas  de  computador  para  processamento  dos  dados coletados na prática de campo.Método Magnetométrico: Teoria Elementar, magnetismo da Terra. Instrumentação, operações de  campo.  Efeitos  magnéticos  de  formas  simples.  Processamento  e  Interpretação.  Prática  de Campo-Treinamento na aquisição de dados magnetométricos. Prática de Processamento-uso de programas de computador para processamento dos dados coletados na prática de campo.

Versão oficial do conteúdo da disciplina: [Métodos Potenciais](https://www.fgel.uerj.br/site/wp-content/uploads/2019/05/M%c3%a9todos-potenciais_GEL04903.pdf)

## Tópicos do curso

* Elementos de teoria do potencial
* Campo de gravidade da Terra
* Gravimetria
* Campo magnético da Terra
* Magnetometria
* Processamento e interpretação de dados potenciais
* Modelagem direta e inversão de campos potenciais
* Transformações de campos potenciais

## Conteúdo didático computacional

>**Aviso:** Os códigos aqui apresentados são parte de uma disciplina e sua usabilidade é, consideravelmente, limitada a nível de pesquisa e desenvolvimento. A universidade não tem qualquer responsabilidade sobre a aplicação, tanto a nível acadêmico quanto profissional, dos códigos aqui apresentados.

- O campo de gravidade
    - [X] Campo de Gravidade real, Terra Normal e Distúrbio de gravidade `gravity_field_and_disturbance.ipynb`
    - [X] Anomalia bouguer pro mundo inteiro `bouguer_anomaly.ipynb`
    - [X] Campo de gravidade na Costa brasileira `brazilian_coast_bouguer_anomaly.ipynb`
    - [X] Campo de gravidade nos Andes `andes_bouguer_anomaly.ipynb`
    - [X] Campo de gravidade no Havaí `hawaii_bouguer_anomaly.ipynb`
    - [X] Campo de gravidade na dorsal mesoceânica `mid_ocean_bouguer_anomaly.ipynb`

- Campo geomagnético e Anomalia de campo total
    - [X] International Geomagnetic Reference Field `IGRF.ipynb`
    - [X] Anomalia de campo total: Anitápolis, SC `TFA_anitapolis.ipynb`
    - [X] Anomalia de campo total: Carajás, PA `TFA_carajas.ipynb`
    - [X] Anomalia de campo total: Montes Claros de Goiás, GO `TFA_montes_claros.ipynb`

- Modelagem gravimetria e magnética
    - [X] Prisma poligonal 2D `2D_polygonal_modeling.ipynb`
    - [X] Bacia bidimensional `basin_2D_modeling.ipynb`
    - [X] Efeito de uma esfera `sphere_modeling.ipynb`
    - [X] Gradiente da gravidade de uma esfera `gravity_gradient_sphere.ipynb` 
    - [X] Efeito de um prisma `prism_modeling.ipynb`
    - [X] Gradiente da gravidade de um prisma `gravity_gradient_prism.ipynb`
    - [X] Modelagem 3D de uma bacia `3D_basin_modeling.ipynb`

- Inversão gravimetria e magnética 
    - [X] Corpo em queda livre (cinemática) `free_fall_body.ipynb`
    - [X] Direção de magnetização de uma esfera `magnetization_direction_sphere.ipynb`
    - [X] Estimativa do relevo do embasamento `basement_estimation_gravity.ipynb`
    - [x] Camada equivalente `processing_eqlayer.ipynb`

- Processamento no domínio da frequência
    - [X] Continuação para cima, Redução ao polo e Amplitude do gradiente total `fourier_processing_mag.ipynb`

## Referências bibliográficas

* MacMillan, W. D. 1930. *The Theory of the Potential*. Dover Publications, Inc.

* Kellogg, O. D. 1967. *Foundations of Potential Theory*. Springer-Verlag.

* Blakely, R. J., 1996, *Potential theory in gravity and magnetic applications*. Cambridge
University Press.

* Hofmann-Wellenhof, B. e H. Moritz, 2005, *Physical Geodesy*. Springer.

* Langel, R. A. e W. J. Hinze, 1998, *The magnetic field of the Earth's lithosphere: the
satellite perspective*. Cambridge University Press.

* Periódicos da área

## Material

Todo o material da disciplina (dados e códigos computacionais) estão disponíveis em um repositório no Github:

https://github.com/andrelreis/metodos-potenciais

As versões ao final de cada ano são marcadas com um *tag* e podem ser vistas em:

https://github.com/andrelreis/metodos-potenciais/releases


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">"Material didático da disciplina Métodos Potenciais"</span>
by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/andrelreis/metodos-potenciais" property="cc:attributionName" rel="cc:attributionURL">André L A Reis</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
