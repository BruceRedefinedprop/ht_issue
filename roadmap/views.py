from django.shortcuts import render
from django.utils import timezone
from issuelog.models import Issue
from .models import Roadmap
from django.contrib.auth.decorators import login_required
from chartit import DataPool, Chart
from django_tables2 import RequestConfig
from .tables import RoadmapTable, TopIssuesTable


"""
roadmap view builds table data required to show the product
roadmap i.e. product release schedule, tables for top feature requests
and bug fix requests.  The tables are built using django_tables2 and 
charts are built using django-chartit.


"""
# Create your views here.
@login_required
def roadmap(request):
    # get query set for top five features
    features = Issue.objects.exclude(issue_status = "closed").filter(
        tag = "feature").order_by('-rating')[:5]
    
    bugs =   Issue.objects.exclude(issue_status = "closed").filter(
        tag = "bug").order_by('-rating')[:5]  
    
    # retrieve roadmap data
    roadmap = Roadmap.objects.all()    
    
    #instantiate table
    roadmap_table = RoadmapTable(roadmap)
    RequestConfig(request).configure(roadmap_table)

    # create Data objects for the charts
    top_features_data = DataPool( series = 
        [{'options' : { 'source' : features},'terms' : ['title', 'rating']
        }]
        )   
        
    top_bugs_data = DataPool( series = 
        [{'options' : { 'source' : bugs},'terms' : ['title', 'rating']
        }]
        ) 
    
    # define chart options. We are creating charts.    
    cht_top_features = Chart(
            datasource = top_features_data,
            series_options =
              [{'options':{
                  'type': 'bar'},
                'terms':{
                  'title': [
                    'rating']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Top Five Features Requested'},
                'xAxis' : { 
                    'title' : {'text' : "Top Features"}
                },   
               'yAxis': {
                    'title': {
                       'text': 'Rating 1-Nice to Do, 5-Must Have'}}})
                       
    cht_top_bugs = Chart(
            datasource = top_bugs_data,
            series_options =
              [{'options':{
                  'type': 'bar'},
                'terms':{
                  'title': [
                    'rating']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Top Five Bugs Fixes Requested'},
                'xAxis' : { 
                    'title' : {'text' : "Top Bugs"}
                },   
               'yAxis': {
                    'title': {
                       'text': 'Rating 1-Nice to Do, 5-Must Have'}}})                   
                       
                       

    return render(request, "roadmap.html" , {'roadmap_table': roadmap_table, 'issues_feature': features, 'issues_bugs': bugs, 'chart_list' : [cht_top_features, cht_top_bugs]})
