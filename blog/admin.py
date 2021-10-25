from django.contrib import admin
from blog.models import KategoriModel
from blog.models.iletisim import IletisimModel
from blog.models.yazi import YazilarModel
from blog.models.yorum import YorumModel
from blog.models.iletisim import IletisimModel

admin.site.register(KategoriModel)


class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik', 'icerik')
    list_display =( 
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )
admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display=('yazan', 'olusturulma_tarihi','guncellenme_tarihi')
    search_fields=('yazan__username',)


admin.site.register(YorumModel, YorumAdmin)

class IletisimAdmin(admin.ModelAdmin):
    list_display=('email',)
    search_fields=('email',)

admin.site.register(IletisimModel, IletisimAdmin)