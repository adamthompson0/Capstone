// Selected elements
function myFunction() {
    const x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
let weatherCond = {
    'rain': 'owf-501',
    'clear-day': 'owf-800',
    'cloudy': 'owf-802',
    'partly-cloudy-day': 'owf-801',


  }

  const apiKey = '2DFWPPKSQFLRAMBHN7URU2KT5';
  const location = '';
  
  // Construct the API URL
  const apiUrl = `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/${location}?key=${apiKey}&unitGroup=us&include=obs`;
  
  // Fetch the weather data from the API
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Get the weather condition code from the API data
      const weatherCode = data.days[0].currentCondition.codes;
  
      // Create a new element to hold the icon
      const icon = document.createElement('i');
  
      // Add the necessary classes to the icon element
      icon.classList.add('owf', `owf-${weatherCode}`);
  
      // Append the icon to the weather-icon element
      document.getElementById('weather-icon').appendChild(icon);
    });

