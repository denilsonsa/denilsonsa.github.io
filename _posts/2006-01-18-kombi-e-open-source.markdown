---
layout: post
title: Kombi é open-source
excerpt: "Meu objetivo neste post não é defender ou atacar as Kombis, nem apontar seus defeitos ou vantagens. Meu objetivo é abordar as diversas características que tenho observado que me fazem concluir que as Kombis são open-source."
lang: pt-br
tag:
- fun
- Open Source
- Rio de Janeiro
---

{% comment %}
_This is a Portuguese post, more interesting (maybe only interesting) to people living in Brazil, specially in Rio de Janeiro._
{% endcomment %}

Se você mora no Rio, pode pular este parágrafo. Se você não mora, gastarei algumas linhas explicando o contexto. Aqui, há centenas ou milhares de [Kombis](https://pt.wikipedia.org/wiki/Volkswagen_Kombi) e vans fazendo transporte "alternativo". Muitas delas fazem linhas parecidas (ou iguais) às linhas de ônibus. Outras, no entanto, fazem itinerários que nenhum outro ônibus faz. Na maior parte das vezes, a tarifa de kombis e vans é mais barata e o tempo de viagem é menor (por diversos motivos, entre eles cortar caminho para evitar congestionamentos). Apesar de quatro pessoas num banco de Kombi ser um pouco apertado, ainda é mais confortável do que ônibus lotado, ou ônibus com bancos tão próximos que não cabem sua perna (caso você seja alto).

Meu objetivo neste "post" não é defender ou atacar as Kombis, nem apontar seus defeitos ou vantagens. Meu objetivo é abordar as diversas características que tenho observado que me fazem concluir que as Kombis são open-source.


## Patches

Se você costuma viajar de Kombi, vai perceber que cada motorista ou dono fez algum tipo de modificação diferente. Dificilmente você encontrará duas Kombis que sejam completamente iguais por dentro e por fora.

Podemos comparar essas modificações com as configurações e patches que cada usuário Linux/Unix/BSD faz com seu sistema.

## Kernel patch

Dentre todos os patches existentes para Kombis, sem dúvida nenhuma o mais popular é o *gas-natural-kit.tar.gz*. Dificilmente você encontrará alguma Kombi rodando sem este patch. Seu objetivo é diminuir o consumo de recursos, de modo que o motorista (usuário) possa utilizar melhor os recursos que possui, separando fatias maiores para outros processos. E isto tudo consegue ser feito sem perda significativa de desempenho.

Este patch na verdade é um kit formado por um pequeno patch aplicado diretamente ao kernel, e uma grande área de armazenamento deixada em user-level. A porção user-level comunica-se com o kernel através de um pequeno tubo. Além disso, ainda é adicionado um software de monitoralmento no painel do veículo (praticamente um módulo extra para o [gkrellm](http://www.gkrellm.net/)).

Muitos usuários se preocupam com a diminuição do espaço livre para user-level, mas a solução mais comum é deixar esta área de armazenamento num lugar pouco acessado, normamente embaixo do banco. Deste modo, a perda de espaço livre existe, mas é insignificante.

Este patch é tão popular que existe para diversos sistemas, embora usuários de táxis e de Kombis sejam a maioria dentre os usuários deste patch. Vale notar que, devido a uma limitação do kernel [Clio](https://pt.wikipedia.org/wiki/Renault_Clio), produzido pela Renault, este patch não pode ser aplicado a ele.

Além disso, devido à grande popularidade, a fabricante das Kombis anunciou que lançará versões com esse patch pré-aplicado de fábrica, mas manterá ainda versões sem o patch, para usuários que assim prefiram.

## Os patches mais populares

Depois do kernel patch citado acima, há diversos patches extremamente populares.

Sem dúvida, o mais popular é aquele deixa a kombi com dois bancos atrás e um banco de 2 lugares na frente (fora o banco do motorista), totalizando 10 passageiros. É tão popular que é impossível encontrar uma Kombi de transporte alternativo sem este patch, ou alguma variação deste patch (como aplicá-lo parcialmente, mantendo apenas 1 lugar para passageiro na frente, ou deixar um dos bancos de trás virado de costas).

A seguir, na lista de popularidade, temos o *itinerário-speaker.tar.gz*, o *porta-automática.tar.gz* e o *luz-interna.tar.gz*. Considero-os empatados em termos de popularidade.

O patch *itinerário-speaker.tar.gz* não toma praticamente nenhum espaço útil do usuário ou dos passageiros. Ele é praticamente invisível, exceto por um pequeno painel de 6 botões que o motorista usa para controlar o funcionamento do patch. Este painel lembra os dockapps [WMButton](http://greek0.net/wmbutton.html), [wmappl](http://wmappl.sourceforge.net/) e [minidock](http://shweps.free.fr/wiki/wakka.php?wiki=DockApps). Apesar de ser pouco vísivel, sua característica é adicionar sons à Kombi, para informar o intinerário a passageiros que estejam a vários metros de distância.

Infelizmente, este patch também pode ser usado para causar um ataque _Denial Of Service_, quando mais de uma Kombi fica produzindo sons repetidamente, o que impede qualquer passageiro de compreender a mensagem falada.

O *porta-automática.tar.gz* ocupa muito mais espaço, cerca de dez a vinte centímetros logo acima da porta da Kombi. Composto basicamente de um motor, uma corrente, um pequeno pedaço de metal que é aplicado à porta e um revestimento plástico, este conjunto de patches permite ao motorista controlar a abertura e fechamento da porta de maneira prática, sem necessidade de força nem da colaboração dos passageiros. Também evita o barulho muito alto quando se fecha a porta de maneira muito bruta.

Devido ao fato de o patch ocupar bastante espaço visível, seus fabricantes aproveitam para incluir, no revestimento de plástico, o logotipo e telefone para contato. Existem dois fabricantes para este patch: Automatic Panther e Seu Prafrente. _Atualização: no final de 2006 já existem pelo menos 4 fabricantes_. Embora seus patches sejam diferentes entre si, seu funcionamento é equivalente.

Vale notar também que o patch fornecido por estes dois fabricantes só é válido para Kombis versão 2 (ou NG - New Generation). As Kombis versão 1 possuem um sistema de portas diferente, incompatível com a versão 2. Mesmo assim, há patches para implementar uma funcionalidade parecida na versão 1. Neste caso, o patch é formado por um conjunto de barras metálicas que funcionam como alavancas e permitem abrir uma das portas através do movimento de apenas uma alavanca, posicionada perto do motorista. Infelizmente, este patch, apesar de bastante engenhoso, permite abrir apenas uma das portas, exigindo ainda colaboração do passageiro para abrir e fechar a segunda porta.

Alguns usuários não possuem condições ou não querem aplicar o patch *porta-automática.tar.gz* em suas Kombis versão 2. Mesmo assim, muitos desses usuários desenvolveram um workaround (quase um patch, está mais para shell script) que envolve usar uma corda para fechar a porta. A abertura continua manual, no entanto. Alguns usuários adicionam uma ou mais polias (roldanas) além da corda, tornando este workaround mais sofisticado. Cheguei a ver um usuário que aplicou 4 roldanas e passou uma corda por todas elas, formando um retângulo no perímetro interno da Kombi. Desta forma, a corda ficava sempre esticada e ele podia abrir e fechar a porta (embora ainda fosse necessário usar a maçaneta manualmente).

Por fim, o *luz-interna.tar.gz* está disponível em diversos modelos. Normalmente o próprio usuário consegue adicionar o patch sozinho. Há modelos com uma pequena luz incandescente ou com luz fluorescente (este fornecido em diversas cores). Algumas vezes os passageiros conseguem notar o source-code desse patch ainda visível, como fios soltos ou passando perto do teto.

## Personalização da aparência

Quase todas as Kombis possuem algum tipo de indicação externa de seu itinerário ou do número da linha:

* faixas coloridas aplicadas à carroceria, cujas cores indicam regiões diferentes da cidade;
* indicador luminoso de origem e destino da linha;
* indicador luminoso do número da linha;
* indicador luminoso do itinerário inteiro;
* itinerário e/ou número da linha colado no pára-brisas como plástico ou um papel plastificado...

Algumas incluem também o preço da tarifa no pára-brisas.

Alguns usuários gostam de colar uma faixa de papel [Con-tact](http://www.vulcan.com.br/Produtos.aspx) ® (todos os direitos reservados) nas portas dianteiras, perto do vidro. Segundo eles, o objetivo é proteger a porta quando tanto passageiros como o próprio motorista apóiam o braço nela.

Outros usuários preferem adicionar enfeites ao espaco interno. É praticamente como trocar o wallpaper do seu desktop. O enfeite mais comum são adesivos (stickers). Alguns preferem colar no máximo 5 adesivos, mas há quem coloque adesivos no teto inteiro. Dentre os diversos tipos de adesivos, destacam-se os de desenho animado e os evangélicos, assim como letras soltas que são usadas para formar pequenas frases ou avisos (como "Cuidado com a cabeça", normalmente colocado perto da porta).

Outro tipo de enfeite menos comum são estrelas, luas, ou figuras quaisquer feitas de plástico que brilha no escuro ou que reage à luz negra.

E falando de aparência de Kombis, não posso deixar de mencionar uma Kombi em especial, da linha 780. Externamente, possui diversos adesivos grandes que lembram a bandeira do Brasil, e outro adesivo com o nome "O Coroa". Possui também diversas luzes extras, uma em cada canto do teto e ainda uma na ponta da antena (esta Kombi até me lembra aqueles carrinhos de brinquedo, cheios de luzes). Internamente, possui diversos adesivos, figuras plásticas como as mencionadas acima, e até mesmo um esqueleto de dinossauro (que brilha no escuro) atrás do último banco. Isso tudo iluminado por luz negra, ou luz violeta. O painel também é repleto de adesivos, inclusive uma estrela de plástico (que brilha no escuro) colada em cima do indicador de alerta (a estrela não é opaca, o alerta ainda é bem visível mesmo com essa estrela colada).

Como se isso tudo não bastasse, a Kombi ainda é bem educada, e agradece quando um passageiro sai. Graças ao *itinerário-speaker.tar.gz*, o motorista aperta um botão e a Kombi fala "Obrigado! Vai com Deus!"

## Patches portados para vans

Alguns dos patches mencionados acima foram portados para vans, que, embora sejam usadas para objetivos similares às Kombis, possuem uma arquitetura diferente.

O *itinerário-speaker.tar.gz* foi desenvolvido de modo que não precisa de nenhum recurso especial de uma arquitetura que não esteja disponível em outra, então é facilmente portável.

O *porta-automática.tar.gz*, por outro lado, depende muito da forma como sistema (em especial, o subsistema de portas) funciona. Mesmo assim, há versões para vans produzidas pela Panther (não sei informar sobre o fabricante Seu Prafrente).

Já o patch *luz-interna.tar.gz* muitas vezes não é necessário, pois a própria van já possui esta funcionalidade implementada. Nada impede, no entanto, que algum usuário resolva aplicar o patch mesmo assim, embora são poucos (ou talvez nenhum) que o façam.

## Conclusões

Notam-se grandes semelhanças entre Kombis e softwares open-source. Em ambos, é muito fácil e é até comum aplicar patches para corrigir ou expandir as funcionalidades do software (da Kombi). Boa parte dos usuários (motoristas) de Kombi mexem ou já mexeram alguma vez no source-code. Além disso, o funcionalmento de Kombis parece seguir a filosofia [KISS (Keep It Simple, Stupid)](https://pt.wikipedia.org/wiki/Keep_It_Simple), filosofia também adotada em diversos softwares open-source.

Por fim, em muitas Kombis o "source" está visível. (Exemplo: já tentou olhar embaixo dos pedais do motorista? Dá para ver o chão.)

E boa viagem!
