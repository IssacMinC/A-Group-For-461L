import React, {useState} from "react"
import TextField from '@mui/material/TextField'
import { Button } from "@mui/material"
import './hwset.css'

function HWSet(props){
    
    const [ava, setAva] = useState(parseInt(props.ava))
    const [textVal, setTextVal] = useState(0)

    function textOnChange(e){
        const num = parseInt(e.target.value)
        setTextVal(num)
    }

    

    async function checkIn(){
        const response = await fetch(`http://127.0.0.1:5000/projectCheckIn/${props.projName}/${props.hwset}/${textVal}`, {
          mode: 'cors',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }, 
        });
        const data = await response.json()
        const message = data["msg"]
        if (message === "check in sucessful"){
            props.getAva()
            props.getHW()
        }
        alert(message)
      }

    async function checkOut(){
        const response = await fetch(`http://127.0.0.1:5000/projectCheckOut/${props.projName}/${props.hwset}/${textVal}`, {
          mode: 'cors',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }, 
        });
        const data = await response.json()
        const message = data["msg"]
        if (message === "check out sucessful"){
            props.getAva()
            props.getHW()
        }
        alert(message)
      }

    return(
        <div className={'HWsep ' + props.hwset}>
                <div className='space-cap'>
                    {props.hwset}: {props.ava}  
                </div> 
                <span className='space-text'>
                    <TextField onChange={textOnChange} className='tf' variant='standard' size='small' placeholder='Enter qty'/>
                </span>
                <span className='space-small'>
                    <Button variant='contained' size='small' onClick={checkIn}>Check in</Button>
                </span> 
                <span className='space-small'>
                    <Button variant='contained' size='small' onClick={checkOut}>Check out</Button>
                </span> 
        </div>
    )
}

export default HWSet