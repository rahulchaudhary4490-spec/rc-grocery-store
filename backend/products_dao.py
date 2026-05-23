from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    try:
        query = ("INSERT INTO products "
                 "(name, uom_id, price_per_unit) "
                 "VALUES (%s, %s, %s)")
        data = (product['product_name'], product['uom_id'], float(product['price_per_unit']))
        cursor.execute(query, data)
        connection.commit()
        # PostgreSQL doesn't support lastrowid, use RETURNING instead
        cursor.execute("SELECT lastval()")
        product_id = cursor.fetchone()[0]
        return product_id
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()

def delete_product(connection, product_id):
    cursor = connection.cursor()
    try:
        query = ("DELETE FROM products where product_id=" + str(product_id))
        cursor.execute(query)
        connection.commit()
        return product_id
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))