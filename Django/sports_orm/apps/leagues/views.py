from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"womens_leagues": League.objects.filter(name__contains="Womens'"),
		"hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"no_football_leagues": League.objects.exclude(sport="Football"),
		"conference_leagues": League.objects.filter(name__contains="Conference"),
		"atlantic_leagues": League.objects.filter(name__contains="Atlantic"),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors_teams": Team.objects.filter(team_name__contains="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"location_ordered_teams": Team.objects.all().order_by("location"),
		"name_reverse_ordered_teams": Team.objects.all().order_by("-team_name"),
		"cooper_players": Player.objects.filter(last_name="Cooper"),
		"joshua_players": Player.objects.filter(first_name="Joshua"),
		"cooper_no_joshua_players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_or_wyatt_players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
