import sqlite3
 
def create_table():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
            ticket_id TEXT PRIMARY KEY,
            movie_name TEXT,
            ticket_quantity INTEGER,
            ticket_price INTEGER)''' )
    
    conn.commit()
    conn.close()
    
    def insert_Tickets():
        conn = sqlite3.connect('Reservation.db')
        cursor = conn.cursor()
        
        Tickets_data = [
            ('T1', 'Movie1', 3,50),
            ('T2', 'Movie2', 2,40),
            ('T3', 'Movie3', 4,60),
            ('T4', 'Movie4', 5,70),
            ('T5', 'Movie5', 1,65)
        ]
        
        cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id, movie_name, ticket_quantity, ticket_price) VALUES (?, ?, ?, ?)', Tickets_data)
        
        conn.commit()
        conn.close()
        
        def get_tickets():
            conn = sqlite3.connect('Reservation.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tickets')
            tickets = cursor.fetchall()
            conn.close()
            
            return tickets
        
        def update_quantity(id,reversed_quantity):
            conn = sqlite3.connect('Reservation.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE Tickets SET ticket_quantity = ticket_quantity - ? WHERE ticket_id = ?',(reversed_quantity,id))
            conn.commit()
            conn.close()
            
            create_table()
            insert_Tickets()