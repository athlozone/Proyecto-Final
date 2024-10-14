# IMPORTAR MODULO
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
import psycopg2
from matplotlib.widgets import Cursor
from psycopg2 import OperationalError

class Comunicacion:

    def __init__(self):
        self.conexion = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                user="postgres",
                password="athlozone",
                host="127.0.0.1",
                port="5432",
                database="Athlozone"
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos")
        except OperationalError as e:
            print(f"Error al conectar a la base de datos: {e}")

# --------------------------------------------- FUNCIONES BASE DE DATOS PARA LA INTERFAZ DE CONTROLAR STOCK ---------------------------------------------

    def mostrarProductos(self):
        if self.conexion is None or self.cursor is None:
            print("No hay conexión a la base de datos")
            return []

        try:
            self.cursor.execute("SELECT * FROM producto")
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []


    def agregarProductoControlarStock(self, id_producto, nombre, descripcion, precio, cantidad_stock, categoria):
        #print("AGREGANDO DESDE CONEXION")
        # AQUI SE DEBE AGREGAR EL CODIGO DE INSERT INTO EL PRODUCTO A AGREGAR A LA BASE DATOS
        #print(f"{id_producto} : {nombre} : {descripcion} : {precio} : {cantidad_stock} : {categoria}")

        try:
            # Crear la consulta SQL para insertar el nuevo producto
            sql = """
                INSERT INTO producto (id_producto, nombre, descripcion, precio, cantidad_stock, categoria)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

            # Crear una tupla con los valores a insertar
            valores = (id_producto, nombre, descripcion, precio, cantidad_stock, categoria)

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, valores)

            # Confirmar la transacción
            self.conexion.commit()

            print(
                f"Producto agregado exitosamente: {id_producto} : {nombre} : {descripcion} : {precio} : {cantidad_stock} : {categoria}")
            return True

        except psycopg2.Error as e:

            # Si ocurre un error, hacer rollback y mostrar el error
            self.conexion.rollback()
            print(f"Error al agregar el producto: {e}")
            return False


    def buscarProductoActualizarControlarStock(self, productoBuscar):

        try:
            # Crear una consulta SQL flexible que busque en todos los campos relevantes
            sql = """
                SELECT * FROM producto
                WHERE id_producto::text ILIKE %s
                OR nombre ILIKE %s
                OR precio::text ILIKE %s
                OR cantidad_stock::text ILIKE %s
                OR categoria ILIKE %s
                """

            # Preparar el valor de búsqueda para que funcione con ILIKE
            valor_busqueda = f"%{productoBuscar}%"

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, [valor_busqueda] * 5)

            # Obtener todos los resultados
            resultados = self.cursor.fetchall()

            if resultados:
                return resultados
            else:
                return []

        except psycopg2.Error as e:
            print(f"Error al buscar el producto: {e}")
            return []


    def actualizarProductoMismoId(self, id_producto, nombre, descripcion, precio, cantidad_stock, categoria):

        print(id_producto, nombre, descripcion, precio, cantidad_stock, categoria)
        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE producto SET 
                     nombre = %s, 
                     descripcion = %s, 
                     precio = %s, 
                     cantidad_stock = %s, 
                     categoria = %s 
                     WHERE id_producto = %s"""

            valores = (nombre, descripcion, precio, cantidad_stock, categoria, id_producto)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return False


    def actualizarProductoConNuevoId(self, id_original, nuevo_id, nombre, descripcion, precio, cantidad_stock, categoria):
        try:
            # Primero verificar que el ID original existe
            self.cursor.execute("SELECT id_producto FROM producto WHERE id_producto = %s", (id_original,))
            if not self.cursor.fetchone():
                print(f"Error: El ID original {id_original} no existe")
                return False

            # Verificar que el nuevo ID no exista
            self.cursor.execute("SELECT id_producto FROM producto WHERE id_producto = %s", (nuevo_id,))
            if self.cursor.fetchone():
                print(f"Error: El nuevo ID {nuevo_id} ya existe")
                return False

            try:
                # Insertar el nuevo registro
                sql_insert = """
                    INSERT INTO producto (id_producto, nombre, descripcion, precio, cantidad_stock, categoria)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                valores_insert = (nuevo_id, nombre, descripcion, precio, cantidad_stock, categoria)
                self.cursor.execute(sql_insert, valores_insert)

                # Eliminar el registro antiguo
                sql_delete = "DELETE FROM producto WHERE id_producto = %s"
                self.cursor.execute(sql_delete, (id_original,))

                # Confirmar los cambios
                self.conexion.commit()
                print(f"Actualización exitosa: ID cambiado de {id_original} a {nuevo_id}")
                return True

            except Exception as e:
                # Si hay cualquier error, deshacer los cambios
                self.conexion.rollback()
                print(f"Error durante la transacción: {e}")
                return False

        except Exception as e:
            print(f"Error en la conexión: {e}")
            return False


    def eliminarProducto(self, id_producto):
        try:
            sql = "DELETE FROM producto WHERE id_producto = %s"
            self.cursor.execute(sql, (id_producto,))
            self.conexion.commit()
            print(f"Producto con ID {id_producto} eliminado de la base de datos")
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar el producto: {e}")
            self.conexion.rollback()
            return False


# --------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------- FUNCIONES BASE DE DATOS PARA LA INTERFAZ DE GESTIONAR PROVEEDORES ---------------------------------------------

    def mostrarProveedores(self):

        if self.conexion is None or self.cursor is None:
            print("No hay conexión a la base de datos")
            return []

        try:
            self.cursor.execute("SELECT * FROM proveedores")
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []



    def agregarProveedor(self, id_proveedor, nombre, email, telefono, direccion):

        try:
            # Crear la consulta SQL para insertar el nuevo producto
            sql = """
                INSERT INTO proveedores (id_proveedor, nombre, email, telefono, direccion)
                VALUES (%s, %s, %s, %s, %s)
                """

            # Crear una tupla con los valores a insertar
            valores = (id_proveedor, nombre, email, telefono, direccion)

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, valores)

            # Confirmar la transacción
            self.conexion.commit()

            print(
                f"Producto agregado exitosamente: {id_proveedor} : {nombre} : {email} : {telefono} : {direccion}")
            return True

        except psycopg2.Error as e:

            # Si ocurre un error, hacer rollback y mostrar el error
            self.conexion.rollback()
            print(f"Error al agregar el proveedor: {e}")
            return False


    def buscarProveedorActualizar(self, proveedorBuscar):

        try:
            # Crear una consulta SQL flexible que busque en todos los campos relevantes
            sql = """
                SELECT * FROM proveedores
                WHERE id_proveedor::text ILIKE %s
                OR nombre ILIKE %s
                OR email::text ILIKE %s
                OR telefono::text ILIKE %s
                OR direccion ILIKE %s
                """

            # Preparar el valor de búsqueda para que funcione con ILIKE
            valor_busqueda = f"%{proveedorBuscar}%"

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, [valor_busqueda] * 5)

            # Obtener todos los resultados
            resultados = self.cursor.fetchall()

            if resultados:
                return resultados
            else:
                return []

        except psycopg2.Error as e:
            print(f"Error al buscar el proveedor: {e}")
            return []


    def actualizarProveedorMismoId(self, idOriginal,nombre, email, telefono, direccion):

        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE proveedores SET 
                     nombre = %s, 
                     email = %s, 
                     telefono = %s, 
                     direccion = %s 
                     WHERE id_proveedor = %s"""

            valores = (nombre, email, telefono, direccion, idOriginal)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar proveedor: {e}")
            return False


    def actualizarProveedorConNuevoId(self, id_original,nuevo_id,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion):
        try:
            # Primero verificar que el ID original existe
            self.cursor.execute("SELECT id_proveedor FROM proveedores WHERE id_proveedor = %s", (id_original,))
            if not self.cursor.fetchone():
                print(f"Error: El ID original {id_original} no existe")
                return False

            # Verificar que el nuevo ID no exista
            self.cursor.execute("SELECT id_proveedor FROM proveedores WHERE id_proveedor = %s", (nuevo_id,))
            if self.cursor.fetchone():
                print(f"Error: El nuevo ID {nuevo_id} ya existe")
                return False

            try:
                # Insertar el nuevo registro
                sql_insert = """
                    INSERT INTO proveedores (id_proveedor, nombre, email, telefono, direccion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores_insert = (nuevo_id, nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)
                self.cursor.execute(sql_insert, valores_insert)

                # Eliminar el registro antiguo
                sql_delete = "DELETE FROM proveedores WHERE id_proveedor = %s"
                self.cursor.execute(sql_delete, (id_original,))

                # Confirmar los cambios
                self.conexion.commit()
                print(f"Actualización exitosa: ID cambiado de {id_original} a {nuevo_id}")
                return True

            except Exception as e:
                # Si hay cualquier error, deshacer los cambios
                self.conexion.rollback()
                print(f"Error durante la transacción: {e}")
                return False

        except Exception as e:
            print(f"Error en la conexión: {e}")
            return False


    def eliminarProveedor(self, id_proveedor):
        try:
            sql = "DELETE FROM proveedores WHERE id_proveedor = %s"
            self.cursor.execute(sql, (id_proveedor,))
            self.conexion.commit()
            print(f"Proveedor con ID {id_proveedor} eliminado de la base de datos")
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar el proveedor: {e}")
            self.conexion.rollback()
            return False

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------- FUNCIONES BASE DE DATOS PARA LA INTERFAZ DE GESTIONAR CLIENTES -------------------------------------------

    def mostrarClientes(self):

        if self.conexion is None or self.cursor is None:
            print("No hay conexión a la base de datos")
            return []

        try:
            self.cursor.execute("SELECT * FROM clientes")
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []


    def agregarCliente(self, id_clientes, nombre, email, telefono, direccion):

        try:
            # Crear la consulta SQL para insertar el nuevo producto
            sql = """
                INSERT INTO clientes (id_clientes, nombre, email, telefono, direccion)
                VALUES (%s, %s, %s, %s, %s)
                """

            # Crear una tupla con los valores a insertar
            valores = (id_clientes, nombre, email, telefono, direccion)

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, valores)

            # Confirmar la transacción
            self.conexion.commit()

            print(
                f"cliente agregado exitosamente: {id_clientes} : {nombre} : {email} : {telefono} : {direccion}")
            return True

        except psycopg2.Error as e:

            # Si ocurre un error, hacer rollback y mostrar el error
            self.conexion.rollback()
            print(f"Error al agregar el cliente: {e}")
            return False


    def buscarClienteActualizar(self, clienteBuscar):

        try:
            # Crear una consulta SQL flexible que busque en todos los campos relevantes
            sql = """
                SELECT * FROM clientes
                WHERE id_clientes::text ILIKE %s
                OR nombre ILIKE %s
                OR email::text ILIKE %s
                OR telefono::text ILIKE %s
                OR direccion ILIKE %s
                """

            # Preparar el valor de búsqueda para que funcione con ILIKE
            valor_busqueda = f"%{clienteBuscar}%"

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, [valor_busqueda] * 5)

            # Obtener todos los resultados
            resultados = self.cursor.fetchall()

            if resultados:
                return resultados
            else:
                return []

        except psycopg2.Error as e:
            print(f"Error al buscar el cliente: {e}")
            return []


    def actualizarClienteMismoId(self, idOriginal,nombre, email, telefono, direccion):

        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE clientes SET 
                     nombre = %s, 
                     email = %s, 
                     telefono = %s, 
                     direccion = %s 
                     WHERE id_clientes = %s"""

            valores = (nombre, email, telefono, direccion, idOriginal)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False


    def actualizarClienteConNuevoId(self, id_original,nuevo_id,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion):
        try:
            # Primero verificar que el ID original existe
            self.cursor.execute("SELECT id_clientes FROM clientes WHERE id_clientes = %s", (id_original,))
            if not self.cursor.fetchone():
                print(f"Error: El ID original {id_original} no existe")
                return False

            # Verificar que el nuevo ID no exista
            self.cursor.execute("SELECT id_clientes FROM clientes WHERE id_clientes = %s", (nuevo_id,))
            if self.cursor.fetchone():
                print(f"Error: El nuevo ID {nuevo_id} ya existe")
                return False

            try:
                # Insertar el nuevo registro
                sql_insert = """
                    INSERT INTO clientes (id_clientes, nombre, email, telefono, direccion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores_insert = (nuevo_id, nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)
                self.cursor.execute(sql_insert, valores_insert)

                # Eliminar el registro antiguo
                sql_delete = "DELETE FROM clientes WHERE id_clientes = %s"
                self.cursor.execute(sql_delete, (id_original,))

                # Confirmar los cambios
                self.conexion.commit()
                print(f"Actualización exitosa: ID cambiado de {id_original} a {nuevo_id}")
                return True

            except Exception as e:
                # Si hay cualquier error, deshacer los cambios
                self.conexion.rollback()
                print(f"Error durante la transacción: {e}")
                return False

        except Exception as e:
            print(f"Error en la conexión: {e}")
            return False



    def eliminarCliente(self, id_clientes):
        try:
            sql = "DELETE FROM clientes WHERE id_clientes = %s"
            self.cursor.execute(sql, (id_clientes,))
            self.conexion.commit()
            print(f"Cliente con ID {id_clientes} eliminado de la base de datos")
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar el cliente: {e}")
            self.conexion.rollback()
            return False


# --------------------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------- FUNCIONES BASE DE DATOS PARA LA INTERFAZ DE REALIZAR VENTAS ---------------------------------------------

    def mostrarVentas(self):

        if self.conexion is None or self.cursor is None:
            print("No hay conexión a la base de datos")
            return []

        try:
            self.cursor.execute("SELECT * FROM ventas")
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []


    def agregarVenta(self, id_venta, fecha, id_clientes, total):

        try:
            # Crear la consulta SQL para insertar el nuevo producto
            sql = """ INSERT INTO ventas (id_venta, fecha, id_clientes, total) VALUES (%s, %s, %s, %s) """

            # Crear una tupla con los valores a insertar
            valores = (id_venta, fecha, id_clientes, total)

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, valores)

            # Confirmar la transacción
            self.conexion.commit()

            print(
                f"venta agregado exitosamente: {id_venta} : {fecha} : {id_clientes} : {total}")
            return True

        except psycopg2.Error as e:

            # Si ocurre un error, hacer rollback y mostrar el error
            self.conexion.rollback()
            print(f"Error al agregar la venta: {e}")
            return False


    def mostrarDetallesVentas(self, idventa):

        if self.conexion is None or self.cursor is None:
            print("No hay conexión a la base de datos")
            return []

        try:
            self.cursor.execute("SELECT * FROM detalles_venta WHERE id_venta = %s", (idventa,))
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []


    def agregarProductoVenta(self, id_venta, id_producto, cantidad, precio_unitario):

        try:
            # Crear la consulta SQL para insertar el nuevo producto
            sql = """ INSERT INTO detalles_venta (id_venta, id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s, %s) """

            # Crear una tupla con los valores a insertar
            valores = (id_venta, id_producto, cantidad, precio_unitario)

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, valores)

            # Confirmar la transacción
            self.conexion.commit()

            print(
                f"venta agregado exitosamente: {id_venta} : {id_producto} : {cantidad} : {precio_unitario}")
            return True

        except psycopg2.Error as e:

            # Si ocurre un error, hacer rollback y mostrar el error
            self.conexion.rollback()
            print(f"Error al agregar producto a la venta: {e}")
            return False


    def buscarVentaActualizar(self, ventaBuscar):

        try:
            # Crear una consulta SQL flexible que busque en todos los campos relevantes
            sql = """
                        SELECT * FROM ventas
                        WHERE id_venta::text ILIKE %s
                        OR CAST(fecha AS TEXT) ILIKE %s
                        OR id_clientes::text ILIKE %s
                        OR total::text ILIKE %s
                """

            # Preparar el valor de búsqueda para que funcione con ILIKE
            valor_busqueda = f"%{ventaBuscar}%"

            # Ejecutar la consulta SQL
            self.cursor.execute(sql, [valor_busqueda] * 4)

            # Obtener todos los resultados
            resultados = self.cursor.fetchall()

            if resultados:
                return resultados
            else:
                return []

        except psycopg2.Error as e:
            print(f"Error al buscar la venta: {e}")
            return []


    def actualizarVentaMismoId(self, idOriginal, nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total):

        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE ventas SET 
                     id_venta = %s, 
                     fecha = %s, 
                     id_clientes = %s, 
                     total = %s 
                     WHERE id_venta = %s"""

            valores = (nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total, idOriginal)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar venta: {e}")
            return False


    def actualizarVentaConNuevoId(self, idOriginal, nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total):
        try:
            # Primero verificar que el ID original existe
            self.cursor.execute("SELECT id_venta FROM ventas WHERE id_venta = %s", (idOriginal,))
            if not self.cursor.fetchone():
                print(f"Error: El ID original {idOriginal} no existe")
                return False

            # Verificar que el nuevo ID no exista
            self.cursor.execute("SELECT id_venta FROM ventas WHERE id_venta = %s", (nuevo_id,))
            if self.cursor.fetchone():
                print(f"Error: El nuevo ID {nuevo_id} ya existe")
                return False

            try:
                # Insertar el nuevo registro
                sql_insert = """
                    INSERT INTO ventas (id_venta, fecha, id_clientes, total)
                    VALUES (%s, %s, %s, %s)
                """

                valores_insert = (nuevo_id, nueva_fecha,nuevo_id_cliente,nuevo_total)
                self.cursor.execute(sql_insert, valores_insert)

                # Eliminar el registro antiguo
                sql_delete = "DELETE FROM ventas WHERE id_venta = %s"
                self.cursor.execute(sql_delete, (idOriginal,))

                # Confirmar los cambios
                self.conexion.commit()
                print(f"Actualización exitosa: ID cambiado de {idOriginal} a {nuevo_id}")
                return True

            except Exception as e:
                # Si hay cualquier error, deshacer los cambios
                self.conexion.rollback()
                print(f"Error durante la transacción: {e}")
                return False

        except Exception as e:
            print(f"Error en la conexión: {e}")
            return False


    def actualizarProductoDetalleVentaMismoId(self, idVentaOriginal,idProductoOriginal, nueva_cantidad, nuevo_precio_unitario):

        print(idVentaOriginal)
        print(idProductoOriginal)
        print(nueva_cantidad)
        print(nuevo_precio_unitario)

        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE detalles_venta SET 
                     cantidad = %s, 
                     precio_unitario = %s 
                     WHERE id_venta = %s AND id_producto = %s"""

            valores = (nueva_cantidad, nuevo_precio_unitario, idVentaOriginal, idProductoOriginal)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar producto de detalle venta: {e}")
            return False


    def actualizarVentaDespuesDeDetalles(self, id_venta, total_venta):

        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE ventas SET 
                     total = %s  WHERE id_venta = %s """

            valores = (total_venta, id_venta)
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar nuevo total de venta: {e}")
            return False


    def eliminarVenta(self, id_venta):
        try:
            sql = "DELETE FROM ventas WHERE id_venta = %s"
            self.cursor.execute(sql, (id_venta,))
            self.conexion.commit()
            print(f"Venta con ID {id_venta} eliminada de la base de datos")
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar la venta: {e}")
            self.conexion.rollback()
            return False


    def eliminarProductoVentaDetalle(self, id_venta, id_producto, cantidad, precio_unitario):

        try:
            sql = "DELETE FROM detalles_venta WHERE id_venta = %s AND id_producto = %s AND cantidad = %s AND precio_unitario = %s"
            self.cursor.execute(sql, (id_venta, id_producto, cantidad, precio_unitario,))
            self.conexion.commit()
            print(f"Producto con ID {id_venta} eliminada de la base de datos")
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar el producto: {e}")
            self.conexion.rollback()
            return False
# --------------------------------------------------------------------------------------------------------------------------------------------------------







# --------------------------------------------- FUNCIONES BASE DE DATOS PARA LA INTERFAZ DE REGISTRAR COMPRAS ---------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------







    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")

    def __del__(self):
        self.cerrar_conexion()

if __name__ == "__main__":
    conec = Comunicacion()
    #productos = conec.mostrarProductos()
    #print(productos)
    conec.cerrar_conexion()
