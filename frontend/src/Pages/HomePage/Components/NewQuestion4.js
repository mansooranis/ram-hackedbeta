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
    var alldata;
    const questionsubmitted = () => {
        axios.post(url+"submitUserData/"+cookies.get("userID"),{
            question:queeeee,
            answer: whatisthea
        }).then(function (res){
            axios.get(url+"machineLearning/"+cookies.get("userID"),{}).then(
                function (res){
                    setqueeee(res["data"]["question"])
                    cookies.set('question5', res["data"]["question"], { path: '/' });
                    axios.get(url+"finalResult/"+cookies.get("userID")).then(
                        function (res){
                            cookies.set("alldata",res["data"])
                        }
                    )
                    setQuestion6(true)
                    console.log(cookies.get("alldata"))
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
            {question6?<div>
                <div>
                    <br/>
                    <table>
                        <tr>
                            <th>Question</th>
                            <th>Emotion</th>
                        </tr>
                        <tr>
                            <td>{cookies.get("alldata")[0]["id"]}</td>
                            <td>{cookies.get("alldata")[0]["emotion"]}</td>
                        </tr>
                        <tr>
                            <td>{cookies.get("alldata")[1]["id"]}</td>
                            <td>{cookies.get("alldata")[1]["emotion"]}</td>
                        </tr>
                        <tr>
                            <td>{cookies.get("alldata")[2]["id"]}</td>
                            <td>{cookies.get("alldata")[2]["emotion"]}</td>
                        </tr>
                        <tr>
                            <td>{cookies.get("alldata")[3]["id"]}</td>
                            <td>{cookies.get("alldata")[3]["emotion"]}</td>
                        </tr>
                        <tr>
                            <td>{cookies.get("alldata")[4]["id"]}</td>
                            <td>{cookies.get("alldata")[4]["emotion"]}</td>
                        </tr>
                    </table>
                    <br/>
                </div>
            </div>:<div></div>}
        </div>
    )
}