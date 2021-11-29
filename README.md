# Manufacturing SPC Dashboard

## Introduction
`Dash-manufacture-spc-dashboard` is a dashboard for monitoring real-time process quality along manufacture production line. 
This is a demo of Dash interactive Python framework developed by [Plotly](https//plot.ly/).


## Built With
* [Dash](https://dash.plot.ly/) - Main server and interactive components 
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots

## Requirements
We suggest you to create a separate virtual environment running Python 3 for this app, and install all of the required dependencies there. Run in Terminal/Command Prompt:

```
git clone https://github.com/plotly/dash-sample-apps.git
cd dash-sample-apps/apps/dash-manufacture-spc-dashboard/
python3 -m virtualenv venv
```
In UNIX system: 

```
source venv/bin/activate
```
In Windows: 

```
venv\Scripts\activate
```

To install all of the required packages to this environment, simply run:

```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the app will be able to run.


## How to use this app

Run this app locally by:
```
python app.py
```
Open http://0.0.0.0:8050/ in your browser, you will see a live-updating dashboard.

## Resources and references
* [Shewhart statistical process control](https://en.wikipedia.org/wiki/Shewhart_individuals_control_chart)
* [Dash User Guide](https://dash.plot.ly/)

