import csv

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search_by_key(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def search_by_value(self, value):
        for bucket in self.table:
            for k, v in bucket:
                if v == value:
                    return k
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                for k, v in bucket:
                    print(f"Hash: {i} Key: {k} Value: {v}")



# Ejemplo práctico
if __name__ == "__main__":
    ht = HashTable(size=20)  # Aumentamos el tamaño para reducir colisiones

    # Inserción manual
    ht.insert("SKU235698", "Carne_Res_Libra")
    ht.insert("SKU44588", "Carton_Huevos_Granjazul_30und")
    ht.insert("SKU458522", "Bebida_energizante_Monster_500ml")

    # Mostrar contenido de la tabla hash
    print("Productos dentro de la base de datos:")
    ht.display()

    # Búsqueda por clave
    print("\nBúsqueda por clave 'SKU235698':")
    print(ht.search_by_key("SKU235698"))

    # Búsqueda por valor
    print("\nBúsqueda por valor 'Bebida_energizante_Monster_500ml")
    print(ht.search_by_value("Bebida_energizante_Monster_500ml"))

