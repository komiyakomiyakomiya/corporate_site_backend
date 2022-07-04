```mermaid
  classDiagram
    Component <|-- ConcreteComponent
    Component <|-- Decorator
    Decorator o-- Component
    Component : +operation()
    ConcreteComponent : +operation()
    Decorator : -component
    Decorator : +operation()
    Decorator <|-- ConcreteDecorator
    ConcreteDecorator : +operation()
```
