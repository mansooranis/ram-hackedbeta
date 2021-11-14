import { Form, Button } from "react-bootstrap";
import Cookies from "universal-cookie"
import { useState } from "react";
import NewQuestion3 from "./NewQuestion3";
const cookies = new Cookies();
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"


export default function NewQuestion2 (props){
    const [queeeee, setqueeee]  = useState(cookies.get("question2"))
    const [whatisthea, setWhatisthea] = useState(false)
    const [question4, setQuestion4] = useState(false)
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question3', res["data"]["question"], { path: '/' });
                    setQuestion4(true)
                }
            )
        })
    }
    return(
        <div className="allquemain">
            <div className="allque">
            {cookies.get("question2")}
            <div className = "">
                <Form>
                    <Form.Control row ={6} as ="textarea" onChange={(event) => {setWhatisthea(event.target.value)}}/>
                </Form>
            </div>
            <br/>
            <Button onClick={questionsubmitted}>Submit</Button>
            {question4?<NewQuestion3 question= {queeeee} answer = ""/>:<div></div>}
            </div>
        </div>
    )
}