<?php
session_start();

// Dummy data untuk login
$valid_username = "user@example.com";
$valid_password = "password123";

// Ambil data dari form
$username = $_POST['username'];
$password = $_POST['password'];

// Cek apakah email dan password sesuai
if ($username == $valid_username && $password == $valid_password) {
    // Simpan session
    $_SESSION['username'] = $username;

    // Redirect ke halaman index.html
    header('Location: index.html');
    exit();
} else {
    // Jika gagal login
    echo "Email atau password salah! <a href='login.html'>Coba lagi</a>";
}
?>
