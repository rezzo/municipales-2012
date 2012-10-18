from django.conf.urls import patterns, include, url
from views import HomeTemplateView, ComunaOverview, ComunaIndices, MetodologiaView, QuienesSomosView, ComunaPreguntales, ReportaView,\
QuePuedoHacerHacerView, NosFaltanDatosView, Ranking
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', HomeTemplateView.as_view(template_name="home.html"), name="home"),
	

	#static pages
	url(r'^metodologia/?$', MetodologiaView.as_view(), name="metodologia"),
	url(r'^somos/?$', QuienesSomosView.as_view(), name="somos"),
	url(r'^fiscaliza/?$', ReportaView.as_view(), name="reporta"),
	url(r'^que_puedo_hacer/?$', QuePuedoHacerHacerView.as_view(), name="que_puedo_hacer"),
	url(r'^nos_faltan_datos/?$', NosFaltanDatosView.as_view(), name="nos_faltan_datos"),
	url(r'^rank/?$', Ranking.as_view(), name="ranking"),
	url(r'^ranking/?$', TemplateView.as_view(template_name="municipales2012/rank.html"), name="rank"),
	
	

	#pages depending on the comuna
	url(r'^(?P<slug>[-\w]+)/indices/?$', ComunaIndices.as_view(), name='comuna-index-detail'),
	url(r'^(?P<slug>[-\w]+)/?$', ComunaOverview.as_view(), name="comuna-overview"),
	url(r'^(?P<slug>[-\w]+)/preguntales/?$', ComunaPreguntales.as_view(), name="comuna-preguntales"),
	
	)
