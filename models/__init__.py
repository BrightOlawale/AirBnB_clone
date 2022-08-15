<<<<<<< HEAD
#!/usr/bin/python3
"""Package initializer for the application."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.load_engine import load_engine
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

storage = FileStorage()
=======
"""Module for FileStorage autoinit."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
>>>>>>> 9a0e1858bb0b2569c3060b86b0fa81f45ddc683d
storage.reload()