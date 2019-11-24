# SsenseAiTask
  #Content :
    #A reactive map where you can select locations / draw shapes /search for places 
    #You can insert, delete and display the locations / shapes infos in/from a database
    #An endpoint in not accessible from the gui ( /api/getdata) it returns all the data stored in hson format
    #Flask backend is used
    

   #Run configs :
      #I used sqlite3 becauase it doesent need much configurations, plus data size is small
      #I used flask_sqlalchemy , so make sure it's installed in order to run the app correctly 
      #To launch the server : "python app.py" in the right directory , the app will run at port 5000
      #Make sure to allow the navigator geolocation so the map will be centered on your location , otherwise it will be centered elsewhere
      
   #Things to improve :
     # It would be better if the frontend and the backend were two separated apps ( not the case here ) so the exchanged data would be on 
        json format and take advantage of the full power of rest apis
     #api versioning
 
  
