from django.contrib import admin
from blog.models import KategoriModel
from blog.models.iletisim import IletisimModel
from blog.models.yazi import YazilarModel
from blog.models.yorum import YorumModel

admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik', 'icerik')
    list_display =( 
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )
@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display=('yazan', 'olusturulma_tarihi','duzenlenme_tarihi')
    search_fields=('yazan__username',)
@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display=('email',)
    search_fields=('email',)
