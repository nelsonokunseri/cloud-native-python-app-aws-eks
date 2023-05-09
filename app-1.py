# import psutil
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     cpu_utilization = psutil.cpu_percent(interval=1)
#     mem_utilization = psutil.virtual_memory().percent
#     ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)

#     return render_template("index.html", cpu_utilization=cpu_utilization, mem_utilization=mem_utilization, ram=ram)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


# import psutil
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     cpu_utilization = psutil.cpu_percent(interval=1)
#     mem_utilization = psutil.virtual_memory().percent
#     ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
#     applications = psutil.process_iter(['name'])

#     return render_template("index.html", cpu_utilization=cpu_utilization, mem_utilization=mem_utilization, ram=ram)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

