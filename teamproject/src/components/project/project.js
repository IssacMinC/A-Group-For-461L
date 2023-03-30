import React from 'react';
import HWSet from '../hwset/hwset'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

function Project(props){

    const cap1 = props.cap1
    const cap2 = props.cap1
    const ava1 = props.ava1
    const ava2 = props.ava2
    
    const sxProps = {
        display:'flex',
        marginTop:1,
        borderBottom:1,
        width:1
    }

    return(
        <Box sx={sxProps}className='project flex-container'>
            <Typography sx={{width:1/4}} className='name' noWrap>{props.name}</Typography>
            <Box className='hw'>
                <HWSet hwset='HWSet1' ava={ava1} max={cap1}></HWSet>
                <HWSet hwset='HWSet2' ava={ava2} max={cap2}></HWSet>
            </Box>
        </Box>
    )
}

export default Project