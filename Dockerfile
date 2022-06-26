#1.Set base image 
FROM python

#2.Set working directory
WORKDIR /opt/app

#3.Provide port number
EXPOSE 500

#4.Copy files to the working directory
COPY . . 

#5.Install dependencies
RUN pip install -r requirements.txt

#6.Command that run when container starts
CMD ["python","/opt/app/src/app.py"] 