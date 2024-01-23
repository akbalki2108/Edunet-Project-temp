from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px


from .forms import SearchForm

df = {}
# Create your views here.
def notebook():
    global df
    df = pd.read_csv("zomato_cleaned.csv")

    


def home(request):
    notebook()
    df.head()
    data_dict={
        'fname':'aditya',
        'lname':'balki',
        'num_list':"asd"
    }
    return  render(request,'home.html',{'data_dict':data_dict})


def about(request):
    return  render(request,'about.html')


def dashboard(request):
    train_data = pd.read_csv("zomato_cleaned.csv")

    tRestaurant = train_data.shape[0]

    average_rating = train_data['rate'].mean()
    average_rating = round(average_rating, 2)

    most_voted_restaurant = train_data.loc[train_data['votes'].idxmax()]['name']

    average_cost_for_two = train_data['cost2plates'].mean()
    average_cost_for_two = round(average_cost_for_two, 2)

    area_distribution = train_data['area'].value_counts()

    online_order_counts = train_data['online_order'].value_counts()

    table_booking_counts = train_data['book_table'].value_counts()

    top_Restaurant_type = train_data['rest_type'].value_counts()

    top_cuisines = train_data['cuisines'].value_counts()

    top_listed_in_type = train_data['listed_in_type'].value_counts()

    listed_in_type_distribution = train_data['listed_in_type'].value_counts()
    df_listed_in_type_distribution = dict()
    labels = []
    data = []

    for element, count in listed_in_type_distribution.items():
        labels.append(element)
        data.append(count)

    df_listed_in_type_distribution["labels"] = labels
    df_listed_in_type_distribution["data"] = data


    fig = px.scatter(train_data, x='cost2plates', y='rate', title='Scatter Plot of Cost vs. Rating')
    graph = fig.to_html(full_html=False)

    # fig2 = px.scatter(train_data, x='location', y='rate', title='Average Rating by Location')
    # graph2 = fig2.to_html(full_html=False)

    fig2 = px.bar(train_data, 
              x='location', 
              y='rate', 
              title='Average Rating by Location', 
              labels={'rate': 'Average Rating'},
              color='location',
              color_discrete_sequence= px.colors.qualitative.Dark24,
              opacity=1,)
    

    # Convert the plot to HTML
    graph2 = fig2.to_html(full_html=False)

    value={
        'tRestaurant' : tRestaurant,
        'average_rating': average_rating,
        'most_voted_restaurant':most_voted_restaurant,
        'average_cost_for_two':average_cost_for_two,
        'topRestaurant':area_distribution.index[0],
        'online_order_counts':online_order_counts["Yes"],
        'table_booking_counts':table_booking_counts["Yes"],
        'top_Restaurant_type':top_Restaurant_type.index[0],
        'top_cuisines':top_cuisines.index[0],
        'top_listed_in_type':top_listed_in_type.index[0],
        'listed_in_type_distribution':df_listed_in_type_distribution,
        'graph':graph,
        'graph2':graph2,


    }
    return  render(request,'dashboard.html',{'value':value})

def load_data(request):
    df = pd.read_csv("zomato_cleaned.csv")
    print(df.head())
    
    for i in df.index:
    
        obj = Zomato(
                name=df['name'][i],
                online_order=df['online_order'][i],
                book_table=df['book_table'][i],
                rate=df['rate'][i],
                votes=df['votes'][i],
                location=df['location'][i],
                rest_type=df['rest_type'][i],
                cuisines=df['cuisines'][i],
                cost2plates=df['cost2plates'][i],
                listed_in_type=df['listed_in_type'][i],
                area=df['area'][i],
        )
        obj.save()
    
    return HttpResponse("data loaded")


def filter_data(request):
    df = pd.read_csv("zomato_cleaned.csv")

    form = SearchForm(request.POST or None)
    result = None

    if request.method == 'POST' and form.is_valid():
        search_query = form.cleaned_data['search_query']
        
        rate = form.cleaned_data['rate']
        rate = int(rate)

        print(search_query)
        print(rate)
        
        query_string = f''
        if search_query and rate:
            query_string = f'location == "{search_query}" and rate >= {rate} and rate < {rate + 1}'
            result = df.query(query_string)
        elif search_query:
            query_string = f'location == "{search_query}"'
            result = df.query(query_string)
        elif rate:
            query_string = f'rate <= {rate} and rate > {rate-1}'
            result = df.query(query_string)
        else:
            # Handle the case where neither search_query nor rate is provided
            result = df.copy()

    col = df.columns.tolist()
    result_dict = result.to_dict(orient='records') if result is not None else []

    context = {'result': result_dict, 'columns': col, 'form': form}
    return render(request, 'filter.html', context)


# form = SearchForm(request.POST or None)
#     result = None

#     if request.method == 'POST' and form.is_valid():
#         search_query = form.cleaned_data['search_query']
#         # Apply the search criteria to your DataFrame
        
    
#     result = df.query('location == "BTM"')
#     col = df.columns.tolist()
#     result_dict = result.to_dict(orient='records')
#     context = {'result': result_dict,'columns':col}

#     return render(request,'filter.html',context)


