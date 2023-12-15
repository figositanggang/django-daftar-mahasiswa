from django.shortcuts import render, redirect
from .models import Mahasiswa
from .forms import MahasiswaCreate, MahasiswaEdit


def index(req):
    mahasiswas = Mahasiswa.objects.all()

    return render(
        req,
        "mahasiswa/index.html",
        {"mahasiswas": mahasiswas},
    )


def create(req):
    form = MahasiswaCreate

    if req.method == "POST":
        form = MahasiswaCreate(req.POST, req.FILES)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(req, "mahasiswa/create.html", {"form": form})

    else:
        return render(
            req,
            "mahasiswa/create.html",
            {"form": form},
        )


def edit(req, nim):
    nim = int(nim)

    try:
        mahasiswa = Mahasiswa.objects.get(nim=nim)
    except Mahasiswa.DoesNotExist:
        return redirect("/")

    form = MahasiswaEdit(req.POST or None, instance=mahasiswa)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(req, "mahasiswa/edit.html", {"form": form, "mahasiswa": mahasiswa})


def delete(req, nim):
    nim = int(nim)

    try:
        mahasiswa = Mahasiswa.objects.get(nim=nim)
        mahasiswa.delete()
    except Mahasiswa.DoesNotExist:
        return

    return redirect("/")
