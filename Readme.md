# DjangoReactProject

## Introduction

This is a repo that contains three parts :
 
  * A backend App(Python using django framework)
 
       * Store of products
       * Add to cart
       * View product
       * Customer Registration
       * Checkout
   
 * Rest api
 
      * Contains all  data from database
  
 * Frontend App (Reactjs app using javascript)

      * Fetching data from Api 

## Requirements

 * Python 3.8
 * npm 6.14.8
 * nodejs  v12.18.2
 * reactjs  17.0.2
 * Visual Studio Code
 
## Setup
To run this project you will need to:


 * Fork this project
 * Clone the repository in your terminal ``` git clone [url goes here] ```
 * Using Visual Studio Code, open the folder with the cloned repository
 * Open a new terminal to run the project


   * To django project:
    * To activate environment 
      
       ```bash
         source env1/bin/activate 
         ```
    * After you learn a project
    
       ```bash
          python3 manage.py runserver 
         ```
    * After opening your browser you have to add /customers/  
    * It should look like this
      
       ```bash
        http://127.0.0.1:8000/customers/
         ```
        
    
     * So that you can see what is in the project and also you can open it on the order browser so that you can be able to open api because reactjs app can't    fetch   data when the api is not active, so you will open api by adding 
       
    
       ```bash
        http://127.0.0.1:8000/api/customers//
         ```
        
 
   * To run reactjs:
    * You have first to cd DjangoReactProject 
    * cd frontend
         
         
      ```bash
         npm start
        ```
         
 
 
 
