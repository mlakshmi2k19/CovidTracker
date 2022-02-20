from flask import Blueprint,render_template,request
from covid_india import states

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    cases={}
    state="Tamil Nadu"
    if request.method=='POST':
        state=request.form.get('state')
        r=states.getdata(state)
        cases={
            'Total':r['Total'],
            'Active':r['Active'],
            'Cured':r['Cured'],
            'Death':r['Death'],
        }
        
        
    return render_template("home.html",cases=cases,state=state)