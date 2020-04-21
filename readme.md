## Building a slack app

Building a slack app starts with creating an app in slack. Navigate to [https://api.slack.com/apps/](https://api.slack.com/apps/) and click on *Start Building*. It should prompt you to name your app and add to a workspace. Creating an app is that simple, however for interactions you need to configure web hooks and interactivity. Incoming web-hooks enables external sources to post data to your slack and interactivity let us communicate with interactions with our app. 

These interactions are required for slack apps to communicate to your backend service. Specify your endpoint in the interactive page, say, http://api.test.com/sports. This means, each interactions with your slack app will be sent to the specified endpoint. For your backend service to post to other channels you need to enable it in OAuth & Permissions. 

Slash commands in slack enables to trigger one particular action and this can grouped to your app. I personally prefer using slash commands as it separates out  commands and you can have separate end-points per slash command, whereas you can just add one for app interactivity.

For instance, you can have a slash command, /football which points to http://api.test.com/football and /cricket which points to http://api.test.com/cricket. The app interactivity will be http://api.test.com/sports which will receive all messages from slack app. 

Other tips: 

One way to keep track of information in interaction would be to add it in values. 
To know what action is being clicked, build your logic around action_id

The example code is a simple snippet to create an interactive app. Mainly showing how to create a dialog, send multi-select messages etc. 

*To run,* 

Build the docker image locally, run  `docker build -f Dockerfile -t sports .`

then, to run it :  `docker run -p 8000:8000 sports`
