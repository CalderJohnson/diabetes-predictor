/* HOW WE WOULD RETRIEVE DATA ON THE REACT APP */
const url = 'http://localhost:8000/form/'

// Example params THESE WILL BE YOUR FORM CONTENTS
let testParams = {
    high_bp: 0.0,
    high_chol: 0.0,
    chol_check: 0.0,
    weight: 80.0,
    height: 1.8,
    smoker: 0.0,
    heart_disease: 0.0,
    physical_activity: 0.0,
    fruit_vege: 0.0,
    alcohol: 0.0,
    stroke: 0.0,
    health_care: 1.0,
    gen_health: 3.0,
    mental_health: 3.0,
    sex: 0.0,
    age: 40.0,
}

let getData = (params) => {
    requestBody = JSON.stringify(params);
    const requestOptions = {
        method: 'POST',
        port: 80,
        headers: {
            'Content-Type': 'application/json', // Specify that the request body is in JSON format
        },
        body: requestBody,
    };
    // Make the POST request
    fetch(url, requestOptions)
        .then((response) => {
            // Check if the response status code indicates success (e.g., 200 OK)
            if (response.ok) {
                return response.json(); // Parse the response as JSON
            } else {
                throw new Error('Request failed');
            }
        })
    .then((data) => {
        /* THIS IS WHERE YOU RENDER THE RESPONSE DATA */
        console.log(data);
    })
    .catch((error) => {
        // Log any errors
        console.error(error);
    });
}

// Test usage (REMOVE THIS)
getData(testParams);