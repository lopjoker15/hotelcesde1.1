class PagoRepository:
    def create_pago(self, db, pago):
        query = """
            INSERT INTO pagos (id_cliente, monto, metodo_pago, fecha)
            VALUES (%s, %s, %s, %s)
        """
        values = (pago.id_cliente, pago.monto, pago.metodo_pago, pago.fecha)
        db.execute_query(query, values)
