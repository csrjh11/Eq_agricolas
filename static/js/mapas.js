class App{
    #map;
    #mapEvent;
    #maquinas = []

    constructor(){
        this._getPosition();
        // this._getLocalStorage();
        // form.addEventListener("submit", this._newWorkout.bind(this));
        // inputType.addEventListener("change", this._toggleElevationField)   
        // containerWorkouts.addEventListener("click", this._moveToPopup.bind(this))     
    }

    _getPosition(){
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(this._loadMap.bind(this), function(){
                alert("Couldn't get current position!")
            })}
    }
    
    _loadMap(pos){
        const{latitude} = pos.coords;
        const{longitude} = pos.coords;

        this.#map = L.map('map').setView([latitude, longitude], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(this.#map);        

        // this.#map.on("click", this._showForm.bind(this));

        // this.#workouts.forEach(work=> this.renderWorkoutMarker(work))

    }

    _showForm(mapE){
        this.#mapEvent = mapE;
        form.classList.remove("hidden")
        inputDistance.focus()        
    }

    _hideform(){
        inputDistance.value = inputDuration.value = inputCadence.value = inputElevation.value = "";

        form.getElementsByClassName.display = "none";
        form.classList.add("hidden");
        setTimeout(()=>form.style.display = "grid", 1000)

    }

    _toggleElevationField(){

        inputElevation.closest(".form__row").classList.toggle("form__row--hidden");
        inputCadence.closest(".form__row").classList.toggle("form__row--hidden");
    }

    // _newWorkout(e){
    //     e.preventDefault()

    //     const validInputs = (...inputs) => inputs.every(inp => Number.isFinite(inp));

    //     const isPositive = (...inputs) => inputs.every(inp => inp > 0)

    //     const type = inputType.value;
    //     const distance = +inputDistance.value;
    //     const duration = +inputDuration.value;
    //     const {lat, lng} = this.#mapEvent.latlng;
    //     let newWorkout;
        


    //     if(type === "running"){
    //         const cadence = +inputCadence.value;
    //         if(!validInputs(distance, duration, cadence) || !isPositive(distance, duration, cadence)) return alert("Inputs must be positive umbers!")
    //         newWorkout = new Running(distance, duration, [lat, lng], cadence);
    //     }

    //     if(type === "cycling"){
    //         const elevation = +inputElevation.value;
    //         if(!validInputs(distance, duration, elevation) || !isPositive(distance, duration)) return alert("Inputs must be positive numbers!")
    //         newWorkout = new Cycling(distance, duration, [lat, lng], elevation);
    //     }

    //     this.#workouts.push(newWorkout)
    //     console.log(newWorkout);
    //     this.renderWorkoutMarker(newWorkout)
    //     this._renderWorkout(newWorkout)
    //     this._hideform()
    //     this._setLocalStorage()
    // }

    // renderWorkoutMarker(wo){
    //     const popu = L.popup({
    //     maxWidth: 250,
    //     minWidth: 100,
    //     autoClose: false,
    //     closeOnClick: false,
    //     className: `${wo.type}-popup`})
    //     L.marker(wo.coords).addTo(this.#map)
    //     .bindPopup(popu)
    //     .setPopupContent(`${wo.type === "running" ? "🏃‍♂": "🚴‍♀️"} ${wo.description}`)
    //     .openPopup();
    // }
    // _renderWorkout(wo){
    //     let commonHtml = `
    //     <li class="workout workout--${wo.type}" data-id="${wo.id}">
    //         <h2 class="workout__title">${wo.description}</h2>
    //         <div class="workout__details">
    //         <span class="workout__icon">${wo.type === "running" ? "🏃‍♂": "🚴‍♀️"}</span>
    //         <span class="workout__value">${wo.distance}</span>
    //         <span class="workout__unit">km</span>
    //         </div>
    //         <div class="workout__details">
    //         <span class="workout__icon">⏱</span>
    //         <span class="workout__value">${wo.duration}</span>
    //         <span class="workout__unit">min</span>
    //         </div>`
    //     if(wo.type === "running"){
    //         commonHtml += `
    //         <div class="workout__details">
    //         <span class="workout__icon">⚡️</span>
    //         <span class="workout__value">${wo.pace.toFixed(1)}</span>
    //         <span class="workout__unit">min/km</span>
    //       </div>
    //       <div class="workout__details">
    //         <span class="workout__icon">🦶🏼</span>
    //         <span class="workout__value">${wo.cadence}</span>
    //         <span class="workout__unit">spm</span>
    //       </div>
    //     </li>`
    //     }
    //     if(wo.type === "cycling"){
    //         commonHtml += `
    //         <div class="workout__details">
    //         <span class="workout__icon">⚡️</span>
    //         <span class="workout__value">${wo.speed.toFixed(1)}</span>
    //         <span class="workout__unit">km/h</span>
    //       </div>
    //       <div class="workout__details">
    //         <span class="workout__icon">⛰</span>
    //         <span class="workout__value">${wo.elev}</span>
    //         <span class="workout__unit">m</span>
    //       </div>
    //     </li>`
    //     }
    //     form.insertAdjacentHTML("afterend", commonHtml)
    // }

    // _moveToPopup(e){
    //     const workoutEl = e.target.closest(".workout");

    //     if(!workoutEl) return;
    //     const workout = this.#workouts.find(wo => wo.id === workoutEl.dataset.id)
        
    //     this.#map.setView(workout.coords, 16, {
    //         animate : true
    //     })
    // }

    // _setLocalStorage(){
    //     localStorage.setItem("workouts", JSON.stringify(this.#workouts))
    // }
    // _getLocalStorage(){
    //     const data = JSON.parse(localStorage.getItem("workouts"))
    //     console.log(data);

    //     if(!data) return

    //     this.#workouts = data;
    //     this.#workouts.forEach(work => this._renderWorkout(work))
    // }
}

const Mapp = new App()