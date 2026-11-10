from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import NoteSerializer
from .models import Note

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer