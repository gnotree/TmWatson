#!/bin/zsh

# Install IBM Watson Python package
pip install ibm-watson
echo "IBM Watson installation complete"

# Create the TmWatson script that runs the TmWatson.py file
echo '#!/bin/zsh' > TmWatson
echo 'python3 "$(dirname "$0")/TmWatson.py" "$@"' >> TmWatson
chmod +x TmWatson

# Move the TmWatson script to /usr/local/bin/ and copy the TmWatson.py file to /usr/local/bin/
sudo mv TmWatson /usr/local/bin/
sudo cp TmWatson.py /usr/local/bin/

echo "TmWatson successfully installed to /usr/local/bin/"

# Terminal Watson - Version 2.1, updated June 7th, 2023 - Developed by GTAI
# In the updated .sh file, we first install the IBM Watson package and then create a TmWatson script that runs the TmWatson.py file using the python3 command. 
# We use $(dirname "$0") to get the path of the directory where the TmWatson script is located, so that we can reference the TmWatson.py file in the same directory.
# After creating the TmWatson script, we move it to /usr/local/bin/ using sudo mv, and then we copy the TmWatson.py file to the same directory using sudo cp. 
# This ensures that both the TmWatson script and the TmWatson.py file are in the same directory, and the script can access the file using the relative path.
# Finally, we print a message to the user indicating that the installation was successful.
# Any advice, recommendations, and/or if you are looking to help out/get involved, contact me at admin@gtai.io!
# This project is open-sourced, all I ask is if you like or enjoy the program, then please share it!
# Terminal Watson - Version 2.2, updated June 7th, 2023 - https://gtai.io
