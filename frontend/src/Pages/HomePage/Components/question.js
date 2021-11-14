import { Form } from "react-bootstrap"
import "./questions.css"
import Cookies from 'universal-cookie';
import { useState } from "react";
import { Button } from "react-bootstrap";
import NewQuestion from "./newQuestion";


const cookies = new Cookies();
const axios = require('axios').default;
const url = "http://91bf-74-3-183-254.ngrok.io/"
export default function Questions(props){
    const [question2, setQuestion2] = useState(false)
    const [whatisthea, setWhatisthea] = useState(false)
    const [queeeee, setqueeee]  = useState("How are you feeling today?")
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question1', res["data"]["question"], { path: '/' });
                    setQuestion2(true)
                    console.log(res["data"]["question"])
                    console.log(res)
                }
            )
        })
    }
    const renderonlyques = () => {
        if (props.answer === ""){
            return(
                <div>
                    <div className="">
                        <Form>
                            <Form.Control as ="textarea" rows = {5} onChange={(event) => {setWhatisthea(event.target.value)}}/>
                        </Form>
                    </div>
                    <br/>
                    <div className="center-this-button">
                        <Button onClick={questionsubmitted}>Submit</Button>
                    </div>
                </div>
            )
        }else{
            return(
                <div>
                    <text>
                        {props.answer}
                    </text>
                </div>
            )
        }
    }
    return(
        <div>
            <div className="questopener">
                <div className="que">
                    <text>{props.question}</text>
                </div>
                <div>
                    <text>
                        {
                            renderonlyques()
                        }
                    </text>
                </div>
            </div>
            {question2?<NewQuestion question= {queeeee} answer = ""/>:<div></div>}
        </div>
    )
}