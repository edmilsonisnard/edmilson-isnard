from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluro, India',
    'salary': 'Rs. 10,000,00'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,000,00'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000,00'
  }
]
@app.route("/")
def hello_worlfd():
  return render_template('home.html', jobs=JOBS,company_name='Edmilson')

@app.route("/api/jobs")
def lost_jobs():
  return jsonify(JOBS)

if __name__ =="__main__":
  app.run(host='0.0.0.0', debug=True)