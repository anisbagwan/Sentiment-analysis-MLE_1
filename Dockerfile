#1.Set base image 
FROM python:3.9

#2.Set working directory
WORKDIR /opt/app

#3.Provide port number
#EXPOSE 5000

#4.Copy files to the working directory
COPY . . 

#5.Install dependencies
RUN pip install -r requirements.txt

#6.Command that run when container starts
CMD ["python","/opt/app/src/app.py"] 