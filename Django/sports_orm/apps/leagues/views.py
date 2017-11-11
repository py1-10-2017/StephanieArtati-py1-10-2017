from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):

	baseball_conference_players = []
	for team in League.objects.get(name="International Collegiate Baseball Conference").teams.all():
		for player in team.curr_players.all():
			baseball_conference_players.append(player)

	amateur_football_conference_lopez_players = []
	for team in League.objects.get(name="American Conference of Amateur Football").teams.all():
		for player in team.curr_players.all():
			if player.last_name == "Lopez":
				amateur_football_conference_lopez_players.append(player)

	all_football_players = []
	for league in League.objects.filter(sport="Football"):
		for team in	league.teams.all():
			for player in team.all_players.all():
				all_football_players.append(player)

	teams_with_sophia = []
	for player in Player.objects.filter(first_name="Sophia"):
		if player.curr_team not in teams_with_sophia: #in case we have multiple sophias in the same team
			teams_with_sophia.append(player.curr_team)

	leagues_with_sophia = []
	for player in Player.objects.filter(first_name="Sophia"):
		leagues_with_sophia.append(player.curr_team.league)

	flores_exclude_washington_roughriders = []
	for player in Player.objects.filter(last_name="Flores"):
		if player.curr_team.team_name != "Roughriders" and player.curr_team.location != "Washington":
			flores_exclude_washington_roughriders.append(player)

	former_wichita_vikings_players = []
	curr_wichita_vikings_players = Team.objects.get(team_name="Vikings", location="Wichita").curr_players.all()
	for player in Team.objects.get(team_name="Vikings", location="Wichita").all_players.all():
		if player not in curr_wichita_vikings_players:
			former_wichita_vikings_players.append(player)

	context = {
		"former_wichita_vikings_players": former_wichita_vikings_players,
		"manitoba_tiger_cats_players": Team.objects.get(team_name="Tiger-Cats", location="Manitoba").all_players.all(),
		"samuel_evans_teams": Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all(),
		"flores_exclude_washington_roughriders": flores_exclude_washington_roughriders,
		"leagues_with_sophia": leagues_with_sophia,
		"teams_with_sophia": teams_with_sophia,
		"all_football_players": all_football_players,
		"amateur_football_conference_lopez_players": amateur_football_conference_lopez_players,
		"baseball_conference_players": baseball_conference_players,
		"boston_penguin_curr_players": Team.objects.get(team_name="Penguins", location="Boston").curr_players.all(),
		"teams_in_atlantic_soccer_conference": League.objects.get(name="Atlantic Soccer Conference").teams.all(),
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
