import "./index.scss"
import RadioGroup from '@mui/material/RadioGroup'
import { FormControl, FormLabel, FormControlLabel, Radio, Box, TextField, Button } from "@mui/material";
import React, { useState } from 'react';

const Form = () => {
    const handleSubmit = (event) => {
        event.preventDefault();
    }

    return(
        <form onSubmit={handleSubmit}>
            <FormControl>
            <FormLabel id="high-bp">Do you have consistently high blood pressure?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="high_bp"
                defaultValue="0"
                name="high_bp"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="high_chol">What is your cholesterol level?</FormLabel>
            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                name = "high_chol"
                >
                <TextField id="outlined-basic" label="Height" variant="outlined" />
            </Box>

            <FormLabel id="cholcheck">Have you had your cholesterol checked in the last five years?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="chol_check"
                defaultValue="0"
                name="chol_check"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="heightm">How tall are you in meters</FormLabel>
            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                name = "height"
                >
                <TextField id="outlined-basic" label="Weight" variant="outlined" />
            </Box>

            <FormLabel id="weightkg">What is your weight in kilograms?</FormLabel>
            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                name = "weight"
                >
                <TextField id="weight" label="Weight" variant="outlined" />
            </Box>
            
            <FormLabel id="smoker">Are you an active smoker?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="smoker"
                defaultValue="0"
                name="smoker"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="stroker">Do you have a history of Stroke?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="stroke"
                defaultValue="0"
                name="stroke"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="heartdisease">Do you have a history of heart disease/heart attack?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="heart_disease"
                defaultValue="0"
                name="heart_disease"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="physical">Have you done any physical activity in the past month?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="physical_activity"
                defaultValue="0"
                name="physical_activity"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="foodie">Do you regularly eat healthy foods?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="fruit_vege"
                defaultValue="0"
                name="fruit_vege"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="alcohol">Are you a heavy alcohol consumer?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="alcohol"
                defaultValue="0"
                name="alcohol"
            >
                <FormControlLabel value="1" control={<Radio />} label="Yes" />
                <FormControlLabel value="0" control={<Radio />} label="No" />
            </RadioGroup>

            <FormLabel id="healthcare">Do you have a proper healthcare plan?</FormLabel>
            <RadioGroup
                row
                aria-labelledbdy="health_care"
                defaultValue="0"
                name="healthcare"
            >
                <FormControlLabel value="0" control={<Radio />} label="Yes" />
                <FormControlLabel value="1" control={<Radio />} label="No" />
            </RadioGroup>
            
            <FormLabel id="genhealth">How would you describe your general health?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="gen_health"
                defaultValue="1"
                name="gen_health"
            >
                <FormControlLabel value="1" control={<Radio />} label="Excellent Health" />
                <FormControlLabel value="2" control={<Radio />} label="Very Good Health" />
                <FormControlLabel value="3" control={<Radio />} label="Good Health" />
                <FormControlLabel value="4" control={<Radio />} label="Fair Health" />
                <FormControlLabel value="5" control={<Radio />} label="Poor Health" />
            </RadioGroup>

            <FormLabel id="menthealth">How would you describe your mental health within the past 30 days?</FormLabel>
            <RadioGroup
                row
                aria-labelledby="mental_health"
                defaultValue="1"
                name="mental_health"
            >
                <FormControlLabel value="1" control={<Radio />} label="Excellent Health" />
                <FormControlLabel value="2" control={<Radio />} label="Very Good Health" />
                <FormControlLabel value="3" control={<Radio />} label="Good Health" />
                <FormControlLabel value="4" control={<Radio />} label="Fair Health" />
                <FormControlLabel value="5" control={<Radio />} label="Poor Health" />
            </RadioGroup>

            <FormLabel id="sex">Do you have a proper healthcare plan?</FormLabel>
            <RadioGroup
                row
                aria-labelledbdy="sex"
                defaultValue="0"
                name="sex"
            >
                <FormControlLabel value="1" control={<Radio />} label="Male" />
                <FormControlLabel value="0" control={<Radio />} label="Female" />
            </RadioGroup>

            <FormLabel id="age">How old are you?</FormLabel>
            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                name="age"
                >
                <TextField id="age" label="Age" variant="outlined" />
            </Box>
            <input type="submit" value="Submit"/>

            </FormControl>
            

        </form>
    )
}

export default Form