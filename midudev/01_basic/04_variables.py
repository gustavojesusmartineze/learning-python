# 4. VARIABLES
my_name = "Gustavo"
print(my_name)

my_age = 34
print(my_age)

my_age = 35
print(my_age)

my_name = 120000
print(my_name)

print(f"My name is {my_name}. I am {my_age} years old.")




# 8. PYTHON'S STRONG TYPING DEMONSTRATION
print("8. PYTHON'S STRONG TYPING DEMONSTRATION:")
print("-" * 40)

# This will cause a TypeError - Python is strongly typed!
print("Demonstrating strong typing:")
try:
    result = "5" + 3  # TypeError: can only concatenate str (not "int") to str
    print(result)
except TypeError as e:
    print(f"TypeError: {e}")

# This also fails - no implicit conversion
try:
    result = "5" * 3.5  # TypeError: can't multiply sequence by non-int of type 'float'
    print(result)
except TypeError as e:
    print(f"TypeError: {e}")

# Explicit conversion is required
print("\nExplicit conversion works:")
result1 = int("5") + 3
print(f"int('5') + 3 = {result1}")

result2 = "5" * int(3.5)
print(f"'5' * int(3.5) = {result2}")

# Dynamic typing demonstration
print("\nDynamic typing demonstration:")
x = 5
print(f"x = {x} (type: {type(x)})")

x = "hello"
print(f"x = {x} (type: {type(x)})")

x = [1, 2, 3]
print(f"x = {x} (type: {type(x)})")

print("\n=== STRONG TYPING DEMONSTRATION COMPLETE ===")



# Constants in Python

print("=== CONSTANTS IN PYTHON ===\n")

# Python doesn't have true constants, but there are several approaches:

# 1. NAMING CONVENTION (Most Common)
print("1. NAMING CONVENTION (Most Common):")
print("-" * 40)

# By convention, use UPPERCASE for constants
PI = 3.14159
GRAVITY = 9.81
MAX_CONNECTIONS = 100
DATABASE_URL = "postgresql://localhost:5432/mydb"

print(f"PI: {PI}")
print(f"GRAVITY: {GRAVITY}")
print(f"MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"DATABASE_URL: {DATABASE_URL}")

# Note: These can still be changed (not truly constant)
PI = 3.14  # This works, but goes against convention
print(f"PI after change: {PI}")

print()

# 2. USING ENUMS (Python 3.4+)
print("2. USING ENUMS (Python 3.4+):")
print("-" * 40)

from enum import Enum, IntEnum, auto

# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Auto-numbered Enum
class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    INACTIVE = auto()

# IntEnum (for integer values)
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print("Color enum:")
for color in Color:
    print(f"  {color.name}: {color.value}")

print("\nStatus enum:")
for status in Status:
    print(f"  {status.name}: {status.value}")

print("\nPriority enum:")
for priority in Priority:
    print(f"  {priority.name}: {priority.value}")

# Using enums
current_color = Color.RED
current_status = Status.ACTIVE
current_priority = Priority.HIGH

print(f"\nCurrent color: {current_color}")
print(f"Current status: {current_status}")
print(f"Current priority: {current_priority}")

print()

# 3. USING NAMEDTUPLES
print("3. USING NAMEDTUPLES:")
print("-" * 40)

from collections import namedtuple

# Define a named tuple for configuration
Config = namedtuple('Config', ['host', 'port', 'timeout'])

# Create constant configuration
DEFAULT_CONFIG = Config(host='localhost', port=8080, timeout=30)
PRODUCTION_CONFIG = Config(host='api.example.com', port=443, timeout=60)

print(f"DEFAULT_CONFIG: {DEFAULT_CONFIG}")
print(f"PRODUCTION_CONFIG: {PRODUCTION_CONFIG}")

# Access by name
print(f"Default host: {DEFAULT_CONFIG.host}")
print(f"Default port: {DEFAULT_CONFIG.port}")

print()

# 4. USING DATACLASSES (Python 3.7+)
print("4. USING DATACLASSES (Python 3.7+):")
print("-" * 40)

from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)  # frozen=True makes it immutable
class Settings:
    debug: bool
    log_level: str
    max_retries: int

# Create constant settings
DEFAULT_SETTINGS = Settings(debug=False, log_level="INFO", max_retries=3)
DEVELOPMENT_SETTINGS = Settings(debug=True, log_level="DEBUG", max_retries=5)

print(f"DEFAULT_SETTINGS: {DEFAULT_SETTINGS}")
print(f"DEVELOPMENT_SETTINGS: {DEVELOPMENT_SETTINGS}")

# This would raise an error (frozen=True)
try:
    DEFAULT_SETTINGS.debug = True
except Exception as e:
    print(f"Cannot modify frozen dataclass: {e}")

print()

# 5. USING TYPING.FINAL (Python 3.8+)
print("5. USING TYPING.FINAL (Python 3.8+):")
print("-" * 40)

from typing import Final

# Final variables (type hints only, not enforced at runtime)
API_VERSION: Final = "v1.0"
MAX_FILE_SIZE: Final[int] = 1024 * 1024  # 1MB
SUPPORTED_LANGUAGES: Final[list] = ["en", "es", "fr"]

print(f"API_VERSION: {API_VERSION}")
print(f"MAX_FILE_SIZE: {MAX_FILE_SIZE}")
print(f"SUPPORTED_LANGUAGES: {SUPPORTED_LANGUAGES}")

# Note: Final is just a type hint, can still be changed at runtime
API_VERSION = "v2.0"  # This works, but IDE will warn
print(f"API_VERSION after change: {API_VERSION}")

print()

# 6. CUSTOM CONSTANT CLASS
print("6. CUSTOM CONSTANT CLASS:")
print("-" * 40)

class Constants:
    """A class to hold constants with protection against modification."""
    
    def __init__(self):
        self._values = {}
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        elif name in self._values:
            raise AttributeError(f"Cannot modify constant '{name}'")
        else:
            self._values[name] = value
            super().__setattr__(name, value)
    
    def __getattr__(self, name):
        if name in self._values:
            return self._values[name]
        raise AttributeError(f"Constant '{name}' not found")

# Create constants instance
APP_CONSTANTS = Constants()
APP_CONSTANTS.APP_NAME = "MyApp"
APP_CONSTANTS.VERSION = "1.0.0"
APP_CONSTANTS.AUTHOR = "John Doe"

print(f"APP_NAME: {APP_CONSTANTS.APP_NAME}")
print(f"VERSION: {APP_CONSTANTS.VERSION}")
print(f"AUTHOR: {APP_CONSTANTS.AUTHOR}")

# This will raise an error
try:
    APP_CONSTANTS.APP_NAME = "NewApp"
except AttributeError as e:
    print(f"Cannot modify constant: {e}")

print()

# 7. PRACTICAL EXAMPLE: APPLICATION CONSTANTS
print("7. PRACTICAL EXAMPLE: APPLICATION CONSTANTS:")
print("-" * 40)

# Database constants
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp"
DB_USER = "admin"
DB_PASSWORD = "secret123"

# API constants
API_BASE_URL = "https://api.example.com"
API_TIMEOUT = 30
API_RETRY_ATTEMPTS = 3

# File constants
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB
ALLOWED_FILE_TYPES = [".jpg", ".png", ".pdf", ".txt"]
UPLOAD_DIR = "/uploads"

# Status codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_ERROR = 500

print("Database Configuration:")
print(f"  Host: {DB_HOST}")
print(f"  Port: {DB_PORT}")
print(f"  Database: {DB_NAME}")

print("\nAPI Configuration:")
print(f"  Base URL: {API_BASE_URL}")
print(f"  Timeout: {API_TIMEOUT}s")
print(f"  Retry attempts: {API_RETRY_ATTEMPTS}")

print("\nFile Configuration:")
print(f"  Max file size: {MAX_FILE_SIZE_BYTES} bytes")
print(f"  Allowed types: {ALLOWED_FILE_TYPES}")
print(f"  Upload directory: {UPLOAD_DIR}")

print("\nHTTP Status Codes:")
print(f"  OK: {HTTP_OK}")
print(f"  Created: {HTTP_CREATED}")
print(f"  Bad Request: {HTTP_BAD_REQUEST}")
print(f"  Not Found: {HTTP_NOT_FOUND}")

print("\n=== CONSTANTS DEMONSTRATION COMPLETE ===") 

is_user_logged_in : bool = True
print(is_user_logged_in)

is_user_logged_in = 500
print(is_user_logged_in)

my_name: str = "Gustavo"
print(my_name)