import React, {useState, useEffect} from 'react';
import HWSet from '../hwset/hwset'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

function Project(props){

    const cap1 = props.cap1
    const cap2 = props.cap1
    const ava1 = props.ava1
    const ava2 = props.ava2

    const [hw1, setHW1] = useState(0)
    const [hw2, setHW2] = useState(0)
    
    const sxProps = {
        display:'flex',
        marginTop:1,
        borderBottom:1,
        width:1
    }

    async function getHW1(){
        const response = await fetch(`/getProjectHW1/${props.name}`, {
          mode: 'cors',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }, 
        });
        const data = await response.json()
        setHW1(data["hwSet1"])
      }

      async function getHW2(){
        const response = await fetch(`/getProjectHW2/${props.name}`, {
          mode: 'cors',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }, 
        });
        const data = await response.json()
        setHW2(data["hwSet2"])
      }  

      useEffect(() => {
        getHW1()
        getHW2()
      }, [])

    return(
        <Box sx={sxProps}className='project flex-container'>
            <Typography sx={{width:1/4}} className='name' noWrap>{props.name}</Typography>
            <Box className='hw'>
                <HWSet hwset='HWSet1' ava={hw1} max={cap1} projName={props.name} getAva = {props.getAva1} getHW = {getHW1}></HWSet>
                <HWSet hwset='HWSet2' ava={hw2} max={cap2} projName={props.name} getAva = {props.getAva2} getHW = {getHW2}></HWSet>
            </Box>
        </Box>
    )
}

export default Project