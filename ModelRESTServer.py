import tensorflow
tensorflow.logging.set_verbosity(tensorflow.logging.ERROR)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'


from flask import Flask, request, jsonify # loading in Flask
from flask_cors import CORS
from ludwig.api import LudwigModel # loading in Ludwig
import pandas as pd # loading pandas for reading csv
from DbMapper import DbMapper

def doPrediction(gender,
    country,
    self_employed,
    family_history,
    no_employees,
    remote_work,
    tech_company,
    benefits,
    care_options,
    wellness_program,
    seek_help,
    anonymity,
    leave,
    mental_health_consequence,
    phys_health_consequence,
    coworkers,
    supervisor,
    mental_health_interview,
    phys_health_interview,
    mental_vs_physical,
    obs_consequence,
    age_range):
    data = [
    gender,
    country,
    self_employed,
    family_history,
    no_employees,
    remote_work,
    tech_company,
    benefits,
    care_options,
    wellness_program,
    seek_help,
    anonymity,
    leave,
    mental_health_consequence,
    phys_health_consequence,
    coworkers,
    supervisor,
    mental_health_interview,
    phys_health_interview,
    mental_vs_physical,
    obs_consequence,
    age_range
	]
    # data = ['male', 'United States', 'No', 'Yes', '6-25', 'Yes', 'Yes', 'Yes', 'Yes', 'No', "Don't know", 'Yes', 'Somewhat easy', 'No', 'No', 'Yes', 'Yes', 
    #         'Maybe', 'Maybe', "Don't know", 'No', '21-30']
    cols = [
	'Gender',
    'Country',
    'self_employed',
    'family_history',
    'no_employees',
    'remote_work',
    'tech_company',
    'benefits',
    'care_options',
    'wellness_program',
    'seek_help',
    'anonymity',
    'leave',
    'mental_health_consequence',
    'phys_health_consequence',
    'coworkers',
    'supervisor',
    'mental_health_interview',
    'phys_health_interview',
    'mental_vs_physical',
    'obs_consequence',
    'age_range'
	]
    print('Data: ', data)
    df = pd.DataFrame([data], columns=cols)
    # making predictions
    pred = model.predict(data_df=df)
    return pred

def maxVal(h):
    k = None
    m = 0
    for key in h:
        if m < int(h[key]):
            m = int(h[key])
            k = key
    return k

def createHash(h, val):
    if val in h:
        h[val] += 1
    else:
        h[val] = 1
    return h

# creating a Flask application
app = Flask(__name__)
CORS(app)

# Load the model
model = LudwigModel.load('results/experiment_run_0/model')

# creating predict url and only allowing post requests.
@app.route('/predict_treatment', methods=['GET'])
def predict():
    # Get data from Post request
    gender = request.args.get('gender')
    country = request.args.get('country')
    self_employed = request.args.get('self_employed')
    family_history = request.args.get('family_history')
    no_employees = request.args.get('no_employees')
    remote_work = request.args.get('remote_work')
    tech_company = request.args.get('tech_company')
    benefits = request.args.get('benefits')
    care_options = request.args.get('care_options')
    wellness_program = request.args.get('wellness_program')
    seek_help = request.args.get('seek_help')
    anonymity = request.args.get('anonymity')
    leave = request.args.get('leave')
    mental_health_consequence = request.args.get('mental_health_consequence')
    phys_health_consequence = request.args.get('phys_health_consequence')
    coworkers = request.args.get('coworkers')
    supervisor = request.args.get('supervisor')
    mental_health_interview = request.args.get('mental_health_interview')
    phys_health_interview = request.args.get('phys_health_interview')
    mental_vs_physical = request.args.get('mental_vs_physical')
    obs_consequence = request.args.get('obs_consequence')
    age_range = request.args.get('age_range')
    # Make prediction
    data = [
    gender,
    country,
    self_employed,
    family_history,
    no_employees,
    remote_work,
    tech_company,
    benefits,
    care_options,
    wellness_program,
    seek_help,
    anonymity,
    leave,
    mental_health_consequence,
    phys_health_consequence,
    coworkers,
    supervisor,
    mental_health_interview,
    phys_health_interview,
    mental_vs_physical,
    obs_consequence,
    age_range
	]
    # data = ['male', 'United States', 'No', 'Yes', '6-25', 'Yes', 'Yes', 'Yes', 'Yes', 'No', "Don't know", 'Yes', 'Somewhat easy', 'No', 'No', 'Yes', 'Yes', 
    #         'Maybe', 'Maybe', "Don't know", 'No', '21-30']
    cols = [
	'Gender',
    'Country',
    'self_employed',
    'family_history',
    'no_employees',
    'remote_work',
    'tech_company',
    'benefits',
    'care_options',
    'wellness_program',
    'seek_help',
    'anonymity',
    'leave',
    'mental_health_consequence',
    'phys_health_consequence',
    'coworkers',
    'supervisor',
    'mental_health_interview',
    'phys_health_interview',
    'mental_vs_physical',
    'obs_consequence',
    'age_range'
	]
    print('Data: ', data)
    df = pd.DataFrame([data], columns=cols)
    # making predictions
    pred = model.predict(data_df=df)
    print(pred['treatment_predictions'][0])
    # returning the predictions as json
    return jsonify(pred['treatment_predictions'][0])

# creating predict url and only allowing post requests.
@app.route('/predict_mental_health_index', methods=['GET'])
def predict_mental_health_index():
    # Get data from Post request
    gender = request.args.get('gender')
    country = request.args.get('country')
    self_employed = request.args.get('self_employed')
    family_history = request.args.get('family_history')
    no_employees = request.args.get('no_employees')
    remote_work = request.args.get('remote_work')
    tech_company = request.args.get('tech_company')
    benefits = request.args.get('benefits')
    care_options = request.args.get('care_options')
    wellness_program = request.args.get('wellness_program')
    seek_help = request.args.get('seek_help')
    anonymity = request.args.get('anonymity')
    leave = request.args.get('leave')
    mental_health_consequence = request.args.get('mental_health_consequence')
    phys_health_consequence = request.args.get('phys_health_consequence')
    coworkers = request.args.get('coworkers')
    supervisor = request.args.get('supervisor')
    mental_health_interview = request.args.get('mental_health_interview')
    phys_health_interview = request.args.get('phys_health_interview')
    mental_vs_physical = request.args.get('mental_vs_physical')
    obs_consequence = request.args.get('obs_consequence')
    age_range = request.args.get('age_range')
    # Make prediction
    pred = doPrediction(gender, country, self_employed, family_history, no_employees, remote_work,
                        tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave,
                        mental_health_consequence, phys_health_consequence, coworkers, supervisor,
                        mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence, age_range)
    print(pred['treatment_probability'][0])
    # returning the predictions as json
    return jsonify(pred['treatment_probability'][0] * 100)

@app.route('/avg_mental_health_index', methods=['GET'])
def avg_mental_health_index():
    db = None

    with open("Db.csv", "r") as tf:
        first = True

        nYesCount = 0
        nCount = 0

        for line in tf:
            if first:
                first = False
                content = line
                db = DbMapper(line)
            else:
                content = db.getValue(line, 'treatment')

                if content is not None and content.lower().strip() == 'yes':
                    nYesCount += 1
                nCount += 1

        res = {}
        res['yes_no'] = str(int(nYesCount * 10000 / nCount) / 100)
        res['avg_mental_index'] = str(59.62)

        print(res)
        return jsonify(res)

@app.route('/age_range_hash', methods=['GET'])
def age_range_hash():
    db = None

    with open("Db.csv", "r") as tf:
        first = True

        ageRangeHash = {}
        nCount = 0

        for line in tf:
            if first:
                first = False
                content = line
                db = DbMapper(line)
            else:
                content = db.getValue(line, 'age_range')

                if content is not None:
                    if content.strip() not in ageRangeHash:
                        ageRangeHash[content.strip()]  = 0
                    
                    ageRangeHash[content.strip()] += 1

                    nCount += 1
        
        ageRangeHash['count'] = nCount

        return jsonify(ageRangeHash)


@app.route('/gender_wise_treatment', methods=['GET'])
def gender_wise_treatment():
    db = None

    with open("Db.csv", "r") as tf:
        first = True

        result = {}
        nCount = 0

        for line in tf:
            if first:
                first = False
                db = DbMapper(line)
            else:
                treatment = db.getValue(line, 'treatment')
                gender = db.getValue(line, 'gender')

                if treatment is not None and gender is not None:
                    if gender.lower().strip() not in result:
                        result[gender.lower().strip()] = {'yes': 0, 'no': 0}

                    result[gender.lower().strip()][treatment.strip().lower()] += 1

                    nCount += 1

        result['count'] = nCount

        return jsonify(result)


@app.route('/add_new_row_to_db', methods=['GET'])
def add_new_row_to_db():
    maxSno = 0
    ageSum = 0

    nCount = 0

    genderM = {}
    countryM = {}
    self_employedM = {}
    family_historyM = {}
    treatmentM = {}
    work_interfereM = {}
    no_employeesM = {}
    remote_workM = {}
    tech_companyM = {}
    benefitsM = {}
    care_optionsM = {}
    wellness_programM = {}
    seek_helpM = {}
    anonymityM = {}
    leaveM = {}
    mental_health_consequenceM = {}
    phys_health_consequenceM = {}
    coworkersM = {}
    supervisorM = {}
    mental_health_interviewM = {}
    phys_health_interviewM = {}
    mental_vs_physicalM = {}
    obs_consequenceM = {}
    age_rangeM = {}

    with open("Db.csv", "r") as tf:
        first = True
        for line in tf:
            if first:
                first = False
            else:
                sno, age, gender, country, self_employed, family_history, treatment, work_interfere, no_employees, remote_work, tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave, mental_health_consequence, phys_health_consequence, coworkers, supervisor, mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence, age_range = line.split(',')

                age_range = age_range.strip()

                maxSno = max(int(maxSno), int(sno))
                ageSum += int(age)

                nCount += 1

                genderM = createHash(genderM, gender)
                countryM = createHash(countryM, country)
                self_employedM = createHash(self_employedM, self_employed)
                family_historyM = createHash(family_historyM, family_history)
                treatmentM = createHash(treatmentM, treatment)
                work_interfereM = createHash(work_interfereM, work_interfere)
                no_employeesM = createHash(no_employeesM, no_employees)
                remote_workM = createHash(remote_workM, remote_work)
                tech_companyM = createHash(tech_companyM, tech_company)
                benefitsM = createHash(benefitsM, benefits)
                care_optionsM = createHash(care_optionsM, care_options)
                wellness_programM = createHash(wellness_programM, wellness_program)
                seek_helpM = createHash(seek_helpM, seek_help)
                anonymityM = createHash(anonymityM, anonymity)
                leaveM = createHash(leaveM, leave)
                mental_health_consequenceM = createHash(mental_health_consequenceM, mental_health_consequence)
                phys_health_consequenceM = createHash(phys_health_consequenceM, phys_health_consequence)
                coworkersM = createHash(coworkersM, coworkers)
                supervisorM = createHash(supervisorM, supervisor)
                mental_health_interviewM = createHash(mental_health_interviewM, mental_health_interview)
                phys_health_interviewM = createHash(phys_health_interviewM, phys_health_interview)
                mental_vs_physicalM = createHash(mental_vs_physicalM, mental_vs_physical)
                obs_consequenceM = createHash(obs_consequenceM, obs_consequence)
                age_rangeM = createHash(age_rangeM, age_range)

            

    sno = maxSno + 1
    age = ageSum // nCount
    gender = maxVal(genderM)
    country = maxVal(countryM)
    self_employed = maxVal(self_employedM)
    family_history = maxVal(family_historyM)
    treatment = maxVal(treatmentM)
    work_interfere = maxVal(work_interfereM)
    no_employees = maxVal(no_employeesM)
    remote_work = maxVal(remote_workM)
    tech_company = maxVal(tech_companyM)
    benefits = maxVal(benefitsM)
    care_options = maxVal(care_optionsM)
    wellness_program = maxVal(wellness_programM)
    seek_help = maxVal(seek_helpM)
    anonymity = maxVal(anonymityM)
    leave = maxVal(leaveM)
    mental_health_consequence = maxVal(mental_health_consequenceM)
    phys_health_consequence = maxVal(phys_health_consequenceM)
    coworkers = maxVal(coworkersM)
    supervisor = maxVal(supervisorM)
    mental_health_interview = maxVal(mental_health_interviewM)
    phys_health_interview = maxVal(phys_health_consequenceM)
    mental_vs_physical = maxVal(mental_vs_physicalM)
    obs_consequence = maxVal(obs_consequenceM)
    age_range = maxVal(age_rangeM)

    


    sno = request.args.get('sno') if request.args.get('sno') is not None else sno
    age = request.args.get('age') if request.args.get('age') is not None else age
    gender = request.args.get('gender') if request.args.get('gender') is not None else gender
    country = request.args.get('country') if request.args.get('country') is not None else country
    self_employed = request.args.get('self_employed') if request.args.get('self_employed') is not None else self_employed
    family_history = request.args.get('family_history') if request.args.get('family_history') is not None else family_history
    treatment = request.args.get('treatment') if request.args.get('treatment') is not None else treatment
    work_interfere = request.args.get('work_interfere') if request.args.get('work_interfere') is not None else work_interfere
    no_employees = request.args.get('no_employees') if request.args.get('no_employees') is not None else no_employees
    remote_work = request.args.get('remote_work') if request.args.get('remote_work') is not None else remote_work
    benefits = request.args.get('benefits') if request.args.get('benefits') is not None else benefits
    care_options = request.args.get('care_options') if request.args.get('care_options') is not None else care_options
    wellness_program = request.args.get('wellness_program') if request.args.get('wellness_program') is not None else wellness_program
    seek_help = request.args.get('seek_help') if request.args.get('seek_help') is not None else seek_help
    anonymity = request.args.get('anonymity') if request.args.get('anonymity') is not None else anonymity
    leave = request.args.get('leave') if request.args.get('leave') is not None else leave
    mental_health_consequence = request.args.get('mental_health_consequence') if request.args.get('mental_health_consequence') is not None else mental_health_consequence
    phys_health_consequence = request.args.get('phys_health_consequence') if request.args.get('phys_health_consequence') is not None else phys_health_consequence
    coworkers = request.args.get('coworkers') if request.args.get('coworkers') is not None else coworkers
    supervisor = request.args.get('supervisor') if request.args.get('supervisor') is not None else supervisor
    mental_health_interview = request.args.get('mental_health_interview') if request.args.get('mental_health_interview') is not None else mental_health_interview
    phys_health_interview = request.args.get('phys_health_interview') if request.args.get('phys_health_interview') is not None else phys_health_interview
    mental_vs_physical = request.args.get('mental_vs_physical') if request.args.get('mental_vs_physical') is not None else mental_vs_physical
    obs_consequence = request.args.get('obs_consequence') if request.args.get('obs_consequence') is not None else obs_consequence
    age_range = request.args.get('age_range') if request.args.get('age_range') is not None else age_range

    print(
        sno,
        age,
        gender,
        country,
        self_employed,
        family_history,
        treatment,
        work_interfere,
        no_employees,
        remote_work,
        tech_company,
        benefits,
        care_options,
        wellness_program,
        seek_help,
        anonymity,
        leave,
        mental_health_consequence,
        phys_health_consequence,
        coworkers,
        supervisor,
        mental_health_interview,
        phys_health_interview,
        mental_vs_physical,
        obs_consequence,
        age_range
    )

    with open("Db.csv", "a") as db:
        db.write(str(sno) + "," + 
            str(age) + "," + 
            gender + "," + 
            country + "," + 
            self_employed + "," + 
            family_history + "," + 
            treatment + "," + 
            work_interfere + "," + 
            no_employees + "," + 
            remote_work + "," + 
            tech_company + "," + 
            benefits + "," + 
            care_options + "," + 
            wellness_program + "," + 
            seek_help + "," + 
            anonymity + "," + 
            leave + "," + 
            mental_health_consequence + "," + 
            phys_health_consequence + "," + 
            coworkers + "," + 
            supervisor + "," + 
            mental_health_interview + "," + 
            phys_health_interview + "," + 
            mental_vs_physical + "," + 
            obs_consequence + "," + 
            age_range + "\n")

    pred = doPrediction(gender, country, self_employed, family_history, no_employees, remote_work,
                    tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave,
                    mental_health_consequence, phys_health_consequence, coworkers, supervisor,
                    mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence, age_range)

    res = {}
    res['sno'] = str(sno)
    res['treatment'] = pred['treatment_predictions'][0]
    res['mental_index'] = str(int(pred['treatment_probability'][0] * 10000) / 100)

    return res

@app.route('/search_with_sno', methods=['GET'])
def search_with_sno():
    snoQ = request.args.get('sno')

    with open("Db.csv", "r") as tf:
        first = True
        for line in tf:
            if first:
                first = False
            else:
                sno, age, gender, country, self_employed, family_history, treatment, work_interfere, no_employees, remote_work, tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave, mental_health_consequence, phys_health_consequence, coworkers, supervisor, mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence, age_range = line.split(',')

                if sno.strip() == snoQ.strip():
                    res = {'sno': sno, 'age': age, 'gender': gender, 'country': country, 'self_employed': self_employed, 'family_history': family_history, 'treatment': treatment, 'work_interfere': work_interfere, 'no_employees': no_employees, 'remote_work': remote_work, 'tech_company': tech_company, 'benefits': benefits, 'care_options': care_options, 'wellness_program': wellness_program, 'seek_help': seek_help, 'anonymity': anonymity, 'leave': leave, 'mental_health_consequence': mental_health_consequence, 'phys_health_consequence': phys_health_consequence, 'coworkers': coworkers, 'supervisor': supervisor, 'mental_health_interview': mental_health_interview, 'phys_health_interview': phys_health_interview, 'mental_vs_physical': mental_vs_physical, 'obs_consequence': obs_consequence, 'age_range': age_range}

                    pred = doPrediction(gender, country, self_employed, family_history, no_employees, remote_work,
                        tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave,
                        mental_health_consequence, phys_health_consequence, coworkers, supervisor,
                        mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence, age_range)
                    
                    res['mental_index'] = str(int(pred['treatment_probability'][0] * 10000) / 100)

                    print(res)

                    return jsonify(res)
    
    return "None"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)

# http://127.0.0.1:3000/predict_treatment?gender=male&country=United States&self_employed=No&family_history=Yes&no_employees=1-5&remote_work=Yes&tech_company=Yes&benefits=Yes&care_options=Yes&wellness_program=No&seek_help=No&anonymity=Yes&leave=Somewhat easy&mental_health_consequence=No&phys_health_consequence=No&coworkers=Some of them&supervisor=Yes&mental_health_interview=Yes&phys_health_interview=No&mental_vs_physical=Yes&obs_consequence=No&age_range=21-30
# http://127.0.0.1:3000/predict_mental_health_index?gender=male&country=United%20States&self_employed=No&family_history=Yes&no_employees=1-5&remote_work=Yes&tech_company=Yes&benefits=Yes&care_options=Yes&wellness_program=No&seek_help=No&anonymity=Yes&leave=Somewhat%20easy&mental_health_consequence=No&phys_health_consequence=No&coworkers=Some%20of%20them&supervisor=Yes&mental_health_interview=Yes&phys_health_interview=No&mental_vs_physical=Yes&obs_consequence=No&age_range=21-30
	