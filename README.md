ML_OPS 
1. Streamlit 
2. Flask
3. Dockerize flask container
    a. docker run --name flask_app_run -p 8080:5000 -d flask_app
    b. docker rm -f flask_app_run
4. Pytest framework 
    a. pytest -s -v -p no:warnings test/
       - '-s' for print statements 
       - '-v' for verbose 
       - '-p no:warnings' for supressing warnings 
    b. app.test_client() automatically triggers the server. There is no need to run the flask app separately as it might binf the 5000 port and then our pytest won't run. 

## To Do 
1. Add CD pipeline
2. Add minimal requirements