import { Form, Button } from "react-bootstrap";
import Cookies from "universal-cookie"
import { useState } from "react";
const cookies = new Cookies();
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"


export default function NewQuestion4 (props){
    const [queeeee, setqueeee]  = useState(cookies.get("question3"))
    const [whatisthea, setWhatisthea] = useState(false)
    const [question6, setQuestion6] = useState(false)
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question5', res["data"]["question"], { path: '/' });
                    setQuestion6(true)
                }
            )
        })
    }
    return(
        <div className="allquemain">
            <div className="allque">
                {cookies.get("question5")}
                <div className = "">
                    <Form>
                        <Form.Control row ={3} as ="textarea" onChange={(event) => {setWhatisthea(event.target.value)}}/>
                    </Form>
                </div>
                <br/>
                <Button onClick={questionsubmitted}>Submit</Button>
            </div>
        </div>
    )
}