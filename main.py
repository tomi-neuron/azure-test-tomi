#!/usr/bin/env python3
# import frontend
from fastapi import FastAPI
from nicegui import app as nicegui_app, ui

app = FastAPI()


# @app.get('/')
# def read_root():
#     return {'Hello': 'World'}

@ui.page('/')
def whatever():
    ui.label('Hello, FastAPI with NiceGUI!')

    # NOTE dark mode will be persistent for each user across tabs and server restarts
    ui.dark_mode().bind_value(nicegui_app.storage.user, 'dark_mode')
    ui.checkbox('dark mode').bind_value(nicegui_app.storage.user, 'dark_mode')

ui.run_with(
    app,
    # mount_path='/gui',  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
    storage_secret='pick your private secret here',  # NOTE setting a secret is optional but allows for persistent storage per user
)

# if __name__ == '__main__':
    # print('Please start the app with the "uvicorn" command as shown in the start.sh script')
