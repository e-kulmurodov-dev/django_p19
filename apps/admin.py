from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from apps.models import ContactModel


class CategoryResource(resources.ModelResource):
    class Meta:
        model = ContactModel
        fields = ("id", "name", 'email', 'phone', 'image')


@admin.register(ContactModel)
class ContactAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ['id', 'name', 'email']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

# from apps.models import Product, Category, Region, District, Film, Language, Post, Comment, Photo, Album, Todo
#
#
# class CategoryResource(resources.ModelResource):
#     class Meta:
#         model = Category
#         fields = ("id", "name")
#
#
# class FilmResource(resources.ModelResource):
#     class Meta:
#         model = Film
#         fields = (
#             'film_id', 'title', 'description', 'release_year', 'language_id', 'rental_duration', 'rental_rate',
#             'length', 'replacement_cost', 'rating', 'last_update', 'special_features', 'fulltext')
#
#
# class LanguageResource(resources.ModelResource):
#     class Meta:
#         model = Language
#         fields = ('name', 'last_update')
#
#
# class ProductsResource(resources.ModelResource):
#     category = fields.Field(
#         column_name="category_id",
#         attribute="category_id",
#         widget=ForeignKeyWidget(Category, field='id')
#     )
#
#     class Meta:
#         model = Product
#         fields = ("id", "name", "price", "description")
#
#
# class RegionResource(resources.ModelResource):
#     class Meta:
#         model = Region
#         fields = ('id', 'name')
#
#
# class DistrictResource(resources.ModelResource):
#     class Meta:
#         model = District
#
#
# @admin.register(Category)
# class CategoryAdmin(ImportExportModelAdmin):
#     resource_class = CategoryResource
#     list_display = ['name', 'last_update']
#     search_fields = ['name']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#
# @admin.register(Product)
# class ProductAdmin(ImportExportModelAdmin):
#     resource_class = ProductsResource
#     list_display = ['name']
#     search_fields = ['name', 'description']
#     autocomplete_fields = ['category']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#
# @admin.register(District)
# class DistrictAdmin(ImportExportModelAdmin):
#     resource_class = DistrictResource
#     list_display = ['name']
#     search_fields = ['name', 'region']
#     autocomplete_fields = ['region']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#
# @admin.register(Region)
# class RegionAdmin(ImportExportModelAdmin):
#     resource_class = RegionResource
#     list_display = ['name']
#     search_fields = ['name']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#
# @admin.register(Language)
# class LanguageAdmin(ImportExportModelAdmin):
#     resource_class = LanguageResource
#     list_display = ['name']
#     search_fields = ['name']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#
# @admin.register(Film)
# class FilmAdmin(ImportExportModelAdmin):
#     resource_class = FilmResource
#     list_display = ['title']
#     search_fields = ['name']
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser
#
#     def has_add_permission(self, request):
#         return request.user.is_superuser
#
#     # inlines = [FilmImageInline]
#
#
# class CommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 1
#     min_num = 1
#     max_num = 3
#
#     fields = ['name', 'email']
#
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     list_display_links = ['title']
#     search_fields = ['title']
#     inlines = [CommentAdmin]
#
#
# class PhotosStackedInline(admin.StackedInline):
#     model = Photo
#     extra = 1
#     min_num = 1
#     max_num = 3
#     fields = ['title', 'url', 'images']
#
#
# @admin.register(Album)
# class AlbumsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     list_display_links = ['id', 'title']
#     search_fields = ['title']
#     inlines = [PhotosStackedInline]
#
#
# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'completed']
#     list_display_links = ['id', 'title']
#     search_fields = ['title']
#
