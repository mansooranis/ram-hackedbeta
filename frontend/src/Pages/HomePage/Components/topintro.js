import "./topintro.css"
import {Button} from "react-bootstrap"
import { Link} from 'react-scroll'
import { useEffect } from "react"

export default function TopIntro(){
    return(
        <div>
            <div className = "top1intro">
                <div className="getstarted">
                    <h1 className = "textintro">Better You Starts Here</h1>
                    <Button variant="dark"><Link activeClass="active" to="iddddd" spy={true} smooth={true} duration={2000}>Get Started</Link></Button>
                </div>
            </div>
        </div>
    )
}
