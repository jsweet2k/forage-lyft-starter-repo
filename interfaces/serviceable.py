from abc import ABC, abstractmethod

# Serviceable Interface
class IServiceable(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass




