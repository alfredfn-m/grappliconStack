from django.contrib import admin
from accounts.models import ( 
    CustomUser, 
    Tournament, 
    Champion, 
    Sex, 
    Age, 
    Rank, 
    Weight, 
    Competitor,
    )

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):

    search_fields = (
        'host__email',
        'name',
    )

    list_display = (
        'host',
        'name',
    )

    fields = (
        'host',
        'name',
        'date_of_tournament',
        'address',
        'city',
        'state_or_province',
        'nation',
    )

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    
    list_display = (
        'champion',
    )



# will need to do raw_id_fields for choices of large amounts
# this should fix problems when filtering and fixing data