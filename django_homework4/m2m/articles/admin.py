from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:

            if form.cleaned_data.get('is_main'):
                if is_main:
                    raise ValidationError('Основным может быть только один отдел')
                else:
                    is_main = True

        if not is_main:
            raise ValidationError('Укажите основной отдел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]