import pyodbc
import urllib2
import logging
from datetime import datetime, timedelta
import json
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def main():
	try:

		with open('config.json') as f:
			data = json.load(f)
		
		DBfile = data['DBfile']
		user = data['user']
		password = data['password']
		
		connStr = (
		r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
		r"DBQ=" + DBfile + ";"
		)
		
		_logger.info('Connecting to DataBase ...')
		conn = pyodbc.connect(connStr)
		cursor = conn.cursor()
		
		attendance_data = []
		user_data = []
		
			# Get Attendance Data
		
		sql = 'select Employeeid, AttendanceDate, Status from AttendanceLogs;'
		for att in cursor.execute(sql):
			if att.AttendanceDate.date() == datetime.now().date():
				att_data={}
				att_data['status'] = att.Status
				#att_data['status'] = 1
				att_data['timestamp'] = datetime.strftime(att.AttendanceDate, '%Y-%m-%d %H:%M:%S') #att.AttendanceDate #datetime.strftime(att.AttendanceDate, '%Y-%m-%d %H:%M:%S')
				att_data['user_id'] = att.Employeeid
				attendance_data.append(att_data)
				
		#print attendance_data
			# Get User Data
		
		sql = "select Employeeid, EmployeeName, NumericCode from Employees;"
		for emp in cursor.execute(sql):
			usr_data = {}
			usr_data['user_id'] = emp.Employeeid
			usr_data['uid'] = emp.NumericCode
			usr_data['name'] = emp.EmployeeName
			user_data.append(usr_data)
			
		#print user_data

		res_data={'attendance_data':attendance_data, 'user_data' : user_data, 'status':True}
		#print res_data

		send_data(res_data)

	except Exception, e:
		_logger.info("Process terminate : {}".format(e))
	finally:
		if conn:
			conn.close()

def send_data(val):
    #type url of vms server
    with open('server_ip_config.txt', 'r') as contentip_file:
        contentip = contentip_file.read()

    vms_url = contentip

    #vms_url="http://localhost:8069"
    serv="/zk_fingerprint/controller/update"
    usr_serv="/zk_fingerprint/get_user/update"
    URL=vms_url+serv
    usr_url = vms_url+usr_serv

    res_data={}
    res_data['params'] = val
    data = json.dumps(res_data)


    #sending attendance data
    req = urllib2.Request(URL, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)
    result_att = response.read()

    # sending user data
    req_usr = urllib2.Request(usr_url, data, {'Content-Type': 'application/json'})
    usr_res = urllib2.urlopen(req_usr)
    result_usr = usr_res.read()

    return True
	
if __name__=='__main__':
    main()
