import "./secondcom.css"
import { InputGroup, Button, FormControl } from "react-bootstrap"
import { useState } from "react";
import Questions from "./question";
import Cookies from 'universal-cookie';
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"

const cookies = new Cookies();
export default function SecondComp(){
    const idnumber = Math.ceil(Math.random()*1000000);
    const [idnum ,  setIdnum] = useState("")
    const [question1, setQuestion1] = useState(false)
    const [otherques, setOtherques] = useState(false)
    const [whatstheans, setWhatstheans] = useState("")
    var listtt = []
    const checkifempty = () => {
        if (idnum === ""){
            axios.post(url+'getUserData',{
                userID: "U"+idnumber
            }).then(function (res){
                setQuestion1(true)
                console.log("posted")
                cookies.set('userID', "U"+idnumber, { path: '/' });
            }).catch(function (e){console.log(e)})
        }else{
            axios.post(url+'getUserData', {
                userID: "U"+idnumber
            }).then(function (res){
                cookies.set('userID', "U"+idnumber, { path: '/' });
                listtt = res
                setOtherques(true)
                console.log("posted")
            })
        }
    }
    const firstsubmit = () => {
        axios.post(url+"submitUserData/U"+idnumber,{
            question:"How are you feeling today?",
            answer : ""
        })
    }
    const takenewlist = () => {
        for (let i = 0; i< listtt.length;i++){
            <Questions question = {listtt[i][1]} answer = {listtt[i][2]}/>
        }
    }
    return(
        <div className= "root-sec">
        <div className="second2comp">
            <div className = "uniqueid">
                <div className= "iddddd" name = "iddddd">
                    <InputGroup className="mb-3">
                        <FormControl
                            placeholder={idnumber}
                            aria-label={idnumber}
                            aria-describedby="basic-addon2"
                            />
                                </InputGroup>
                                <InputGroup className="mb-3">
                                <FormControl
                                        placeholder="password"
                                        aria-label="password"
                                        aria-describedby="basic-addon2"
                                        onChange =  {event => setIdnum(event.target.value)}
                                        />
                                </InputGroup>
                                <Button variant="outline-secondary" id="button-addon2" onClick={checkifempty}>
                                        submit
                        </Button>
                </div>
            </div>
            <br/>
            </div>
                {question1 ? <div>
                    <Questions question = "How are you feeling today?" answer = ""/>
                            </div> : <div></div>} 
                {otherques? takenewlist:<div></div>}
        </div>
    )
}
