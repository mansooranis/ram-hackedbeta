import { Form, Button } from "react-bootstrap";
import NewQuestion4 from "./NewQuestion4";
import Cookies from "universal-cookie"
import { useState } from "react";
const cookies = new Cookies();
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"


export default function NewQuestion3 (props){
    const [queeeee, setqueeee]  = useState(cookies.get("question3"))
    const [whatisthea, setWhatisthea] = useState(false)
    const [question5, setQuestion5] = useState(false)
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question4', res["data"]["question"], { path: '/' });
                    setQuestion5(true)
                }
            )
        })
    }
    return(
        <div className="allquemain">
            <div className="allque">
                {cookies.get("question3")}
                <div className = "">
                    <Form>
                        <Form.Control row ={3} as ="textarea" onChange={(event) => {setWhatisthea(event.target.value)}}/>
                    </Form>
                </div>
                <br/>
                <Button onClick={questionsubmitted}>Submit</Button>
                {question5?<NewQuestion4 question= {queeeee} answer = ""/>:<div></div>}
            </div>
        </div>
    )
}