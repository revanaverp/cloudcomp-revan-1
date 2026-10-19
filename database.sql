-- Buat Tabel User
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL
);

-- Insert Data Awal (Dummy Data)
INSERT INTO user (username, password) VALUES ('fakhriizzulhaq', 'password123');
INSERT INTO user (username, password) VALUES ('asprak_kompus', 'asprak2026');
INSERT INTO user (username, password) VALUES ('budi_santoso', 'budi123');
INSERT INTO user (username, password) VALUES ('caca_marica', 'caca456');
INSERT INTO user (username, password) VALUES ('dewi_lestari', 'dewi789');
