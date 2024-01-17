from django.db import models

ProdiChoices = (
    (
        "Teknik Informatika",
        "Teknik Informatika",
    ),
    (
        "Sistem Informasi",
        "Sistem Informasi",
    ),
    (
        "Manajemen",
        "Manajemen",
    ),
    (
        "Akuntansi",
        "Akuntansi",
    ),
)

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=50, unique=True, null=False, default="")
    nama = models.CharField(max_length=255)
    prodi = models.CharField(
        max_length=50, choices=ProdiChoices, default="Teknik Informatika"
    )
    kelas = models.CharField(max_length=20)
    alamat = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.nim}-{self.nama}"
