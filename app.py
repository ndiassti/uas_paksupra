from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector

app = Flask(__name__)

# Setel kunci rahasia untuk pengelolaan sesi (dibutuhkan untuk sesi)
app.secret_key = 'kunci_rahasia_anda_di_sini'  # Pastikan ini adalah kunci yang unik dan aman

# Menghubungkan ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Ganti dengan password Anda
    database="website_db"
)

cursor = conn.cursor()

# Kredensial yang Anda tentukan sendiri
VALID_EMAIL = 'user@example.com'
VALID_PASSWORD = '123456'

# Route untuk halaman utama - menampilkan halaman login terlebih dahulu
@app.route('/')
def home():
    # Periksa apakah pengguna sudah login, jika sudah, alihkan ke halaman index
    if 'logged_in' in session:
        return redirect(url_for('index'))  # Jika sudah login, arahkan ke halaman index
    return render_template('login.html')  # Tampilkan halaman login jika belum login

# Route untuk login - menangani pengiriman formulir dan logika login
@app.route('/login', methods=['POST'])
def login():
    # Ambil data dari form
    email = request.form.get('email')
    password = request.form.get('password')

    # Cek kredensial login
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        session['logged_in'] = True  # Setel status login di sesi
        return redirect(url_for('index'))  # Arahkan ke halaman index setelah login berhasil
    else:
        # Jika login gagal, kembalikan ke halaman login dengan pesan error
        error_message = "Email atau password salah. Coba lagi."
        return render_template('login.html', error=error_message)

# Route untuk halaman index - halaman utama yang terlihat setelah login
@app.route('/index')
def index():
    # Periksa apakah pengguna sudah login, jika tidak, arahkan ke halaman login
    if 'logged_in' not in session:
        return redirect(url_for('home'))  # Jika belum login, arahkan ke halaman login

    # Ambil daftar produk dari database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    return render_template('index.html', products=products)  # Tampilkan halaman utama setelah login

# Route untuk logout - menghapus sesi login
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Hapus sesi login
    return redirect(url_for('home'))  # Arahkan kembali ke halaman login setelah logout

if __name__ == '__main__':
    app.run(port=50751, debug=True)