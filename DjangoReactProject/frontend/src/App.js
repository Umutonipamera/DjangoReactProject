import React,{Component} from "react";

class App extends Component {

  constructor(props){
    super(props);
    this.state ={
      items :[],
      isLoaded:false,
    }
  }
  componentDidMount(){
    fetch("http://127.0.0.1:8000/api/customers//")
        .then(res => res.json())
        .then(json =>{
          this.setState({
            isLoaded:true,
            items:json,
          })

        });
 
  }

  render(){
    var{isLoaded,items} = this.state;
    if(!isLoaded){
      return <div>Loading...</div>;
    }
    else{

    }
     
       return(
       <div className="App">

       <ul>
         {items.map(item =>(
            <li key={item.id}>
                First_name:{item.first_name} |
                Last_name:{item.last_name} |
                Email_address:{item.email_address} |
                Gender:{item.gender} |
                Description:{item.description} |
                Attachnment:{item.attachnment} 

            </li>
         ))};
         
       </ul>

      </div>
    );
  }
}
export default App;