from django.db import models


class Mahasiswa(models.Model):
    class Prodi(models.TextChoices):
        TI = (
            "Teknik Informatika",
            "Teknik Informatika",
        )
        SI = (
            "Sistem Informasi",
            "Sistem Informasi",
        )
        MA = (
            "Manajemen",
            "Manajemen",
        )
        AK = (
            "Akuntansi",
            "Akuntansi",
        )

    nim = models.CharField(max_length=50, unique=True, null=False, default="")
    nama = models.CharField(max_length=255)
    prodi = models.CharField(max_length=50, choices=Prodi, default=Prodi.TI)
    kelas = models.CharField(max_length=20)
    alamat = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.nim}-{self.nama}"
