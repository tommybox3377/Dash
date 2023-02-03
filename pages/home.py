import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div(
    style={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
    children=[
        html.Div([
            html.Img(src=r'assets/main_pic.jpg', alt='image', height=300, width=400)], style={'textAlign': 'center'},
        ),
        html.Br(),
        html.P(
            "Hello, my name is Tom and welcome to my site! I was raised in Pennsylvania and have worked and lived in various states across the east coast of the United States. My leisurely hobbies are traveling, weightlifting, video games, rock climbing, and chess - although I'm also interested in all things technology and computers. My main goals are to live a happy and healthy life, travel as much as I possibly can, and have a career that I am passionate about!",
            style={'text-align': 'center'}),

        html.Br(),
        html.Br(),
        html.H4("Aviation Career", style={'text-align': 'center'}),
        html.P(
            "I started my professional career by receiving an Airframe and Powerplant License as well as an Associates degree from Embry-Riddle Aeronautical University. Utilizing that education, I worked as a line technician at Avflight in Harrisburg, PA. At Harrisburg I worked mostly on regional jets as well as Ground Support Equipment, there I got my feet wet working in a high stress, fast paced environment due to the quick turnover of aircraft flying in and out of the airport. After about a year in Harrisburg I went back to Embry-Riddle to specialize in Avionics.",
            style={'text-align': 'center'}),
        html.P(
            "After receiving a minor degree in Avionics Line Maintenance, I furthered my career when I got a job as an Assembly Line Inspector at Honda Aircraft Company in Greensboro, NC. I was inspecting the work done by technicians on the assembly line building the HA-420 HondaJet. I worked in almost every part of the assembly line, such as structures, installation of engines, hydraulics, and avionics systems, and performing functional tests on those systems. Therefore, I became well versed in inspecting the work done according to the engineer’s specifications. I was also involved in root cause analysis in some of the issues that arose – with this I helped ensure that issues were solved thoroughly.",
            style={'text-align': 'center'}),
        html.P(
            "My most recent aviation employment was an Avionics Technician at Gulfstream’s service center in Savannah, GA. I troubleshot, fixed, and performed preventative/scheduled maintenance on Gulfstream aircraft, mostly GIV’s. With the high value of the jets and the components I was dealing with, an extra level of care and consideration was put on the work being done. This high value also imposed tight schedules and requirements for the high profile customers I served.",
            style={'text-align': 'center'}),
        html.P(
            "These experiences have given me the technical knowledge and skills spanning a wide range of the aviation field. Additionally, and more importantly, I’ve experienced what is required of fast-paced work with exceptionally high standards. In order to maintain peak performance at those jobs, I developed and cultivated personal and interpersonal skills for my coworkers and superiors. Despite garnering offers to continue working from each previous workplace, I left solely because the job wasn’t a great fit for me. I would gladly take their standing offers to return to any of these establishments, but I am trying to find a company and industry that is a good match for me.",
            style={'text-align': 'center'}),

        html.Br(),
        html.H4("Software Experience ", style={'text-align': 'center'}),
        html.P(
            "Although I was always interested in technology, electronics, and computers, I didn’t begin coding until a friend of mine started making video games using GameMaker Studio. He introduced me to the GameMaker Language while we were finishing his game. I put my newly-learned skills to the test by making my first game, ‘Make It Red’. It was a fun, simple project that showed me the massive capabilities of modern computing - I very quickly got hooked on programming. After finishing ‘Make It Red’, I began and quickly launched my second game, ‘Letter Rain’.",
            style={'text-align': 'center'}),
        html.P(
            "These games were certainly a fantastic milestone in my programming endeavor, however I wanted to expand my programming knowledge into the data/back-end field. After a short stint with Ruby, I moved over to Python and use MySQL as my database of Choice. Currently, I enjoy making small projects to test my knowledge and press the bounds of its possibilities. My preferred projects are scraping data from the web and running it through a data processing pipeline all the way through to algorithms.",
            style={'text-align': 'center'}),
        html.P(
            "I got my first Software job at Awato. While my primary role was a customer support technician, when all the support tickets were done I was able to help them utilize their data. Since Awato was a small start-up I got to work closely with the whole team and worked to develop member specific as well as company-wide data analytics tools. It was a great experience with a great company that helped me get practical experience with data that also helped Awato make business decisions.",
            style={'text-align': 'center'}),
        html.P(
            r"With Awato getting acquired and me wanting to further double down on data science I left Awato on good terms to start an fintech start-up with some friends. We are currently in the R&D phase which is a great learning opportunity while also providing an exciting challenge to overcome a monumental challenge.",
            style={'text-align': 'center'}),
        html.P(
            "Since most of the software I worked on is proprietary, I have made this site to showcase some of the things I have learned over the past years. It is made with Dash and manually hosted on a cloud server. From the data science side to the DevOps challenges to host and secure a cloud server. Check out the other pages to see some cool data, or the ‘contact me’ to get in touch!",
            style={'text-align': 'center'}),
        html.P("", style={'text-align': 'center'}),
    ])
