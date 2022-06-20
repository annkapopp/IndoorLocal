# Indoor Localisation

For this scenario, the task was to detect and estimate steps in data of a path we walked along. This data was recorded by an accelerator and a gyroscope in our phones.

## Data acquisition
We chose and recorded two paths for this task:
- Building 64, first floor. Starting point and endpoint was the hallway by the elevator.
- Karlebach Park

We used two different devices for recording by using the app *phyphox*.
- iPhone XR (Building 64): 
  - Accelerometer rate: 100.0 Hz
  - Gyroscope rate: 100.0 Hz 
- (Karlebach Park)

Before moving along the track, we stayed idle for 5-10 seconds for later reference. The smartphone was held in the same position the whole time.

## Preprocessing
Before using the data for steps detection and estimation, it had to be preprocessed for noice removing and for bringing it into the right format. This is further explained and shown in `preprocessing.ipynb`.

## Step detection
The detection of the steps taken were based on the accelerator's data. For this, the norm of all dimensions was sufficient. The main approch was to detect local maxima in the signal which is explained in `step_detection.ipynb` in more detail.

## Step estimation


