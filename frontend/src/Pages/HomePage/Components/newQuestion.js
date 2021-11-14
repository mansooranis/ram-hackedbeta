import { Form, Button } from "react-bootstrap";
import Cookies from "universal-cookie"
import { useState } from "react";
import NewQuestion2 from "./NewQuestion2";
const cookies = new Cookies();
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"


export default function NewQuestion (props){
    const [queeeee, setqueeee]  = useState(cookies.get("question2"))
    const [whatisthea, setWhatisthea] = useState(false)
    const [question3, setQuestion3] = useState(false)
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question2', res["data"]["question"], { path: '/' });
                    setQuestion3(true)
                }
            )
        })
    }
    return(
        <div className="allquemain">
            <div className="allque">
                {cookies.get("question1")}
                <div className = "">
                    <Form>
                        <Form.Control row ={3} as ="textarea" onChange={(event) => {setWhatisthea(event.target.value)}}/>
                    </Form>
                </div>
                <br/>
                <div className="center-this-button">
                    <Button onClick={questionsubmitted}>Submit</Button>
                </div>
                {question3?<NewQuestion2 question= {queeeee} answer = ""/>:<div></div>}
            </div>
        </div>
    )
}