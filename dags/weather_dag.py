from airflow import DAG
from datetime import timedelta,datetime



default_args ={
  'owner':'airflow',
  'depends_on_past':False,
  'start_date':datetime(2023,1,8),
  'email':['myemail@domain.com'],
  'email_on_failure':False,
  'email_on_retry':False,
  'retries':2,
  'retry_delay':timedelta(minuties=2)
}

with DAG('weadther_dog'
         ,default_args=default_args
         ,schedule_interval='@delay'
         ,catchap=False ) as dag: 
  
    is_weather_api_ready=HttpSensor(
      task_id='is_weather_api_ready',
      http_conn_id='weathermap_api',
      endpoint='https://api.openweathermap.org/data/2.5/weather?q=Portland&appid=619df18b3b1f6dffdc1e24efae815ae3'
      # caoy patse end point 
    )
    
    
    # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    
    # https://openweathermap.org/current