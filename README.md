# Indoor Localisation

For this scenario, the task was to detect and estimate steps in data of a path we walked along. This data was recorded by an accelerator and a gyroscope in our phones.

## Recording 
We chose and recorded two paths for this task:
- Building 64, first floor. Starting point and endpoint was the hallway by the elevator.
- Karlebach Park

We used two different devices for recording by using the app *phyphox*.
- iPhone XR (Building 64): 
  - Accelerometer rate: 100.0 Hz
  - Gyroscope rate: 100.0 Hz 
- Sony XPeria 1(Karlebach Park):
  - Accelerometer rate: 412.0 Hz
  - Gyroscope rate: 412.0 Hz  

## Preprocessing
Before using the data for steps detection and estimation, it had to be preprocessed for noice removing and for bringing it into the right format. This is further explained and shown in `preprocessing.ipynb`.

## Step detection
The detection of the steps taken were based on the accelerator's data. For this, the norm of all dimensions was sufficient. The main approch was to detect local maxima in the signal which is explained in `step_detection.ipynb` in more detail.

## Step estimation
The step estimation is entirely based on the outline given in the project. More detail can be found in the respective notebooks (`geb64.ipynb` and `karlebach.ipynb`). 

# Results

The plots can be found in the respective notebooks. For a rough outline, the step estimation on the data of building 64 worked very well. A full trajectory was almost able to be estimated.

For the Karlebachpark the estimation did not work very well. Whether this is due to the higher frequency of the recording, irregularities in the recording device, the software, errors in the code or other factors was not able to be determined. It might also be due to large differences in resolution between the gyro and accelerometer sensors.

