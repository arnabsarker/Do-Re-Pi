# Do-Re-Pi
An ear trainer by Allen He and Arnab Sarker

The Do-Re-Pi is a musical ear trainer made using the Raspberry Pi. Musicians are often required to identify the interval between two notes, so the Do-Re-Pi serves as an aid to help new musicians distinguish between intervals. Musicians tend to use "shortcuts" to identify intervals (for example, the "Jaws" theme is the "iconic" minor second), so the Do-Re-Pi takes advantage of this trick to help users get the intervals to associate sounds with intervals.

__Usage__

Our ear trainer plays two notes upon the touch of a button, and then asks for user input to see if they can identify the interval between the two notes that were just played. If the user is correct, then the Pi will play an encouraging "Yeah!" for the user. Otherwise, it will tell the user what the proper interval was and then play one of the "shortcut" songs to help them remember the interval better for the next time.

__The Script__

Our project was written as a Python script that runs on startup. We used the ‘mpg123’ library to play audio files from the Pi, and we used the ‘GPIO’ library to receive input from the buttons. Our script was a simple loop that would first wait for the user to press the “next” button before generating a random number to match with a random interval. The Pi would then play the matched interval and wait for further user input. Once input was received, the Pi would see if it was the correct input, and play the appropriate response. It then goes back to waiting for the user to press “next.” 

__The Hardware__

The hardware for the Pi involved attaching the pins from the Pi onto a breadboard, and then constructing several circuits in parallel, with inputs going into specific pins on the Pi, so we could identify them in our code. Each of these circuits used a button which was connected to ground in such a way that whenever the button was pressed, the input for that part of the circuit would be grounded. We could then figure out what a user's input was based on which input had 0V as its value. The final product is shown below.

![Alt text](https://github.com/arnabsarker/Do-Re-Pi/blob/master/picture.jpg?raw=true "Do-Re-Pi")
