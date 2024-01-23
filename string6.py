#Execute a String of Code in Python
import types
 
code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a)  # 11