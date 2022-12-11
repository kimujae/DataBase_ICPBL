from django import forms
from .models import Board, Reply


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["subject", "content", "category"]
        labels = {
            "subject": "제목",
            "content": "내용",
            "category": "카테고리",
        }

class PhotoForm(forms.Form):
    class Meta:

        fields = ["Photo"]
        labels = {
            "Photo": "사진",
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]
        labels = {
            "content": "내용",
        }

