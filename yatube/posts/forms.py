# from django import forms
# from django.utils.translation import gettextlazy as _
#
# from .models import Comment, Post
#
#
# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('text', 'group', 'image')
#         labels = {
#             'text': ('Текст записи'),
#             'group': ('Группа'),
#         }
#         helptexts = {
#             'text': ('Текст новой записи'),
#             'group': _('Группа, к которой будет относиться запись'),
#         }