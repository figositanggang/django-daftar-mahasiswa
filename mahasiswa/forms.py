from django import forms
from django.forms import NumberInput, TextInput, Select
from .models import Mahasiswa

class MahasiswaCreate(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = "__all__"
        widgets = {
            "nim": NumberInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "NIM",
                },
            ),
            "nama": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Nama",
                },
            ),
            "prodi": Select(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Prodi",
                },
            ),
            "kelas": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Kelas",
                },
            ),
            "alamat": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Alamat",
                },
            ),
        }

class MahasiswaEdit(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ["nama", "prodi", "kelas", "alamat"]
        widgets = {
            "nama": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Nama",
                },
            ),
            "prodi": Select(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Prodi",
                },
            ),
            "kelas": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Kelas",
                },
            ),
            "alamat": TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-1/2",
                    "placeholder": "Alamat",
                },
            ),
        }
