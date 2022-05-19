from abc import ABC,abstractmethod
from typing import Any, List

class DatabaseInterface(ABC):
    """
    Abstract Class to represent a Interface.
    All Database classes must be implement this interface
    (Dependency Inversion Principle)
    """
    
    # @abstractmethod
    # def instance(self):
    #     """
    #     Abstract method to return the instance.
    #     This method must be implemented in all classes
    #     that wants to implement the 'Database' interface
        
    #     Raises
    #     ------
    #     NotImplementedError
    #         Raises a NotImplementedError because this is an 
    #         abstract method and must be implemented 
    #     """
    #     raise NotImplementedError(
    #         'This method is abstract. You must implement it'
    #     )
    
    @abstractmethod
    def connect(self):
        """
        Abstract method to connect to the database.
        This method must be implemented in all classes
        that wants to implement the 'Database' interface
        
        Returns
        -------
        MySQLConnection
            A reference to the MySQL connection.
        
        Raises
        ------
        NotImplementedError
            Raises a NotImplementedError because this is an 
            abstract method and must be implemented 
        """
        raise NotImplementedError(
            'This method is abstract. You must implement it'
        )
        
    @abstractmethod
    def close(self):
        """Abstract method to close the database connection
        
            This method must be implemented in all classes
            that wants to implement the 'Database' interface

        Raises
        ------
        NotImplementedError
            Raises a NotImplementedError because this is an 
            abstract method and must be implemented 

        """
        raise NotImplementedError(
            'This method is abstract. You must implement it'
        )
        
    
    @abstractmethod
    def execute_query(self, query: str, params: List[Any] = []):
        """
        Abstract method to execute the query received as argument.
        This method must be implemented in all classes
        that wants to implement the 'Database' interface
        
        Parameters
        ----------
        query: str
            The query to be executed
        
        params: List
            A list of parameters that will fulfill the query
            
        Raises
        -----------
        NotImplementedError
            Raises a NotImplementedError because this is an 
            abstract method and must be implemented 
        """
        raise NotImplementedError(
            'This method is abstract. You must implement it'
        )
    
    @abstractmethod
    def commit(self):
        """
        Abstract method to commit something into the database.
        This method must be implemented in all classes
        that wants to implement the 'Database' interface
        
        Raises
        ------
        NotImplementedError
            Raises a NotImplementedError because this is an 
            abstract method and must be implemented 
        """
        raise NotImplementedError(
            'This method is abstract. You must implement it'
        )
    
    @abstractmethod
    def rollback(self):
        """
        Abstract method to rollback in the database.
        This method must be implemented in all classes
        that wants to implement the 'Database' interface
        
        Raises
        ------
        NotImplementedError
            Raises a NotImplementedError because this is an 
            abstract method and must be implemented 
        """
        raise NotImplementedError(
            'This method is abstract. You must implement it'
        )