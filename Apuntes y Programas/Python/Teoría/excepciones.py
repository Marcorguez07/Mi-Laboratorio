# DOCUMENTO DE ESTUDIO
# MARCOKISTAN 2026

# EXCEPCIONES

# try , except hacen lo que esperas...
# raise Exception("razon"), lanzará una excepcion con el valor str razon
# el except puede usarse como condicional para una excepción concreta, útil para
# cuando por ejemplo tenemos excepciones personalizadas.

# Podemos crear una excepción personalizada simplemente usando heritage de la
# clase ya creada Exception como parametro de la clase.

# ejemplo:

class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando un usuario intenta retirar más dinero del que tiene."""
    pass

def retirar_dinero(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError(f"Intento de retirar {cantidad} con solo {saldo} en cuenta.")
    return saldo - cantidad

retirar_dinero(10, 20)

# ejemplo de Except usado como condicional

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa, a menos que seas un viajero del tiempo.")
    return True

try:
    verificar_edad(-5)
except ValueError as e:
    print(f"Atrapamos un error: {e}")
