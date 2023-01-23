import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div(
    style={
        'margin': 0,
        'padding': 20,
    },
    children=[

    html.H1(children='Home Page', style={'text-align': 'center'}),

    html.H3("Personal Info",style={'text-align': 'center'}),
    html.Div([
        html.Img(src=r'assets/main_pic.jpg', alt='image', height='50%', width='50%')], style={'textAlign': 'center'},
    ),
    html.P("I was raised in Pennsylvania and have worked and lived in various states across the east coast of the United States. My leisurely hobbies are traveling, weightlifting, and video games, although I'm also interested in all things technology and computers. My main goals are to live a happy and healthy life, travel as much as I possibly can, and find a career that I am passionate about!", style={'text-align': 'center'}),

    html.Br(),
    html.Br(),
    html.H3("Profession Info",style={'text-align': 'center'}),
    html.H4("Aviation Career",style={'text-align': 'center'}),
    html.P("I started my professional career by receiving an Airframe and Powerplant License as well as an Associates degree from Embry-Riddle Aeronautical University. Utilizing that education, I worked as a line technician at Avflight in Harrisburg, PA. At Harrisburg I worked mostly on regional jets as well as Ground Support Equipment, there I got my feet wet working in a high stress, fast paced environment due to the quick turnover of aircraft flying in and out of the airport. After about a year in Harrisburg I went back to Embry-Riddle to specialize in Avionics.",style={'text-align': 'center'}),
    html.P("After receiving a minor degree in Avionics Line Maintenance, I furthered my career when I got a job as an Assembly Line Inspector at Honda Aircraft Company in Greensboro, NC. I was inspecting the work done by technicians on the assembly line building the HA-420 HondaJet. I worked in almost every part of the assembly line, such as structures, installation of engines, hydraulics, and avionics systems, and performing functional tests on those systems. Therefore, I became well versed in inspecting the work done according to the engineer’s specifications. I was also involved in root cause analysis in some of the issues that arose - this helped ensure that issues were solved thoroughly instead of patched.",style={'text-align': 'center'}),
    html.P("My most recent aviation employment was an Avionics Technician at Gulfstream’s service center in Savannah, GA. I troubleshot, fixed, and performed preventative/scheduled maintenance on Gulfstream aircraft, mostly GIV’s. With the high value of the jets and the components I was dealing with, an extra level of care and consideration was put on the work being done. This high value also imposed tight schedules and requirements for the high profile customers I served. ",style={'text-align': 'center'}),
    html.P("These experiences have given me the necessary technical knowledge and skills spanning a wide range of the aviation field. Additionally, and more importantly, I’ve experienced what is required of fast-paced work with exceptionally high standards. In order to maintain peak performance at those jobs, I developed and cultivated personal and interpersonal skills for my coworkers and superiors. Despite garnering offers to continue working from each previous workplace, I left solely because the job wasn’t a great fit for me. I would gladly take their standing offers to return to any of these establishments, but I am trying to find a company that is a good match for me.",style={'text-align': 'center'}),

    html.Br(),
    html.H4("Software Experience ",style={'text-align': 'center'}),
    html.P("Although I was always interested in technology, electronics, and computers, I didn’t begin coding until a friend of mine started making video games using GameMaker Studio. He introduced me to the GameMaker Language while we were finishing his game. I put my newly-learned skills to the test by making my first game, <i>Make It Red</i> (check the projects tab for more info on some of the projects mentioned here!). It was a fun, simple project that showed me the massive capabilities of modern computing - I very quickly got hooked on programming. After finishing <i>Make It Red</i>, I began and quickly launched my second game, <i>Letter Rain</i>.",style={'text-align': 'center'}),
    html.P("After taking a short break from making games, I wanted to create more in-depth games while  expanding my coding experience. Despite GameMaker being a great tool for beginners, I saw its shortcomings with its niche language and lack of 3D development. I then transitioned to Unity, which utilizes C#. I created a few small projects, but I did not make a full production-level game.",style={'text-align': 'center'}),
    html.P("These games were certainly a fantastic milestone in my programming endeavour, however I wanted to expand my programming knowledge into the data/back-end field. After a short stint with Ruby, I moved over to Python using PyCharm (my current language of choice) and use MySQL as my database. Currently, I enjoy making small projects to test my knowledge and press the bounds of its possibilities. My preferred projects are scraping data from the web, and then running that data through algorithms.",style={'text-align': 'center'}),
    html.P("To continue furthering my programming knowledge, I am utilizing a number of Udemy Classes and YouTube tutorials. CodeWars keeps my knowledge fresh and up to date since I enjoy a good coding challenge - this includes checking how other programmers solve the same challenge. Although I strongly prefer back-end processing, I ventured to make this website using Django and Bootstrap! I enjoy the challenge programming offers and I hope to start a new career in Software Development.",style={'text-align': 'center'}),

])
