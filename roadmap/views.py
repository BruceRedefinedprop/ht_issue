from django.shortcuts import render
from django.utils import timezone
from issuelog.models import Post
from django.contrib.auth.decorators import login_required
from chartit import DataPool, Chart

# Create your views here.
@login_required
def roadmap(request):
    # get query set for top five features
    features = Post.objects.exclude(post_status = "closed").filter(
        tag = "feature").order_by('-rating')[:5]
    bugs =   Post.objects.exclude(post_status = "closed").filter(
        tag = "bug").order_by('-rating')[:5]  
        
        
    top_features_data = DataPool( series = 
        [{'options' : { 'source' : features},'terms' : ['title', 'rating']
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

    return render(request, "roadmap.html" , {'posts_feature': features, 'post_bugs': bugs, 
        'top_features_data' : cht_top_features})
