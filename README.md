# Projeto de Demonstração de Padrões de Projeto - Sistema de Cafeteria

Este projeto é uma implementação prática de diversos padrões de projeto do "Gang of Four" (GoF), aplicados ao domínio de um sistema de pedidos para uma cafeteria. O objetivo é demonstrar como esses padrões ajudam a criar um software mais flexível, manutenível e escalável, seguindo as melhores práticas de arquitetura de software.

O código foi estruturado para isolar responsabilidades e desacoplar componentes, permitindo que novas funcionalidades (como novas bebidas, ingredientes ou métodos de pagamento) sejam adicionadas com o mínimo de impacto no código existente.

---

## Mapa dos Padrões Implementados

A tabela abaixo detalha os padrões de projeto utilizados, os arquivos onde suas implementações principais podem ser encontradas e as classes ou métodos centrais que os representam.

| Padrão de Projeto | Arquivo(s) Principal(is) | Classe/Método Chave |
| :--- | :--- | :--- |
| **Factory Method** (Simple Factory) | `beverage_factory.py` | `BeverageFactory.create()` |
| **Decorator** | `decorators.py` | `Milk`, `Chocolate`, `WhippedCream` |
| **Strategy** | `payment_strategy.py`, `pix.py`, `card.py` | `PaymentStrategy.pay()` |
| **Observer** | `subject.py`, `observers.py` | `Subject.notify()` |
| **Command** | `command.py`, `order_command.py` | `OrderCommand.execute()` |

---

## Instruções de Execução

Para executar a demonstração do sistema, siga os passos abaixo.

### Pré-requisitos

- Python 3.7 ou superior.

### Execução

1.  Clone ou faça o download deste repositório.
2.  Navegue até o diretório raiz do projeto.
3.  Execute o arquivo `main.py` a partir do terminal:

    ```bash
    python main.py
    ```

4.  O script executará uma série de operações de demonstração, incluindo:
    - Criação de um pedido de café com múltiplos adicionais (Decorator).
    - Notificação de observadores sobre o status do pedido (Observer).
    - Processamento de pagamentos usando diferentes estratégias (Strategy).
    - Execução de um pedido encapsulado como um objeto (Command).

O resultado das operações será exibido no console, e um arquivo de log chamado `order_log.txt` será criado (ou atualizado) no mesmo diretório, demonstrando a ação do `LoggerNotifier`.
