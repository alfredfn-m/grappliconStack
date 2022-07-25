from django.contrib import admin
from accounts.models import ( 
    CustomUser, 
    Tournament,
    Event,
    Champion, 
    Sex, 
    Age, 
    Rank, 
    Weight, 
    Competitor,
    Round,
    Result,
    )

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        'email',
    ]

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):

    list_display = [
        'host',
        'name',
    ]

    search_fields = [
        'name',
    ]

    raw_id_fields = [
        'host',
    ]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = [
        'id',
    ]

    search_fields = [
        'tournament',
        'id',
    ]

    raw_id_fields = [
        'tournament',
    ]


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    
    list_display = [
        'champion',
    ]

    raw_id_fields = [
        'event',
    ]


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):

    model = Sex

    search_fields = [
        'event__id',
    ]

    list_display = [
        'event_id',
        'get_tournament_name',
        'sex',
    ]

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.event.tournament.name


    raw_id_fields = [
        'event',
    ]


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):

    search_fields = [
        'sex__event__id',
    ]

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'age',
        'sex',
    ]

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.sex.event.tournament.name


    raw_id_fields = [
        'sex',
    ]


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):

    search_fields = [
        'age__sex__event__id',
    ]

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'get_sex',
        'age',
        'rank',
    ]

    @admin.display(description='Sex')
    def get_sex(self,obj):
        return obj.age.sex

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.age.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.age.sex.event.tournament.name

    raw_id_fields = [
        'age',
    ]

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):

    search_fields = [
        'rank__age__sex__event__id',
    ]   

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'get_sex',
        'get_age',
        'rank',
        'weight',
    ]

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.rank.age.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.rank.age.sex.event.tournament.name

    @admin.display(description='Sex')
    def get_sex(self,obj):
        return obj.rank.age.sex

    @admin.display(description='Age')
    def get_age(self,obj):
        return obj.rank.age

    raw_id_fields = [
        'rank',
    ]

@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    search_fields = [
        'weight__rank__age__sex__event__id',
    ]

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'get_sex',
        'get_age',
        'get_rank',
        'weight',
        'competitor',
        'points',
    ]

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.weight.rank.age.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.weight.rank.age.sex.event.tournament.name

    @admin.display(description='Sex')
    def get_sex(self,obj):
        return obj.weight.rank.age.sex

    @admin.display(description='Age')
    def get_age(self,obj):
        return obj.weight.rank.age

    @admin.display(description='Rank')
    def get_rank(self,obj):
        return obj.weight.rank


    raw_id_fields = [
        'weight',
    ]

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):

    search_fields = [
        'weight__rank__age__sex__event__id',
    ]

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'get_sex',
        'get_age',
        'get_rank',
        'weight',
        'round',
    ]

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.weight.rank.age.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.weight.rank.age.sex.event.tournament.name

    @admin.display(description='Sex')
    def get_sex(self,obj):
        return obj.weight.rank.age.sex

    @admin.display(description='Age')
    def get_age(self,obj):
        return obj.weight.rank.age

    @admin.display(description='Rank')
    def get_rank(self,obj):
        return obj.weight.rank


    raw_id_fields = [
        'weight',
    ]

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    search_fields = [
        'round__weight__rank__age__sex__event__id',
    ]

    list_display = [
        'get_event_id',
        'get_tournament_name',
        'get_sex',
        'get_age',
        'get_rank',
        'get_weight',
        'round',
    ]

    @admin.display(description='Event ID')
    def get_event_id(self,obj):
        return obj.weight.rank.age.sex.event.id

    @admin.display(description='Tournament Name')
    def get_tournament_name(self,obj):
        return obj.weight.rank.age.sex.event.tournament.name

    @admin.display(description='Sex')
    def get_sex(self,obj):
        return obj.weight.rank.age.sex

    @admin.display(description='Age')
    def get_age(self,obj):
        return obj.weight.rank.age

    @admin.display(description='Rank')
    def get_rank(self,obj):
        return obj.weight.rank

    @admin.display(description='Weight')
    def get_weight(self,obj):
        return obj.round.weight

    raw_id_fields = [
        'round',
        'competitorA',
        'competitorB',
        'winner',
    ]

