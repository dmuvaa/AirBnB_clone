#!/usr/bin/env

"""Creates a creates a class for the airbnbconsole project."""


class BaseModel:
    """class that will be the base model to be inherited."""
    def __init__(self):
        """Function to initialize the BaseModel1 instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """function that returns the string representation of BaseModel11."""
        return "[{}] ({}) {}"\
                .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the attr to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns all instance attributes key values."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
