import "./topintro.css"
import {Button} from "react-bootstrap"

export default function TopIntro(){
    return(
        <div>
            <div className = "top1intro">
                <div className="getstarted">
                    <h1 className = "textintro">Better You Starts Here</h1>
                    <Button variant="dark">Get Started</Button>
                </div>
            </div>
        </div>
    )
}
