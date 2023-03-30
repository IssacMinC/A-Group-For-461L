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

    function checkIn(){

    }

    function checkOut(){

    }

    return(
        <div className={'HWsep ' + props.hwset}>
                <div className='space-cap'>
                    {props.hwset}: {ava}/{props.max}  
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