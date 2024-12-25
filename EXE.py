from tkinter import messagebox
import os
import pyodbc
import datetime
from pymodbus.client import ModbusTcpClient
import webbrowser

teslead_db = None
TesleadSmartSyncX = None

def initial_msg(title, message):
    messagebox.showinfo(title, message)
    app_name = "TesleadSmartSyncX"
    os.system("taskkill /f /im " + app_name + ".exe")
initial_msg("Teslead SmartSyncX", "Welcome to Teslead SmartSyncX. Ready to begin.")

if not os.path.exists("D:/TesleadSmartSyncX/Database"):
    os.makedirs("D:/TesleadSmartSyncX/Database")
if not os.path.exists("D:/TesleadSmartSyncX/Reports"):
    os.makedirs("D:/TesleadSmartSyncX/Reports")
if not os.path.exists("D:/TesleadSmartSyncX/Excel-PDF_reports"):
    os.makedirs("D:/TesleadSmartSyncX/Excel-PDF_reports")

def local_db():
    global teslead_db
    teslead_X = "DRIVER={MySQL ODBC 9.0 ANSI Driver};Server=localhost;Port=3306;Database=qnq;Uid=root;Password=;OPTION=3;"
    conn = pyodbc.connect(teslead_X)
    try:
        teslead_db = conn.cursor()
    except Exception as e:
        print(f"Database connection error: {e}")
        local_db()
local_db()

month_year = datetime.date.today().strftime('%m%Y')
current_status = f"current_status_{month_year}"
master_actuator = f"master_actuator_{month_year}"
pressure_analysis = f"pressure_analysis_{month_year}"
teslead_db.execute("CREATE TABLE IF NOT EXISTS qnq_completed." + current_status + " (`id` INT(11) NOT NULL ,`sales_order_no` VARCHAR(50) NOT NULL DEFAULT '',`sales_item_no` VARCHAR(50) NOT NULL DEFAULT '',`valve_serial_number` VARCHAR(50) NOT NULL DEFAULT '123',`pressure` DOUBLE(18,2) NOT NULL DEFAULT '0.00',`hydro_pressure` DOUBLE(18,2) NOT NULL DEFAULT '0.00',`date_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',`start_graph` int(11) NOT NULL DEFAULT '1',`test_type` INT(11) NOT NULL DEFAULT '3',`created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,`type_code` int(11) NOT NULL DEFAULT '0',`type_name` VARCHAR(50) NOT NULL DEFAULT '',`pressure_range` INT(11) NOT NULL DEFAULT '0',`cycle_complete` ENUM('0','1') NOT NULL DEFAULT '1') ENGINE=INNODB DEFAULT CHARSET=latin1")
teslead_db.commit()
teslead_db.execute("CREATE TABLE IF NOT EXISTS qnq_completed." + pressure_analysis + " (`id` int(11) NOT NULL, `set_pressure` double(18,3) NOT NULL DEFAULT '0.000', `temprature` double(18,3) NOT NULL DEFAULT '0.000', `max_pressure` double(18,3) NOT NULL DEFAULT '0.000', `pressure_unit` varchar(10) NOT NULL DEFAULT '', `pressure` double(18,3) NOT NULL DEFAULT '0.000', `hydro_pressure` double(18,2) NOT NULL DEFAULT '0.00', `result_pressure` double(18,3) NOT NULL DEFAULT '0.000', `gauge_drop` double(18,3) NOT NULL DEFAULT '0.000', `cavity_connector_l` double(18,3) NOT NULL DEFAULT '0.000', `cavity_connector_r` double(18,3) NOT NULL DEFAULT '0.000', `torque` varchar(50) NOT NULL DEFAULT '', `valve_size` varchar(50) NOT NULL DEFAULT '', `valve_type` varchar(50) NOT NULL DEFAULT '', `valve_class` varchar(50) NOT NULL DEFAULT '', `tested_by` varchar(50) NOT NULL DEFAULT '', `approved_by` varchar(50) NOT NULL DEFAULT '', `valve_tag_no` varchar(50) NOT NULL DEFAULT '', `valve_serial_number` varchar(50) NOT NULL DEFAULT '0', `set_time_unit` varchar(50) NOT NULL DEFAULT '', `set_time` int(11) NOT NULL DEFAULT '0', `actual_time` int(11) NOT NULL DEFAULT '0', `test_type` int(11) NOT NULL DEFAULT '0', `write_hmi` int(1) NOT NULL DEFAULT '1', `start` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `end` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `cycle_start` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `cycle_end` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `valve_status` int(11) NOT NULL DEFAULT '3', `status` int(11) NOT NULL DEFAULT '0', `date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `start_graph` int(11) NOT NULL DEFAULT '0', `type_code` int(11) NOT NULL DEFAULT '0', `type_name` varchar(50) NOT NULL DEFAULT '', `pressure_range` int(11) NOT NULL DEFAULT '0', `shell_material` int(11) NOT NULL DEFAULT '0', `sales_order_no` varchar(50) NOT NULL DEFAULT '', `sales_item_no` varchar(50) NOT NULL DEFAULT '', `gad_no` varchar(50) NOT NULL DEFAULT '', `stem_orientation` varchar(50) NOT NULL DEFAULT '', `gear_actuator` varchar(50) NOT NULL DEFAULT '', `ma_gear_ratio` varchar(50) NOT NULL DEFAULT '', `ga_drg_no` varchar(50) NOT NULL DEFAULT '', `appilicability` varchar(50) NOT NULL DEFAULT '', `body_heat` varchar(50) NOT NULL DEFAULT '', `body_mp` varchar(50) NOT NULL DEFAULT '', `body_rt` varchar(50) NOT NULL DEFAULT '', `bonnet_heat` varchar(50) NOT NULL DEFAULT '', `bonnet_mp` varchar(50) NOT NULL DEFAULT '', `bonnet_rt` varchar(50) NOT NULL DEFAULT '', `extn_heat` varchar(50) NOT NULL DEFAULT '', `extn_mp` varchar(50) NOT NULL DEFAULT '', `extn_rt` varchar(50) NOT NULL DEFAULT '', `hydro_1` varchar(50) NOT NULL DEFAULT '', `hydro_2` varchar(50) NOT NULL DEFAULT '', `air_1` varchar(50) NOT NULL DEFAULT '', `air_2` varchar(50) NOT NULL DEFAULT '', `others_1` varchar(50) NOT NULL DEFAULT '', `others_2` varchar(50) NOT NULL DEFAULT '', `others_3` varchar(50) NOT NULL DEFAULT '', `cal_due_hydro_1` datetime NOT NULL, `cal_due_hydro_2` datetime NOT NULL, `cal_due_air_1` datetime NOT NULL, `cal_due_air_2` datetime NOT NULL, `cal_due_others_1` datetime NOT NULL, `cal_due_others_2` datetime NOT NULL, `cal_due_others_3` datetime NOT NULL, `ep_success` enum('0','1') NOT NULL DEFAULT '1', `send_status` enum('yes','no') NOT NULL DEFAULT 'no', `cycle_complete` enum('0','1') NOT NULL DEFAULT '1', `ip_address` varchar(50) NOT NULL DEFAULT '', `report_no` varchar(50) NOT NULL DEFAULT '', `wrench` varchar(50) NOT NULL DEFAULT '', `ball_disc_heat` varchar(50) NOT NULL DEFAULT '', `ball_disc_mp` varchar(50) NOT NULL DEFAULT '', `ball_disc_rt` varchar(50) NOT NULL DEFAULT '', `standard_id` int(11) NOT NULL, `range_hydro_1` varchar(50) NOT NULL DEFAULT '', `range_hydro_2` varchar(50) NOT NULL DEFAULT '', `range_air_1` varchar(50) NOT NULL DEFAULT '', `range_air_2` varchar(50) NOT NULL DEFAULT '', `range_others_1` varchar(50) NOT NULL DEFAULT '', `range_others_2` varchar(50) NOT NULL DEFAULT '', `range_others_3` varchar(50) NOT NULL DEFAULT '', `cal_done_hydro_1` datetime NOT NULL, `cal_done_hydro_2` datetime NOT NULL, `cal_done_air_1` datetime NOT NULL, `cal_done_air_2` datetime NOT NULL, `cal_done_others_1` datetime NOT NULL, `cal_done_others_2` datetime NOT NULL, `cal_done_others_3` datetime NOT NULL, `range_wrench` varchar(50) NOT NULL DEFAULT '', `cal_due_wrench` datetime NOT NULL, `torque_value` varchar(50) NOT NULL DEFAULT '') ENGINE=InnoDB DEFAULT CHARSET=latin1;")
teslead_db.commit()
teslead_db.execute("CREATE TABLE IF NOT EXISTS qnq_completed." + master_actuator + " (`id` INT(11) NOT NULL ,`valve_serial_no` VARCHAR(50) NOT NULL DEFAULT '',`actuator_model_main` VARCHAR(50) NOT NULL DEFAULT '',`actuator_model_by_pass1` VARCHAR(50) NOT NULL DEFAULT '',`actuator_model_by_pass2` VARCHAR(50) NOT NULL DEFAULT '',`wiring_diagram_main` VARCHAR(50) NOT NULL DEFAULT '',`wiring_diagram_by_pass1` VARCHAR(50) NOT NULL DEFAULT '',`wiring_diagram_by_pass2` VARCHAR(50) NOT NULL DEFAULT '',`rpm_value_main` VARCHAR(50) NOT NULL DEFAULT '',`rpm_value_by_pass1` VARCHAR(50) NOT NULL DEFAULT '',`rpm_value_by_pass2` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_open_to_close_main` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_open_to_close_by_pass1` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_open_to_close_by_pass2` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_close_to_open_by_main` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_close_to_open_by_pass1` VARCHAR(50) NOT NULL DEFAULT '',`oper_time_close_to_open_by_pass2` VARCHAR(50) NOT NULL DEFAULT '',`act_s_no` VARCHAR(50) NOT NULL DEFAULT '',`torque_setting` VARCHAR(50) NOT NULL DEFAULT '',`bye_pass_valve_sl_no` VARCHAR(50) NOT NULL DEFAULT '',`closing` VARCHAR(50) NOT NULL DEFAULT '',`break_open` VARCHAR(50) NOT NULL DEFAULT '',`eye_bolt_torque` VARCHAR(50) NOT NULL DEFAULT '',`valve_drying` VARCHAR(50) NOT NULL DEFAULT '',`result_drying` VARCHAR(50) NOT NULL DEFAULT '',`remarks` VARCHAR(300) NOT NULL DEFAULT '',`shift` VARCHAR(50) NOT NULL DEFAULT '',`breakaway` varchar(50) NOT NULL DEFAULT '',`media_drained` varchar(50) NOT NULL DEFAULT '',`vent_bleeder` varchar(50) NOT NULL DEFAULT '',`torque_break_nm` varchar(50) NOT NULL DEFAULT '',`torque_run` varchar(50) NOT NULL DEFAULT '',`actuator_make` varchar(50) NOT NULL DEFAULT '',`open_torque1` varchar(50) NOT NULL DEFAULT '',`open_torque2` varchar(50) NOT NULL DEFAULT '',`close_torque1` varchar(50) NOT NULL DEFAULT '',`close_torque2` varchar(50) NOT NULL DEFAULT '',`operate_time1` varchar(50) NOT NULL DEFAULT '',`operate_time2` varchar(50) NOT NULL DEFAULT '',`operate_time3` varchar(50) NOT NULL DEFAULT '',`date_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',`actuator_tag_no` varchar(50) NOT NULL DEFAULT '',`rated_torque` varchar(50) NOT NULL DEFAULT '',`cycle_complete` ENUM('0','1') NOT NULL DEFAULT '1') ENGINE=INNODB DEFAULT CHARSET=latin1")
teslead_db.commit()
# teslead_db.execute("INSERT INTO qnq_completed." + current_status + " (id,sales_order_no,sales_item_no,valve_serial_number,pressure,hydro_pressure,date_time,start_graph,test_type,created_on,type_code,type_name,pressure_range,cycle_complete) SELECT id,sales_order_no,sales_item_no,valve_serial_number,pressure,hydro_pressure,date_time,start_graph,test_type,created_on,type_code,type_name,pressure_range,cycle_complete FROM current_status WHERE cycle_complete = '0'")
# teslead_db.commit()
# teslead_db.execute("INSERT INTO qnq_completed." + pressure_analysis + " (id,temprature,set_pressure,max_pressure,pressure_unit,pressure,hydro_pressure,result_pressure,gauge_drop,valve_size,valve_type,valve_class,tested_by,approved_by,valve_tag_no,valve_serial_number,set_time_unit,set_time,actual_time,test_type,write_hmi,START,END,cycle_start,cycle_end,valve_status,STATUS,date_time,start_graph,type_code,type_name,pressure_range,shell_material,sales_order_no,sales_item_no,gad_no,stem_orientation,gear_actuator,ma_gear_ratio,ga_drg_no,appilicability,body_heat,body_mp,body_rt,bonnet_heat,bonnet_mp,bonnet_rt,extn_heat,extn_mp,extn_rt,hydro_1,hydro_2,air_1,air_2,others_1,others_2,others_3,cal_due_hydro_1,cal_due_hydro_2,cal_due_air_1,cal_due_air_2,cal_due_others_1,cal_due_others_2,cal_due_others_3,ep_success,send_status,cycle_complete,ip_address) SELECT id,temprature,set_pressure,max_pressure,pressure_unit,pressure,hydro_pressure,result_pressure,gauge_drop,valve_size,valve_type,valve_class,tested_by,approved_by,valve_tag_no,valve_serial_number,set_time_unit,set_time,actual_time,test_type,write_hmi,START,END,cycle_start,cycle_end,valve_status,STATUS,date_time,start_graph,type_code,type_name,pressure_range,shell_material,sales_order_no,sales_item_no,gad_no,stem_orientation,gear_actuator,ma_gear_ratio,ga_drg_no,appilicability,body_heat,body_mp,body_rt,bonnet_heat,bonnet_mp,bonnet_rt,extn_heat,extn_mp,extn_rt,hydro_1,hydro_2,air_1,air_2,others_1,others_2,others_3,cal_due_hydro_1,cal_due_hydro_2,cal_due_air_1,cal_due_air_2,cal_due_others_1,cal_due_others_2,cal_due_others_3,ep_success,send_status,cycle_complete,ip_address FROM pressure_analysis WHERE cycle_complete = '0'")
# teslead_db.commit()
# teslead_db.execute("INSERT INTO qnq_completed." + master_actuator + " (id,valve_serial_no,actuator_model_main,actuator_model_by_pass1,actuator_model_by_pass2,wiring_diagram_main,wiring_diagram_by_pass1,wiring_diagram_by_pass2,rpm_value_main,rpm_value_by_pass1,rpm_value_by_pass2,oper_time_open_to_close_main,oper_time_open_to_close_by_pass1,oper_time_open_to_close_by_pass2,oper_time_close_to_open_by_main,oper_time_close_to_open_by_pass1,oper_time_close_to_open_by_pass2,act_s_no,torque_setting,bye_pass_valve_sl_no,closing,break_open,eye_bolt_torque,valve_drying,result_drying,remarks,shift,breakaway,media_drained,vent_bleeder,torque_break_nm,torque_run,actuator_make,open_torque1,open_torque2,close_torque1,close_torque2,operate_time1,operate_time2,operate_time3,date_time,actuator_tag_no,rated_torque,cycle_complete)SELECT id,valve_serial_no,actuator_model_main,actuator_model_by_pass1,actuator_model_by_pass2,wiring_diagram_main,wiring_diagram_by_pass1,wiring_diagram_by_pass2,rpm_value_main,rpm_value_by_pass1,rpm_value_by_pass2,oper_time_open_to_close_main,oper_time_open_to_close_by_pass1,oper_time_open_to_close_by_pass2,oper_time_close_to_open_by_main,oper_time_close_to_open_by_pass1,oper_time_close_to_open_by_pass2,act_s_no,torque_setting,bye_pass_valve_sl_no,closing,break_open,eye_bolt_torque,valve_drying,result_drying,remarks,shift,breakaway,media_drained,vent_bleeder,torque_break_nm,torque_run,actuator_make,open_torque1,open_torque2,close_torque1,close_torque2,operate_time1,operate_time2,operate_time3,date_time,actuator_tag_no,rated_torque, cycle_complete FROM master_actuator WHERE cycle_complete = '0'")
# teslead_db.commit()
# teslead_db.execute("DELETE FROM pressure_analysis WHERE cycle_complete = '0'")
# teslead_db.commit()
# teslead_db.execute("DELETE FROM current_status WHERE cycle_complete = '0'")
# teslead_db.commit()
# teslead_db.execute("DELETE FROM master_actuator WHERE cycle_complete = '0'")
# teslead_db.commit()

os.chdir("E:\\xampp\\mysql\\bin")
os.system("cmd /c mysqldump --database qnq --single-transaction --add-drop-database --triggers --routines --events --user=root --password= > D:\\TesleadSmartSyncX\\Database\\qnq-{}.sql".format(datetime.datetime.now().strftime("%Y-%m-%d")))
os.system("cmd /c mysqldump --database qnq_completed --single-transaction --add-drop-database --triggers --routines --events --user=root --password= > D:\\TesleadSmartSyncX\\Database\\qnq_completed-{}.sql".format(datetime.datetime.now().strftime("%Y-%m-%d")))

def hmi_sync():
    global teslead_db, TesleadSmartSyncX
    ip_address = teslead_db.execute("select ip_address from master_ip_address;").fetchone()[0]
    TesleadSmartSyncX = ModbusTcpClient(ip_address)
    TesleadSmartSyncX.connect()
hmi_sync()

webbrowser.open("http://localhost/aruna/")

def getstatus(xad):
    global TesleadSmartSyncX
    while True:
        try:
            return TesleadSmartSyncX.read_holding_registers(xad, 1).registers[0]
        except Exception as e:
            print(f"Error in getstatus: {e}")
            local_db()
            hmi_sync()
def setstatus(xad, value):
    global TesleadSmartSyncX
    while True:
        try:
            TesleadSmartSyncX.write_register(int(xad), int(value))
            return None
        except Exception as e:
            print(f"Error in setstatus: {e}")
            local_db()
            hmi_sync()

def main_thread():
    global teslead_db, TesleadSmartSyncX
    while True:
        
            