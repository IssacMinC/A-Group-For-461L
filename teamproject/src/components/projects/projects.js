import React, {useState} from 'react';
import List from '@mui/material/List'
import { Box } from '@mui/system';
import Project from '../project/project';


function Projects(props){

    console.log(props)
    const [ava1, setAva1] = useState(props.ava1)
    const [ava2, setAva2] = useState(props.ava2)

    const hwProps = {
        cap1:props.cap1,
        cap2:props.cap2,
        ava1:ava1,
        ava2:ava2,
        getAva1:props.getAva1,
        getAva2:props.getAva2
    }

    const rows = props.projectList.map(p => <Box><Project {...p} {...hwProps}/></Box>)
    const sxProps = {
        alignItems: 'center',
        width:9/10   
    }

    return(
        <Box sx={sxProps}>
            <List>
                {rows}
            </List>
        </Box>

    );
}

export default Projects