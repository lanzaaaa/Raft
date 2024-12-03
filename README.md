# Raft - Algoritmos de Consenso

Este repositório contém uma implementação simples do **algoritmo de consenso Raft** para sistemas distribuídos. O Raft é um algoritmo de consenso projetado para ser compreensível, que visa resolver o problema de manter uma cópia consistente de dados entre múltiplos servidores em um sistema distribuído.

A implementação simula a eleição de líderes em um cluster de nós Raft e inclui tratamento de falhas e a transição entre os estados do Raft (follower, candidate, leader).

## Descrição do Projeto

O algoritmo Raft é usado para garantir que todos os nós em um sistema distribuído concordem sobre o estado de um sistema de forma confiável, mesmo na presença de falhas. Os principais componentes do algoritmo são:

1. **Fases do Raft**:
   - **Follower**: Nós aguardam batimentos cardíacos do líder.
   - **Candidate**: Quando um nó não recebe batimentos cardíacos por um tempo, ele tenta se tornar o líder.
   - **Leader**: O nó que recebe votos suficientes e assume a responsabilidade de coordenar o sistema.

2. **Eleição de Líder**: Quando o sistema começa, um nó se torna candidato e solicita votos aos outros nós para se tornar o líder.

3. **Tolerância a Falhas**: O Raft foi projetado para tolerar falhas de nós e continuar funcionando sem perder dados, o que é garantido através de sua estratégia de consenso.

## Como Configurar o Ambiente e Executar o Código

### 1. **Clonando o Repositório**

Clone este repositório para a sua máquina local:

```bash
git clone https://github.com/lanzaaaa/Raft.git
