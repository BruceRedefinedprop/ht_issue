from django.shortcuts import render
from django.utils import timezone
from issuelog.models import Issue
from .models import Roadmap
from django.contrib.auth.decorators import login_required
from chartit import DataPool, Chart

# Create your views here.
@login_required
def roadmap(request):
    # get query set for top five features
    features = Issue.objects.exclude(issue_status = "closed").filter(
        tag = "feature").order_by('-rating')[:5]
    bugs =   Issue.objects.exclude(issue_status = "closed").filter(
        tag = "bug").order_by('-rating')[:5]  
    
    roadmap = Roadmap.objects.all()    

    top_features_data = DataPool( series = 
        [{'options' : { 'source' : features},'terms' : ['title', 'rating']
        }]
        )   
        
    top_bugs_data = DataPool( series = 
        [{'options' : { 'source' : bugs},'terms' : ['title', 'rating']
        }]
        ) 
    
        
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
                   'text': 'Top 5 Features Requested'},
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
                   'text': 'Top 5 Bugs Requested'},
                'xAxis' : { 
                    'title' : {'text' : "Top Bugs"}
                },   
               'yAxis': {
                    'title': {
                       'text': 'Rating 1-Nice to Do, 5-Must Have'}}})                   
                       
                       

    return render(request, "roadmap.html" , {'roadmap': roadmap, 'issues_feature': features, 'issues_bugs': bugs, 
        'chart_list' : [cht_top_features, cht_top_bugs]})
