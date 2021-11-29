from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        counter_dict = dict()
        for form in self.forms:

            if form.cleaned_data.get('is_main'):
                counter_dict['true'] = counter_dict.get('true', 0) + 1

        if counter_dict.get('true') is None:
            raise ValidationError('Укажите основной отдел')

        if counter_dict.get('true') > 1:
            raise ValidationError('Основным может быть только один отдел')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    extra = 0
